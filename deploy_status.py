#!/usr/bin/env python3
html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="30">
<title>Campione Infrastructure</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;500;600;700&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
<style>
:root{--bg:#030712;--bg2:#0d1117;--border:#1e2d3d;--green:#00ff88;--blue:#38bdf8;--gold:#fbbf24;--red:#ef4444;--orange:#f97316;--purple:#a78bfa;--muted:#4b5563;--text:#e2e8f0;--dim:#94a3b8;--mono:'Share Tech Mono',monospace;--ui:'Rajdhani',sans-serif;--head:'Orbitron',sans-serif;}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{background:var(--bg);color:var(--text);font-family:var(--ui);min-height:100vh;overflow-x:hidden;}
body::before{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,255,136,0.012) 2px,rgba(0,255,136,0.012) 4px);pointer-events:none;z-index:9999;}
header{padding:18px 28px 14px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;position:relative;}
header::after{content:'';position:absolute;bottom:-1px;left:0;width:35%;height:1px;background:linear-gradient(90deg,var(--green),transparent);}
.logo{font-family:var(--head);font-size:20px;font-weight:900;letter-spacing:3px;color:var(--green);text-shadow:0 0 25px rgba(0,255,136,0.4);}
.logo span{color:var(--blue);}
.hdr-meta{font-family:var(--mono);font-size:10px;color:var(--muted);text-align:right;line-height:1.9;}
.hdr-meta b{color:var(--blue);}
.ticker-wrap{background:var(--bg2);border-bottom:1px solid var(--border);padding:7px 28px;overflow:hidden;white-space:nowrap;}
.ticker{display:inline-block;animation:ticker 50s linear infinite;font-family:var(--mono);font-size:11px;color:var(--muted);}
.ticker .ti{margin-right:50px;}.ticker .ti b{color:var(--green);}
.ticker .ti.b b{color:var(--blue);}.ticker .ti.g b{color:var(--gold);}.ticker .ti.p b{color:var(--purple);}
@keyframes ticker{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.nav{display:flex;gap:0;border-bottom:1px solid var(--border);background:var(--bg2);padding:0 28px;overflow-x:auto;}
.tab{font-family:var(--mono);font-size:11px;letter-spacing:1px;padding:11px 16px;cursor:pointer;color:var(--muted);border-bottom:2px solid transparent;transition:all 0.2s;white-space:nowrap;}
.tab:hover{color:var(--text);}.tab.active{color:var(--green);border-bottom-color:var(--green);}
.panel{display:none;padding:20px 28px 32px;}.panel.active{display:block;}
.grid{display:grid;gap:14px;}.g12{grid-template-columns:repeat(12,1fr);}
.c3{grid-column:span 3}.c4{grid-column:span 4}.c5{grid-column:span 5}.c6{grid-column:span 6}.c8{grid-column:span 8}.c9{grid-column:span 9}.c12{grid-column:span 12}
@media(max-width:1100px){.c3,.c4{grid-column:span 6}.c5,.c8,.c9{grid-column:span 12}}
@media(max-width:700px){[class^="c"]{grid-column:span 12}.panel{padding:12px 14px}}
.card{background:var(--bg2);border:1px solid var(--border);border-radius:8px;padding:18px;position:relative;overflow:hidden;}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent);opacity:0.35;}
.card.cb::before{background:linear-gradient(90deg,var(--blue),transparent);}
.card.cg::before{background:linear-gradient(90deg,var(--gold),transparent);}
.card.cp::before{background:linear-gradient(90deg,var(--purple),transparent);}
.card.cr::before{background:linear-gradient(90deg,var(--red),transparent);}
.ct{font-family:var(--mono);font-size:9px;letter-spacing:3px;color:var(--muted);margin-bottom:14px;text-transform:uppercase;}
.srow{display:flex;align-items:center;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(30,45,61,0.6);}
.srow:last-child{border-bottom:none;}
.slbl{font-size:13px;font-weight:600;color:var(--dim);}
.sval{font-family:var(--mono);font-size:13px;color:var(--green);}
.sval.b{color:var(--blue);}.sval.g{color:var(--gold);}.sval.p{color:var(--purple);}.sval.r{color:var(--red);}
.badge{font-family:var(--mono);font-size:9px;letter-spacing:1px;padding:2px 8px;border-radius:3px;}
.bg{background:rgba(0,255,136,0.1);color:var(--green);border:1px solid rgba(0,255,136,0.25);}
.bb{background:rgba(56,189,248,0.1);color:var(--blue);border:1px solid rgba(56,189,248,0.25);}
.bgo{background:rgba(251,191,36,0.1);color:var(--gold);border:1px solid rgba(251,191,36,0.25);}
.br{background:rgba(239,68,68,0.1);color:var(--red);border:1px solid rgba(239,68,68,0.25);}
.bp{background:rgba(167,139,250,0.1);color:var(--purple);border:1px solid rgba(167,139,250,0.25);}
.bm{background:rgba(75,85,99,0.2);color:var(--muted);border:1px solid rgba(75,85,99,0.3);}
.bignum{font-family:var(--head);font-size:36px;font-weight:900;color:var(--green);line-height:1;animation:pg 3s ease-in-out infinite;}
@keyframes pg{0%,100%{text-shadow:0 0 20px rgba(0,255,136,0.3)}50%{text-shadow:0 0 50px rgba(0,255,136,0.7)}}
.bignum.b{color:var(--blue);animation:none;}
.bignum.g{color:var(--gold);animation:none;}
.bignum.p{color:var(--purple);animation:none;}
.bignum.r{color:var(--red);animation:none;}
.bcenter{text-align:center;padding:8px 0 14px;}
.bsub{font-family:var(--mono);font-size:9px;color:var(--muted);letter-spacing:2px;margin-top:5px;}
.pb-w{margin:6px 0;}.pb-l{display:flex;justify-content:space-between;font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:4px;}
.pb{height:4px;background:var(--border);border-radius:2px;overflow:hidden;}
.pb-f{height:100%;border-radius:2px;background:linear-gradient(90deg,var(--green),var(--blue));transition:width 1s ease;}
.pb-f.warn{background:linear-gradient(90deg,var(--gold),var(--orange));}
.pb-f.danger{background:linear-gradient(90deg,var(--orange),var(--red));}
table.tx{width:100%;border-collapse:collapse;font-family:var(--mono);font-size:11px;}
table.tx th{text-align:left;padding:6px 8px;color:var(--muted);font-size:9px;letter-spacing:2px;border-bottom:1px solid var(--border);font-weight:normal;}
table.tx td{padding:7px 8px;border-bottom:1px solid rgba(30,45,61,0.4);vertical-align:middle;}
table.tx tr:last-child td{border-bottom:none;}
table.tx tr{animation:si 0.3s ease;}
@keyframes si{from{opacity:0;transform:translateX(-6px)}to{opacity:1;transform:translateX(0)}}
.addr{color:var(--muted);max-width:130px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.tamt{color:var(--green);}.tamt.b{color:var(--blue);}.tpair{color:var(--gold);}.trate{color:var(--purple);}.tts{color:var(--muted);font-size:9px;}
.stbl{max-height:360px;overflow-y:auto;}
.stbl::-webkit-scrollbar{width:3px;}
.stbl::-webkit-scrollbar-thumb{background:var(--border);}
.empty{text-align:center;padding:30px;font-family:var(--mono);font-size:11px;color:var(--muted);}
.pubkey{font-family:var(--mono);font-size:9px;color:var(--muted);word-break:break-all;background:rgba(0,0,0,0.3);padding:8px;border-radius:4px;margin-top:8px;border:1px solid var(--border);}
footer{border-top:1px solid var(--border);padding:10px 28px;display:flex;justify-content:space-between;align-items:center;}
.ftl{font-family:var(--mono);font-size:9px;color:var(--muted);}.ftl b{color:var(--green);}
.udots{display:flex;gap:3px;}
.udot{width:7px;height:7px;border-radius:2px;background:var(--green);opacity:0.8;}
.udot.m{background:var(--red);opacity:0.5;}
</style>
</head>
<body>
<header>
  <div>
    <div class="logo">CAMPIONE <span>INFRA</span></div>
    <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-top:3px;">OPERATIONS CENTER — LIVE</div>
  </div>
  <div class="hdr-meta"><b>5.78.101.177</b> · Hetzner CCX33 · Hillsboro OR<br>
  Disk: <b id="hdr-disk">—</b> · RAM: <b id="hdr-ram">—</b> · Up: <b id="hdr-uptime">—</b><br>
  Updated: <span id="htime">—</span></div>
</header>

<div class="ticker-wrap">
  <div class="ticker">
    <span class="ti">BTC BLOCK <b id="tk-btc">943,900</b></span>
    <span class="ti b">XRPL <b id="tk-xrpl">—</b></span>
    <span class="ti g">COSMOS <b id="tk-cosmos">—</b></span>
    <span class="ti p">LND PEERS <b id="tk-lnd">3</b></span>
    <span class="ti">PAYMENTS <b id="tk-pay">—</b></span>
    <span class="ti b">DEX TRADES <b id="tk-dex">—</b></span>
    <span class="ti g">STELLAR <b id="tk-stellar">SYNCING</b></span>
    <span class="ti">CHAINLINK <b>HEALTHY</b></span>
    <span class="ti">DISK <b id="tk-disk">—</b></span>
    <span class="ti">BTC BLOCK <b id="tk-btc2">943,900</b></span>
    <span class="ti b">XRPL <b id="tk-xrpl2">—</b></span>
    <span class="ti g">COSMOS <b id="tk-cosmos2">—</b></span>
    <span class="ti p">LND PEERS <b id="tk-lnd2">3</b></span>
    <span class="ti">PAYMENTS <b id="tk-pay2">—</b></span>
    <span class="ti b">DEX TRADES <b id="tk-dex2">—</b></span>
    <span class="ti g">STELLAR <b>SYNCING</b></span>
    <span class="ti">CHAINLINK <b>HEALTHY</b></span>
    <span class="ti">DISK <b id="tk-disk2">—</b></span>
  </div>
</div>

<div class="nav">
  <div class="tab active" onclick="showTab('overview')">⚡ OVERVIEW</div>
  <div class="tab" onclick="showTab('bitcoin')">₿ BITCOIN</div>
  <div class="tab" onclick="showTab('lightning')">⚡ LIGHTNING</div>
  <div class="tab" onclick="showTab('xrpl')">💧 XRPL</div>
  <div class="tab" onclick="showTab('stellar')">⭐ STELLAR</div>
  <div class="tab" onclick="showTab('cosmos')">🪐 COSMOS</div>
  <div class="tab" onclick="showTab('chainlink')">🔗 CHAINLINK</div>
  <div class="tab" onclick="showTab('system')">🖥 SYSTEM</div>
</div>

<!-- OVERVIEW -->
<div class="panel active" id="panel-overview">
  <div class="grid g12">
    <div class="card c3 cg">
      <div class="ct">₿ Bitcoin</div>
      <div class="bcenter"><div class="bignum g" id="ov-btc">—</div><div class="bsub">BLOCK HEIGHT</div></div>
      <div class="pb-w"><div class="pb-l"><span>SYNC</span><span id="ov-btc-pct">—</span></div><div class="pb"><div class="pb-f" id="ov-btc-bar" style="width:0%"></div></div></div>
      <div class="srow"><span class="slbl">Network</span><span class="sval g">MAINNET</span></div>
      <div class="srow"><span class="slbl">Status</span><span class="badge bg" id="ov-btc-st">CHECKING</span></div>
    </div>
    <div class="card c3 cp">
      <div class="ct">⚡ Lightning</div>
      <div class="bcenter"><div class="bignum p" id="ov-lnd-peers">—</div><div class="bsub">PEERS</div></div>
      <div class="srow"><span class="slbl">Alias</span><span class="sval p">CampioneNode</span></div>
      <div class="srow"><span class="slbl">Channels</span><span class="sval p" id="ov-lnd-ch">0</span></div>
      <div class="srow"><span class="slbl">Balance</span><span class="sval p" id="ov-lnd-bal">0 sats</span></div>
      <div class="srow"><span class="slbl">Synced</span><span class="badge bg" id="ov-lnd-sync">CHECKING</span></div>
    </div>
    <div class="card c3 cb">
      <div class="ct">💧 XRPL</div>
      <div class="bcenter"><div class="bignum b" id="ov-xrpl">—</div><div class="bsub">CURRENT LEDGER</div></div>
      <div class="srow"><span class="slbl">Payments</span><span class="sval" id="ov-pay">—</span></div>
      <div class="srow"><span class="slbl">DEX Trades</span><span class="sval b" id="ov-dex">—</span></div>
      <div class="srow"><span class="slbl">Volume</span><span class="sval g" id="ov-vol">—</span></div>
    </div>
    <div class="card c3">
      <div class="ct">🖥 System</div>
      <div class="pb-w"><div class="pb-l"><span>DISK</span><span id="ov-disk-pct">—</span></div><div class="pb"><div class="pb-f warn" id="ov-disk-bar" style="width:0%"></div></div></div>
      <div class="pb-w"><div class="pb-l"><span>RAM</span><span id="ov-ram-pct">—</span></div><div class="pb"><div class="pb-f" id="ov-ram-bar" style="width:0%"></div></div></div>
      <div class="srow"><span class="slbl">Disk</span><span class="sval g" id="ov-disk-val">—</span></div>
      <div class="srow"><span class="slbl">Uptime</span><span class="sval b" id="ov-uptime">—</span></div>
    </div>
    <div class="card c6">
      <div class="ct">⚙️ All Services</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:0;">
        <div class="srow"><span class="slbl">🪐 Cosmos</span><span class="badge bg" id="sv-cosmos">CHECKING</span></div>
        <div class="srow"><span class="slbl">💧 XRPL</span><span class="badge bg" id="sv-xrpl">CHECKING</span></div>
        <div class="srow"><span class="slbl">⭐ Stellar</span><span class="badge bgo" id="sv-stellar">SYNCING</span></div>
        <div class="srow"><span class="slbl">₿ Bitcoin</span><span class="badge bg" id="sv-btc">CHECKING</span></div>
        <div class="srow"><span class="slbl">⚡ Lightning</span><span class="badge bg" id="sv-lnd">CHECKING</span></div>
        <div class="srow"><span class="slbl">🔗 Chainlink</span><span class="badge bg" id="sv-cl">HEALTHY</span></div>
        <div class="srow"><span class="slbl">📊 Graph Node</span><span class="badge bg">RUNNING</span></div>
        <div class="srow"><span class="slbl">🔗 Blockchain API</span><span class="badge bg" id="sv-bapi">CHECKING</span></div>
        <div class="srow"><span class="slbl">💧 Ripple Dripple</span><span class="badge bg" id="sv-rd">CHECKING</span></div>
        <div class="srow"><span class="slbl">🌐 Nginx SSL</span><span class="badge bg">ACTIVE</span></div>
      </div>
    </div>
    <div class="card c6 cb">
      <div class="ct">📡 Live XRPL Feed</div>
      <div class="stbl"><table class="tx"><thead><tr><th>TYPE</th><th>FROM</th><th>TO</th><th>AMOUNT</th><th>TIME</th></tr></thead><tbody id="ov-feed"></tbody></table></div>
    </div>
    <div class="card c6">
      <div class="ct">🪐 Cosmos + ⭐ Stellar</div>
      <div class="srow"><span class="slbl">Cosmos Block</span><span class="sval g" id="ov-cosmos-block">—</span></div>
      <div class="srow"><span class="slbl">Cosmos Network</span><span class="sval g" id="ov-cosmos-net">—</span></div>
      <div class="srow"><span class="slbl">Cosmos Catching Up</span><span class="sval" id="ov-cosmos-sync">—</span></div>
      <div class="srow"><span class="slbl">Stellar Ingest</span><span class="sval b" id="ov-stellar-ingest">—</span></div>
      <div class="srow"><span class="slbl">Stellar History</span><span class="sval b" id="ov-stellar-hist">—</span></div>
      <div class="srow"><span class="slbl">Stellar Sync %</span><span class="sval b" id="ov-stellar-pct">—</span></div>
    </div>
    <div class="card c6 cg">
      <div class="ct">₿ Bitcoin + ⚡ Lightning Details</div>
      <div class="srow"><span class="slbl">BTC Blocks</span><span class="sval g" id="ov-btc2">—</span></div>
      <div class="srow"><span class="slbl">BTC Pruned</span><span class="sval g" id="ov-btc-pruned">—</span></div>
      <div class="srow"><span class="slbl">LND Version</span><span class="sval" id="ov-lnd-ver">—</span></div>
      <div class="srow"><span class="slbl">LND Pubkey</span><span class="sval b" style="font-size:9px;word-break:break-all" id="ov-lnd-pub">—</span></div>
      <div class="srow"><span class="slbl">Deposit Address</span><span class="sval" style="font-size:9px">bc1qk6eg4rlwdyjqv53gpv6g9sd0hk0k3p9h7flgav</span></div>
    </div>
  </div>
</div>

<!-- BITCOIN -->
<div class="panel" id="panel-bitcoin">
  <div class="grid g12">
    <div class="card c4 cg">
      <div class="ct">₿ Bitcoin Node</div>
      <div class="bcenter"><div class="bignum g" id="bt-blocks">—</div><div class="bsub">BLOCK HEIGHT</div></div>
      <div class="pb-w"><div class="pb-l"><span>SYNC</span><span id="bt-pct">—</span></div><div class="pb"><div class="pb-f" id="bt-bar" style="width:0%"></div></div></div>
      <div class="srow"><span class="slbl">Headers</span><span class="sval g" id="bt-headers">—</span></div>
      <div class="srow"><span class="slbl">Network</span><span class="sval g" id="bt-net">—</span></div>
      <div class="srow"><span class="slbl">Pruned</span><span class="sval g" id="bt-pruned">—</span></div>
      <div class="srow"><span class="slbl">Prune Height</span><span class="sval g" id="bt-ph">—</span></div>
      <div class="srow"><span class="slbl">Size on Disk</span><span class="sval g" id="bt-size">—</span></div>
      <div class="srow"><span class="slbl">Status</span><span class="badge bg" id="bt-st">CHECKING</span></div>
    </div>
    <div class="card c4">
      <div class="ct">₿ Node Config</div>
      <div class="srow"><span class="slbl">Implementation</span><span class="sval g">Bitcoin Core 30.2</span></div>
      <div class="srow"><span class="slbl">Install</span><span class="sval g">Snap</span></div>
      <div class="srow"><span class="slbl">Data Dir</span><span style="font-family:var(--mono);font-size:11px;color:var(--muted)">/root/.bitcoin</span></div>
      <div class="srow"><span class="slbl">RPC Port</span><span class="sval">8332</span></div>
      <div class="srow"><span class="slbl">ZMQ Blocks</span><span class="sval">28332</span></div>
      <div class="srow"><span class="slbl">ZMQ TX</span><span class="sval">28333</span></div>
      <div class="srow"><span class="slbl">LND Connected</span><span class="badge bg">YES</span></div>
    </div>
    <div class="card c4 cp">
      <div class="ct">⚡ Lightning Connected</div>
      <div class="bcenter"><div class="bignum p" id="bt-lnd-peers">—</div><div class="bsub">LND PEERS</div></div>
      <div class="srow"><span class="slbl">Active Channels</span><span class="sval p" id="bt-lnd-ch">—</span></div>
      <div class="srow"><span class="slbl">Wallet Balance</span><span class="sval p" id="bt-lnd-bal">—</span></div>
      <div class="srow"><span class="slbl">Synced to Graph</span><span class="badge bg" id="bt-lnd-graph">CHECKING</span></div>
    </div>
  </div>
</div>

<!-- LIGHTNING -->
<div class="panel" id="panel-lightning">
  <div class="grid g12">
    <div class="card c4 cp">
      <div class="ct">⚡ LND Node</div>
      <div class="bcenter"><div class="bignum p" id="ln-peers">—</div><div class="bsub">PEERS</div></div>
      <div class="srow"><span class="slbl">Alias</span><span class="sval p">CampioneNode</span></div>
      <div class="srow"><span class="slbl">Version</span><span class="sval p" id="ln-ver">—</span></div>
      <div class="srow"><span class="slbl">Block Height</span><span class="sval" id="ln-block">—</span></div>
      <div class="srow"><span class="slbl">Synced Chain</span><span class="badge bg" id="ln-sync">CHECKING</span></div>
      <div class="srow"><span class="slbl">Synced Graph</span><span class="badge bg" id="ln-graph">CHECKING</span></div>
      <div class="srow"><span class="slbl">Active Channels</span><span class="sval p" id="ln-active">0</span></div>
      <div class="srow"><span class="slbl">Pending Channels</span><span class="sval" id="ln-pending">0</span></div>
    </div>
    <div class="card c4">
      <div class="ct">⚡ Wallet Balance</div>
      <div class="bcenter"><div class="bignum" id="ln-bal">0</div><div class="bsub">CONFIRMED SATS</div></div>
      <div class="srow"><span class="slbl">Unconfirmed</span><span class="sval g" id="ln-unconf">0</span></div>
      <div class="srow"><span class="slbl">Channel Balance</span><span class="sval b" id="ln-chbal">0</span></div>
      <div class="srow"><span class="slbl">Status</span><span class="badge bgo">AWAITING FUNDING</span></div>
      <div style="margin-top:14px;">
        <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:6px;">DEPOSIT ADDRESS</div>
        <div class="pubkey">bc1qk6eg4rlwdyjqv53gpv6g9sd0hk0k3p9h7flgav</div>
      </div>
    </div>
    <div class="card c4 cb">
      <div class="ct">⚡ Node Identity</div>
      <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:6px;">PUBLIC KEY</div>
      <div class="pubkey" style="color:var(--blue)">0383f3e497f390b7cfedd12198d7542ae9fe062c1b9d71ca2ed49a73b1ab633b3c</div>
      <div style="margin-top:14px;">
        <div class="srow"><span class="slbl">Connect</span><span style="font-family:var(--mono);font-size:9px;color:var(--muted)">pubkey@5.78.101.177:9735</span></div>
        <div class="srow"><span class="slbl">Color</span><span style="font-family:var(--mono);font-size:13px;color:#00ff88">#00ff88</span></div>
        <div class="srow"><span class="slbl">P2P Port</span><span class="sval">9735</span></div>
        <div class="srow"><span class="slbl">RPC Port</span><span class="sval">10009</span></div>
      </div>
    </div>
    <div class="card c6">
      <div class="ct">⚡ Routing Fee History</div>
      <div class="bcenter"><div class="bignum" id="ln-fees">0</div><div class="bsub">TOTAL SATS EARNED ROUTING</div></div>
      <div class="srow"><span class="slbl">Total Routes</span><span class="sval" id="ln-routes">0</span></div>
      <div class="srow"><span class="slbl">Status</span><span class="badge bgo">AWAITING CHANNELS</span></div>
    </div>
    <div class="card c6 cp">
      <div class="ct">⚡ Income Potential</div>
      <div class="srow"><span class="slbl">Routing Fees</span><span class="sval p">1-100 sats/payment</span></div>
      <div class="srow"><span class="slbl">API Access</span><span class="sval p">$50-500/mo</span></div>
      <div class="srow"><span class="slbl">BTC↔XRP Swaps</span><span class="sval p">Fee per swap</span></div>
      <div class="srow"><span class="slbl">Next Step</span><span class="badge bgo">FUND WALLET</span></div>
    </div>
  </div>
</div>

<!-- XRPL -->
<div class="panel" id="panel-xrpl">
  <div class="grid g12">
    <div class="card c4 cb">
      <div class="ct">💧 XRPL Stats</div>
      <div class="bcenter"><div class="bignum b" id="xp-ledger">—</div><div class="bsub">CURRENT LEDGER</div></div>
      <div class="srow"><span class="slbl">Total Payments</span><span class="sval" id="xp-pay">—</span></div>
      <div class="srow"><span class="slbl">DEX Trades</span><span class="sval b" id="xp-dex">—</span></div>
      <div class="srow"><span class="slbl">Volume XRP</span><span class="sval g" id="xp-vol">—</span></div>
      <div class="srow"><span class="slbl">Whale Alerts</span><span class="sval r" id="xp-whales">0</span></div>
      <div class="srow"><span class="slbl">Status</span><span class="badge bg" id="xp-conn">LIVE</span></div>
    </div>
    <div class="card c8 cb">
      <div class="ct">💸 Recent Payments</div>
      <div class="stbl"><table class="tx"><thead><tr><th>TX ID</th><th>SENDER</th><th>RECEIVER</th><th>AMOUNT</th><th>FEE</th><th>AGO</th></tr></thead><tbody id="xp-tbl"></tbody></table></div>
    </div>
    <div class="card c4">
      <div class="ct">🔄 DEX Stats</div>
      <div class="bcenter"><div class="bignum b" id="dx-total">—</div><div class="bsub">DEX TRADES</div></div>
      <div class="srow"><span class="slbl">Top Pair</span><span class="sval g">XRP/RUSD</span></div>
      <div class="srow"><span class="slbl">Avg Rate</span><span class="sval p" id="dx-rate">—</span></div>
    </div>
    <div class="card c8 cg">
      <div class="ct">🔄 DEX Trades</div>
      <div class="stbl"><table class="tx"><thead><tr><th>TX ID</th><th>ACCOUNT</th><th>PAIR</th><th>PAYS</th><th>GETS</th><th>RATE</th><th>AGO</th></tr></thead><tbody id="dx-tbl"></tbody></table></div>
    </div>
  </div>
</div>

<!-- STELLAR -->
<div class="panel" id="panel-stellar">
  <div class="grid g12">
    <div class="card c4 cb">
      <div class="ct">⭐ Stellar Horizon</div>
      <div class="bcenter"><div class="bignum b" style="font-size:22px" id="st-ingest">—</div><div class="bsub">INGEST LEDGER</div></div>
      <div class="pb-w"><div class="pb-l"><span>SYNC PROGRESS</span><span id="st-pct">—</span></div><div class="pb"><div class="pb-f" id="st-bar" style="width:0%"></div></div></div>
      <div class="srow"><span class="slbl">History Ledger</span><span class="sval b" id="st-hist">—</span></div>
      <div class="srow"><span class="slbl">Core Ledger</span><span class="sval b" id="st-core">—</span></div>
      <div class="srow"><span class="slbl">Horizon Version</span><span class="sval" id="st-ver">—</span></div>
      <div class="srow"><span class="slbl">Protocol</span><span class="sval b" id="st-proto">—</span></div>
      <div class="srow"><span class="slbl">Mode</span><span class="badge bgo">CAPTIVE CORE</span></div>
    </div>
    <div class="card c8">
      <div class="ct">⭐ Recent Stellar Transactions</div>
      <div id="st-feed"><div class="empty" style="color:var(--gold)">⭐ Horizon catching up from history archives...<br><span style="color:var(--muted);font-size:10px">Transactions will appear once synced to current ledger</span></div></div>
    </div>
  </div>
</div>

<!-- COSMOS -->
<div class="panel" id="panel-cosmos">
  <div class="grid g12">
    <div class="card c4">
      <div class="ct">🪐 Cosmos Hub</div>
      <div class="bcenter"><div class="bignum g" id="co-block">—</div><div class="bsub">BLOCK HEIGHT</div></div>
      <div class="srow"><span class="slbl">Network</span><span class="sval g" id="co-net">—</span></div>
      <div class="srow"><span class="slbl">Version</span><span class="sval" id="co-ver">—</span></div>
      <div class="srow"><span class="slbl">Node ID</span><span style="font-family:var(--mono);font-size:9px;color:var(--muted)" id="co-id">—</span></div>
      <div class="srow"><span class="slbl">Catching Up</span><span class="badge bg" id="co-sync">CHECKING</span></div>
      <div class="srow"><span class="slbl">Block Time</span><span class="sval b" id="co-time">—</span></div>
    </div>
    <div class="card c8">
      <div class="ct">🪐 Cosmos Details</div>
      <div class="srow"><span class="slbl">Chain Data</span><span class="sval">/root/.gaia (125GB)</span></div>
      <div class="srow"><span class="slbl">Binary</span><span class="sval">/usr/local/bin/gaiad v27.1.0</span></div>
      <div class="srow"><span class="slbl">RPC Port</span><span class="sval">26657</span></div>
      <div class="srow"><span class="slbl">P2P Port</span><span class="sval">26656</span></div>
      <div class="srow"><span class="slbl">Service</span><span class="badge bg">SYSTEMCTL</span></div>
      <div class="srow"><span class="slbl">Staking Income</span><span class="badge bgo">NEEDS ATOM TOKENS</span></div>
    </div>
  </div>
</div>

<!-- CHAINLINK -->
<div class="panel" id="panel-chainlink">
  <div class="grid g12">
    <div class="card c4 cp">
      <div class="ct">🔗 Chainlink Node</div>
      <div class="bcenter"><div class="bignum p" id="cl-pass">—</div><div class="bsub">CHECKS PASSING</div></div>
      <div class="srow"><span class="slbl">Version</span><span class="sval p">2.26.0</span></div>
      <div class="srow"><span class="slbl">Network</span><span class="sval p">ETH MAINNET</span></div>
      <div class="srow"><span class="slbl">Chain ID</span><span class="sval">1</span></div>
      <div class="srow"><span class="slbl">ETH Node</span><span class="badge bgo" id="cl-eth">CHECKING</span></div>
      <div class="srow"><span class="slbl">Oracle Income</span><span class="badge bgo">NEEDS ALCHEMY KEY</span></div>
    </div>
    <div class="card c8 cp">
      <div class="ct">🔗 Health Checks</div>
      <div class="stbl"><table class="tx"><thead><tr><th>CHECK</th><th>STATUS</th><th>OUTPUT</th></tr></thead><tbody id="cl-tbl"></tbody></table></div>
    </div>
  </div>
</div>

<!-- SYSTEM -->
<div class="panel" id="panel-system">
  <div class="grid g12">
    <div class="card c4">
      <div class="ct">🖥 Server</div>
      <div class="pb-w"><div class="pb-l"><span>DISK</span><span id="sy-disk-pct">—</span></div><div class="pb"><div class="pb-f warn" id="sy-disk-bar" style="width:0%"></div></div></div>
      <div class="pb-w"><div class="pb-l"><span>RAM</span><span id="sy-ram-pct">—</span></div><div class="pb"><div class="pb-f" id="sy-ram-bar" style="width:0%"></div></div></div>
      <div class="srow"><span class="slbl">Disk Total</span><span class="sval g" id="sy-disk-total">—</span></div>
      <div class="srow"><span class="slbl">Disk Used</span><span class="sval g" id="sy-disk-used">—</span></div>
      <div class="srow"><span class="slbl">Disk Free</span><span class="sval g" id="sy-disk-free">—</span></div>
      <div class="srow"><span class="slbl">RAM Used</span><span class="sval" id="sy-ram-used">—</span></div>
      <div class="srow"><span class="slbl">Uptime</span><span class="sval b" id="sy-uptime">—</span></div>
    </div>
    <div class="card c4">
      <div class="ct">🖥 Infrastructure</div>
      <div class="srow"><span class="slbl">Provider</span><span class="sval b">Hetzner Cloud</span></div>
      <div class="srow"><span class="slbl">Plan</span><span class="sval b">CCX33</span></div>
      <div class="srow"><span class="slbl">IP</span><span class="sval">5.78.101.177</span></div>
      <div class="srow"><span class="slbl">OS</span><span class="sval">Ubuntu 24.04</span></div>
      <div class="srow"><span class="slbl">RAM</span><span class="sval">30 GB</span></div>
      <div class="srow"><span class="slbl">Storage</span><span class="sval">226 GB SSD</span></div>
      <div class="srow"><span class="slbl">Location</span><span class="sval b">Hillsboro, OR</span></div>
    </div>
    <div class="card c4">
      <div class="ct">🌐 Endpoints</div>
      <div class="srow"><span class="slbl">Main</span><span style="font-family:var(--mono);font-size:9px;color:var(--blue)">campioneinfrastructure.com</span></div>
      <div class="srow"><span class="slbl">API</span><span style="font-family:var(--mono);font-size:9px;color:var(--blue)">/api/v1/health</span></div>
      <div class="srow"><span class="slbl">Ripple Dripple</span><span style="font-family:var(--mono);font-size:9px;color:var(--blue)">api.rippledripple...</span></div>
      <div class="srow"><span class="slbl">Horizon</span><span style="font-family:var(--mono);font-size:9px;color:var(--blue)">horizon.campione...</span></div>
      <div class="srow"><span class="slbl">Chainlink UI</span><span style="font-family:var(--mono);font-size:9px;color:var(--blue)">5.78.101.177:6688</span></div>
      <div class="srow"><span class="slbl">LND P2P</span><span style="font-family:var(--mono);font-size:9px;color:var(--purple)">5.78.101.177:9735</span></div>
    </div>
  </div>
</div>

<footer>
  <div class="ftl">AUTO-REFRESH <b>30s</b> &nbsp;|&nbsp; <b id="ftime">—</b> &nbsp;|&nbsp; HETZNER CCX33 &nbsp;|&nbsp; ALL SYSTEMS LIVE</div>
  <div class="udots" id="udots"></div>
</footer>

<script>
const API = 'https://campioneinfrastructure.com';
function showTab(id){document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));document.querySelector('[onclick="showTab(\''+id+'\')"]').classList.add('active');document.getElementById('panel-'+id).classList.add('active');}
const ud=document.getElementById('udots');for(let i=0;i<30;i++){const d=document.createElement('div');d.className='udot'+(Math.random()>0.96?' m':'');ud.appendChild(d);}
function sa(a){return a?a.slice(0,8)+'...'+a.slice(-4):'—';}
function st(id){return id?id.slice(0,10)+'...':'—';}
function ago(ts){const d=Math.floor(Date.now()/1000)-ts;if(d<60)return d+'s';if(d<3600)return Math.floor(d/60)+'m';return Math.floor(d/3600)+'h';}
function fxrp(v){return parseFloat(v||0).toFixed(4)+' XRP';}
function set(id,val){const el=document.getElementById(id);if(el)el.textContent=val;}
function setClass(id,cls){const el=document.getElementById(id);if(el)el.className='badge '+cls;}
const tcls={Payment:'bg',OfferCreate:'bgo',AMMDeposit:'bgo',TrustSet:'bm',EscrowCreate:'bb',NFTokenMint:'bp'};

