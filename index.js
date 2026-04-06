const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');
const axios = require('axios');
const xrpl = require('xrpl');
const { execSync } = require('child_process');
const fs = require('fs');

const app = express();
const PORT = 3000;
const GRAPH_URL = 'http://localhost:8001/subgraphs/name/chainlink-price-feeds';

app.use(helmet());
app.use(cors());
app.use(morgan('combined'));
app.use(express.json());

const freeLimiter = rateLimit({ windowMs: 60*1000, max: 60, message: { error: 'Rate limit exceeded.' }});
const store = {
  payments: [], dexTrades: [], whaleAlerts: [],
  stats: { connected: false, lastLedger: 0, totalPayments: 0, totalVolume: 0, startTime: Date.now() }
};
const WHALE = 10000;
const MAX = 1000;
const XRPL_SERVERS = ['wss://xrplcluster.com','wss://s1.ripple.com','wss://s2.ripple.com'];
let serverIndex = 0;

// ── XRPL ──────────────────────────────────────────────────────────────────────
async function startXRPL() {
  const url = XRPL_SERVERS[serverIndex % XRPL_SERVERS.length];
  serverIndex++;
  console.log('Connecting to', url);
  try {
    const client = new xrpl.Client(url, { timeout: 20000, connectionTimeout: 10000 });
    client.on('disconnected', () => { store.stats.connected = false; console.log('Disconnected, retrying...'); setTimeout(startXRPL, 5000); });
    client.on('error', (e) => { console.log('XRPL error:', e.message); });
    await client.connect();
    store.stats.connected = true;
    console.log('Connected to', url);
    await client.request({ command: 'subscribe', streams: ['ledger','transactions'] });
    client.on('ledgerClosed', (l) => { store.stats.lastLedger = l.ledger_index; });
    client.on('transaction', (tx) => { try { processTx(tx); } catch(e) { console.log('TX error:', e.message); } });
  } catch(e) {
    store.stats.connected = false;
    console.log('Failed:', e.message, '— retrying in 5s');
    setTimeout(startXRPL, 5000);
  }
}

function processTx(tx) {
  const t = tx.tx_json || tx.transaction;
  if (!t) return;
  const meta = tx.meta;
  if (!meta || (meta.TransactionResult && meta.TransactionResult !== 'tesSUCCESS')) return;
  const ts = xrpl.rippleTimeToUnixTime(t.date || tx.close_time || 0);
  if (t.TransactionType === 'Payment') {
    let amount = 0, currency = 'XRP';
    if (typeof t.Amount === 'string') { amount = parseFloat(xrpl.dropsToXrp(t.Amount)); }
    else if (typeof t.Amount === 'object') { amount = parseFloat(t.Amount.value); currency = t.Amount.currency; }
    const p = { id: tx.hash||t.hash, sender: t.Account, receiver: t.Destination, amount: amount.toFixed(6), currency, fee: xrpl.dropsToXrp(t.Fee||'0'), timestamp: Math.floor(ts/1000) };
    store.payments.unshift(p); if (store.payments.length > MAX) store.payments.pop();
    store.stats.totalPayments++; if (currency === 'XRP') store.stats.totalVolume += amount;
    if (amount >= WHALE && currency === 'XRP') {
      const w = { id: tx.hash||t.hash, chain: 'XRPL', sender: t.Account, receiver: t.Destination, amount: amount.toFixed(2), currency, timestamp: Math.floor(ts/1000), txHash: tx.hash||t.hash };
      store.whaleAlerts.unshift(w); if (store.whaleAlerts.length > 100) store.whaleAlerts.pop();
    }
  }
  if (t.TransactionType === 'OfferCreate') {
    const tp = t.TakerPays, tg = t.TakerGets;
    if (!tp || !tg) return;
    const pc = typeof tp === 'string' ? 'XRP' : tp.currency;
    const gc = typeof tg === 'string' ? 'XRP' : tg.currency;
    const pa = typeof tp === 'string' ? parseFloat(xrpl.dropsToXrp(tp)) : parseFloat(tp.value);
    const ga = typeof tg === 'string' ? parseFloat(xrpl.dropsToXrp(tg)) : parseFloat(tg.value);
    const tr = { id: tx.hash||t.hash, account: t.Account, takerPays: pa.toFixed(6), paysCurrency: pc, takerGets: ga.toFixed(6), getsCurrency: gc, pair: pc+'/'+gc, rate: pa > 0 ? (ga/pa).toFixed(8) : '0', timestamp: Math.floor(ts/1000) };
    store.dexTrades.unshift(tr); if (store.dexTrades.length > MAX) store.dexTrades.pop();
  }
}

