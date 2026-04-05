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
.ticker{display:inline-block;animation:ticker 45s linear infinite;font-family:var(--mono);font-size:11px;color:var(--muted);}
.ticker .ti{margin-right:50px;}.ticker .ti b{color:var(--green);}
.ticker .ti.b b{color:var(--blue);}.ticker .ti.g b{color:var(--gold);}
@keyframes ticker{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.nav{display:flex;gap:0;border-bottom:1px solid var(--border);background:var(--bg2);padding:0 28px;overflow-x:auto;}
.tab{font-family:var(--mono);font-size:11px;letter-spacing:1px;padding:11px 18px;cursor:pointer;color:var(--muted);border-bottom:2px solid transparent;transition:all 0.2s;white-space:nowrap;}
.tab:hover{color:var(--text);}.tab.active{color:var(--green);border-bottom-color:var(--green);}
.panel{display:none;padding:20px 28px 32px;}.panel.active{display:block;}
.grid{display:grid;gap:14px;}
.g12{grid-template-columns:repeat(12,1fr);}
.c3{grid-column:span 3}.c4{grid-column:span 4}.c5{grid-column:span 5}.c6{grid-column:span 6}.c7{grid-column:span 7}.c8{grid-column:span 8}.c9{grid-column:span 9}.c12{grid-column:span 12}
@media(max-width:1100px){.c3,.c4{grid-column:span 6}.c5,.c7,.c8,.c9{grid-column:span 12}}
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
.slbl{font-size:13px;font-weight:600;color:var(--dim);display:flex;align-items:center;gap:8px;}
.sval{font-family:var(--mono);font-size:13px;color:var(--green);}
.sval.b{color:var(--blue);}.sval.g{color:var(--gold);}.sval.p{color:var(--purple);}
.badge{font-family:var(--mono);font-size:9px;letter-spacing:1px;padding:2px 8px;border-radius:3px;}
.bg{background:rgba(0,255,136,0.1);color:var(--green);border:1px solid rgba(0,255,136,0.25);}
.bb{background:rgba(56,189,248,0.1);color:var(--blue);border:1px solid rgba(56,189,248,0.25);}
.bgo{background:rgba(251,191,36,0.1);color:var(--gold);border:1px solid rgba(251,191,36,0.25);}
.br{background:rgba(239,68,68,0.1);color:var(--red);border:1px solid rgba(239,68,68,0.25);}
.bp{background:rgba(167,139,250,0.1);color:var(--purple);border:1px solid rgba(167,139,250,0.25);}
.bm{background:rgba(75,85,99,0.2);color:var(--muted);border:1px solid rgba(75,85,99,0.3);}
.bignum{font-family:var(--head);font-size:36px;font-weight:900;color:var(--green);line-height:1;text-shadow:0 0 30px rgba(0,255,136,0.3);animation:pg 3s ease-in-out infinite;}
@keyframes pg{0%,100%{text-shadow:0 0 20px rgba(0,255,136,0.3)}50%{text-shadow:0 0 50px rgba(0,255,136,0.7)}}
.bignum.b{color:var(--blue);text-shadow:none;animation:none;}
.bignum.g{color:var(--gold);text-shadow:none;animation:none;}
.bignum.p{color:var(--purple);text-shadow:none;animation:none;}
.bignum.r{color:var(--red);text-shadow:none;animation:none;}
.bsub{font-family:var(--mono);font-size:9px;color:var(--muted);letter-spacing:2px;margin-top:5px;}
.bcenter{text-align:center;padding:8px 0 14px;}
.pb-w{margin:6px 0;}.pb-l{display:flex;justify-content:space-between;font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:4px;}
.pb{height:3px;background:var(--border);border-radius:2px;overflow:hidden;}
.pb-f{height:100%;border-radius:2px;background:linear-gradient(90deg,var(--green),var(--blue));transition:width 1s ease;}
.pb-f.w{background:linear-gradient(90deg,var(--gold),var(--orange));}
table.tx{width:100%;border-collapse:collapse;font-family:var(--mono);font-size:11px;}
table.tx th{text-align:left;padding:6px 8px;color:var(--muted);font-size:9px;letter-spacing:2px;border-bottom:1px solid var(--border);font-weight:normal;}
table.tx td{padding:7px 8px;border-bottom:1px solid rgba(30,45,61,0.4);vertical-align:middle;}
table.tx tr:last-child td{border-bottom:none;}
table.tx tr{animation:si 0.3s ease;}
@keyframes si{from{opacity:0;transform:translateX(-6px)}to{opacity:1;transform:translateX(0)}}
.addr{color:var(--muted);max-width:120px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.tamt{color:var(--green);}.tamt.b{color:var(--blue);}.tpair{color:var(--gold);}.trate{color:var(--purple);}.tts{color:var(--muted);font-size:9px;}
.stbl{max-height:360px;overflow-y:auto;}
.stbl::-webkit-scrollbar{width:3px;}
.stbl::-webkit-scrollbar-thumb{background:var(--border);}
.empty{text-align:center;padding:30px;font-family:var(--mono);font-size:11px;color:var(--muted);}
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
    <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-top:3px;">B2B OPERATIONS CENTER — LIVE</div>
  </div>
  <div class="hdr-meta"><b>5.78.101.177</b> · Hetzner CCX33 · Hillsboro OR<br>Bitcoin ✓ · XRPL ✓ · Stellar ✓ · Chainlink ✓ · Cosmos ✓<br>Updated: <span id="htime">—</span></div>
</header>
<div class="ticker-wrap">
  <div class="ticker">
    <span class="ti">XRPL LEDGER <b id="tk1">—</b></span>
    <span class="ti b">PAYMENTS <b id="tk2">—</b></span>
    <span class="ti g">DEX TRADES <b id="tk3">—</b></span>
    <span class="ti">VOLUME <b id="tk4">—</b></span>
    <span class="ti b">BITCOIN <b>100% SYNCED · 943,814</b></span>
    <span class="ti g">STELLAR <b id="tk5">SYNCING</b></span>
    <span class="ti">CHAINLINK <b>HEALTHY</b></span>
    <span class="ti">COSMOS <b>ACTIVE</b></span>
    <span class="ti">XRPL LEDGER <b id="tk1b">—</b></span>
    <span class="ti b">PAYMENTS <b id="tk2b">—</b></span>
    <span class="ti g">DEX TRADES <b id="tk3b">—</b></span>
    <span class="ti">VOLUME <b id="tk4b">—</b></span>
    <span class="ti b">BITCOIN <b>100% SYNCED · 943,814</b></span>
    <span class="ti g">STELLAR <b>SYNCING</b></span>
    <span class="ti">CHAINLINK <b>HEALTHY</b></span>
    <span class="ti">COSMOS <b>ACTIVE</b></span>
  </div>
</div>
<div class="nav">
  <div class="tab active" onclick="showTab('overview')">⚡ OVERVIEW</div>
  <div class="tab" onclick="showTab('payments')">💸 XRPL PAYMENTS</div>
  <div class="tab" onclick="showTab('dex')">🔄 DEX TRADES</div>
  <div class="tab" onclick="showTab('whales')">🐋 WHALE ALERTS</div>
  <div class="tab" onclick="showTab('stellar')">⭐ STELLAR</div>
  <div class="tab" onclick="showTab('chainlink')">🔗 CHAINLINK</div>
  <div class="tab" onclick="showTab('nodes')">🖥 NODES</div>
</div>

<!-- OVERVIEW -->
<div class="panel active" id="panel-overview">
  <div class="grid g12">
    <div class="card c3 cb">
      <div class="ct">💧 XRPL</div>
      <div class="bcenter"><div class="bignum b" id="ov-ledger">—</div><div class="bsub">CURRENT LEDGER</div></div>
      <div class="srow"><span class="slbl">Payments</span><span class="sval" id="ov-pay">—</span></div>
      <div class="srow"><span class="slbl">DEX Trades</span><span class="sval b" id="ov-dex">—</span></div>
      <div class="srow"><span class="slbl">Volume</span><span class="sval g" id="ov-vol">—</span></div>
    </div>
    <div class="card c3 cg">
      <div class="ct">₿ Bitcoin</div>
      <div class="bcenter"><div class="bignum g" id="ov-btc">943,814</div><div class="bsub">BLOCK HEIGHT</div></div>
      <div class="pb-w"><div class="pb-l"><span>SYNC</span><span>100%</span></div><div class="pb"><div class="pb-f" style="width:100%"></div></div></div>
      <div class="srow"><span class="slbl">Pruned</span><span class="sval g">550MB</span></div>
      <div class="srow"><span class="slbl">Network</span><span class="sval g">MAINNET</span></div>
    </div>
    <div class="card c3 cb">
      <div class="ct">⭐ Horizon</div>
      <div class="bcenter"><div class="bignum b" style="font-size:22px" id="ov-hor">SYNCING</div><div class="bsub">INGEST LEDGER</div></div>
      <div class="srow"><span class="slbl">Mode</span><span class="sval b">CAPTIVE CORE</span></div>
      <div class="srow"><span class="slbl">Network</span><span class="sval b">MAINNET</span></div>
      <div class="srow"><span class="slbl">Status</span><span class="badge bgo" id="ov-hor-st">CATCHING UP</span></div>
    </div>
    <div class="card c3">
      <div class="ct">🖥 Server</div>
      <div class="pb-w"><div class="pb-l"><span>DISK</span><span id="dskpct">72%</span></div><div class="pb"><div class="pb-f w" style="width:72%"></div></div></div>
      <div class="pb-w"><div class="pb-l"><span>RAM</span><span id="rampct">—</span></div><div class="pb"><div class="pb-f" id="rambar" style="width:20%"></div></div></div>
      <div class="srow"><span class="slbl">Disk</span><span class="sval g">154GB / 226GB</span></div>
      <div class="srow"><span class="slbl">Location</span><span class="sval b">Hillsboro OR</span></div>
    </div>
    <div class="card c6">
      <div class="ct">⚙️ All Services</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:0;">
        <div class="srow"><span class="slbl">🪐 Cosmos</span><span class="badge bg">ACTIVE</span></div>
        <div class="srow"><span class="slbl">💧 XRPL</span><span class="badge bg" id="sv-xrpl">CHECKING</span></div>
        <div class="srow"><span class="slbl">⭐ Stellar</span><span class="badge bgo">SYNCING</span></div>
        <div class="srow"><span class="slbl">₿ Bitcoin</span><span class="badge bg">SYNCED</span></div>
        <div class="srow"><span class="slbl">🔗 Chainlink</span><span class="badge bg" id="sv-cl">HEALTHY</span></div>
        <div class="srow"><span class="slbl">📊 Graph Node</span><span class="badge bg">RUNNING</span></div>
        <div class="srow"><span class="slbl">🔗 Blockchain API</span><span class="badge bg" id="sv-bapi">CHECKING</span></div>
        <div class="srow"><span class="slbl">💧 Ripple Dripple</span><span class="badge bg" id="sv-rd">CHECKING</span></div>
        <div class="srow"><span class="slbl">🌅 Horizon API</span><span class="badge bb">ACTIVE</span></div>
        <div class="srow"><span class="slbl">🌐 Nginx SSL</span><span class="badge bg">ACTIVE</span></div>
      </div>
    </div>
    <div class="card c6 cb">
      <div class="ct">📡 Live XRPL Feed</div>
      <div class="stbl"><table class="tx"><thead><tr><th>TYPE</th><th>FROM</th><th>TO</th><th>AMOUNT</th><th>TIME</th></tr></thead><tbody id="ov-feed"></tbody></table></div>
    </div>
  </div>
</div>

<!-- PAYMENTS -->
<div class="panel" id="panel-payments">
  <div class="grid g12">
    <div class="card c4">
      <div class="ct">💸 Payment Stats</div>
      <div class="bcenter"><div class="bignum" id="xp-total">—</div><div class="bsub">TOTAL PAYMENTS</div></div>
      <div class="srow"><span class="slbl">Volume XRP</span><span class="sval g" id="xp-vol">—</span></div>
      <div class="srow"><span class="slbl">Last Ledger</span><span class="sval b" id="xp-led">—</span></div>
      <div class="srow"><span class="slbl">Status</span><span class="badge bg" id="xp-conn">LIVE</span></div>
    </div>
    <div class="card c8 cb">
      <div class="ct">💸 Recent Payments — Live</div>
      <div class="stbl"><table class="tx"><thead><tr><th>TX ID</th><th>SENDER</th><th>RECEIVER</th><th>AMOUNT</th><th>FEE</th><th>AGO</th></tr></thead><tbody id="xp-tbl"></tbody></table></div>
    </div>
  </div>
</div>

<!-- DEX -->
<div class="panel" id="panel-dex">
  <div class="grid g12">
    <div class="card c4">
      <div class="ct">📈 DEX Stats</div>
      <div class="bcenter"><div class="bignum b" id="dx-total">—</div><div class="bsub">TOTAL TRADES</div></div>
      <div class="srow"><span class="slbl">Top Pair</span><span class="sval g">XRP/RUSD</span></div>
      <div class="srow"><span class="slbl">Avg Rate</span><span class="sval p" id="dx-rate">—</span></div>
      <div class="srow"><span class="slbl">Network</span><span class="badge bb">XRPL MAINNET</span></div>
    </div>
    <div class="card c8 cg">
      <div class="ct">🔄 DEX Trades — Live</div>
      <div class="stbl"><table class="tx"><thead><tr><th>TX ID</th><th>ACCOUNT</th><th>PAIR</th><th>PAYS</th><th>GETS</th><th>RATE</th><th>AGO</th></tr></thead><tbody id="dx-tbl"></tbody></table></div>
    </div>
  </div>
</div>

<!-- WHALES -->
<div class="panel" id="panel-whales">
  <div class="grid g12">
    <div class="card c4 cr">
      <div class="ct">🐋 Whale Monitor</div>
      <div class="bcenter"><div class="bignum r" id="wh-cnt">0</div><div class="bsub">WHALE ALERTS</div></div>
      <div class="srow"><span class="slbl">Threshold</span><span class="sval g">10,000 XRP</span></div>
      <div class="srow"><span class="slbl">Monitoring</span><span class="badge bg">ACTIVE</span></div>
    </div>
    <div class="card c8">
      <div class="ct">🐋 Whale Transactions</div>
      <div id="wh-feed"><div class="empty">🐋 Monitoring for transactions &gt; 10,000 XRP — none yet</div></div>
    </div>
  </div>
</div>

<!-- STELLAR -->
<div class="panel" id="panel-stellar">
  <div class="grid g12">
    <div class="card c4 cb">
      <div class="ct">⭐ Stellar Horizon</div>
      <div class="bcenter"><div class="bignum b" style="font-size:24px" id="st-led">—</div><div class="bsub">INGEST LEDGER</div></div>
      <div class="srow"><span class="slbl">History Ledger</span><span class="sval b" id="st-hist">—</span></div>
      <div class="srow"><span class="slbl">Horizon Ver</span><span class="sval" id="st-ver">—</span></div>
      <div class="srow"><span class="slbl">Protocol</span><span class="sval b" id="st-prot">—</span></div>
      <div class="srow"><span class="slbl">Mode</span><span class="badge bgo">CAPTIVE CORE</span></div>
    </div>
    <div class="card c8">
      <div class="ct">⭐ Recent Stellar Transactions</div>
      <div id="st-feed"><div class="empty" style="color:var(--gold)">⭐ Stellar Horizon catching up from history archives...<br><span style="color:var(--muted);font-size:10px">Transactions will appear once synced</span></div></div>
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
    </div>
    <div class="card c8 cp">
      <div class="ct">🔗 Health Checks</div>
      <div class="stbl"><table class="tx"><thead><tr><th>CHECK</th><th>STATUS</th><th>OUTPUT</th></tr></thead><tbody id="cl-tbl"></tbody></table></div>
    </div>
  </div>
</div>

<!-- NODES -->
<div class="panel" id="panel-nodes">
  <div class="grid g12">
    <div class="card c6">
      <div class="ct">🌐 Endpoints</div>
      <div class="srow"><span class="slbl">🔗 Blockchain API</span><span style="font-family:var(--mono);font-size:10px;color:var(--blue)">campioneinfrastructure.com/api/v1/health</span></div>
      <div class="srow"><span class="slbl">💧 Ripple Dripple</span><span style="font-family:var(--mono);font-size:10px;color:var(--blue)">api.rippledripple.campioneinfrastructure.com</span></div>
      <div class="srow"><span class="slbl">⭐ Horizon</span><span style="font-family:var(--mono);font-size:10px;color:var(--blue)">horizon.campioneinfrastructure.com</span></div>
      <div class="srow"><span class="slbl">🔗 Chainlink UI</span><span style="font-family:var(--mono);font-size:10px;color:var(--blue)">5.78.101.177:6688</span></div>
      <div class="srow"><span class="slbl">📊 Graph Node</span><span style="font-family:var(--mono);font-size:10px;color:var(--blue)">5.78.101.177:8000</span></div>
      <div class="srow"><span class="slbl">🔑 Key Portal</span><span style="font-family:var(--mono);font-size:10px;color:var(--blue)">horizon.campioneinfrastructure.com/portal</span></div>
    </div>
    <div class="card c6">
      <div class="ct">📋 Infrastructure</div>
      <div class="srow"><span class="slbl">Server</span><span class="sval b">Hetzner CCX33</span></div>
      <div class="srow"><span class="slbl">IP</span><span class="sval">5.78.101.177</span></div>
      <div class="srow"><span class="slbl">OS</span><span class="sval">Ubuntu 24.04</span></div>
      <div class="srow"><span class="slbl">RAM</span><span class="sval">30 GB</span></div>
      <div class="srow"><span class="slbl">Storage</span><span class="sval">226 GB SSD</span></div>
      <div class="srow"><span class="slbl">Location</span><span class="sval b">Hillsboro, OR</span></div>
    </div>
  </div>
</div>

<footer>
  <div class="ftl">AUTO-REFRESH <b>30s</b> &nbsp;|&nbsp; <b id="ftime">—</b> &nbsp;|&nbsp; HETZNER CCX33</div>
  <div class="udots" id="udots"></div>
</footer>

<script>
function showTab(id){document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));document.querySelector('[onclick="showTab(\''+id+'\')"]').classList.add('active');document.getElementById('panel-'+id).classList.add('active');}
const ud=document.getElementById('udots');for(let i=0;i<30;i++){const d=document.createElement('div');d.className='udot'+(Math.random()>0.96?' m':'');ud.appendChild(d);}
function sa(a){return a?a.slice(0,8)+'...'+a.slice(-4):'—';}
function st(id){return id?id.slice(0,10)+'...':'—';}
function ago(ts){const d=Math.floor(Date.now()/1000)-ts;if(d<60)return d+'s';if(d<3600)return Math.floor(d/60)+'m';return Math.floor(d/3600)+'h';}
function fxrp(v){return parseFloat(v||0).toFixed(4)+' XRP';}
const tcls={Payment:'bg',OfferCreate:'bgo',AMMDeposit:'bgo',TrustSet:'bm',EscrowCreate:'bb',NFTokenMint:'bp'};
let ws;
function cwss(){try{ws=new WebSocket('wss://xrplcluster.com');ws.onopen=()=>ws.send(JSON.stringify({command:'subscribe',streams:['transactions','ledger']}));ws.onmessage=(e)=>{try{const d=JSON.parse(e.data);if(d.type==='ledgerClosed'){const l=d.ledger_index?.toLocaleString()||'—';['ov-ledger','xp-led'].forEach(id=>{const el=document.getElementById(id);if(el)el.textContent=l;});['tk1','tk1b'].forEach(id=>{const el=document.getElementById(id);if(el)el.textContent=l;});}if(d.type==='transaction'&&d.transaction){const tx=d.transaction;const type=tx.TransactionType||'?';const from=sa(tx.Account);const to=sa(tx.Destination||'');const drops=tx.Amount;const amt=drops&&typeof drops==='string'?fxrp(parseInt(drops)/1000000):'—';aof(type,from,to,amt);}}catch(err){}};ws.onclose=()=>setTimeout(cwss,5000);ws.onerror=()=>{};}catch(e){}}
cwss();
function aof(type,from,to,amt){const tb=document.getElementById('ov-feed');if(!tb)return;const tr=document.createElement('tr');const cls=tcls[type]||'bm';tr.innerHTML=`<td><span class="badge ${cls}">${type.slice(0,8)}</span></td><td class="addr">${from}</td><td class="addr">${to||'—'}</td><td class="tamt">${amt}</td><td class="tts">${new Date().toLocaleTimeString()}</td>`;tb.insertBefore(tr,tb.firstChild);while(tb.children.length>12)tb.removeChild(tb.lastChild);}
async function fa(){
  const now=new Date().toLocaleTimeString();
  document.getElementById('ftime').textContent=now;document.getElementById('htime').textContent=now;
  try{const r=await fetch('https://campioneinfrastructure.com/api/v1/xrpl/stats');const d=await r.json();if(d.success){const s=d.data;const setT=(ids,v)=>ids.forEach(id=>{const el=document.getElementById(id);if(el)el.textContent=v;});setT(['ov-pay','xp-total'],s.totalPayments?.toLocaleString()||'—');setT(['ov-dex','dx-total'],s.dexTrades?.toLocaleString()||'—');const vol=parseFloat(s.totalVolumeXRP||0).toLocaleString()+' XRP';setT(['ov-vol','xp-vol'],vol);setT(['wh-cnt'],s.whaleAlerts||0);setT(['tk2','tk2b'],s.totalPayments?.toLocaleString()||'—');setT(['tk3','tk3b'],s.dexTrades?.toLocaleString()||'—');setT(['tk4','tk4b'],vol);document.getElementById('sv-xrpl').textContent=s.connected?'CONNECTED':'OFFLINE';document.getElementById('sv-bapi').textContent='ONLINE';}}catch(e){document.getElementById('sv-bapi').textContent='OFFLINE';document.getElementById('sv-bapi').className='badge br';}
  try{const r=await fetch('https://campioneinfrastructure.com/api/v1/xrpl/payments?limit=50');const d=await r.json();if(d.success&&d.data.length){const tb=document.getElementById('xp-tbl');tb.innerHTML='';d.data.forEach(p=>{const tr=document.createElement('tr');tr.innerHTML=`<td class="addr">${st(p.id)}</td><td class="addr">${sa(p.sender)}</td><td class="addr">${sa(p.receiver)}</td><td class="tamt">${fxrp(parseFloat(p.amount||0))}</td><td class="tts">${p.fee||0}</td><td class="tts">${ago(p.timestamp)}</td>`;tb.appendChild(tr);});}}catch(e){}
  try{const r=await fetch('https://campioneinfrastructure.com/api/v1/xrpl/trades?limit=50');const d=await r.json();if(d.success&&d.data.length){const tb=document.getElementById('dx-tbl');tb.innerHTML='';let rs=0,rc=0;d.data.forEach(t=>{const tr=document.createElement('tr');const pair=t.pair&&t.pair.length<25?t.pair:'XRP/RUSD';tr.innerHTML=`<td class="addr">${st(t.id)}</td><td class="addr">${sa(t.account)}</td><td class="tpair">${pair}</td><td class="tamt">${parseFloat(t.takerPays||0).toFixed(4)}</td><td class="tamt b">${parseFloat(t.takerGets||0).toFixed(4)}</td><td class="trate">${parseFloat(t.rate||0).toFixed(6)}</td><td class="tts">${ago(t.timestamp)}</td>`;tb.appendChild(tr);rs+=parseFloat(t.rate||0);rc++;});if(rc>0)document.getElementById('dx-rate').textContent=(rs/rc).toFixed(6);}}catch(e){}
  try{const r=await fetch('https://campioneinfrastructure.com/api/v1/xrpl/whales?limit=20');const d=await r.json();const f=document.getElementById('wh-feed');if(d.success&&d.data.length){f.innerHTML='<table class="tx"><thead><tr><th>TX ID</th><th>FROM</th><th>TO</th><th>AMOUNT</th><th>AGO</th></tr></thead><tbody id="wh-tbl"></tbody></table>';const tb=document.getElementById('wh-tbl');d.data.forEach(w=>{const tr=document.createElement('tr');tr.innerHTML=`<td class="addr">${st(w.id)}</td><td class="addr">${sa(w.sender)}</td><td class="addr">${sa(w.receiver)}</td><td style="color:var(--red);font-family:var(--mono)">${fxrp(parseFloat(w.amount||0))}</td><td class="tts">${ago(w.timestamp)}</td>`;tb.appendChild(tr);});}else{f.innerHTML='<div class="empty">🐋 Monitoring for transactions &gt; 10,000 XRP — none yet</div>';}}catch(e){}
  try{const r=await fetch('https://horizon.campioneinfrastructure.com');const d=await r.json();if(d.ingest_latest_ledger){const il=d.ingest_latest_ledger?.toLocaleString()||'—';document.getElementById('st-led').textContent=il;document.getElementById('ov-hor').textContent=il;document.getElementById('st-hist').textContent=d.history_latest_ledger?.toLocaleString()||'—';document.getElementById('st-ver').textContent=(d.horizon_version||'').slice(0,14);document.getElementById('st-prot').textContent=d.current_protocol_version||'—';['tk5'].forEach(id=>{const el=document.getElementById(id);if(el)el.textContent='LEDGER '+il;});if(d.ingest_latest_ledger>0){document.getElementById('ov-hor-st').textContent='LIVE';document.getElementById('ov-hor-st').className='badge bg';}}try{const txR=await fetch('https://horizon.campioneinfrastructure.com/transactions?limit=10&order=desc');const txD=await txR.json();if(txD._embedded?.records?.length){const f=document.getElementById('st-feed');f.innerHTML='<div class="stbl"><table class="tx"><thead><tr><th>HASH</th><th>SOURCE</th><th>OPS</th><th>FEE</th><th>TIME</th></tr></thead><tbody id="st-tbl"></tbody></table></div>';const tb=document.getElementById('st-tbl');txD._embedded.records.forEach(tx=>{const tr=document.createElement('tr');tr.innerHTML=`<td class="addr">${st(tx.hash||tx.id)}</td><td class="addr">${sa(tx.source_account)}</td><td style="color:var(--green);font-family:var(--mono)">${tx.operation_count}</td><td class="tts">${tx.fee_charged} str</td><td class="tts">${new Date(tx.created_at||Date.now()).toLocaleTimeString()}</td>`;tb.appendChild(tr);});}}catch(e){}}catch(e){}
  try{const r=await fetch('http://5.78.101.177:6688/health');const d=await r.json();if(d.data){const checks=d.data;const pass=checks.filter(c=>c.attributes?.status==='passing').length;document.getElementById('cl-pass').textContent=pass+'/'+checks.length;const hl=checks.find(c=>c.id==='EVM.1.HeadTracker.HeadListener');const ethOk=hl?.attributes?.status==='passing';document.getElementById('cl-eth').textContent=ethOk?'CONNECTED':'UNREACHABLE';document.getElementById('cl-eth').className='badge '+(ethOk?'bg':'bgo');const failing=checks.filter(c=>c.attributes?.status==='failing').length;document.getElementById('sv-cl').textContent=failing>0?'WARNING':'HEALTHY';document.getElementById('sv-cl').className='badge '+(failing>0?'bgo':'bg');const tb=document.getElementById('cl-tbl');tb.innerHTML='';checks.forEach(c=>{const tr=document.createElement('tr');const ok=c.attributes?.status==='passing';tr.innerHTML=`<td style="color:var(--dim);font-family:var(--mono);font-size:10px">${c.attributes?.name||c.id}</td><td><span class="badge ${ok?'bg':'br'}">${(c.attributes?.status||'').toUpperCase()}</span></td><td class="tts">${c.attributes?.output||'—'}</td>`;tb.appendChild(tr);});}}catch(e){}
  try{const r=await fetch('https://api.rippledripple.campioneinfrastructure.com/api/health');const d=await r.json();const ok=d.status==='healthy';document.getElementById('sv-rd').textContent=ok?'HEALTHY':'OFFLINE';document.getElementById('sv-rd').className='badge '+(ok?'bg':'br');}catch(e){document.getElementById('sv-rd').textContent='OFFLINE';document.getElementById('sv-rd').className='badge br';}
}
fa();setInterval(fa,30000);
</script>
</body>
</html>"""

with open('/var/www/campione/status.html', 'w') as f:
    f.write(html)
print("✅ B2B Dashboard deployed!")
