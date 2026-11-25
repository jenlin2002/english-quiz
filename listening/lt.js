// 聽力訓練（listening/）共用程式：播放（每回一個 all.mp3，用 data-t="開始,結束" 播一段）、作答時每題聽幾次的限制、
// 重聽速度（一般／慢速）、聽寫練習、目錄頁顯示這台裝置的成績。作答／送出／訂正／計點由 grammar2/gquiz.js 處理。
(function(){
  const C = window.LT || {};
  const mem = {};
  const get = k => { try{ return localStorage.getItem(k); }catch(e){ return k in mem ? mem[k] : null; } };
  const set = (k, v) => { try{ localStorage.setItem(k, v); }catch(e){ mem[k] = v; } };
  const del = k => { try{ localStorage.removeItem(k); }catch(e){ delete mem[k]; } };
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const who = () => (get('quizStudentName') || '').trim();

  // ---- 播放 ----
  const audio = new Audio();
  audio.preload = 'auto';
  let cur = null, stopAt = 0, timer = 0;
  function stop(){
    audio.pause(); clearInterval(timer);
    if(cur){ cur.classList.remove('playing'); cur = null; }
  }
  // 整個 all.mp3 先下載成 blob 再播：任何伺服器都能準確跳到 #t 的位置（不靠 Range 請求）
  let loading = null;
  function load(){
    if(!loading) loading = fetch(C.audio).then(r => { if(!r.ok) throw r.status; return r.blob(); })
      .then(b => new Promise(res => { audio.src = URL.createObjectURL(b); audio.addEventListener('loadedmetadata', res, { once: true }); audio.load(); }))
      .catch(e => { loading = null; throw e; });
    return loading;
  }
  // onStart：真的開始播放才呼叫（算「聽了一次」）；音檔還沒載完時先顯示「載入中」，iPad 若擋自動播放就請他再按一次
  function play(btn, rate, onStart){
    stop();
    const t = btn.dataset.t.split(',').map(Number);
    cur = btn; btn.classList.add('playing'); stopAt = t[1];
    const go = () => {
      btn.classList.remove('loading');
      if(cur !== btn) return;
      try{ audio.currentTime = t[0]; }catch(e){}
      audio.playbackRate = rate || 1;
      audio.play().then(() => { if(onStart) onStart(); }, () => { stop(); flash(btn, '再按一次 ▶'); });
      clearInterval(timer);
      timer = setInterval(() => { if(audio.currentTime >= stopAt || audio.ended) stop(); }, 50);
    };
    if(audio.readyState >= 1) go();
    else { btn.classList.add('loading'); load().then(go, () => { btn.classList.remove('loading'); stop(); alert('音檔載入失敗，請檢查網路後再按一次。'); }); }
  }
  function flash(btn, text){ const o = btn.textContent; btn.textContent = text; setTimeout(() => { if(btn.textContent === text) btn.textContent = o; }, 2500); }
  if(window.LT) setTimeout(() => load().catch(() => {}), 300);   // 先在背景下載，按播放時就能馬上播
  audio.addEventListener('ended', stop);
  window.addEventListener('pagehide', stop);

  // ---- 重聽速度 ----
  let rate = +(get('ltRate') || 1) || 1;
  function showRate(){ document.querySelectorAll('.lt-speed button').forEach(b => b.classList.toggle('on', +b.dataset.rate === rate)); }

  // ---- 作答時每題聽幾次（這台裝置、這個登入者；重新測驗或沒有暫存時歸零） ----
  const playsKey = () => 'ltPlays:' + location.pathname + ':' + (who() || '-');
  const draftKey = () => 'gqDraft:' + location.pathname + ':' + (who() || '-');
  let plays = {};
  try{ plays = get(draftKey()) ? JSON.parse(get(playsKey()) || '{}') : {}; }catch(e){}
  if(!get(draftKey())) del(playsKey());
  const limited = btn => {
    const it = btn.closest('.gq-item');
    return C.plays > 0 && it && !it.classList.contains('done') && !it.classList.contains('gq-redo');
  };
  function label(btn){
    if(!limited(btn)){ btn.textContent = '▶ 播放'; btn.classList.remove('used'); return; }
    const left = C.plays - (plays[btn.dataset.id] || 0);
    btn.textContent = left > 0 ? '▶ 播放（還可以聽 ' + left + ' 次）' : '已經聽 ' + C.plays + ' 次了';
    btn.classList.toggle('used', left <= 0);
  }
  const relabel = () => document.querySelectorAll('.lt-play').forEach(label);

  document.addEventListener('click', e => {
    const sp = e.target.closest('.lt-speed button');
    if(sp){ rate = +sp.dataset.rate; set('ltRate', String(rate)); showRate(); return; }
    const pb = e.target.closest('.lt-play');
    if(pb){
      if(cur === pb){ stop(); return; }
      if(limited(pb)){
        const used = plays[pb.dataset.id] || 0;
        if(used >= C.plays){ alert('這一題已經聽 ' + C.plays + ' 次了，憑印象作答吧！送出後可以再重聽。'); return; }
        play(pb, 1, () => { plays[pb.dataset.id] = (plays[pb.dataset.id] || 0) + 1; set(playsKey(), JSON.stringify(plays)); label(pb); });
      } else play(pb, rate);
      return;
    }
    const sb = e.target.closest('.lt-say');
    if(sb){ if(cur === sb) stop(); else play(sb, rate); return; }
    if(e.target.closest('[data-act="restart"]')) setTimeout(() => { if(!get(draftKey())){ plays = {}; del(playsKey()); relabel(); } }, 0);
  });

  // gquiz 每次重畫題目後，按鈕文字重新標上剩幾次
  const gq = document.getElementById('gquiz');
  if(gq){
    new MutationObserver(() => { relabel(); saveScore(); }).observe(gq, { childList: true });
    relabel();
  }

  // 送出後在這台裝置記一筆成績（目錄頁顯示）：從 gquiz 的暫存或結果列讀
  function saveScore(){
    const top = document.getElementById('gqTop');
    if(!top || !window.GQUIZ) return;
    const m = /得分\s*(\d+)\s*\/\s*(\d+)/.exec(top.textContent);
    if(!m) return;
    const id = location.pathname.replace(/.*\//, '').replace(/\.html$/, '');
    const k = 'ltScore:' + (who() || '-');
    let all = {};
    try{ all = JSON.parse(get(k) || '{}'); }catch(e){}
    const prev = all[id];
    if(prev && prev.at && Date.now() - prev.at < 5000) return;
    if(!prev || !prev.first) all[id] = { first: +m[1], total: +m[2], at: Date.now(), best: +m[1] };
    else { prev.best = Math.max(prev.best || 0, +m[1]); }
    set(k, JSON.stringify(all));
  }

  // ---- 目錄頁：這台裝置的成績 ----
  document.querySelectorAll('.lc-st[data-id]').forEach(el => {
    let all = {};
    try{ all = JSON.parse(get('ltScore:' + (who() || '-')) || '{}'); }catch(e){}
    const s = all[el.dataset.id];
    if(s) el.innerHTML = '✅ 第一次 ' + s.first + ' / ' + s.total + '（' + Math.round(s.first / s.total * 100) + '%）';
  });

  // ---- 聽寫 ----
  const D = document.getElementById('ltDict');
  if(D && window.LTD){
    const words = s => String(s).toLowerCase().replace(/[’‘]/g, "'").replace(/[^a-z0-9':.-]+/g, ' ').replace(/(^|\s)[.:-]+|[.:-]+(?=\s|$)/g, ' ').trim().split(/\s+/).filter(Boolean);
    const dKey = 'ltDict:' + location.pathname + ':' + (who() || '-');
    let saved = {};
    try{ saved = JSON.parse(get(dKey) || '{}'); }catch(e){}
    D.innerHTML = '<ol class="lt-dict">' + LTD.map((it, i) =>
      '<li data-i="' + i + '"><div class="ld-row"><button type="button" class="lt-say ld-play" data-t="' + it.t + '">▶ 播放</button>' +
      '<input class="ld-in" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="把聽到的英文打出來" value="' + esc(saved[i] || '') + '">' +
      '<button type="button" class="btn ld-check">對答案</button></div><div class="ld-res"></div></li>').join('') + '</ol>' +
      '<div class="ld-sum"></div>';
    D.addEventListener('input', e => {
      const li = e.target.closest('li'); if(!li || !e.target.classList.contains('ld-in')) return;
      saved[li.dataset.i] = e.target.value; set(dKey, JSON.stringify(saved));
    });
    D.addEventListener('keydown', e => { if(e.key === 'Enter' && e.target.classList.contains('ld-in')) e.target.closest('li').querySelector('.ld-check').click(); });
    D.addEventListener('click', e => {
      const b = e.target.closest('.ld-check'); if(!b) return;
      const li = b.closest('li'), it = LTD[+li.dataset.i];
      const want = words(it.en), got = words(li.querySelector('.ld-in').value);
      // 最長共同子序列：照順序對到的字算對
      const L = Array.from({ length: want.length + 1 }, () => new Array(got.length + 1).fill(0));
      for(let i = want.length - 1; i >= 0; i--) for(let j = got.length - 1; j >= 0; j--)
        L[i][j] = want[i] === got[j] ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
      const hit = new Array(want.length).fill(false);
      for(let i = 0, j = 0; i < want.length && j < got.length;){
        if(want[i] === got[j]){ hit[i] = true; i++; j++; } else if(L[i + 1][j] >= L[i][j + 1]) i++; else j++;
      }
      const ok = hit.filter(Boolean).length, all = ok === want.length && got.length === want.length;
      const shown = it.en.split(/\s+/); let wi = 0;
      const marked = shown.map(tok => { const n = words(tok).length; const good = hit.slice(wi, wi + n).every(Boolean); wi += n; return '<span class="' + (good ? 'ok' : 'ng') + '">' + esc(tok) + '</span>'; }).join(' ');
      li.querySelector('.ld-res').innerHTML = (all ? '<b class="ld-all">🎉 全對！</b> ' : '<b>聽對 ' + ok + ' / ' + want.length + ' 個字</b>　') +
        '<div class="ld-ans">' + marked + '</div><div class="ld-zh">' + esc(it.zh) + '</div>';
      li.classList.toggle('perfect', all);
      const done = D.querySelectorAll('li.perfect').length;
      D.querySelector('.ld-sum').textContent = '全對 ' + done + ' / ' + LTD.length + ' 句' + (done === LTD.length ? '　🎉 全部聽寫正確！' : '');
    });
  }
  showRate();
})();
