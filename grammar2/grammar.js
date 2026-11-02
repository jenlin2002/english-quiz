// 國二文法分科區：單元頁練習題（點選即對答、顯示詳解；不計點數、不同步試算表）
// 每頁用 window.PRACTICE = [{ level, q, opts:[...], answer: 正確選項索引, exp }] 提供題目
(function(){
  const box = document.getElementById('practice');
  if(!box || !window.PRACTICE) return;
  const QS = window.PRACTICE;
  const state = QS.map(() => null); // null 未作答；true 對；false 錯
  const letters = 'ABCD';

  function render(onlyWrong){
    box.innerHTML = '';
    const bar = document.createElement('div');
    bar.className = 'score-bar';
    bar.innerHTML = '<span id="pScore"></span><span>' +
      '<button class="btn alt" id="pRetry">✏️ 只重做錯題</button> ' +
      '<button class="btn" id="pReset">↺ 全部重做</button></span>';
    box.appendChild(bar);

    let lastLevel = '';
    QS.forEach((item, i) => {
      if(onlyWrong && state[i] !== false) return;
      if(item.level !== lastLevel){
        lastLevel = item.level;
        const lv = document.createElement('div');
        lv.className = 'level';
        lv.textContent = item.level;
        box.appendChild(lv);
      }
      if(onlyWrong) state[i] = null;
      const q = document.createElement('div');
      q.className = 'q';
      q.innerHTML = '<div class="q-stem"><span class="num">' + (i + 1) + '.</span>' + item.q + '</div>' +
        '<div class="q-opts"></div><div class="q-exp"></div>';
      const opts = q.querySelector('.q-opts');
      item.opts.forEach((o, k) => {
        const b = document.createElement('button');
        b.className = 'q-opt';
        b.innerHTML = '(' + letters[k] + ') ' + o;
        b.onclick = () => pick(q, item, i, k);
        opts.appendChild(b);
      });
      box.appendChild(q);
    });
    document.getElementById('pRetry').onclick = () => render(true);
    document.getElementById('pReset').onclick = () => { state.fill(null); render(false); };
    updateScore();
  }

  function pick(q, item, i, k){
    const btns = q.querySelectorAll('.q-opt');
    btns.forEach(b => b.disabled = true);
    btns[item.answer].classList.add('right');
    const ok = k === item.answer;
    if(!ok) btns[k].classList.add('wrong');
    state[i] = ok;
    q.classList.add('done', ok ? 'hit' : 'miss');
    q.querySelector('.q-exp').innerHTML =
      '<span class="verdict">' + (ok ? '✓ 答對了！' : '✗ 正解是 (' + letters[item.answer] + ')') + '</span>　' + item.exp;
    updateScore();
  }

  function updateScore(){
    const done = state.filter(s => s !== null).length;
    const right = state.filter(s => s === true).length;
    const wrong = state.filter(s => s === false).length;
    document.getElementById('pScore').innerHTML =
      '已作答 <b>' + done + '</b> / ' + QS.length + '　答對 <b>' + right + '</b>　答錯 <b>' + wrong + '</b>';
    document.getElementById('pRetry').disabled = wrong === 0;
  }

  render(false);
})();
