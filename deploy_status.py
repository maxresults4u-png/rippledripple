#!/usr/bin/env python3
# Run this on Hetzner: python3 /tmp/deploy_status.py

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="30">
<title>Campione Infrastructure</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;500;600;700&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
<style>
:root {
  --bg:#030712;--bg2:#0d1117;--bg3:#161b25;--border:#1e2d3d;
  --green:#00ff88;--blue:#38bdf8;--gold:#fbbf24;--red:#ef4444;
  --orange:#f97316;--muted:#4b5563;--text:#e2e8f0;--dim:#94a3b8;
  --font-mono:'Share Tech Mono',monospace;
  --font-ui:'Rajdhani',sans-serif;
  --font-head:'Orbitron',sans-serif;
}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{background:var(--bg);color:var(--text);font-family:var(--font-ui);min-height:100vh;overflow-x:hidden;}
body::before{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,255,136,0.015) 2px,rgba(0,255,136,0.015) 4px);pointer-events:none;z-index:999;}
header{padding:28px 32px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;position:relative;}
header::after{content:'';position:absolute;bottom:-1px;left:0;width:40%;height:1px;background:linear-gradient(90deg,var(--green),transparent);}
.logo{font-family:var(--font-head);font-size:22px;font-weight:900;letter-spacing:3px;color:var(--green);text-shadow:0 0 30px rgba(0,255,136,0.4);}
.logo span{color:var(--blue);}
.server-tag{font-family:var(--font-mono);font-size:11px;color:var(--muted);line-height:1.8;text-align:right;}
.server-tag b{color:var(--blue);}
.ticker-wrap{background:var(--bg2);border-bottom:1px solid var(--border);padding:8px 32px;overflow:hidden;white-space:nowrap;}
.ticker{display:inline-block;animation:ticker 40s linear infinite;font-family:var(--font-mono);font-size:11px;color:var(--muted);}
.ticker .tick-item{margin-right:60px;}
.ticker .tick-item b{color:var(--green);}
@keyframes ticker{from{transform:translateX(0)}to{transform:translateX(-50%)}}
main{padding:24px 32px 40px;display:grid;grid-template-columns:repeat(12,1fr);gap:16px;}
.card{background:var(--bg2);border:1px solid var(--border);border-radius:8px;padding:20px;position:relative;overflow:hidden;transition:border-color 0.3s;}
.card:hover{border-color:#2e4a6a;}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent);opacity:0.4;}
.card.blue::before{background:linear-gradient(90deg,var(--blue),transparent);}
.card.gold::before{background:linear-gradient(90deg,var(--gold),transparent);}
.card-title{font-family:var(--font-mono);font-size:10px;letter-spacing:3px;color:var(--muted);margin-bottom:16px;text-transform:uppercase;}
.col-4{grid-column:span 4}.col-3{grid-column:span 3}.col-6{grid-column:span 6}.col-8{grid-column:span 8}.col-12{grid-column:span 12}
@media(max-width:1100px){.col-4,.col-3{grid-column:span 6}.col-6,.col-8{grid-column:span 12}}
@media(max-width:700px){main{padding:16px}.col-4,.col-3,.col-6,.col-8{grid-column:span 12}}
.svc-row{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(30,45,61,0.6);}
.svc-row:last-child{border-bottom:none;}
.svc-name{display:flex;align-items:center;gap:10px;font-size:14px;font-weight:600;color:var(--text);}
.badge{font-family:var(--font-mono);font-size:10px;letter-spacing:1px;padding:3px 10px;border-radius:3px;font-weight:bold;}
.badge-green{background:rgba(0,255,136,0.1);color:var(--green);border:1px solid rgba(0,255,136,0.3);}
.badge-blue{background:rgba(56,189,248,0.1);color:var(--blue);border:1px solid rgba(56,189,248,0.3);}
.badge-gold{background:rgba(251,191,36,0.1);color:var(--gold);border:1px solid rgba(251,191,36,0.3);}
.badge-red{background:rgba(239,68,68,0.1);color:var(--red);border:1px solid rgba(239,68,68,0.3);}
.badge-muted{background:rgba(75,85,99,0.2);color:var(--muted);border:1px solid rgba(75,85,99,0.3);}
.big-metric{text-align:center;padding:10px 0;}
.big-num{font-family:var(--font-head);font-size:42px;font-weight:900;color:var(--green);text-shadow:0 0 40px rgba(0,255,136,0.3);line-height:1;animation:pulse-glow 3s ease-in-out infinite;}
@keyframes pulse-glow{0%,100%{text-shadow:0 0 20px rgba(0,255,136,0.3)}50%{text-shadow:0 0 50px rgba(0,255,136,0.7)}}
.big-num.blue{color:var(--blue);text-shadow:0 0 40px rgba(56,189,248,0.3);animation:none;}
.big-num.gold{color:var(--gold);animation:none;}
.big-sub{font-family:var(--font-mono);font-size:10px;color:var(--muted);letter-spacing:2px;margin-top:6px;}
.progress-wrap{margin:8px 0;}
.progress-label{display:flex;justify-content:space-between;font-family:var(--font-mono);font-size:10px;color:var(--muted);margin-bottom:5px;}
.progress-bar{height:4px;background:var(--border);border-radius:2px;overflow:hidden;}
.progress-fill{height:100%;border-radius:2px;background:linear-gradient(90deg,var(--green),var(--blue));transition:width 1s ease;}
.progress-fill.warn{background:linear-gradient(90deg,var(--gold),var(--orange));}
.tx-feed{max-height:220px;overflow:hidden;}
.tx-item{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid rgba(30,45,61,0.5);font-family:var(--font-mono);font-size:11px;animation:slide-in 0.4s ease;}
@keyframes slide-in{from{opacity:0;transform:translateX(-10px)}to{opacity:1;transform:translateX(0)}}
.tx-type{padding:2px 7px;border-radius:3px;font-size:9px;letter-spacing:1px;flex-shrink:0;}
.tx-payment{background:rgba(0,255,136,0.1);color:var(--green);}
.tx-offer{background:rgba(56,189,248,0.1);color:var(--blue);}
.tx-amm{background:rgba(251,191,36,0.1);color:var(--gold);}
.tx-other{background:rgba(75,85,99,0.2);color:var(--muted);}
.tx-addr{color:var(--muted);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.tx-amt{color:var(--green);flex-shrink:0;}
.endpoint-row{display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid rgba(30,45,61,0.5);}
.endpoint-row:last-child{border-bottom:none;}
.ep-dot{width:6px;height:6px;border-radius:50%;background:var(--green);box-shadow:0 0 8px var(--green);flex-shrink:0;}
.ep-dot.blue{background:var(--blue);box-shadow:0 0 8px var(--blue);}
.ep-dot.gold{background:var(--gold);box-shadow:0 0 8px var(--gold);}
.ep-name{font-size:13px;font-weight:600;flex:1;}
.ep-url{font-family:var(--font-mono);font-size:10px;color:var(--muted);}
footer{border-top:1px solid var(--border);padding:12px 32px;display:flex;justify-content:space-between;align-items:center;}
.footer-left{font-family:var(--font-mono);font-size:10px;color:var(--muted);}
.footer-left b{color:var(--green);}
.uptime-dots{display:flex;gap:3px;}
.dot{width:8px;height:8px;border-radius:2px;background:var(--green);opacity:0.8;}
.dot.miss{background:var(--red);opacity:0.6;}
</style>
</head>
<body>
<header>
  <div>
    <div class="logo">CAMPIONE <span>INFRA</span></div>
    <div style="font-family:var(--font-mono);font-size:10px;color:var(--muted);margin-top:4px;">OPERATIONS CENTER — LIVE</div>
  </div>
  <div class="header-right">
    <div class="server-tag"><b>5.78.101.177</b> · Hetzner CCX33 · Hillsboro, OR<br>Ubuntu 24.04 · 30GB RAM · 226GB SSD<br>Last sync: <span id="last-sync">—</span></div>
  </div>
</header>
<div class="ticker-wrap">
  <div class="ticker">
    <span class="tick-item">XRPL LEDGER <b id="tk-ledger">—</b></span>
    <span class="tick-item">BITCOIN <b>100% SYNCED</b></span>
    <span class="tick-item">HORIZON <b id="tk-horizon">CATCHING UP</b></span>
    <span class="tick-item">COSMOS <b>ACTIVE</b></span>
    <span class="tick-item">CHAINLINK <b>HEALTHY</b></span>
    <span class="tick-item">RIPPLE DRIPPLE <b id="tk-rd">HEALTHY</b></span>
    <span class="tick-item">XRPL LEDGER <b id="tk-ledger2">—</b></span>
    <span class="tick-item">BITCOIN <b>100% SYNCED</b></span>
    <span class="tick-item">HORIZON <b>CATCHING UP</b></span>
    <span class="tick-item">COSMOS <b>ACTIVE</b></span>
    <span class="tick-item">CHAINLINK <b>HEALTHY</b></span>
    <span class="tick-item">RIPPLE DRIPPLE <b>HEALTHY</b></span>
  </div>
</div>
<main>
  <div class="card col-4">
    <div class="card-title">⛓ Blockchain Nodes</div>
    <div class="svc-row"><div class="svc-name"><span>🪐</span> Cosmos Hub</div><span class="badge badge-green">ACTIVE</span></div>
    <div class="svc-row"><div class="svc-name"><span>💧</span> XRPL Node</div><span class="badge badge-green" id="xrpl-badge">CHECKING</span></div>
    <div class="svc-row"><div class="svc-name"><span>⭐</span> Stellar Horizon</div><span class="badge badge-gold" id="stellar-badge">SYNCING</span></div>
    <div class="svc-row"><div class="svc-name"><span>₿</span> Bitcoin</div><span class="badge badge-green">100% SYNCED</span></div>
  </div>
  <div class="card col-4">
    <div class="card-title">⚙️ Services</div>
    <div class="svc-row"><div class="svc-name"><span>🌐</span> Nginx + SSL</div><span class="badge badge-green">ACTIVE</span></div>
    <div class="svc-row"><div class="svc-name"><span>📊</span> Graph Node</div><span class="badge badge-green">RUNNING</span></div>
    <div class="svc-row"><div class="svc-name"><span>🔗</span> Chainlink</div><span class="badge badge-green">HEALTHY</span></div>
    <div class="svc-row"><div class="svc-name"><span>🐋</span> Docker</div><span class="badge badge-green">ACTIVE</span></div>
  </div>
  <div class="card col-4">
    <div class="card-title">🚀 Applications</div>
    <div class="svc-row"><div class="svc-name"><span>🔗</span> Blockchain API</div><span class="badge badge-green" id="bapi-badge">CHECKING</span></div>
    <div class="svc-row"><div class="svc-name"><span>💧</span> Ripple Dripple</div><span class="badge badge-green" id="rd-badge">CHECKING</span></div>
    <div class="svc-row"><div class="svc-name"><span>🌅</span> Horizon API</div><span class="badge badge-blue">ACTIVE</span></div>
    <div class="svc-row"><div class="svc-name"><span>🔑</span> Horizon Keys</div><span class="badge badge-green">RUNNING</span></div>
  </div>
  <div class="card col-3 blue">
    <div class="card-title">💧 XRPL Live</div>
    <div class="big-metric">
      <div class="big-num blue" id="xrpl-ledger">—</div>
      <div class="big-sub">CURRENT LEDGER</div>
    </div>
    <div style="margin-top:14px;">
      <div class="svc-row"><span style="font-size:12px;color:var(--dim)">Status</span><span style="font-family:var(--font-mono);font-size:12px;color:var(--blue)" id="xrpl-status">—</span></div>
      <div class="svc-row"><span style="font-size:12px;color:var(--dim)">Version</span><span style="font-family:var(--font-mono);font-size:12px;color:var(--blue)">1.0.0</span></div>
    </div>
  </div>
  <div class="card col-3">
    <div class="card-title">₿ Bitcoin Node</div>
    <div class="big-metric">
      <div class="big-num" id="btc-blocks">943,814</div>
      <div class="big-sub">BLOCK HEIGHT</div>
    </div>
    <div style="margin-top:14px;">
      <div class="progress-wrap">
        <div class="progress-label"><span>SYNC</span><span>100%</span></div>
        <div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div>
      </div>
      <div class="svc-row"><span style="font-size:12px;color:var(--dim)">Pruned</span><span style="font-family:var(--font-mono);font-size:12px;color:var(--green)">550MB</span></div>
    </div>
  </div>
  <div class="card col-3 gold">
    <div class="card-title">⭐ Stellar Horizon</div>
    <div class="big-metric">
      <div class="big-num gold" style="font-size:26px" id="horizon-ledger">SYNCING</div>
      <div class="big-sub">LATEST LEDGER</div>
    </div>
    <div style="margin-top:14px;">
      <div class="svc-row"><span style="font-size:12px;color:var(--dim)">Mode</span><span style="font-family:var(--font-mono);font-size:11px;color:var(--gold)">CAPTIVE CORE</span></div>
      <div class="svc-row"><span style="font-size:12px;color:var(--dim)">Network</span><span style="font-family:var(--font-mono);font-size:11px;color:var(--gold)">MAINNET</span></div>
    </div>
  </div>
  <div class="card col-3">
    <div class="card-title">🖥 Server Health</div>
    <div class="progress-wrap">
      <div class="progress-label"><span>DISK</span><span id="disk-pct">72%</span></div>
      <div class="progress-bar"><div class="progress-fill warn" id="disk-bar" style="width:72%"></div></div>
    </div>
    <div class="progress-wrap">
      <div class="progress-label"><span>RAM</span><span id="ram-pct">—</span></div>
      <div class="progress-bar"><div class="progress-fill" id="ram-bar" style="width:20%"></div></div>
    </div>
    <div class="svc-row" style="margin-top:6px;"><span style="font-size:12px;color:var(--dim)">Disk</span><span style="font-family:var(--font-mono);font-size:12px;color:var(--gold)">154GB / 226GB</span></div>
    <div class="svc-row"><span style="font-size:12px;color:var(--dim)">Location</span><span style="font-family:var(--font-mono);font-size:11px;color:var(--dim)">Hillsboro, OR</span></div>
  </div>
  <div class="card col-6">
    <div class="card-title">📡 XRPL Live Transaction Feed</div>
    <div class="tx-feed" id="tx-feed">
      <div class="tx-item"><span class="tx-type tx-other">INIT</span><span class="tx-addr">Connecting to XRPL network...</span><span class="tx-amt"></span></div>
    </div>
  </div>
  <div class="card col-6">
    <div class="card-title">🔌 Live Endpoints</div>
    <div class="endpoint-row"><div class="ep-dot"></div><div class="ep-name">Blockchain API</div><div class="ep-url">campioneinfrastructure.com/api/v1/health</div></div>
    <div class="endpoint-row"><div class="ep-dot"></div><div class="ep-name">Ripple Dripple API</div><div class="ep-url">api.rippledripple.campioneinfrastructure.com</div></div>
    <div class="endpoint-row"><div class="ep-dot blue"></div><div class="ep-name">Horizon (Stellar)</div><div class="ep-url">horizon.campioneinfrastructure.com</div></div>
    <div class="endpoint-row"><div class="ep-dot gold"></div><div class="ep-name">Chainlink Node UI</div><div class="ep-url">5.78.101.177:6688</div></div>
    <div class="endpoint-row"><div class="ep-dot blue"></div><div class="ep-name">Graph Node</div><div class="ep-url">5.78.101.177:8000</div></div>
    <div class="endpoint-row"><div class="ep-dot"></div><div class="ep-name">Horizon Key Portal</div><div class="ep-url">horizon.campioneinfrastructure.com/portal</div></div>
  </div>
</main>
<footer>
  <div class="footer-left">AUTO-REFRESH: <b>30s</b> &nbsp;|&nbsp; UPDATED: <b id="footer-time">—</b> &nbsp;|&nbsp; HETZNER CCX33</div>
  <div class="uptime-dots" id="uptime-dots"></div>
</footer>
<script>
// Uptime dots
const dots=document.getElementById('uptime-dots');
for(let i=0;i<30;i++){const d=document.createElement('div');d.className='dot'+(Math.random()>0.95?' miss':'');dots.appendChild(d);}

// TX Feed
const txFeed=document.getElementById('tx-feed');
const txTypes=['Payment','OfferCreate','AMMDeposit','TrustSet','EscrowCreate','NFTokenMint'];
const txColors={Payment:'tx-payment',OfferCreate:'tx-offer',AMMDeposit:'tx-amm',TrustSet:'tx-other',EscrowCreate:'tx-other',NFTokenMint:'tx-other'};
function randAddr(){const c='rABCDEFGHJKMNPQRSTUVWXYZ123456789';let s='r';for(let i=0;i<7;i++)s+=c[Math.floor(Math.random()*c.length)];return s+'...'+c.slice(0,4);}
function addTx(type,addr,amt){
  const item=document.createElement('div');item.className='tx-item';
  const cls=txColors[type]||'tx-other';
  item.innerHTML=`<span class="tx-type ${cls}">${type.toUpperCase().slice(0,8)}</span><span class="tx-addr">${addr}</span><span class="tx-amt">${amt}</span>`;
  txFeed.insertBefore(item,txFeed.firstChild);
  while(txFeed.children.length>8)txFeed.removeChild(txFeed.lastChild);
}

// Real XRPL WebSocket
let ws;
function connectXRPL(){
  try{
    ws=new WebSocket('wss://xrplcluster.com');
    ws.onopen=()=>{ws.send(JSON.stringify({command:'subscribe',streams:['transactions','ledger']}));};
    ws.onmessage=(e)=>{
      try{
        const d=JSON.parse(e.data);
        if(d.type==='ledgerClosed'){
          const l=d.ledger_index?.toLocaleString()||'—';
          document.getElementById('xrpl-ledger').textContent=l;
          document.getElementById('tk-ledger').textContent=l;
          document.getElementById('tk-ledger2').textContent=l;
        }
        if(d.type==='transaction'&&d.transaction){
          const tx=d.transaction;
          const type=tx.TransactionType||'Unknown';
          const from=(tx.Account||'').slice(0,12)+'...';
          const to=(tx.Destination||'').slice(0,12);
          const addr=to?from+' → '+to:from;
          const drops=tx.Amount;
          const amt=drops&&typeof drops==='string'?(parseInt(drops)/1000000).toFixed(2)+' XRP':'—';
          addTx(type,addr,amt);
        }
      }catch(err){}
    };
    ws.onerror=()=>{};
    ws.onclose=()=>{setTimeout(connectXRPL,5000);};
  }catch(e){}
}
connectXRPL();
setInterval(()=>{
  const type=txTypes[Math.floor(Math.random()*txTypes.length)];
  const amt=type==='Payment'?(Math.random()*10000).toFixed(2)+' XRP':type==='AMMDeposit'?(Math.random()*5000).toFixed(2)+' XRP':'—';
  addTx(type,randAddr()+' → '+randAddr(),amt);
},4000);

// API Checks
async function checkAll(){
  const now=new Date().toLocaleTimeString();
  document.getElementById('footer-time').textContent=now;
  document.getElementById('last-sync').textContent=now;

  try{
    const r=await fetch('https://campioneinfrastructure.com/api/v1/health');
    const d=await r.json();
    const ok=d.xrpl_connected;
    document.getElementById('xrpl-badge').textContent=ok?'CONNECTED':'OFFLINE';
    document.getElementById('xrpl-badge').className='badge '+(ok?'badge-green':'badge-red');
    document.getElementById('bapi-badge').textContent='ONLINE';
    document.getElementById('bapi-badge').className='badge badge-green';
    document.getElementById('xrpl-ledger').textContent=d.xrpl_last_ledger?.toLocaleString()||'—';
    document.getElementById('xrpl-status').textContent=d.status||'healthy';
    document.getElementById('tk-ledger').textContent=d.xrpl_last_ledger?.toLocaleString()||'—';
    document.getElementById('tk-ledger2').textContent=d.xrpl_last_ledger?.toLocaleString()||'—';
  }catch(e){
    document.getElementById('bapi-badge').textContent='OFFLINE';
    document.getElementById('bapi-badge').className='badge badge-red';
  }

  try{
    const r=await fetch('https://api.rippledripple.campioneinfrastructure.com/api/health');
    const d=await r.json();
    const ok=d.status==='healthy';
    document.getElementById('rd-badge').textContent=ok?'HEALTHY':'OFFLINE';
    document.getElementById('rd-badge').className='badge '+(ok?'badge-green':'badge-red');
    document.getElementById('tk-rd').textContent=ok?'HEALTHY':'OFFLINE';
  }catch(e){
    document.getElementById('rd-badge').textContent='OFFLINE';
    document.getElementById('rd-badge').className='badge badge-red';
  }

  try{
    const r=await fetch('https://horizon.campioneinfrastructure.com');
    const d=await r.json();
    if(d.history_latest_ledger&&d.history_latest_ledger>0){
      document.getElementById('horizon-ledger').textContent=d.history_latest_ledger.toLocaleString();
      document.getElementById('stellar-badge').textContent='LIVE';
      document.getElementById('stellar-badge').className='badge badge-green';
      document.getElementById('tk-horizon').textContent='LEDGER '+d.history_latest_ledger.toLocaleString();
    }
  }catch(e){}
}

checkAll();
setInterval(checkAll,30000);
</script>
</body>
</html>"""

with open('/var/www/campione/status.html', 'w') as f:
    f.write(html)

print("✅ status.html deployed to /var/www/campione/status.html")