// XRPL WebSocket
let ws;
function cwss(){try{ws=new WebSocket('wss://xrplcluster.com');ws.onopen=()=>ws.send(JSON.stringify({command:'subscribe',streams:['transactions','ledger']}));ws.onmessage=(e)=>{try{const d=JSON.parse(e.data);if(d.type==='ledgerClosed'){const l=d.ledger_index?.toLocaleString()||'—';['ov-xrpl','xp-ledger'].forEach(id=>set(id,l));['tk-xrpl','tk-xrpl2'].forEach(id=>set(id,l));}if(d.type==='transaction'&&d.transaction){const tx=d.transaction;const type=tx.TransactionType||'?';const from=sa(tx.Account);const to=sa(tx.Destination||'');const drops=tx.Amount;const amt=drops&&typeof drops==='string'?fxrp(parseInt(drops)/1000000):'—';aof(type,from,to,amt);}}catch(err){}};ws.onclose=()=>setTimeout(cwss,5000);ws.onerror=()=>{};}catch(e){}}
cwss();
function aof(type,from,to,amt){const tb=document.getElementById('ov-feed');if(!tb)return;const tr=document.createElement('tr');const cls=tcls[type]||'bm';tr.innerHTML=`<td><span class="badge ${cls}">${type.slice(0,8)}</span></td><td class="addr">${from}</td><td class="addr">${to||'—'}</td><td class="tamt">${amt}</td><td class="tts">${new Date().toLocaleTimeString()}</td>`;tb.insertBefore(tr,tb.firstChild);while(tb.children.length>12)tb.removeChild(tb.lastChild);}

