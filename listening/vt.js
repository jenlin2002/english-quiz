// 影片聽力（listening/vNN.html）共用程式：用 YouTube IFrame API 播影片的一段（data-t="開始秒,結束秒"），
// 作答時每段可以聽幾次（window.VT.plays）、遮住畫面（影片本身有燒進去的中英字幕）、單字表 🔊（瀏覽器語音）。
// 作答／送出／訂正／計點由 grammar2/gquiz.js 處理；重聽速度、目錄頁成績由 lt.js 處理（共用 ltRate、ltScore）。
(function(){
  const C = window.VT || {};
  const mem = {};
  const get = k => { try{ return localStorage.getItem(k); }catch(e){ return k in mem ? mem[k] : null; } };
  const set = (k, v) => { try{ localStorage.setItem(k, v); }catch(e){ mem[k] = v; } };
  const del = k => { try{ localStorage.removeItem(k); }catch(e){ delete mem[k]; } };
  const who = () => (get('quizStudentName') || '').trim();
  const fmt = s => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');

  // ---- YouTube 播放器 ----
  let player = null, ready = false, cur = null, stopAt = 0, timer = 0, pending = null;
  window.onYouTubeIframeAPIReady = function(){
    player = new YT.Player('vtPlayer', {
      videoId: C.video,
      playerVars: { controls: 0, disablekb: 1, rel: 0, playsinline: 1, cc_load_policy: 0, iv_load_policy: 3, start: C.start || 0 },
      events: {
        onReady: () => { ready = true; },
        onStateChange: e => {
          if(e.data === YT.PlayerState.PLAYING && pending){ const f = pending; pending = null; f(); }
          if(e.data === YT.PlayerState.ENDED) stop();
        }
      }
    });
  };
  const s = document.createElement('script'); s.src = 'https://www.youtube.com/iframe_api'; document.head.appendChild(s);

  function stop(){
    clearInterval(timer); pending = null;
    if(player && ready) try{ player.pauseVideo(); }catch(e){}
    if(cur){ cur.classList.remove('playing'); cur = null; }
    status('');
  }
  function status(t){ const el = document.getElementById('vtStatus'); if(el) el.textContent = t; }
  function play(btn, rate, onStart){
    stop();
    if(!ready){ flash(btn, '影片還在載入，等一下再按'); return; }
    const t = btn.dataset.t.split(',').map(Number);
    cur = btn; btn.classList.add('playing'); stopAt = t[1];
    pending = () => { if(onStart) onStart(); };
    player.setPlaybackRate(rate || 1);
    player.seekTo(t[0], true);
    player.playVideo();
    // iPhone／iPad 有時候要先點一下影片畫面才能播
    setTimeout(() => { if(cur === btn && pending){ stop(); flash(btn, '先點一下影片畫面，再按一次'); } }, 4000);
    timer = setInterval(() => {
      const now = player.getCurrentTime ? player.getCurrentTime() : 0;
      if(cur === btn) status('▶ 播放中 ' + fmt(Math.max(now, t[0])) + ' / ' + fmt(t[1]));
      if(now >= stopAt) stop();
    }, 200);
  }
  function flash(btn, text){ const o = btn.textContent; btn.textContent = text; setTimeout(() => { if(btn.textContent === text) btn.textContent = o; }, 2500); }
  window.addEventListener('pagehide', stop);
  const rate = () => +(get('ltRate') || 1) || 1;

  // ---- 遮住畫面（預設遮住：影片燒了中英字幕，作答時只用聽的） ----
  const cover = document.getElementById('vtCover'), ctg = document.getElementById('vtCoverBtn');
  function showCover(on){
    if(!cover) return;
    cover.hidden = !on;
    if(ctg) ctg.textContent = on ? '👀 顯示畫面（會看到字幕）' : '🙈 遮住畫面（只用聽的）';
    set('vtCover', on ? '1' : '0');
  }
  showCover(get('vtCover') !== '0');
  if(ctg) ctg.addEventListener('click', () => showCover(cover.hidden));

  // ---- 作答時每段可以聽幾次（重新測驗或沒有暫存時歸零） ----
  const playsKey = () => 'vtPlays:' + location.pathname + ':' + (who() || '-');
  const draftKey = () => 'gqDraft:' + location.pathname + ':' + (who() || '-');
  let plays = {};
  try{ plays = get(draftKey()) ? JSON.parse(get(playsKey()) || '{}') : {}; }catch(e){}
  if(!get(draftKey())) del(playsKey());
  // 這一段還有題目在作答（不是已對完答案、也不是訂正中）就限制次數
  const limited = btn => {
    const sec = btn.closest('.gq-sec');
    return C.plays > 0 && sec && [...sec.querySelectorAll('.gq-item')].some(it => !it.classList.contains('done') && !it.classList.contains('gq-redo'));
  };
  function label(btn){
    const t = btn.dataset.t.split(',').map(Number), rng = '（' + fmt(t[0]) + '–' + fmt(t[1]) + '）';
    if(!limited(btn)){ btn.textContent = '▶ 播放這一段' + rng; btn.classList.remove('used'); return; }
    const left = C.plays - (plays[btn.dataset.id] || 0);
    btn.textContent = left > 0 ? '▶ 播放這一段' + rng + '　還可以聽 ' + left + ' 次' : '這一段已經聽 ' + C.plays + ' 次了';
    btn.classList.toggle('used', left <= 0);
  }
  const relabel = () => document.querySelectorAll('.vt-play').forEach(label);

  document.addEventListener('click', e => {
    const pb = e.target.closest('.vt-play');
    if(pb){
      if(cur === pb){ stop(); return; }
      if(limited(pb)){
        const used = plays[pb.dataset.id] || 0;
        if(used >= C.plays){ alert('這一段已經聽 ' + C.plays + ' 次了，憑印象作答吧！送出後可以再重聽。'); return; }
        play(pb, 1, () => { plays[pb.dataset.id] = (plays[pb.dataset.id] || 0) + 1; set(playsKey(), JSON.stringify(plays)); label(pb); });
      } else play(pb, rate());
      return;
    }
    const sb = e.target.closest('.vt-say');
    if(sb){ if(cur === sb) stop(); else play(sb, rate()); return; }
    if(e.target.closest('#vtStop')){ stop(); return; }
    const wb = e.target.closest('.vw-say');
    if(wb && 'speechSynthesis' in window){
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(wb.dataset.say); u.lang = 'en-US'; u.rate = 0.9; speechSynthesis.speak(u);
      return;
    }
    if(e.target.closest('[data-act="restart"]')) setTimeout(() => { if(!get(draftKey())){ plays = {}; del(playsKey()); relabel(); } }, 0);
  });

  const gq = document.getElementById('gquiz');
  if(gq){ new MutationObserver(relabel).observe(gq, { childList: true }); relabel(); }

  // ---- 重點片語（原句就是題目）：送出成績（有題目已對完答案）後才打開 ----
  const after = document.querySelectorAll('.vt-after');
  function unlock(){
    const open = !gq || !!gq.querySelector('.gq-item.done');
    after.forEach(s => s.classList.toggle('locked', !open));
  }
  if(after.length){
    unlock();
    if(gq) new MutationObserver(unlock).observe(gq, { childList: true, subtree: true, attributes: true, attributeFilter: ['class'] });
  }

  // ---- 遮中文／遮英文（原文、片語、單字表；遮住的字點一下可以偷看。題目和選項的英文不遮） ----
  document.querySelectorAll('.vw-ex').forEach(ex => [...ex.childNodes].forEach(n => {
    if(n.nodeType === 3 && n.textContent.trim()){ const sp = document.createElement('span'); sp.className = 'en'; sp.textContent = n.textContent; n.replaceWith(sp); }
  }));
  const hide = { zh: get('vtHideZh') === '1', en: get('vtHideEn') === '1' };
  const hideBar = () => '<div class="vt-hide">自我練習：<button type="button" data-hide="zh">🙈 遮中文</button><button type="button" data-hide="en">🙈 遮英文</button><small>遮住的字點一下可以偷看</small></div>';
  const speed = document.querySelector('.lt-speed');
  if(speed) speed.insertAdjacentHTML('afterend', hideBar());
  document.querySelectorAll('.vt-words').forEach(ol => ol.insertAdjacentHTML('beforebegin', hideBar()));
  function applyHide(){
    document.body.classList.toggle('vt-hzh', hide.zh);
    document.body.classList.toggle('vt-hen', hide.en);
    document.querySelectorAll('.vt-hide button').forEach(b => {
      const on = hide[b.dataset.hide];
      b.classList.toggle('on', on);
      b.textContent = (on ? '👀 顯示' : '🙈 遮') + (b.dataset.hide === 'zh' ? '中文' : '英文');
    });
    document.querySelectorAll('.vt-peek').forEach(el => el.classList.remove('vt-peek'));
  }
  applyHide();
  document.addEventListener('click', e => {
    const hb = e.target.closest('.vt-hide button');
    if(hb){ const k = hb.dataset.hide; hide[k] = !hide[k]; set(k === 'zh' ? 'vtHideZh' : 'vtHideEn', hide[k] ? '1' : '0'); applyHide(); return; }
    if(!hide.zh && !hide.en) return;
    const m = e.target.closest('.vt-hzh .lt-opzh, .vt-hzh .zh, .vt-hzh .vw-zh, .vt-hen .lt-line .en, .vt-hen .vp-quote .en, .vt-hen .vw-ex .en, .vt-hen .vw-en');
    if(m && !m.closest('h1')) m.classList.toggle('vt-peek');
  });

  // ---- 單字表：存字卡（有 /cards/cards.js 時） ----
  function cardBtns(){
    if(!window.Cards || !Cards.btn) return;
    document.querySelectorAll('.vw-item[data-en]').forEach(li => {
      const head = li.querySelector('.vw-head');
      head.insertAdjacentHTML('beforeend', ' ' + Cards.btn({ en: li.dataset.en, zh: li.dataset.zh, pos: li.dataset.pos, ex: li.dataset.ex, exzh: li.dataset.exzh,
        src: '影片聽力｜' + (C.title || ''), url: location.pathname }));
    });
  }
  // points.js 在頁尾載入；等它好了再載入 /cards/cards.js
  if(document.querySelector('.vw-item')) window.addEventListener('load', () => {
    if(!window.Points) return;
    if(window.Cards) return cardBtns();
    const sc = document.createElement('script'); sc.src = '/cards/cards.js?v=20261117a'; sc.onload = cardBtns; document.head.appendChild(sc);
  });
})();
