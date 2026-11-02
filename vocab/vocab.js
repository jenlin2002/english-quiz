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
