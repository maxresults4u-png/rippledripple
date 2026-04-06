require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { Xumm } = require('xumm');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 4000;

app.use(cors());
app.use(express.json());

const xumm = new Xumm(process.env.XUMM_API_KEY, process.env.XUMM_API_SECRET);

// ------------------------------------------------------
// GLOBAL LIVE VALUES (DEFAULTS)
// ------------------------------------------------------
global.ebitCurrentSupply = 0;
global.ebitBurnedTotal = 0;
global.ebitTreasuryBalance = 0;
global.ebitAmmState = "unknown";
global.ebitPrice = 0;
global.ebitVolume24h = 0;

// ------------------------------------------------------
// XRPL LIVE UPDATE FUNCTIONS
// ------------------------------------------------------

// 1. SUPPLY + BURN TOTAL
async function updateSupply() {
  try {
    const response = await axios.post('https://xrplcluster.com', {
      method: 'account_lines',
      params: [{
        account: "rEbITxxxxxxxxxxxxxxxxxxxxxxxxxxxx", // TODO: your issuer
        ledger_index: "validated"
      }]
    });

    const lines = response.data.result.lines || [];

    const supplyLine = lines.find(l => l.currency === "EBIT");
    const burnedLine = lines.find(l => l.currency === "EBITBURN");

    global.ebitCurrentSupply = supplyLine ? Number(supplyLine.balance) : 0;
    global.ebitBurnedTotal = burnedLine ? Number(burnedLine.balance) : 0;

  } catch (e) {
    console.log("Supply update error:", e.message);
  }
}

// 2. TREASURY BALANCE
async function updateTreasury() {
  try {
    const response = await axios.post('https://xrplcluster.com', {
      method: 'account_info',
      params: [{
        account: "rTREASURYxxxxxxxxxxxxxxxxxxxxxxxx", // TODO: your treasury wallet
        ledger_index: "validated"
      }]
    });

    const drops = response.data.result.account_data.Balance;
    global.ebitTreasuryBalance = Number(drops) / 1_000_000;

  } catch (e) {
    console.log("Treasury update error:", e.message);
  }
}

// 3. AMM POOL STATE
async function updateAmm() {
  try {
    const response = await axios.post('https://xrplcluster.com', {
      method: 'amm_info',
      params: [{
        asset: { currency: "EBIT", issuer: "rEbITxxxxxxxxxxxxxxxxxxxx" },
        asset2: { currency: "XRP" }
      }]
    });

    global.ebitAmmState = response.data.result.amm || "unknown";

  } catch (e) {
    global.ebitAmmState = "unknown";
  }
}

// 4. PRICE + VOLUME
async function updateMarket() {
  try {
    const response = await axios.post('https://xrplcluster.com', {
      method: 'book_offers',
      params: [{
        taker_gets: { currency: "EBIT", issuer: "rEbITxxxxxxxxxxxxxxxxxxxx" },
        taker_pays: { currency: "XRP" },
        limit: 20
      }]
    });

    const offers = response.data.result.offers || [];

    if (offers.length > 0) {
      const best = offers[0];
      global.ebitPrice = Number(best.TakerPays) / Number(best.TakerGets);
    }

    global.ebitVolume24h = 0; // placeholder

  } catch (e) {
    console.log("Market update error:", e.message);
  }
}

// ------------------------------------------------------
// UPDATE INTERVALS (EVERY 15 SECONDS)
// ------------------------------------------------------
setInterval(updateSupply, 15000);
setInterval(updateTreasury, 15000);
setInterval(updateAmm, 15000);
setInterval(updateMarket, 15000);

// ------------------------------------------------------
// HEALTH CHECK
// ------------------------------------------------------
app.get('/api/health', (req, res) => {
  res.json({ status: 'healthy', service: 'Ripple Dripple API' });
});

// ------------------------------------------------------
// XUMM SIGN-IN
// ------------------------------------------------------
app.post('/api/signin', async (req, res) => {
  try {
    const payload = await xumm.payload.create({
      txjson: { TransactionType: 'SignIn' }
    });

    res.json({
      success: true,
      uuid: payload.uuid,
      qr: payload.refs.qr_png,
      deeplink: payload.next.always
    });
  } catch (e) {
    res.status(500).json({ success: false, error: e.message });
  }
});

app.get('/api/signin/:uuid', async (req, res) => {
  try {
    const result = await xumm.payload.get(req.params.uuid);
    res.json({
      success: true,
      signed: result.meta.signed,
      account: result.response.account || null
    });
  } catch (e) {
    res.status(500).json({ success: false, error: e.message });
  }
});

// ------------------------------------------------------
// XRP BALANCE LOOKUP
// ------------------------------------------------------
app.get('/api/balance/:address', async (req, res) => {
  try {
    const response = await axios.post('https://xrplcluster.com', {
      method: 'account_info',
      params: [{ account: req.params.address, ledger_index: 'current' }]
    });

    const data = response.data.result;

    if (data.status === 'error') {
      return res.json({ success: true, xrp: 0 });
    }

    const xrp = parseInt(data.account_data.Balance) / 1000000;

    res.json({ success: true, xrp: xrp.toFixed(6) });
  } catch (e) {
    res.status(500).json({ success: false, error: e.message });
  }
});

// ------------------------------------------------------
// AMM DEPOSIT
// ------------------------------------------------------
app.post('/api/amm/deposit', async (req, res) => {
  try {
    const { account, amountXRP } = req.body;
    const drops = Math.floor(amountXRP * 1000000).toString();

    const payload = await xumm.payload.create({
      txjson: {
        TransactionType: 'AMMDeposit',
        Account: account,
        Asset: { currency: 'XRP' },
        Asset2: {
          currency: 'USD',
          issuer: 'rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B'
        },
        Amount: drops,
        Flags: 524288
      }
    });

    res.json({
      success: true,
      uuid: payload.uuid,
      qr: payload.refs.qr_png,
      deeplink: payload.next.always
    });
  } catch (e) {
    res.status(500).json({ success: false, error: e.message });
  }
});

// ------------------------------------------------------
// ISO 20022 EBIT STATUS ENDPOINT
// ------------------------------------------------------
app.get('/iso/ebit/status', (req, res) => {
  const payload = {
    event: {
      lastUpdate: new Date().toISOString(),
      schema: "ebit.iso20022.v1"
    },
    amount: {
      currentSupply: global.ebitCurrentSupply,
      burnedTotal: global.ebitBurnedTotal,
      treasuryBalance: global.ebitTreasuryBalance
    },
    market: {
      price: global.ebitPrice,
      volume24h: global.ebitVolume24h
    },
    status: {
      network: "XRPL",
      ammPool: global.ebitAmmState,
      treasury: global.ebitTreasuryState || "unknown"
    }
  };

  res.json(payload);
});

// ------------------------------------------------------
// START SERVER (MUST BE LAST)
// ------------------------------------------------------
app.listen(PORT, '0.0.0.0', () =>
  console.log('Ripple Dripple API on port ' + PORT)
);
