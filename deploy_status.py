#!/usr/bin/env python3
html = open('/var/www/campione/status.html').read()

# Add tab button
if "showTab('api')" not in html:
    html = html.replace(
        "<div class=\"tab\" onclick=\"showTab('income')\">💰 INCOME</div>",
        "<div class=\"tab\" onclick=\"showTab('income')\">💰 INCOME</div>\n  <div class=\"tab\" onclick=\"showTab('api')\">🚀 API</div>"
    )

# Remove old api panel if exists
import re
html = re.sub(r'<!-- API SHOWCASE -->.*?(?=<!-- |\Z)', '', html, flags=re.DOTALL)

api_panel = """
<!-- API TAB -->
<div class="panel" id="panel-api">
<style>
.api-tabs{display:flex;gap:0;border-bottom:1px solid var(--border);margin-bottom:14px;overflow-x:auto;}
.api-tab{font-family:var(--mono);font-size:10px;letter-spacing:1px;padding:9px 14px;cursor:pointer;color:var(--muted);border-bottom:2px solid transparent;white-space:nowrap;}
.api-tab:hover{color:var(--text);}.api-tab.on{color:var(--blue);border-bottom-color:var(--blue);}
.apanel{display:none;}.apanel.on{display:block;}
.ajson{background:rgba(0,0,0,0.4);border-radius:4px;padding:12px;font-family:var(--mono);font-size:10px;line-height:1.7;overflow-x:auto;max-height:280px;overflow-y:auto;border:1px solid var(--border);}
.ajson .jk{color:var(--blue);}.ajson .jv{color:var(--green);}.ajson .jn{color:var(--gold);}.ajson .jb{color:var(--red);}
</style>
  <div class="grid g12">
    <div class="card c12" style="padding:14px 20px;border-color:rgba(56,189,248,0.25);">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
        <div>
          <div style="font-family:var(--head);font-size:18px;font-weight:900;color:var(--blue);">Campione Blockchain API — Live Customer View</div>
          <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-top:3px;">This is exactly what your paying customers see — real data from your nodes</div>
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;">
          <div class="card cb" style="padding:10px 16px;margin:0;text-align:center;">
            <div style="font-family:var(--mono);font-size:9px;color:var(--muted);">XRPL PAYMENTS</div>
            <div style="font-family:var(--head);font-size:20px;color:var(--blue)" id="ap-pay">—</div>
          </div>
          <div class="card cg" style="padding:10px 16px;margin:0;text-align:center;">
            <div style="font-family:var(--mono);font-size:9px;color:var(--muted);">DEX TRADES</div>
            <div style="font-family:var(--head);font-size:20px;color:var(--green)" id="ap-dex">—</div>
          </div>
          <div class="card" style="padding:10px 16px;margin:0;text-align:center;">
            <div style="font-family:var(--mono);font-size:9px;color:var(--muted);">WHALE ALERTS</div>
            <div style="font-family:var(--head);font-size:20px;color:var(--red)" id="ap-whale">—</div>
          </div>
          <div class="card" style="padding:10px 16px;margin:0;text-align:center;">
            <div style="font-family:var(--mono);font-size:9px;color:var(--muted);">XRPL LEDGER</div>
            <div style="font-family:var(--head);font-size:20px;color:var(--text)" id="ap-led">—</div>
          </div>
        </div>
      </div>
    </div>

    <div class="card c12">
      <div class="api-tabs">
        <div class="api-tab on" onclick="swapi(this,'payments')">💸 XRPL PAYMENTS</div>
        <div class="api-tab" onclick="swapi(this,'dex')">🔄 DEX TRADES</div>
        <div class="api-tab" onclick="swapi(this,'whales')">🐋 WHALE ALERTS</div>
        <div class="api-tab" onclick="swapi(this,'bitcoin')">₿ BITCOIN</div>
        <div class="api-tab" onclick="swapi(this,'cosmos')">🪐 COSMOS</div>
        <div class="api-tab" onclick="swapi(this,'lightning')">⚡ LIGHTNING</div>
        <div class="api-tab" onclick="swapi(this,'stellar')">⭐ STELLAR</div>
        <div class="api-tab" onclick="swapi(this,'rawjson')">{ } RAW JSON</div>
      </div>

      <!-- PAYMENTS -->
      <div class="apanel on" id="ap-payments">
        <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:8px;">ENDPOINT: GET /api/v1/xrpl/payments — what trading bots and wallet apps pay for</div>
        <div class="stbl"><table class="tx"><thead><tr><th>TX HASH</th><th>FROM</th><th>TO</th><th>AMOUNT</th><th>CURRENCY</th><th>FEE</th><th>AGO</th></tr></thead><tbody id="apt-pay"></tbody></table></div>
      </div>

      <!-- DEX -->
      <div class="apanel" id="ap-dex-panel">
        <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:8px;">ENDPOINT: GET /api/v1/xrpl/trades — what DeFi analytics dashboards pay for</div>
        <div class="stbl"><table class="tx"><thead><tr><th>TX HASH</th><th>ACCOUNT</th><th>PAIR</th><th>PAYS</th><th>GETS</th><th>RATE</th><th>AGO</th></tr></thead><tbody id="apt-dex"></tbody></table></div>
      </div>

      <!-- WHALES -->
      <div class="apanel" id="ap-whales-panel">
        <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:8px;">ENDPOINT: GET /api/v1/xrpl/whales — what compliance and AML tools pay for</div>
        <div id="apt-whale"><div class="empty" style="color:var(--gold)">🐋 Monitoring for transactions over 10,000 XRP...</div></div>
      </div>

      <!-- BITCOIN -->
      <div class="apanel" id="ap-bitcoin">
        <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:8px;">ENDPOINT: GET /api/v1/bitcoin/status</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
          <div>
            <div class="srow"><span class="slbl">Block height</span><span class="sval g" id="abt-blocks">—</span></div>
            <div class="srow"><span class="slbl">Sync progress</span><span class="sval g" id="abt-sync">—</span></div>
            <div class="srow"><span class="slbl">Network</span><span class="sval g" id="abt-net">—</span></div>
            <div class="srow"><span class="slbl">Pruned</span><span class="sval g" id="abt-pruned">—</span></div>
            <div class="srow"><span class="slbl">Disk size</span><span class="sval g" id="abt-size">—</span></div>
            <div class="srow"><span class="slbl">Status</span><span class="badge bg" id="abt-st">CHECKING</span></div>
          </div>
          <div class="ajson" id="abt-json">loading...</div>
        </div>
      </div>

      <!-- COSMOS -->
      <div class="apanel" id="ap-cosmos">
        <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:8px;">ENDPOINT: GET /api/v1/cosmos/status</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
          <div>
            <div class="srow"><span class="slbl">Block height</span><span class="sval b" id="aco-block">—</span></div>
            <div class="srow"><span class="slbl">Network</span><span class="sval b" id="aco-net">—</span></div>
            <div class="srow"><span class="slbl">Version</span><span class="sval b" id="aco-ver">—</span></div>
            <div class="srow"><span class="slbl">Block time</span><span class="sval b" id="aco-time">—</span></div>
            <div class="srow"><span class="slbl">Catching up</span><span class="badge bg" id="aco-sync">CHECKING</span></div>
          </div>
          <div class="ajson" id="aco-json">loading...</div>
        </div>
      </div>

      <!-- LIGHTNING -->
      <div class="apanel" id="ap-lightning">
        <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:8px;">ENDPOINT: GET /api/v1/lightning/status + /api/v1/lightning/balance</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
          <div>
            <div class="srow"><span class="slbl">Alias</span><span class="sval p" id="aln-alias">—</span></div>
            <div class="srow"><span class="slbl">Block height</span><span class="sval p" id="aln-block">—</span></div>
            <div class="srow"><span class="slbl">Peers</span><span class="sval p" id="aln-peers">—</span></div>
            <div class="srow"><span class="slbl">Active channels</span><span class="sval p" id="aln-ch">—</span></div>
            <div class="srow"><span class="slbl">Wallet balance</span><span class="sval p" id="aln-bal">—</span></div>
            <div class="srow"><span class="slbl">Synced chain</span><span class="badge bg" id="aln-sync">CHECKING</span></div>
            <div class="srow"><span class="slbl">Synced graph</span><span class="badge bg" id="aln-graph">CHECKING</span></div>
          </div>
          <div class="ajson" id="aln-json">loading...</div>
        </div>
      </div>

      <!-- STELLAR -->
      <div class="apanel" id="ap-stellar">
        <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:8px;">ENDPOINT: GET /api/v1/stellar/status</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
          <div>
            <div class="srow"><span class="slbl">Ingest ledger</span><span class="sval b" id="ast-ingest">—</span></div>
            <div class="srow"><span class="slbl">History ledger</span><span class="sval b" id="ast-hist">—</span></div>
            <div class="srow"><span class="slbl">Core ledger</span><span class="sval b" id="ast-core">—</span></div>
            <div class="srow"><span class="slbl">Sync %</span><span class="sval b" id="ast-pct">—</span></div>
            <div class="srow"><span class="slbl">Protocol</span><span class="sval b" id="ast-proto">—</span></div>
            <div class="srow"><span class="slbl">Status</span><span class="badge bgo" id="ast-st">SYNCING</span></div>
          </div>
          <div class="ajson" id="ast-json">loading...</div>
        </div>
      </div>

      <!-- RAW JSON -->
      <div class="apanel" id="ap-rawjson">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
          <div>
            <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:6px;">GET /api/v1/xrpl/payments — developer receives:</div>
            <div class="ajson" id="arj-pay">loading...</div>
          </div>
          <div>
            <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:6px;">GET /api/v1/xrpl/stats — developer receives:</div>
            <div class="ajson" id="arj-stats">loading...</div>
          </div>
        </div>
      </div>

    </div>

    <div class="card c12 cb">
      <div class="ct">💰 Why Customers Pay — Competitive Advantage</div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">
        <div class="srow" style="flex-direction:column;align-items:flex-start;gap:4px;border:none;"><span style="font-family:var(--mono);font-size:9px;color:var(--muted);">QUICKNODE XRPL ONLY</span><span class="sval r" style="font-size:18px;">$299/mo</span></div>
        <div class="srow" style="flex-direction:column;align-items:flex-start;gap:4px;border:none;"><span style="font-family:var(--mono);font-size:9px;color:var(--muted);">ALCHEMY</span><span class="sval r" style="font-size:18px;">No XRPL/Stellar</span></div>
        <div class="srow" style="flex-direction:column;align-items:flex-start;gap:4px;border:none;"><span style="font-family:var(--mono);font-size:9px;color:var(--muted);">INFURA</span><span class="sval r" style="font-size:18px;">No XRPL/Cosmos</span></div>
        <div class="srow" style="flex-direction:column;align-items:flex-start;gap:4px;border:none;"><span style="font-family:var(--mono);font-size:9px;color:var(--muted);">CAMPIONE — ALL 5 CHAINS</span><span class="sval g" style="font-size:18px;">$49/mo</span></div>
      </div>
    </div>
  </div>
</div>
"""