async function fa(){
  const now=new Date().toLocaleTimeString();
  set('ftime',now);set('htime',now);

  // Bitcoin
  try{const r=await fetch(API+'/api/v1/bitcoin/status');const d=await r.json();if(d.success){const b=d.data;const pct=parseFloat(b.syncProgress);set('ov-btc',parseInt(b.blocks).toLocaleString());set('ov-btc2',parseInt(b.blocks).toLocaleString());set('ov-btc-pct',pct.toFixed(2)+'%');set('bt-blocks',parseInt(b.blocks).toLocaleString());set('bt-headers',parseInt(b.headers).toLocaleString());set('bt-pct',pct.toFixed(2)+'%');set('bt-net',b.network);set('bt-pruned',b.pruned?'YES':'NO');set('bt-ph',parseInt(b.pruneHeight||0).toLocaleString());set('bt-size',((b.sizeOnDisk||0)/1024/1024/1024).toFixed(2)+' GB');set('ov-btc-pruned',b.pruned?'Pruned 550MB':'Full');const synced=pct>99.99;document.getElementById('ov-btc-bar').style.width=pct+'%';document.getElementById('bt-bar').style.width=pct+'%';setClass('ov-btc-st',synced?'bg':'bgo');set('ov-btc-st',synced?'SYNCED':'SYNCING');setClass('bt-st',synced?'bg':'bgo');set('bt-st',synced?'SYNCED':'SYNCING');setClass('sv-btc','bg');set('sv-btc','SYNCED');set('tk-btc',parseInt(b.blocks).toLocaleString());set('tk-btc2',parseInt(b.blocks).toLocaleString());}}catch(e){setClass('sv-btc','br');set('sv-btc','OFFLINE');}

  // Lightning
  try{const r=await fetch(API+'/api/v1/lightning/status');const d=await r.json();if(d.success){const b=d.data;set('ov-lnd-peers',b.numPeers);set('ov-lnd-ch',b.numActiveChannels);set('ln-peers',b.numPeers);set('ln-ver',(b.version||'').split(' ')[0]);set('ln-block',parseInt(b.blockHeight).toLocaleString());set('ln-active',b.numActiveChannels);set('ln-pending',b.numPendingChannels);set('bt-lnd-peers',b.numPeers);set('bt-lnd-ch',b.numActiveChannels);setClass('ln-sync',b.syncedToChain?'bg':'br');set('ln-sync',b.syncedToChain?'YES':'NO');setClass('ln-graph',b.syncedToGraph?'bg':'bgo');set('ln-graph',b.syncedToGraph?'YES':'SYNCING');setClass('bt-lnd-graph',b.syncedToGraph?'bg':'bgo');set('bt-lnd-graph',b.syncedToGraph?'YES':'SYNCING');set('ov-lnd-sync',b.syncedToChain?'SYNCED':'SYNCING');setClass('ov-lnd-sync',b.syncedToChain?'bg':'bgo');set('ov-lnd-pub',b.pubkey);setClass('sv-lnd','bg');set('sv-lnd','ACTIVE');['tk-lnd','tk-lnd2'].forEach(id=>set(id,b.numPeers));}}catch(e){setClass('sv-lnd','br');set('sv-lnd','OFFLINE');}

  // Lightning Balance
  try{const r=await fetch(API+'/api/v1/lightning/balance');const d=await r.json();if(d.success){const b=d.data;set('ov-lnd-bal',b.confirmedSats.toLocaleString()+' sats');set('ln-bal',b.confirmedSats.toLocaleString());set('ln-unconf',b.unconfirmedSats.toLocaleString());set('ln-chbal',b.channelBalanceSats.toLocaleString());set('bt-lnd-bal',b.confirmedSats.toLocaleString()+' sats');}}catch(e){}

  // Lightning Forwarding
  try{const r=await fetch(API+'/api/v1/lightning/forwarding');const d=await r.json();if(d.success){set('ln-fees',(d.totalFeesSats||0).toLocaleString());set('ln-routes',d.count.toLocaleString());}}catch(e){}

  // XRPL Stats
  try{const r=await fetch(API+'/api/v1/xrpl/stats');const d=await r.json();if(d.success){const s=d.data;set('ov-pay',s.totalPayments?.toLocaleString()||'—');set('ov-dex',s.dexTrades?.toLocaleString()||'—');const vol=parseFloat(s.totalVolumeXRP||0).toLocaleString()+' XRP';set('ov-vol',vol);set('xp-pay',s.totalPayments?.toLocaleString()||'—');set('xp-dex',s.dexTrades?.toLocaleString()||'—');set('xp-vol',vol);set('xp-whales',s.whaleAlerts||0);set('dx-total',s.dexTrades?.toLocaleString()||'—');setClass('sv-xrpl',s.connected?'bg':'br');set('sv-xrpl',s.connected?'CONNECTED':'OFFLINE');setClass('sv-bapi','bg');set('sv-bapi','ONLINE');['tk-pay','tk-pay2'].forEach(id=>set(id,s.totalPayments?.toLocaleString()||'—'));['tk-dex','tk-dex2'].forEach(id=>set(id,s.dexTrades?.toLocaleString()||'—'));}}catch(e){setClass('sv-bapi','br');set('sv-bapi','OFFLINE');}

  // XRPL Payments
  try{const r=await fetch(API+'/api/v1/xrpl/payments?limit=50');const d=await r.json();if(d.success&&d.data.length){const tb=document.getElementById('xp-tbl');tb.innerHTML='';d.data.forEach(p=>{const tr=document.createElement('tr');tr.innerHTML=`<td class="addr">${st(p.id)}</td><td class="addr">${sa(p.sender)}</td><td class="addr">${sa(p.receiver)}</td><td class="tamt">${fxrp(parseFloat(p.amount||0))}</td><td class="tts">${p.fee||0}</td><td class="tts">${ago(p.timestamp)}</td>`;tb.appendChild(tr);});}}catch(e){}

  // DEX Trades
  try{const r=await fetch(API+'/api/v1/xrpl/trades?limit=50');const d=await r.json();if(d.success&&d.data.length){const tb=document.getElementById('dx-tbl');tb.innerHTML='';let rs=0,rc=0;d.data.forEach(t=>{const tr=document.createElement('tr');const pair=t.pair&&t.pair.length<25?t.pair:'XRP/RUSD';tr.innerHTML=`<td class="addr">${st(t.id)}</td><td class="addr">${sa(t.account)}</td><td class="tpair">${pair}</td><td class="tamt">${parseFloat(t.takerPays||0).toFixed(4)}</td><td class="tamt b">${parseFloat(t.takerGets||0).toFixed(4)}</td><td class="trate">${parseFloat(t.rate||0).toFixed(6)}</td><td class="tts">${ago(t.timestamp)}</td>`;tb.appendChild(tr);rs+=parseFloat(t.rate||0);rc++;});if(rc>0)set('dx-rate',(rs/rc).toFixed(6));}}catch(e){}

  // Stellar
  try{const r=await fetch(API+'/api/v1/stellar/status');const d=await r.json();if(d.success){const b=d.data;set('ov-stellar-ingest',parseInt(b.ingestLatestLedger||0).toLocaleString());set('ov-stellar-hist',parseInt(b.historyLatestLedger||0).toLocaleString());set('ov-stellar-pct',b.syncProgress+'%');set('st-ingest',parseInt(b.ingestLatestLedger||0).toLocaleString());set('st-hist',parseInt(b.historyLatestLedger||0).toLocaleString());set('st-core',parseInt(b.coreLatestLedger||0).toLocaleString());set('st-ver',(b.horizonVersion||'').slice(0,14));set('st-proto',b.protocol||'—');set('st-pct',b.syncProgress+'%');document.getElementById('st-bar').style.width=Math.min(parseFloat(b.syncProgress||0),100)+'%';const synced=parseInt(b.ingestLatestLedger)>0&&parseFloat(b.syncProgress)>99;setClass('sv-stellar',synced?'bg':'bgo');set('sv-stellar',synced?'LIVE':'SYNCING');['tk-stellar'].forEach(id=>set(id,synced?'LIVE':'SYNCING '+b.syncProgress+'%'));}}catch(e){}

  // Stellar Transactions
  try{const r=await fetch(API+'/api/v1/stellar/transactions?limit=10');const d=await r.json();if(d.success&&d.data.length){const f=document.getElementById('st-feed');f.innerHTML='<div class="stbl"><table class="tx"><thead><tr><th>HASH</th><th>SOURCE</th><th>OPS</th><th>FEE</th><th>TIME</th></tr></thead><tbody id="st-tbl"></tbody></table></div>';const tb=document.getElementById('st-tbl');d.data.forEach(tx=>{const tr=document.createElement('tr');tr.innerHTML=`<td class="addr">${st(tx.hash||tx.id)}</td><td class="addr">${sa(tx.source_account)}</td><td style="color:var(--green);font-family:var(--mono)">${tx.operation_count}</td><td class="tts">${tx.fee_charged}</td><td class="tts">${new Date(tx.created_at||Date.now()).toLocaleTimeString()}</td>`;tb.appendChild(tr);});}}catch(e){}

  // Cosmos
  try{const r=await fetch(API+'/api/v1/cosmos/status');const d=await r.json();if(d.success){const b=d.data;set('ov-cosmos-block',parseInt(b.latestBlockHeight||0).toLocaleString());set('ov-cosmos-net',b.network||'—');set('ov-cosmos-sync',b.catchingUp?'YES':'NO');set('co-block',parseInt(b.latestBlockHeight||0).toLocaleString());set('co-net',b.network||'—');set('co-ver',b.version||'—');set('co-id',(b.nodeId||'').slice(0,20)+'...');set('co-time',new Date(b.latestBlockTime||Date.now()).toLocaleTimeString());setClass('co-sync',b.catchingUp?'bgo':'bg');set('co-sync',b.catchingUp?'YES':'NO');setClass('sv-cosmos',b.catchingUp?'bgo':'bg');set('sv-cosmos',b.catchingUp?'SYNCING':'SYNCED');['tk-cosmos','tk-cosmos2'].forEach(id=>set(id,parseInt(b.latestBlockHeight||0).toLocaleString()));}}catch(e){setClass('sv-cosmos','br');set('sv-cosmos','OFFLINE');}

  // Chainlink
  try{const r=await fetch('http://5.78.101.177:6688/health');const d=await r.json();if(d.data){const checks=d.data;const pass=checks.filter(c=>c.attributes?.status==='passing').length;set('cl-pass',pass+'/'+checks.length);const hl=checks.find(c=>c.id==='EVM.1.HeadTracker.HeadListener');const ethOk=hl?.attributes?.status==='passing';set('cl-eth',ethOk?'CONNECTED':'UNREACHABLE');setClass('cl-eth',ethOk?'bg':'bgo');const failing=checks.filter(c=>c.attributes?.status==='failing').length;setClass('sv-cl',failing>0?'bgo':'bg');set('sv-cl',failing>0?'WARNING':'HEALTHY');const tb=document.getElementById('cl-tbl');tb.innerHTML='';checks.forEach(c=>{const tr=document.createElement('tr');const ok=c.attributes?.status==='passing';tr.innerHTML=`<td style="color:var(--dim);font-family:var(--mono);font-size:10px">${c.attributes?.name||c.id}</td><td><span class="badge ${ok?'bg':'br'}">${(c.attributes?.status||'').toUpperCase()}</span></td><td class="tts">${c.attributes?.output||'—'}</td>`;tb.appendChild(tr);});}}catch(e){}

  // System
  try{const r=await fetch(API+'/api/v1/system/status');const d=await r.json();if(d.success){const b=d.data;const diskPct=parseInt(b.disk.usePercent||0);const ramPct=parseFloat(b.memory.usedPercent||0);set('hdr-disk',b.disk.usePercent);set('hdr-ram',ramPct.toFixed(0)+'%');set('hdr-uptime',b.uptime);set('ov-disk-pct',b.disk.usePercent);set('ov-disk-val',b.disk.used+' / '+b.disk.total);set('ov-uptime',b.uptime);set('ov-ram-pct',ramPct.toFixed(1)+'%');set('sy-disk-total',b.disk.total);set('sy-disk-used',b.disk.used);set('sy-disk-free',b.disk.free);set('sy-disk-pct',b.disk.usePercent);set('sy-uptime',b.uptime);set('sy-ram-pct',ramPct.toFixed(1)+'%');set('sy-ram-used',((b.memory.usedBytes||0)/1024/1024/1024).toFixed(1)+' GB');document.getElementById('ov-disk-bar').style.width=diskPct+'%';document.getElementById('ov-ram-bar').style.width=ramPct+'%';document.getElementById('sy-disk-bar').style.width=diskPct+'%';document.getElementById('sy-ram-bar').style.width=ramPct+'%';const dc=diskPct>85?'danger':diskPct>75?'warn':'';document.getElementById('ov-disk-bar').className='pb-f '+dc;document.getElementById('sy-disk-bar').className='pb-f '+dc;set('tk-disk',b.disk.usePercent);set('tk-disk2',b.disk.usePercent);}}catch(e){}

  // Ripple Dripple
  try{const r=await fetch('https://api.rippledripple.campioneinfrastructure.com/api/health');const d=await r.json();const ok=d.status==='healthy';setClass('sv-rd',ok?'bg':'br');set('sv-rd',ok?'HEALTHY':'OFFLINE');}catch(e){setClass('sv-rd','br');set('sv-rd','OFFLINE');}
}

fa();setInterval(fa,30000);
</script>
</body>
</html>"""

with open('/var/www/campione/status.html', 'w') as f:
    f.write(html)
print("✅ Full unified dashboard deployed!")
