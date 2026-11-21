// 寫作園地（2026-11-21）：說說看（🎤 語音轉文字）、句型填空、短文（自動檢查＋文法拼字＋AI 建議、送出計點、存試算表）
// 頁面資料 window.WRITING 由 tools/writing_gen/build_writing.py 產生；目錄頁沒有 WRITING，只顯示各主題的完成狀態。
(function(){
  const CFG = window.WRITING || null;
  const SYNC_URL = 'https://script.google.com/macros/s/AKfycbwqd9cr_3MfXK8hzs8Y-YPQQUqOH5vKtW_vMav1nMAAt9VkBCP_5WP6Q1TDngIlr51U/exec';   // 和測驗同一份試算表
  const mem = {};
  const get = k => { try{ return localStorage.getItem(k); }catch(e){ return k in mem ? mem[k] : null; } };
  const set = (k, v) => { try{ localStorage.setItem(k, v); }catch(e){ mem[k] = v; } };
  const who = () => (get('quizStudentName') || '').trim();
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;' }[c]));
  const draftKey = path => 'wr:' + (path || location.pathname) + ':' + (who().toUpperCase() || 'GUEST');

  // ---- 目錄頁：各主題的完成狀態 ----
  if(!CFG){
    document.querySelectorAll('.wu-st[data-unit]').forEach(el => {
      let d = null;
      try{ d = JSON.parse(get(draftKey(new URL(el.dataset.unit + '.html', location.href).pathname)) || 'null'); }catch(e){}
      if(d && d.sent) el.innerHTML = '✅ 已送出作文（' + esc(d.sent.level === 2 ? '★★' : '★') + '，' + esc(d.sent.date) + '）';
      else if(d && d.text) el.textContent = '✏️ 作文寫到一半';
    });
    return;
  }

  // ---- 播放（合併音檔 all.mp3#t=開始,結束；沒有 mp3 就用瀏覽器語音）----
  let cur = null;
  function stopAll(){
    if(cur){ cur.pause(); cur = null; }
    try{ speechSynthesis.cancel(); }catch(e){}
    document.querySelectorAll('.say.playing').forEach(b => b.classList.remove('playing'));
  }
  function tts(text, btn){
    try{
      const u = new SpeechSynthesisUtterance(text); u.lang = 'en-US'; u.rate = 0.9;
      u.onend = u.onerror = () => btn && btn.classList.remove('playing');
      speechSynthesis.speak(u);
    }catch(e){ if(btn) btn.classList.remove('playing'); }
  }
  function play(btn){
    stopAll();
    btn.classList.add('playing');
    const a = new Audio(btn.dataset.src);
    let fell = false;
    const done = () => btn.classList.remove('playing');
    const fb = () => { if(fell) return; fell = true; tts(btn.dataset.say, btn); };
    const m = /#t=[\d.]+,([\d.]+)/.exec(btn.dataset.src || '');
    if(m){ const end = +m[1]; a.addEventListener('timeupdate', () => { if(a.currentTime >= end){ a.pause(); done(); } }); }
    a.addEventListener('pause', done);
    a.addEventListener('ended', done);
    a.addEventListener('error', fb);
    const p = a.play(); if(p && p.catch) p.catch(e => { if(!(e && e.name === 'AbortError')) fb(); });
    cur = a;
  }

  // ---- 🎤 語音轉文字（Chrome、Edge、Android、iPhone／iPad 的 Safari）----
  const Rec = window.SpeechRecognition || window.webkitSpeechRecognition;
  let rec = null, recBtn = null;
  function target(btn){
    const k = btn.dataset.for;
    return k === 'text' ? document.getElementById('wrText') : document.querySelector('[data-key="' + k + '"]');
  }
  function listen(btn){
    if(rec){ try{ rec.stop(); }catch(e){} if(recBtn === btn) return; }
    const el = target(btn); if(!el) return;
    rec = new Rec(); recBtn = btn;
    rec.lang = 'en-US'; rec.interimResults = false; rec.maxAlternatives = 1;
    btn.classList.add('rec'); btn.textContent = '⏺';
    rec.onresult = e => {
      let t = Array.from(e.results).map(r => r[0].transcript).join(' ').trim();
      if(!t) return;
      if(el.tagName === 'TEXTAREA'){
        t = t.charAt(0).toUpperCase() + t.slice(1);
        if(!/[.!?]$/.test(t)) t += '.';
        el.value = (el.value.trim() ? el.value.replace(/\s*$/, ' ') : '') + t;
      } else el.value = (el.value.trim() ? el.value.trim() + ' ' : '') + t;
      el.dispatchEvent(new Event('input', { bubbles:true }));
    };
    rec.onerror = e => { if(e.error === 'not-allowed') alert('瀏覽器沒有允許使用麥克風。請在網址列旁邊的設定允許麥克風，或直接打字。'); };
    rec.onend = () => { btn.classList.remove('rec'); btn.textContent = '🎤'; rec = null; recBtn = null; };
    try{ rec.start(); }catch(e){ rec.onend(); }
  }
  if(!Rec) document.documentElement.classList.add('no-mic');

  // ---- 草稿（每個登入者各自一份，存在這台裝置）----
  let D = {};
  try{ D = JSON.parse(get(draftKey()) || '{}') || {}; }catch(e){ D = {}; }
  D.inputs = D.inputs || {};
  let saveT = null;
  const save = () => { clearTimeout(saveT); saveT = setTimeout(() => set(draftKey(), JSON.stringify(D)), 300); };
  document.querySelectorAll('[data-key]').forEach(el => {
    if(D.inputs[el.dataset.key] != null) el.value = D.inputs[el.dataset.key];
    el.addEventListener('input', () => { D.inputs[el.dataset.key] = el.value; save(); ideas(); });
  });

  document.addEventListener('click', e => {
    const s = e.target.closest('.say');
    if(s){ e.preventDefault(); play(s); return; }
    const mic = e.target.closest('.mic');
    if(mic){ e.preventDefault(); if(Rec) listen(mic); return; }
    const sh = e.target.closest('.wr-show');
    if(sh){ const ex = sh.nextElementSibling; ex.hidden = !ex.hidden; sh.textContent = ex.hidden ? '看例句' : '收起例句'; }
  });

  // ---- ☆ 存字卡（首頁 repo 的 /cards/cards.js）----
  function need(src, test){ if(test()) return Promise.resolve(); return new Promise(r => { const s = document.createElement('script'); s.src = src; s.onload = s.onerror = r; document.head.appendChild(s); }); }
  const abs = u => { try{ if(!u) return ''; const x = new URL(u, location.href); return x.pathname + x.hash; }catch(e){ return ''; } };
  function addStars(){
    if(!window.Cards) return;
    document.querySelectorAll('.wr-word').forEach(c => {
      const say = c.querySelector('.vc-say:not(.sm)');
      const card = { en: c.dataset.en, zh: c.querySelector('.vc-zh').textContent, ex: c.querySelector('.vc-en').textContent, exzh: c.querySelector('.vc-exzh').textContent,
                     audio: say ? abs(say.dataset.src) : '', src: '寫作園地｜' + CFG.title, url: location.pathname };
      c.querySelector('.ww-head').insertAdjacentHTML('beforeend', ' ' + Cards.btn(card));
    });
  }
  setTimeout(() => need('/cards/cards.js?v=20261117a', () => window.Cards).then(addStars), 400);

  // ---- ⑤ 寫短文 ----
  const box = document.getElementById('wrWrite');
  const LV = { 1: { min: 30, words: 2, link: false, name: '★ 基本' }, 2: { min: 50, words: 3, link: true, name: '★★ 挑戰' } };
  let level = D.level || 1;
  const LINKS = /\b(because|so|but|when|after|before|then|first|also|and then|if)\b/i;
  box.innerHTML =
    '<div class="wr-level">選擇難度：<button class="btn" data-lv="1">★ 基本：30 字以上</button> <button class="btn" data-lv="2">★★ 挑戰：50 字以上（英檢段落寫作）</button></div>' +
    '<div class="wr-prompt"><div class="wp-en">' + esc(CFG.prompt) + '</div><div class="wp-zh">' + esc(CFG.zh) + '</div><div class="wp-tip">📌 ' + esc(CFG.tense) + '</div></div>' +
    '<div class="wr-guide"><b>可以照這些問題的順序寫：</b><ol>' + CFG.qs.map(q => '<li>' + esc(q[0]) + ' <span>' + esc(q[1]) + '</span></li>').join('') + '</ol></div>' +
    '<div class="wr-ideas" id="wrIdeas"></div>' +
    '<div class="wr-editor"><textarea id="wrText" rows="9" placeholder="在這裡寫你的短文（英文）。可以按 🎤 用說的，再自己修改。" spellcheck="false" autocapitalize="sentences" data-dict-off></textarea>' +
    '<div class="wr-bar"><button class="mic" type="button" data-for="text" title="用說的">🎤</button><span id="wrCount"></span><span class="wr-mic-note">（這個瀏覽器不支援語音輸入，請直接打字）</span></div></div>' +
    '<ul class="wr-checks" id="wrChecks"></ul>' +
    '<div class="wr-actions"><button class="btn" id="wrCheck">🔍 檢查我的作文</button> <button class="btn alt big" id="wrSend" disabled>📤 送出作文</button></div>' +
    '<div id="wrFeedback"></div><div id="wrDone"></div>';
  const ta = document.getElementById('wrText');
  ta.value = D.text || '';

  function ideas(){
    const list = [];
    document.querySelectorAll('.wr-speak [data-key]').forEach(el => { if(el.value.trim()) list.push(el.value.trim()); });
    CFG.frames.forEach((f, i) => {
      const ins = [...document.querySelectorAll('[data-key^="f' + (i + 1) + '-"]')].map(x => x.value.trim());
      if(ins.length && ins.every(Boolean)){ let k = 0; list.push(f.replace(/____/g, () => ins[k++])); }
    });
    const el = document.getElementById('wrIdeas');
    if(!el) return;
    el.innerHTML = list.length ? '<b>你在步驟 ①③ 寫的句子</b>（按「＋」放進短文，再修改成過去式或連起來）<ul>' +
      list.map((s, i) => '<li><button class="btn sm" data-idea="' + i + '">＋</button> ' + esc(s) + '</li>').join('') + '</ul>' : '';
    el.querySelectorAll('[data-idea]').forEach(b => b.onclick = () => {
      let s = list[+b.dataset.idea]; s = s.charAt(0).toUpperCase() + s.slice(1); if(!/[.!?]$/.test(s)) s += '.';
      ta.value = (ta.value.trim() ? ta.value.replace(/\s*$/, ' ') : '') + s; ta.dispatchEvent(new Event('input'));
    });
  }

  const words = t => (t.match(/[A-Za-z]+(?:'[A-Za-z]+)?/g) || []);
  function checks(){
    const t = ta.value.trim(), L = LV[level], n = words(t).length;
    const sents = t.split(/(?<=[.!?])\s+/).filter(s => s.trim());
    let badCap = 0;   // 句子開頭小寫＋句子中間單獨的小寫 i
    sents.forEach(s => { s = s.trim(); if(/^[a-z]/.test(s)) badCap++; badCap += (s.slice(1).match(/\bi\b/g) || []).length; });
    const used = CFG.targets.filter(x => new RegExp('\\b(' + x.rx + ')\\b', 'i').test(t)).map(x => x.en);
    const out = [
      { ok: n >= L.min, t: '字數 ' + n + ' / ' + L.min + ' 字以上' },
      { ok: !!t && badCap === 0, t: '句子開頭大寫、I 要大寫' + (badCap ? '（還有 ' + badCap + ' 處）' : '') },
      { ok: /[.!?]["')]?$/.test(t), t: '句子結尾要有句點（. ! ?）' },
      { ok: used.length >= L.words, t: '用到字詞庫的字 ' + used.length + ' / ' + L.words + ' 個' + (used.length ? '：' + used.join('、') : '') },
    ];
    if(L.link) out.push({ ok: LINKS.test(t), t: '用到連接詞（because、so、but、when、after、then…）' });
    return out;
  }
  function refresh(){
    const c = checks();
    document.getElementById('wrCount').textContent = words(ta.value).length + ' 字';
    document.getElementById('wrChecks').innerHTML = c.map(x => '<li class="' + (x.ok ? 'ok' : 'no') + '">' + (x.ok ? '✅ ' : '⬜ ') + esc(x.t) + '</li>').join('');
    document.getElementById('wrSend').disabled = !c.every(x => x.ok);
    box.querySelectorAll('[data-lv]').forEach(b => b.classList.toggle('alt', +b.dataset.lv === level));
  }
  ta.addEventListener('input', () => { D.text = ta.value; save(); refresh(); if(lastCheck && lastCheck.text !== ta.value) markStale(); });
  box.querySelectorAll('[data-lv]').forEach(b => b.onclick = () => { level = +b.dataset.lv; D.level = level; save(); refresh(); });

  // ---- 🔍 檢查：文法拼字（LanguageTool）＋ AI 建議（Cloudflare Workers AI）----
  const TYPE = { misspelling: '拼字', grammar: '文法', typographical: '標點／大小寫', style: '用字', whitespace: '空格', uncategorized: '其他', duplication: '重複' };
  let lastCheck = null;
  function mapLT(ms){
    return (ms || []).slice(0, 25).map(m => ({ offset: m.offset, length: m.length, message: m.message, short: m.shortMessage,
      rep: (m.replacements || []).slice(0, 3).map(r => r.value), type: (m.rule && m.rule.issueType) || '' }));
  }
  async function runCheck(text){
    let r = null;
    try{
      const res = await fetch('/api/write-check', { method:'POST', headers:{ 'content-type':'application/json' },
        body: JSON.stringify({ text, topic: CFG.topic, prompt: CFG.prompt, tense: CFG.tense, level }) });
      if(res.ok && /json/.test(res.headers.get('content-type') || '')) r = await res.json();
    }catch(e){}
    if(!r || !r.grammar){
      try{
        const lt = await fetch('https://api.languagetool.org/v2/check', { method:'POST', headers:{ 'content-type':'application/x-www-form-urlencoded' },
          body: new URLSearchParams({ text, language:'en-US' }) });
        r = Object.assign(r || {}, { grammar: mapLT((await lt.json()).matches) });
      }catch(e){ r = r || {}; r.grammarError = true; }
    }
    return r;
  }
  function markStale(){ const f = document.querySelector('.wr-gram'); if(f) f.classList.add('stale'); }
  function showFeedback(r, text){
    const g = r.grammar || [];
    let h = '<div class="wr-fb">';
    h += '<h3>📝 文法和拼字</h3>';
    if(r.grammarError) h += '<p class="muted">文法檢查暫時連不上，請稍後再按一次。</p>';
    else if(!g.length) h += '<p class="good">👍 沒有找到文法或拼字錯誤！</p>';
    else{
      h += '<p class="muted">找到 ' + g.length + ' 個可能要改的地方。按「改成…」會直接幫你改（改完再檢查一次）；不一定每個都要改，想一想再決定。</p><ol class="wr-gram">';
      g.forEach((m, i) => {
        const a = Math.max(0, m.offset - 25), b = Math.min(text.length, m.offset + m.length + 25);
        const ctx = (a > 0 ? '…' : '') + esc(text.slice(a, m.offset)) + '<mark>' + esc(text.slice(m.offset, m.offset + m.length)) + '</mark>' + esc(text.slice(m.offset + m.length, b)) + (b < text.length ? '…' : '');
        h += '<li><span class="tag">' + esc(TYPE[m.type] || '提醒') + '</span> ' + ctx + '<div class="msg">' + esc(m.message) + '</div>' +
          (m.rep.length ? '<div>' + m.rep.map(v => '<button class="btn sm" data-fix="' + i + '" data-v="' + esc(v) + '">改成「' + esc(v) + '」</button>').join(' ') + '</div>' : '') + '</li>';
      });
      h += '</ol>';
    }
    h += '<h3>🤖 AI 老師的建議</h3>';
    if(r.aiReady === false || r.ai === undefined && !r.aiError) h += '<p class="muted">AI 建議還沒啟用（家長在 Cloudflare 開啟 Workers AI 後就會出現）。</p>';
    else if(r.aiError || !r.ai) h += '<p class="muted">AI 建議這次沒有回應，請稍後再按一次「檢查」。</p>';
    else{
      const ai = r.ai;
      if(ai.praise) h += '<p class="good">🌟 ' + esc(ai.praise) + '</p>';
      if(ai.tips && ai.tips.length) h += '<ol class="wr-tips">' + ai.tips.map(t => '<li>' + (t.wrong ? '<s>' + esc(t.wrong) + '</s> → ' : '') + (t.right ? '<b>' + esc(t.right) + '</b>' : '') + '<div>' + esc(t.why || '') + '</div></li>').join('') + '</ol>';
      if(ai.idea) h += '<p>💡 ' + esc(ai.idea) + '</p>';
    }
    h += '</div>';
    document.getElementById('wrFeedback').innerHTML = h;
    document.querySelectorAll('[data-fix]').forEach(b => b.onclick = () => {
      if(ta.value !== text){ alert('作文已經改過了，請先再按一次「🔍 檢查我的作文」。'); return; }
      const m = g[+b.dataset.fix];
      const nt = text.slice(0, m.offset) + b.dataset.v + text.slice(m.offset + m.length);
      // 同一次檢查的其他位置要跟著位移
      const diff = b.dataset.v.length - m.length;
      g.forEach(x => { if(x !== m && x.offset > m.offset) x.offset += diff; });
      m.length = 0; m.offset = -1e9;
      ta.value = nt; text = nt; lastCheck.text = nt; D.text = nt; save(); refresh();
      b.closest('li').classList.add('fixed'); b.closest('div').innerHTML = '✔ 已改成「' + esc(b.dataset.v) + '」';
    });
  }
  document.getElementById('wrCheck').onclick = async () => {
    const text = ta.value;
    if(words(text).length < 5){ alert('先寫幾句再檢查喔！'); return; }
    const today = new Date().toISOString().slice(0, 10);
    D.checks = D.checks && D.checks.day === today ? D.checks : { day: today, n: 0 };
    if(D.checks.n >= 10){ alert('今天這篇已經檢查 10 次了，自己再讀一讀、改一改，明天再檢查吧！'); return; }
    const b = document.getElementById('wrCheck'); b.disabled = true; b.textContent = '⏳ 檢查中…';
    const r = await runCheck(text);
    D.checks.n++; save();
    b.disabled = false; b.textContent = '🔍 再檢查一次';
    lastCheck = { text, r };
    showFeedback(r, text);
  };

  // ---- 📤 送出：存到試算表＋計點，然後看範文 ----
  async function sync(payload){
    const name = who();
    if(!name) return '☁️ 還沒登入，作文沒有送出到試算表（範文照樣可以看）';
    try{
      await fetch(get('quizSyncUrl') || SYNC_URL, { method:'POST', mode:'no-cors', headers:{ 'Content-Type':'text/plain;charset=utf-8' }, body: JSON.stringify(Object.assign({ name }, payload)) });
      return '☁️ 作文已送出到試算表，家長看得到';
    }catch(e){ return '☁️ 送出失敗，請檢查網路連線再按一次'; }
  }
  function modelHtml(){
    return '<div class="wr-model"><h3>📖 範文（參考就好，不用一樣）</h3>' +
      [1, 2].map(k => '<div class="wm"><div class="wm-h">' + LV[k].name + ' <button class="say-m btn sm" data-m="' + k + '">🔊 聽範文</button></div><p>' + esc(CFG.model[k]) + '</p></div>').join('') + '</div>';
  }
  document.getElementById('wrSend').onclick = async () => {
    const text = ta.value.trim(), c = checks();
    if(!c.every(x => x.ok)) return;
    if(!lastCheck || lastCheck.text !== ta.value){
      if(!confirm('還沒用「🔍 檢查我的作文」檢查最新的版本，確定要直接送出嗎？')) return;
    }
    const g = lastCheck && lastCheck.text === ta.value ? (lastCheck.r.grammar || []).filter(m => m.offset >= 0) : null;
    const ai = lastCheck && lastCheck.r && lastCheck.r.ai;
    const total = c.length + 1, correct = c.length + (g && g.length === 0 ? 1 : 0);
    const mode = '寫作短文 ' + LV[level].name;
    const details = [
      { q: '題目：' + CFG.prompt + '（' + LV[level].name + '）', picked: text, correct: '', isCorrect: true },
      { q: '字數', picked: String(words(text).length), correct: '', isCorrect: true },
      { q: '文法拼字提醒（送出時還有）', picked: g == null ? '沒有檢查最新版本' : (g.length ? g.map(m => text.substr(m.offset, m.length) + '：' + m.message).join('｜') : '沒有'), correct: '', isCorrect: g ? g.length === 0 : false },
      { q: 'AI 建議', picked: ai ? [ai.praise].concat((ai.tips || []).map(t => (t.wrong || '') + '→' + (t.right || '') + ' ' + (t.why || ''))).filter(Boolean).join('｜') : '（沒有）', correct: '', isCorrect: true },
    ];
    const b = document.getElementById('wrSend'); b.disabled = true; b.textContent = '⏳ 送出中…';
    const msg = await sync({ week: CFG.label, mode, score: correct, total, percent: Math.round(correct / total * 100), details });
    if(who() && window.Points) Points.earn({ name: who(), label: CFG.label, mode, correct, total });
    D.sent = { level, date: new Date().toLocaleDateString('zh-TW'), words: words(text).length }; save();
    b.textContent = '📤 再送出一次'; b.disabled = false;
    document.getElementById('wrDone').innerHTML = '<div class="wr-ok">🎉 作文送出了！' + esc(msg) + '<br>（同一天再送出，作文會再存一份，點數只算第一次）</div>' + modelHtml();
    document.querySelectorAll('.say-m').forEach(x => x.onclick = () => { const h = document.querySelector('.wr-m' + x.dataset.m); if(h) play(h); });
    document.getElementById('wrDone').scrollIntoView({ behavior:'smooth', block:'start' });
  };

  ideas(); refresh();
  if(D.sent){ document.getElementById('wrDone').innerHTML = '<div class="wr-ok">✅ 你在 ' + esc(D.sent.date) + ' 送出過這篇作文（' + esc(LV[D.sent.level].name) + '）。可以再修改、再送出一次。</div>' + modelHtml();
    document.querySelectorAll('.say-m').forEach(x => x.onclick = () => { const h = document.querySelector('.wr-m' + x.dataset.m); if(h) play(h); }); }
})();
