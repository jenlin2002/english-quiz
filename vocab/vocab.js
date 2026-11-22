// 單字區單字卡：🔊 播放（先用 mp3，沒有就用瀏覽器語音）、遮中文／遮英文、全部播放
(function(){
  const grid = document.getElementById('cards');
  if(!grid) return;
  let cur = null, queue = [];
  const tts = 'speechSynthesis' in window;
  // 全部播放的狀態（2026-11-22 使用者：按了全部播放停不下來、畫面一直往下捲 → 加暫停／停止）
  //   gen：每次停止／暫停就 +1，舊的播放結束回呼看到 gen 變了就不再接下一個字
  let gen = 0, paused = false, curBtn = null, total = 0, bar = null;

  function halt(){
    if(cur){ cur.pause(); cur = null; }
    if(tts) speechSynthesis.cancel();
    document.querySelectorAll('.vc-say.playing, .vc-card.playing').forEach(e => e.classList.remove('playing'));
  }
  function stop(){
    gen++; queue = []; paused = false; curBtn = null;
    halt();
    showBar(false);
  }
  function speak(text, done){
    if(!tts){ done(); return; }
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US'; u.rate = 0.85;
    u.onend = u.onerror = done;
    speechSynthesis.speak(u);
  }
  function play(btn, done){
    done = done || function(){};
    const card = btn.closest('.vc-card');
    btn.classList.add('playing'); if(card) card.classList.add('playing');
    let over = false;
    const fin = () => { if(over) return; over = true; btn.classList.remove('playing'); if(card) card.classList.remove('playing'); done(); };
    const a = new Audio(btn.dataset.src);
    let fell = false;
    const fb = () => { if(fell) return; fell = true; speak(btn.dataset.say, fin); };
    a.addEventListener('ended', fin);
    // 合併音檔（all.mp3#t=開始,結束）：播到結束時間就停（有的瀏覽器不會自己停在 #t 的結尾）
    const clip = /#t=[\d.]+,([\d.]+)/.exec(btn.dataset.src || '');
    if(clip){
      const end = +clip[1];
      a.addEventListener('timeupdate', () => { if(a.currentTime >= end){ a.pause(); fin(); } });
      a.addEventListener('pause', () => { if(cur === a && a.currentTime >= end - 0.3) fin(); });   // 瀏覽器自己停在 #t 結尾時只會觸發 pause
    }
    a.addEventListener('error', fb);
    const p = a.play(); if(p && p.catch) p.catch(e => { if(!(e && e.name === 'AbortError')) fb(); });
    cur = a;
  }
  function next(){
    if(paused) return;
    const b = queue.shift();
    if(!b){ stop(); return; }   // 全部播完：收起控制列
    curBtn = b;
    const g = gen;
    b.scrollIntoView({ block:'nearest', behavior:'smooth' });
    play(b, () => { if(g !== gen) return; setTimeout(() => { if(g === gen) next(); }, 500); });
    showBar(true);
  }
  function pauseAll(){
    if(paused || !curBtn) return;
    paused = true; gen++;
    queue.unshift(curBtn);   // 繼續時從這個字重新唸
    halt();
    showBar(true);
  }
  function resumeAll(){
    if(!paused) return;
    paused = false;
    next();
  }

  // 全部播放時畫面下方中間的控制列：⏸ 暫停／▶ 繼續、⏹ 停止、目前第幾個字
  function showBar(on){
    const btns = document.querySelectorAll('[data-play-all]');
    btns.forEach(b => {
      if(!b.dataset.label) b.dataset.label = b.textContent;
      b.textContent = on ? '⏹ 停止播放' : b.dataset.label;
      b.classList.toggle('on', on);
    });
    if(!on){ if(bar) bar.style.display = 'none'; return; }
    if(!bar){
      bar = document.createElement('div');
      bar.id = 'vcPlayBar';
      bar.style.cssText = 'position:fixed;left:50%;transform:translateX(-50%);bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:9500;'
        + 'display:flex;align-items:center;gap:8px;padding:8px 10px 8px 16px;border-radius:999px;background:#163026;color:#F7F3E8;'
        + 'border:2px solid #E8B94A;box-shadow:0 6px 20px rgba(0,0,0,.35);font-family:"Noto Sans TC",sans-serif;font-size:15px;max-width:calc(100vw - 24px);';
      bar.innerHTML = '<span data-vc-now style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:40vw"></span>'
        + '<button type="button" data-vc-pause style="border:none;border-radius:999px;padding:8px 14px;font-size:15px;font-weight:700;cursor:pointer;background:#E8B94A;color:#24332B;white-space:nowrap"></button>'
        + '<button type="button" data-vc-stop style="border:none;border-radius:999px;padding:8px 14px;font-size:15px;font-weight:700;cursor:pointer;background:#D97A6C;color:#fff;white-space:nowrap">⏹ 停止</button>';
      document.body.appendChild(bar);
      bar.querySelector('[data-vc-pause]').addEventListener('click', () => paused ? resumeAll() : pauseAll());
      bar.querySelector('[data-vc-stop]').addEventListener('click', stop);
    }
    bar.style.display = 'flex';
    const n = total - queue.length + (paused ? 1 : 0);
    const card = curBtn && curBtn.closest('.vc-card');
    const wEl = card && card.querySelector('.vc-word');
    const word = wEl ? wEl.textContent : '';
    bar.querySelector('[data-vc-now]').textContent = (paused ? '已暫停 ' : '▶ ') + n + ' / ' + total + (word ? '　' + word.trim() : '');
    bar.querySelector('[data-vc-pause]').textContent = paused ? '▶ 繼續' : '⏸ 暫停';
  }
  document.addEventListener('keydown', e => { if(e.key === 'Escape' && (curBtn || paused)) stop(); });
  window.addEventListener('pagehide', stop);

  // 每個登入者自己的進度（gquiz.js 記在這台裝置 vocabProgress:<這一頁>:<登入者>）：
  //   答錯、還要複習的字 → 紅色；第一次就答對的字 → 暗灰色（不用再背）；全部答對 → 整個單元變灰。
  //   家長 PARENT（和測試帳號 TEST）看 BRANDEN、MELISSA 兩個人的統計，卡片只標紅、不變灰。
  const esc = s => String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
  //   每個字的狀態：本站答過的（vocabWords:<登入者>，所有單元共用）優先；沒答過就看 WORD UP 熟悉度（vocab/wordup/status.json）：
  //   不熟＝'w' 紅色（先複習）、熟記＝'k' 只標小標籤（不變灰、照樣要考）；只有本站答對 'm' 才變灰
  let WU = null;
  async function loadWordUp(){
    if(WU) return WU;
    try{ WU = await (await fetch(new URL('../wordup/status.json', location.href), { cache:'no-cache' })).json(); }catch(e){ WU = {}; }
    return WU;
  }
  function statusOf(p){
    const m = new Map();
    const u = ((WU || {}).users || {})[p];
    if(u) Object.keys(u.words).forEach(w => m.set(w.toLowerCase(), { s: u.words[w][0] === '熟記' ? 'k' : 'w', src: 'wordup', lv: u.words[w][0] }));
    try{ const mine = JSON.parse(localStorage.getItem('vocabWords:' + p) || '{}'); Object.keys(mine).forEach(w => m.set(w, { s: mine[w], src: 'site' })); }catch(e){}
    return { map: m, updated: u && u.updated };
  }
  async function showProgress(){
    let name = '';
    try{ name = (localStorage.getItem('quizStudentName') || '').trim().toUpperCase(); }catch(e){}
    await loadWordUp();
    const old = document.getElementById('vcProgress');
    if(old) old.remove();
    const cards = [...grid.querySelectorAll('.vc-card')];
    cards.forEach(c => { c.classList.remove('wrong', 'mastered', 'wu-known'); c.removeAttribute('data-tag'); });
    grid.classList.remove('all-mastered');
    if(!name) return;
    const parent = /^(PARENT|TEST)$/.test(name);
    const people = parent ? ['BRANDEN', 'MELISSA'] : [name];
    const wordOf = c => c.querySelector('.vc-word').textContent.trim();
    const n = cards.length, tags = new Map(), rows = [];
    people.forEach(p => {
      let rec = null;
      try{ rec = JSON.parse(localStorage.getItem('vocabProgress:' + location.pathname + ':' + p) || 'null'); }catch(e){}
      const st = statusOf(p);
      const sOf = c => st.map.get(wordOf(c).toLowerCase());
      const known = cards.filter(sOf);
      if(!known.length){ rows.push('<div class="vp-row"><b>' + esc(p) + '</b>：還沒做過這個單元的測驗。按「📝 單元測驗」開始，每個字都會考到。</div>'); return; }
      if(!rec) rec = { at: st.updated || Date.now() };
      const ms = new Set(cards.filter(c => sOf(c) && sOf(c).s === 'm').map(wordOf)), wr = new Set(cards.filter(c => sOf(c) && sOf(c).s === 'w').map(wordOf));
      const m = cards.filter(c => ms.has(wordOf(c))).length;
      const redWords = cards.filter(c => wr.has(wordOf(c)) && !ms.has(wordOf(c))).map(wordOf);
      const pct = Math.round(m / n * 100);
      if(!parent) cards.forEach(c => {
        const w = wordOf(c), s = sOf(c);
        if(ms.has(w)){ c.classList.add('mastered'); tags.set(c, '已答對'); }
        else if(wr.has(w)){ c.classList.add('wrong'); tags.set(c, s.src === 'wordup' ? 'WORD UP：' + s.lv : p + ' 答錯'); }
        else if(s && s.s === 'k'){ c.classList.add('wu-known'); tags.set(c, 'WORD UP 熟記（待測驗）'); }
      });
      else redWords.forEach(w => { const c = cards.find(x => wordOf(x) === w); c.classList.add('wrong'); tags.set(c, (tags.get(c) ? tags.get(c).replace(' 答錯', '') + '、' : '') + p + ' 答錯'); });
      if(m >= n){
        if(!parent) grid.classList.add('all-mastered');
        rows.push('<div class="vp-row vp-done"><b>' + esc(p) + '</b>：🎉 ' + n + ' 個字全部答對！這個單元不用再背了。</div>');
        return;
      }
      rows.push('<div class="vp-row"><b>' + esc(p) + '</b>：答對率 <b>' + pct + '%</b>（答對 ' + m + ' / ' + n + ' 個字），' +
        '<span class="vp-red">還有 ' + redWords.length + ' 個紅字要複習</span>' + (n - m - redWords.length ? '，' + (n - m - redWords.length) + ' 個還沒在本站考過' : '') +
        (cards.filter(c => (sOf(c) || {}).s === 'k').length ? '（其中 ' + cards.filter(c => (sOf(c) || {}).s === 'k').length + ' 個 WORD UP 標熟記，考對才算會）' : '') +
        '<div class="vp-bar"><i style="width:' + pct + '%"></i></div>' +
        (redWords.length ? '<div class="vp-words">要複習：' + redWords.map(esc).join('、') + '</div>' : '') +
        '<div class="vp-tip">複習紅色的字後，再按「📝 單元測驗」——只會考還沒答對的字。（' + new Date(rec.at).toLocaleDateString() + ' 測驗）</div></div>');
    });
    tags.forEach((t, c) => c.setAttribute('data-tag', t));
    const box = document.createElement('div');
    box.id = 'vcProgress';
    box.className = 'vc-progress';
    box.innerHTML = '<div class="vp-title">📊 我的學習進度</div>' + rows.join('');
    grid.parentNode.insertBefore(box, grid);
  }
  showProgress();
  window.addEventListener('pageshow', showProgress);

  document.addEventListener('click', e => {
    const say = e.target.closest('.vc-say');
    if(say){ stop(); play(say); return; }
    const hide = e.target.closest('[data-hide]');
    if(hide){
      const cls = 'hide-' + hide.dataset.hide;
      const on = grid.classList.toggle(cls);
      hide.classList.toggle('on', on);
      grid.querySelectorAll('.peek').forEach(x => x.classList.remove('peek'));
      return;
    }
    if(e.target.closest('[data-play-all]')){
      const wasOn = !!(curBtn || paused);
      stop();
      if(wasOn) return;   // 播放中再按一次＝停止
      queue = Array.prototype.slice.call(grid.querySelectorAll('.vc-say:not(.sm)'));
      total = queue.length;
      next();
      return;
    }
    const peek = e.target.closest('.vc-zh, .vc-exzh, .vc-word, .vc-en');
    if(peek && (grid.classList.contains('hide-zh') || grid.classList.contains('hide-en'))) peek.classList.toggle('peek');
  });

  // ---- 我的字卡（2026-11-17）：每張單字卡加「☆ 存字卡」（首頁 repo 的 /cards/cards.js，要登入、用存摺同一個後端）----
  const abs = (u) => { try{ if(!u) return ''; const x = new URL(u, location.href); return x.pathname + x.hash; }catch(e){ return ''; } };   // hash：合併音檔的 #t=開始,結束
  const txt = (el, sel) => { const x = el.querySelector(sel); return x ? x.textContent.trim() : ''; };
  function addStars(){
    if(!window.Cards) return;
    grid.querySelectorAll('.vc-card').forEach(c => {
      if(c.querySelector('.ck-star')) return;
      const img = c.querySelector('.vc-photo'), say = c.querySelector('.vc-say:not(.sm)');
      const card = { en: txt(c, '.vc-word'), zh: txt(c, '.vc-zh'), pos: txt(c, '.vc-pos'), ex: txt(c, '.vc-en'), exzh: txt(c, '.vc-exzh'),
        img: img ? abs(img.getAttribute('src')) : '', audio: say ? abs(say.dataset.src) : '', src: '國中2000字｜' + document.title.replace(/[｜|].*$/, '').trim(), url: location.pathname };
      const head = c.querySelector('.vc-head');
      if(card.en && head) head.insertAdjacentHTML('beforeend', ' ' + Cards.btn(card));
    });
  }
  function need(src, test){ if(test()) return Promise.resolve(); return new Promise(r => { const s = document.createElement('script'); s.src = src; s.onload = s.onerror = r; document.head.appendChild(s); }); }
  need(new URL('../points.js', document.currentScript ? document.currentScript.src : location.href).href, () => window.Points)
    .then(() => need('/cards/cards.js?v=20261117a', () => window.Cards)).then(addStars);
})();