html = html.replace('<footer>', api_panel + '\n<footer>')

# Add JS for API tab
api_js = """
  // API Tab data
  function swapi(el,id){
    document.querySelectorAll('.api-tab').forEach(t=>t.classList.remove('on'));
    document.querySelectorAll('.apanel').forEach(p=>p.classList.remove('on'));
    el.classList.add('on');
    const pid=id==='dex'?'ap-dex-panel':id==='whales'?'ap-whales-panel':'ap-'+id;
    const el2=document.getElementById(pid);if(el2)el2.classList.add('on');
  }
  function apiFmt(obj){
    const s=JSON.stringify(obj,null,2);
    return s.replace(/(".*?"):/g,'<span class="jk">$1</span>:').replace(/: (".*?")/g,': <span class="jv">$1</span>').replace(/: (true|false)/g,': <span class="jb">$1</span>').replace(/: (\\d+\\.?\\d*)/g,': <span class="jn">$1</span>');
  }
  async function loadApiTab(){
    try{const r=await fetch(API+'/api/v1/xrpl/stats');const d=await r.json();if(d.success){set('ap-pay',parseInt(d.data.totalPayments||0).toLocaleString());set('ap-dex',parseInt(d.data.dexTrades||0).toLocaleString());set('ap-whale',d.data.whaleAlerts||0);const rs=document.getElementById('arj-stats');if(rs)rs.innerHTML=apiFmt(d);}}catch(e){}
    try{const r=await fetch(API+'/api/v1/xrpl/payments?limit=50');const d=await r.json();if(d.success&&d.data.length){const tb=document.getElementById('apt-pay');if(tb){tb.innerHTML='';d.data.forEach(p=>{const tr=document.createElement('tr');const ago=Math.floor(Date.now()/1000)-p.timestamp;const agoStr=ago<60?ago+'s':Math.floor(ago/60)+'m';tr.innerHTML=`<td style="font-family:var(--mono);font-size:9px;color:var(--muted)">${p.id?p.id.slice(0,10)+'...':''}</td><td class="addr">${p.sender?p.sender.slice(0,10)+'...':''}</td><td class="addr">${p.receiver?p.receiver.slice(0,10)+'...':''}</td><td class="tamt">${parseFloat(p.amount||0).toFixed(4)}</td><td><span class="badge ${p.currency==='XRP'?'bg':'bb'}">${p.currency||'XRP'}</span></td><td class="tts">${p.fee||0}</td><td class="tts">${agoStr} ago</td>`;tb.appendChild(tr);});} const rp=document.getElementById('arj-pay');if(rp)rp.innerHTML=apiFmt({success:true,count:d.data.length,data:d.data.slice(0,2)});}}catch(e){}
    try{const r=await fetch(API+'/api/v1/xrpl/trades?limit=50');const d=await r.json();if(d.success&&d.data.length){const tb=document.getElementById('apt-dex');if(tb){tb.innerHTML='';d.data.forEach(t=>{const tr=document.createElement('tr');const ago=Math.floor(Date.now()/1000)-t.timestamp;const agoStr=ago<60?ago+'s':Math.floor(ago/60)+'m';const pair=(t.pair||'XRP/RUSD').slice(0,14);tr.innerHTML=`<td style="font-family:var(--mono);font-size:9px;color:var(--muted)">${t.id?t.id.slice(0,10)+'...':''}</td><td class="addr">${t.account?t.account.slice(0,10)+'...':''}</td><td class="tpair">${pair}</td><td class="tamt">${parseFloat(t.takerPays||0).toFixed(4)}</td><td class="tamt b">${parseFloat(t.takerGets||0).toFixed(4)}</td><td class="trate">${parseFloat(t.rate||0).toFixed(6)}</td><td class="tts">${agoStr} ago</td>`;tb.appendChild(tr);});}}}catch(e){}
    try{const r=await fetch(API+'/api/v1/xrpl/whales?limit=20');const d=await r.json();if(d.success&&d.data.length){const wf=document.getElementById('apt-whale');if(wf){wf.innerHTML='<table class="tx"><thead><tr><th>TX HASH</th><th>FROM</th><th>TO</th><th>AMOUNT XRP</th><th>AGO</th></tr></thead><tbody id="apt-whale-tb"></tbody></table>';const tb=document.getElementById('apt-whale-tb');d.data.forEach(w=>{const tr=document.createElement('tr');const ago=Math.floor(Date.now()/1000)-w.timestamp;const agoStr=ago<60?ago+'s':Math.floor(ago/60)+'m';tr.innerHTML=`<td class="tts">${w.txHash?w.txHash.slice(0,10)+'...':''}</td><td class="addr">${w.sender?w.sender.slice(0,10)+'...':''}</td><td class="addr">${w.receiver?w.receiver.slice(0,10)+'...':''}</td><td style="font-family:var(--mono);color:var(--red);font-weight:500">${parseFloat(w.amount||0).toLocaleString()}</td><td class="tts">${agoStr} ago</td>`;tb.appendChild(tr);});}}}catch(e){}
    try{const r=await fetch(API+'/api/v1/bitcoin/status');const d=await r.json();if(d.success){const b=d.data;set('abt-blocks',parseInt(b.blocks||0).toLocaleString());set('abt-sync',b.syncProgress+'%');set('abt-net',b.network||'—');set('abt-pruned',b.pruned?'Yes':'No');set('abt-size',((b.sizeOnDisk||0)/1024/1024/1024).toFixed(2)+' GB');const st=document.getElementById('abt-st');if(st){st.textContent=parseFloat(b.syncProgress)>99.99?'SYNCED':'SYNCING';}const j=document.getElementById('abt-json');if(j)j.innerHTML=apiFmt(d);}}catch(e){}
    try{const r=await fetch(API+'/api/v1/cosmos/status');const d=await r.json();if(d.success){const b=d.data;set('aco-block',parseInt(b.latestBlockHeight||0).toLocaleString());set('aco-net',b.network||'—');set('aco-ver',b.version||'—');set('aco-time',b.latestBlockTime?new Date(b.latestBlockTime).toLocaleTimeString():'—');const cs=document.getElementById('aco-sync');if(cs){cs.textContent=b.catchingUp?'CATCHING UP':'SYNCED';cs.className='badge '+(b.catchingUp?'bgo':'bg');}const j=document.getElementById('aco-json');if(j)j.innerHTML=apiFmt(d);}}catch(e){}
    try{const r=await fetch(API+'/api/v1/lightning/status');const d=await r.json();if(d.success){const b=d.data;set('aln-alias',b.alias||'—');set('aln-block',parseInt(b.blockHeight||0).toLocaleString());set('aln-peers',b.numPeers||0);set('aln-ch',b.numActiveChannels||0);const ls=document.getElementById('aln-sync');if(ls){ls.textContent=b.syncedToChain?'YES':'NO';ls.className='badge '+(b.syncedToChain?'bg':'br');}const lg=document.getElementById('aln-graph');if(lg){lg.textContent=b.syncedToGraph?'YES':'SYNCING';lg.className='badge '+(b.syncedToGraph?'bg':'bgo');}const j=document.getElementById('aln-json');if(j)j.innerHTML=apiFmt(d);}}catch(e){}
    try{const r=await fetch(API+'/api/v1/lightning/balance');const d=await r.json();if(d.success)set('aln-bal',parseInt(d.data.confirmedSats||0).toLocaleString()+' sats');}catch(e){}
    try{const r=await fetch(API+'/api/v1/stellar/status');const d=await r.json();if(d.success){const b=d.data;set('ast-ingest',parseInt(b.ingestLatestLedger||0).toLocaleString());set('ast-hist',parseInt(b.historyLatestLedger||0).toLocaleString());set('ast-core',parseInt(b.coreLatestLedger||0).toLocaleString());set('ast-pct',b.syncProgress+'%');set('ast-proto',b.protocol||'—');const ss=document.getElementById('ast-st');const synced=parseFloat(b.syncProgress||0)>99;if(ss){ss.textContent=synced?'LIVE':'SYNCING';ss.className='badge '+(synced?'bg':'bgo');}const j=document.getElementById('ast-json');if(j)j.innerHTML=apiFmt(d);}}catch(e){}
  }
  loadApiTab();
  setInterval(loadApiTab,20000);
"""

html = html.replace('  loadApiTab();\n  setInterval(loadApiTab,20000);', '')
html = html.replace('  // API Tab data', '')
html = html.replace('fa();setInterval(fa,30000);', api_js + '\nfa();setInterval(fa,30000);')

open('/var/www/campione/status.html', 'w').write(html)
print("✅ API Showcase tab deployed live!")
