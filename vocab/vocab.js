// 單字區單字卡：🔊 播放（先用 mp3，沒有就用瀏覽器語音）、遮中文／遮英文、全部播放
(function(){
  const grid = document.getElementById('cards');
  if(!grid) return;
  let cur = null, queue = [];
  const tts = 'speechSynthesis' in window;

  function stop(){
    queue = [];
    if(cur){ cur.pause(); cur = null; }
    if(tts) speechSynthesis.cancel();
    document.querySelectorAll('.playing').forEach(e => e.classList.remove('playing'));
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
    const fin = () => { btn.classList.remove('playing'); if(card) card.classList.remove('playing'); done(); };
    const a = new Audio(btn.dataset.src);
    let fell = false;
    const fb = () => { if(fell) return; fell = true; speak(btn.dataset.say, fin); };
    a.addEventListener('ended', fin);
    a.addEventListener('error', fb);
    const p = a.play(); if(p && p.catch) p.catch(e => { if(!(e && e.name === 'AbortError')) fb(); });
    cur = a;
  }
  function next(){
    const b = queue.shift();
    if(!b) return;
    b.scrollIntoView({ block:'nearest', behavior:'smooth' });
    play(b, () => setTimeout(next, 500));
  }

  // 每個登入者自己的進度（gquiz.js 記在這台裝置 vocabProgress:<這一頁>:<登入者>）：
  //   答錯、還要複習的字 → 紅色；第一次就答對的字 → 暗灰色（不用再背）；全部答對 → 整個單元變灰。
  //   家長 PARENT（和測試帳號 TEST）看 BRANDEN、MELISSA 兩個人的統計，卡片只標紅、不變灰。
  const esc = s => String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
  //   每個字的狀態：本站答過的（vocabWords:<登入者>，所有單元共用）優先；沒答過就用 WORD UP 熟悉度（vocab/wordup/status.json）
  let WU = null;
  async function loadWordUp(){
    if(WU) return WU;
    try{ WU = await (await fetch(new URL('../wordup/status.json', location.href), { cache:'no-cache' })).json(); }catch(e){ WU = {}; }
    return WU;
  }
  function statusOf(p){
    const m = new Map();
    const u = ((WU || {}).users || {})[p];
    if(u) Object.keys(u.words).forEach(w => m.set(w.toLowerCase(), { s: u.words[w][0] === '熟記' ? 'm' : 'w', src: 'wordup', lv: u.words[w][0] }));
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
    cards.forEach(c => { c.classList.remove('wrong', 'mastered'); c.removeAttribute('data-tag'); });
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
        if(ms.has(w)){ c.classList.add('mastered'); tags.set(c, s.src === 'wordup' ? 'WORD UP 熟記' : '已答對'); }
        else if(wr.has(w)){ c.classList.add('wrong'); tags.set(c, s.src === 'wordup' ? 'WORD UP：' + s.lv : p + ' 答錯'); }
      });
      else redWords.forEach(w => { const c = cards.find(x => wordOf(x) === w); c.classList.add('wrong'); tags.set(c, (tags.get(c) ? tags.get(c).replace(' 答錯', '') + '、' : '') + p + ' 答錯'); });
      if(m >= n){
        if(!parent) grid.classList.add('all-mastered');
        rows.push('<div class="vp-row vp-done"><b>' + esc(p) + '</b>：🎉 ' + n + ' 個字全部答對！這個單元不用再背了。</div>');
        return;
      }
      rows.push('<div class="vp-row"><b>' + esc(p) + '</b>：答對率 <b>' + pct + '%</b>（答對 ' + m + ' / ' + n + ' 個字），' +
        '<span class="vp-red">還有 ' + redWords.length + ' 個紅字要複習</span>' + (n - m - redWords.length ? '，' + (n - m - redWords.length) + ' 個還沒考到' : '') +
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
      stop();
      queue = Array.prototype.slice.call(grid.querySelectorAll('.vc-say:not(.sm)'));
      next();
      return;
    }
    const peek = e.target.closest('.vc-zh, .vc-exzh, .vc-word, .vc-en');
    if(peek && (grid.classList.contains('hide-zh') || grid.classList.contains('hide-en'))) peek.classList.toggle('peek');
  });
})();