// ── HELPERS ───────────────────────────────────────────────────────────────────
function runCmd(cmd) {
  try { return execSync(cmd, { timeout: 8000 }).toString().trim(); }
  catch(e) { return null; }
}

async function queryGraph(query) {
  const res = await axios.post(GRAPH_URL, { query }, { headers: { 'Content-Type': 'application/json' }, timeout: 5000 });
  return res.data;
}

// ── ROUTES ────────────────────────────────────────────────────────────────────

app.get('/', (req, res) => { res.json({ name: 'Blockchain Intelligence API', version: '1.0.0', status: 'live' }); });

// Health
app.get('/api/v1/health', (req, res) => {
  res.json({ status: 'healthy', timestamp: new Date().toISOString(), version: '1.0.0', xrpl_connected: store.stats.connected, xrpl_last_ledger: store.stats.lastLedger });
});

// ── BITCOIN ──
app.get('/api/v1/bitcoin/status', freeLimiter, (req, res) => {
  try {
    const raw = runCmd('/snap/bitcoin-core/current/bin/bitcoin-cli -datadir=/root/.bitcoin getblockchaininfo');
    if (!raw) return res.json({ success: false, error: 'Bitcoin not running' });
    const d = JSON.parse(raw);
    res.json({
      success: true,
      data: {
        blocks: d.blocks,
        headers: d.headers,
        syncProgress: (d.verificationprogress * 100).toFixed(4),
        synced: d.verificationprogress > 0.9999,
        pruned: d.pruned,
        pruneHeight: d.pruneheight,
        network: d.chain,
        sizeOnDisk: d.size_on_disk
      }
    });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

// ── LND LIGHTNING ──
app.get('/api/v1/lightning/status', freeLimiter, (req, res) => {
  try {
    const raw = runCmd('lncli getinfo');
    if (!raw) return res.json({ success: false, error: 'LND not running' });
    const d = JSON.parse(raw);
    res.json({
      success: true,
      data: {
        alias: d.alias,
        pubkey: d.identity_pubkey,
        blockHeight: d.block_height,
        syncedToChain: d.synced_to_chain,
        syncedToGraph: d.synced_to_graph,
        numPeers: d.num_peers,
        numActiveChannels: d.num_active_channels,
        numInactiveChannels: d.num_inactive_channels,
        numPendingChannels: d.num_pending_channels,
        version: d.version,
        color: d.color
      }
    });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

app.get('/api/v1/lightning/balance', freeLimiter, (req, res) => {
  try {
    const raw = runCmd('lncli walletbalance');
    if (!raw) return res.json({ success: false, error: 'LND not running' });
    const d = JSON.parse(raw);
    const chanRaw = runCmd('lncli channelbalance');
    const chan = chanRaw ? JSON.parse(chanRaw) : {};
    res.json({
      success: true,
      data: {
        confirmedSats: parseInt(d.confirmed_balance || 0),
        unconfirmedSats: parseInt(d.unconfirmed_balance || 0),
        totalSats: parseInt(d.total_balance || 0),
        channelBalanceSats: parseInt(chan.balance || 0),
        pendingChannelSats: parseInt(chan.pending_open_balance || 0)
      }
    });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

app.get('/api/v1/lightning/channels', freeLimiter, (req, res) => {
  try {
    const raw = runCmd('lncli listchannels');
    if (!raw) return res.json({ success: false, error: 'LND not running' });
    const d = JSON.parse(raw);
    res.json({ success: true, count: d.channels.length, data: d.channels });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

app.get('/api/v1/lightning/peers', freeLimiter, (req, res) => {
  try {
    const raw = runCmd('lncli listpeers');
    if (!raw) return res.json({ success: false, error: 'LND not running' });
    const d = JSON.parse(raw);
    res.json({ success: true, count: d.peers.length, data: d.peers });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

app.get('/api/v1/lightning/payments', freeLimiter, (req, res) => {
  try {
    const raw = runCmd('lncli listpayments --max_payments=20');
    if (!raw) return res.json({ success: false, error: 'LND not running' });
    const d = JSON.parse(raw);
    res.json({ success: true, count: d.payments.length, data: d.payments });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

app.get('/api/v1/lightning/forwarding', freeLimiter, (req, res) => {
  try {
    const raw = runCmd('lncli fwdinghistory --max_events=50');
    if (!raw) return res.json({ success: false, error: 'LND not running' });
    const d = JSON.parse(raw);
    const totalFeesSats = d.forwarding_events.reduce((sum, e) => sum + parseInt(e.fee||0), 0);
    res.json({ success: true, count: d.forwarding_events.length, totalFeesSats, data: d.forwarding_events });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

// ── STELLAR HORIZON ──
app.get('/api/v1/stellar/status', freeLimiter, async (req, res) => {
  try {
    const r = await axios.get('http://localhost:8002/', { timeout: 5000 });
    const d = r.data;
    res.json({
      success: true,
      data: {
        horizonVersion: d.horizon_version,
        coreVersion: d.core_version,
        ingestLatestLedger: d.ingest_latest_ledger,
        historyLatestLedger: d.history_latest_ledger,
        historyElderLedger: d.history_elder_ledger,
        coreLatestLedger: d.core_latest_ledger,
        networkPassphrase: d.network_passphrase,
        protocol: d.current_protocol_version,
        syncProgress: d.core_latest_ledger > 0 ? ((d.ingest_latest_ledger / d.core_latest_ledger) * 100).toFixed(2) : '0'
      }
    });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

app.get('/api/v1/stellar/transactions', freeLimiter, async (req, res) => {
  try {
    const limit = Math.min(parseInt(req.query.limit)||20, 100);
    const r = await axios.get(`http://localhost:8002/transactions?limit=${limit}&order=desc`, { timeout: 5000 });
    const records = r.data._embedded?.records || [];
    res.json({ success: true, count: records.length, data: records });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

// ── COSMOS ──
app.get('/api/v1/cosmos/status', freeLimiter, async (req, res) => {
  try {
    const r = await axios.get('http://localhost:26657/status', { timeout: 5000 });
    const d = r.data.result;
    res.json({
      success: true,
      data: {
        nodeId: d.node_info?.id,
        network: d.node_info?.network,
        version: d.node_info?.version,
        latestBlockHeight: parseInt(d.sync_info?.latest_block_height || 0),
        latestBlockTime: d.sync_info?.latest_block_time,
        catchingUp: d.sync_info?.catching_up,
        votingPower: d.validator_info?.voting_power
      }
    });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

// ── SYSTEM ──
app.get('/api/v1/system/status', freeLimiter, (req, res) => {
  try {
    const disk = runCmd("df -h / | tail -1 | awk '{print $2,$3,$4,$5}'");
    const mem = runCmd("free -b | grep Mem | awk '{print $2,$3,$4}'");
    const uptime = runCmd('uptime -p');
    const diskParts = disk ? disk.split(' ') : [];
    const memParts = mem ? mem.split(' ') : [];
    res.json({
      success: true,
      data: {
        disk: {
          total: diskParts[0] || '?',
          used: diskParts[1] || '?',
          free: diskParts[2] || '?',
          usePercent: diskParts[3] || '?'
        },
        memory: {
          totalBytes: parseInt(memParts[0] || 0),
          usedBytes: parseInt(memParts[1] || 0),
          freeBytes: parseInt(memParts[2] || 0),
          usedPercent: memParts[0] ? ((parseInt(memParts[1])/parseInt(memParts[0]))*100).toFixed(1) : '?'
        },
        uptime: uptime || '?',
        timestamp: new Date().toISOString()
      }
    });
  } catch(e) { res.status(500).json({ success: false, error: e.message }); }
});

// ── XRPL ──
app.get('/api/v1/chainlink/prices', freeLimiter, async (req, res) => {
  try { const limit = Math.min(parseInt(req.query.limit)||10,100); const data = await queryGraph(`{ priceFeeds(first:${limit},orderBy:timestamp,orderDirection:desc){id pair price decimals timestamp blockNumber transmitter}}`); res.json({ success:true, count:data.data.priceFeeds.length, data:data.data.priceFeeds }); }
  catch(e) { res.status(500).json({ success:false, error:'Failed to fetch price feeds' }); }
});
app.get('/api/v1/chainlink/deviations', freeLimiter, async (req, res) => {
  try { const limit = Math.min(parseInt(req.query.limit)||10,100); const data = await queryGraph(`{ priceDeviations(first:${limit},orderBy:timestamp,orderDirection:desc){id pair previousPrice newPrice deviationPercent timestamp blockNumber}}`); res.json({ success:true, count:data.data.priceDeviations.length, data:data.data.priceDeviations }); }
  catch(e) { res.status(500).json({ success:false, error:'Failed to fetch deviations' }); }
});
app.get('/api/v1/xrpl/payments', freeLimiter, (req, res) => { const limit = Math.min(parseInt(req.query.limit)||10,100); res.json({ success:true, count:store.payments.slice(0,limit).length, data:store.payments.slice(0,limit) }); });
app.get('/api/v1/xrpl/trades', freeLimiter, (req, res) => { const limit = Math.min(parseInt(req.query.limit)||10,100); res.json({ success:true, count:store.dexTrades.slice(0,limit).length, data:store.dexTrades.slice(0,limit) }); });
app.get('/api/v1/xrpl/whales', freeLimiter, (req, res) => { const limit = Math.min(parseInt(req.query.limit)||10,100); res.json({ success:true, count:store.whaleAlerts.slice(0,limit).length, data:store.whaleAlerts.slice(0,limit) }); });
app.get('/api/v1/xrpl/stats', freeLimiter, (req, res) => { res.json({ success:true, data:{ connected:store.stats.connected, lastLedger:store.stats.lastLedger, totalPayments:store.stats.totalPayments, totalVolumeXRP:store.stats.totalVolume.toFixed(2), whaleAlerts:store.whaleAlerts.length, dexTrades:store.dexTrades.length }}); });
app.get('/api/v1/alerts/whales', freeLimiter, (req, res) => { const limit = Math.min(parseInt(req.query.limit)||10,100); res.json({ success:true, count:store.whaleAlerts.slice(0,limit).length, data:store.whaleAlerts.slice(0,limit) }); });

app.use((req, res) => { res.status(404).json({ error:'Endpoint not found' }); });
process.on('uncaughtException', (e) => { console.error('Uncaught:', e.message); });
process.on('unhandledRejection', (e) => { console.error('Unhandled:', e); });
// -------------------------------------------
// ISO 20022 EBIT Status Endpoint (Safe Add-On)
// -------------------------------------------

app.get('/iso/ebit/status', (req, res) => {
  const payload = {
    event: {
      lastUpdate: new Date().toISOString(),
      schema: "ebit.iso20022.v1"
    },
    amount: {
      currentSupply: global.ebitCurrentSupply || 0,
      burnedTotal: global.ebitBurnedTotal || 0,
      treasuryBalance: global.ebitTreasuryBalance || 0
    },
    market: {
      price: global.ebitPrice || 0,
      volume24h: global.ebitVolume24h || 0
    },
    status: {
      network: "XRPL",
      ammPool: global.ebitAmmState || "unknown",
      treasury: global.ebitTreasuryState || "unknown"
    }
  };

  res.json(payload);
});

app.listen(PORT, '0.0.0.0', () => { console.log('API running on port ' + PORT); startXRPL(); });
