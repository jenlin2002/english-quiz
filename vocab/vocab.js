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
  function markWrong(){
    let name = '', rec = null;
    try{
      name = (localStorage.getItem('quizStudentName') || '').trim();
      if(name) rec = JSON.parse(localStorage.getItem('vocabWrong:' + location.pathname + ':' + name.toUpperCase()) || 'null');
    }catch(e){}
    const old = document.getElementById('vcWrongNote');
    if(old) old.remove();
    grid.querySelectorAll('.vc-card.wrong').forEach(c => c.classList.remove('wrong'));
    if(!rec || !rec.words || !rec.words.length) return;
    const cands = rec.words.map(s => String(s || '').toLowerCase().trim()).filter(Boolean);
    const hit = w => cands.some(c => c === w || c.split(/[^a-z'-]+/).includes(w) ||
      (w.length >= 3 && c.indexOf(' ') < 0 && c.startsWith(w) && c.length - w.length <= 4));   // stamps、swimming、dishes
    let n = 0;
    grid.querySelectorAll('.vc-card').forEach(card => {
      const el = card.querySelector('.vc-word');
      if(el && hit(el.textContent.toLowerCase().trim())){ card.classList.add('wrong'); n++; }
    });
    if(!n) return;
    const note = document.createElement('div');
    note.id = 'vcWrongNote';
    note.className = 'vc-wrong-note';
    note.textContent = '🔴 紅色的 ' + n + ' 個字是 ' + name + ' 上次測驗答錯的字（' + new Date(rec.at).toLocaleDateString() + '），再多聽、多唸幾次！';
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
