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

  // 上次測驗錯的字標紅（gquiz.js 送出時記在 vocabWrong:<這一頁>:<登入者>，只看這台裝置）
  //   學生只看自己的；家長 PARENT（和測試帳號 TEST）會一起看到 BRANDEN、MELISSA 在這台裝置答錯的字
  function markWrong(){
    let name = '';
    try{ name = (localStorage.getItem('quizStudentName') || '').trim().toUpperCase(); }catch(e){}
    const old = document.getElementById('vcWrongNote');
    if(old) old.remove();
    grid.querySelectorAll('.vc-card.wrong').forEach(c => { c.classList.remove('wrong'); c.removeAttribute('data-wrong-by'); });
    if(!name) return;
    const people = /^(PARENT|TEST)$/.test(name) ? [name, 'BRANDEN', 'MELISSA'] : [name];
    const by = new Map();   // 卡片 → 答錯的人
    const lines = [];
    people.forEach(p => {
      let rec = null;
      try{ rec = JSON.parse(localStorage.getItem('vocabWrong:' + location.pathname + ':' + p) || 'null'); }catch(e){}
      if(!rec || !rec.words || !rec.words.length) return;
      const cands = rec.words.map(s => String(s || '').toLowerCase().trim()).filter(Boolean);
      const hit = w => cands.some(c => c === w || c.split(/[^a-z'-]+/).includes(w) ||
        (w.length >= 3 && c.indexOf(' ') < 0 && c.startsWith(w) && c.length - w.length <= 4));   // stamps、swimming、dishes
      const words = [];
      grid.querySelectorAll('.vc-card').forEach(card => {
        const el = card.querySelector('.vc-word');
        if(el && hit(el.textContent.toLowerCase().trim())){ by.set(card, (by.get(card) || []).concat(p)); words.push(el.textContent.trim()); }
      });
      if(words.length) lines.push(p + ' 上次測驗（' + new Date(rec.at).toLocaleDateString() + '）答錯 ' + words.length + ' 個：' + words.join('、'));
    });
    if(!lines.length) return;
    by.forEach((ps, card) => { card.classList.add('wrong'); card.setAttribute('data-wrong-by', ps.join('、') + ' 答錯'); });
    const note = document.createElement('div');
    note.id = 'vcWrongNote';
    note.className = 'vc-wrong-note';
    note.innerHTML = '🔴 紅框的字是上次測驗答錯的字，再多聽、多唸幾次！<br>' + lines.map(l => l.replace(/[&<>]/g, '')).join('<br>');
    grid.parentNode.insertBefore(note, grid);
  }
  markWrong();
  window.addEventListener('pageshow', markWrong);

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
