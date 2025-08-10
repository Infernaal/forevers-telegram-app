// Global console interceptor & on-screen log overlay
// Automatically executed when imported.

(function(){
  if (window.__CUSTOM_LOGGER_INSTALLED__) return; // prevent double install (e.g. HMR)
  window.__CUSTOM_LOGGER_INSTALLED__ = true;

  const original = {
    log: console.log.bind(console),
    info: console.info ? console.info.bind(console) : console.log.bind(console),
    warn: console.warn.bind(console),
    error: console.error.bind(console),
    debug: console.debug ? console.debug.bind(console) : console.log.bind(console),
    group: console.group ? console.group.bind(console) : null,
    groupCollapsed: console.groupCollapsed ? console.groupCollapsed.bind(console) : null,
    groupEnd: console.groupEnd ? console.groupEnd.bind(console) : null,
  };

  const levels = {
    log: '#FFFFFF',
    info: '#9CDCFE',
    debug: '#B5CEA8',
    warn: '#FFA500',
    error: '#FF5555'
  };

  const state = {
    buffer: [],
    max: 400,
    groupDepth: 0,
  outbound: [],
  flushTimer: null,
  };

  // Overlay explicitly disabled for production & development (shipping only)
  const OVERLAY_ENABLED = false;

  let overlay = null; // never created now
  let toolbar = null;
  let toggleBtn = null;
  let autoScrollChk = { checked: false };

  function styleBtn(btn){
    Object.assign(btn.style, {
      background: '#222', color: '#ddd', border: '1px solid #333', padding: '2px 8px', cursor: 'pointer'
    });
    btn.onmouseenter = ()=> btn.style.background = '#333';
    btn.onmouseleave = ()=> btn.style.background = (overlay && overlay.style.display==='none' ? '#222' : '#444');
  }

  // (No overlay branch removed)

  function appendEntry(entry){ /* no visual output */ }

  function escapeHtml(str){
    return str.replace(/[&<>"]/g, c=>({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;' }[c]));
  }

  function serializeArg(arg){
    if (typeof arg === 'string') return arg;
    try {
      if (arg instanceof Error) {
        return arg.stack || (arg.name+': '+arg.message);
      }
      return JSON.stringify(arg, replacer, 2);
    } catch { return '[Unserializable]'; }
  }

  function replacer(key, value){
    if (value && typeof value === 'object') {
      if (value instanceof Window) return '[Window]';
      if (value instanceof Document) return '[Document]';
    }
    return value;
  }

  function formatForDownload(entry){
    return `[${entry.ts}] ${entry.level.toUpperCase()} ${' '.repeat(entry.groupDepth*2)}${entry.text}`;
  }

  function now(){
    const d = new Date();
    return d.toISOString().split('T')[1]; // time part
  }

  function push(level, args){
    const text = args.map(serializeArg).join(' ');
  const entry = { level, text, ts: now(), groupDepth: state.groupDepth };
    state.buffer.push(entry);
    if (state.buffer.length > state.max) state.buffer.shift();
    appendEntry(entry);
  queueOutbound(entry);
  }

  // Override methods
  console.log = (...a)=>{ push('log', a); original.log(...a); };
  console.info = (...a)=>{ push('info', a); original.info(...a); };
  console.debug = (...a)=>{ push('debug', a); original.debug(...a); };
  console.warn = (...a)=>{ push('warn', a); original.warn(...a); };
  console.error = (...a)=>{ push('error', a); original.error(...a); };

  console.group = (label)=>{
    push('log', [label||'(group)']);
    state.groupDepth++;
    if (original.group) original.group(label);
  };
  console.groupCollapsed = (label)=>{
    push('log', [label||'(group collapsed)']);
    state.groupDepth++;
    if (original.groupCollapsed) original.groupCollapsed(label);
  };
  console.groupEnd = ()=>{
    state.groupDepth = Math.max(0, state.groupDepth-1);
    if (original.groupEnd) original.groupEnd();
  };

  // Capture unhandled errors
  window.addEventListener('error', (e)=>{
    push('error', ['UnhandledError:', e.message, e.error]);
  });
  window.addEventListener('unhandledrejection', (e)=>{
    push('error', ['UnhandledRejection:', e.reason]);
  });

  // Expose utilities
  window.__APP_LOGS__ = {
    export: ()=>state.buffer.slice(),
    original,
    forceFlush: flushOutbound,
    overlayEnabled: false
  };

  // -------- Remote shipping ---------
  const LOG_ENDPOINT = (window.__LOG_ENDPOINT_OVERRIDE__) || (window.__API_BASE__ ? window.__API_BASE__ + '/logs' : '/api/v1/dbdc/logs');
  const SESSION_ID = crypto.randomUUID ? crypto.randomUUID() : Math.random().toString(36).slice(2);
  const USER_ID_HINT = (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.initDataUnsafe && window.Telegram.WebApp.initDataUnsafe.user && window.Telegram.WebApp.initDataUnsafe.user.id) || undefined;
  const APP_VERSION = (window.__APP_VERSION__) || undefined;

  function queueOutbound(entry){
    // Only send selected levels to reduce traffic
    if (!['log','info','warn','error'].includes(entry.level)) return;
    state.outbound.push({
      level: entry.level,
      message: entry.text.slice(0, 5000),
      ts: entry.ts,
      context: undefined,
      source: detectSource(entry.text)
    });
    scheduleFlush();
  }

  function detectSource(text){
    if (/TonConnect|\bTON\b/i.test(text)) return 'tonconnect';
    return undefined;
  }

  function scheduleFlush(){
    if (state.flushTimer) return;
    state.flushTimer = setTimeout(()=>{
      flushOutbound();
    }, 2000); // 2s debounce
    if (state.outbound.length >= 30) {
      // burst threshold
      flushOutbound();
    }
  }

  async function flushOutbound(){
    if (!state.outbound.length) return;
    const batch = state.outbound.splice(0, state.outbound.length);
    clearTimeout(state.flushTimer); state.flushTimer = null;
    try {
      await fetch(LOG_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type':'application/json' },
        body: JSON.stringify({
          entries: batch,
            session: SESSION_ID,
            user_id: USER_ID_HINT ? String(USER_ID_HINT) : null,
            app_version: APP_VERSION || null
        })
      });
    } catch (e) {
      // put back (simple retry, limited)
      batch.forEach(b=> state.outbound.unshift(b));
      if (state.outbound.length > 1000) state.outbound.length = 1000; // cap
    }
  }

  // Flush before unload
  window.addEventListener('beforeunload', ()=>{ flushOutbound(); });
})();
