# 影片聽力頁產生程式：python tools/listening_gen/build_video.py v01 [v02 …]
# 資料檔 tools/listening_gen/lt_vNN.py（VIDEO dict），輸出 listening/vNN.html。
# 影片用 YouTube 原本的播放器（listening/vt.js），不下載影片、不錄音；作答／訂正／計點用 grammar2/gquiz.js。
import html, importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
E = lambda s: html.escape(str(s), quote=True)


def fmt(s):
    return '%d:%02d' % (s // 60, s % 60)


def line_html(t0, t1, who, en, zh):
    return ('<div class="lt-line"><button type="button" class="vt-say" data-t="%d,%d" title="重聽這一句（影片 %s）">🔊</button> '
            '<b class="lt-tag">%s</b><span class="en">%s</span><span class="zh">%s</span></div>') % (t0, t1, fmt(t0), E(who), E(en), E(zh))


def build(v):
    vid = v['id']
    secs = []
    for si, seg in enumerate(v['segments']):
        t0, t1 = seg['t']
        items = []
        for it in seg['items']:
            exp = ('<div class="lt-tr"><div class="lt-trh">📝 影片原文（依自動字幕整理）</div>' +
                   ''.join(line_html(*ln) for ln in it['lines']) +
                   '<div class="lt-opzh">選項：%s</div><div class="lt-tip">💡 %s</div></div>') % (E(it['optzh']), it['tip'])
            items.append({'type': 'mc', 'q': '<div class="lt-qtext">%s</div>' % E(it['q']),
                          'opts': [E(o) for o in it['opts']], 'answer': it['answer'], 'exp': exp})
        note = ('<button type="button" class="vt-play" data-id="s%d" data-t="%d,%d">▶ 播放這一段</button><br>%s'
                % (si + 1, t0, t1, E(seg['note'])))
        secs.append({'title': '%s（%d 題）' % (seg['title'], len(items)), 'note': note, 'items': items})
    n = sum(len(s['items']) for s in secs)
    label = 'Listening ' + vid.upper()
    gq = {'label': label, 'title': '影片聽力 ' + v['title'], 'back': 'index.html', 'mode': '影片聽力',
          'links': '<a class="btn" href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">▶ 到 YouTube 看完整影片</a> '
                   '<a class="btn" href="index.html">聽力訓練目錄</a>' % v['yt'],
          'sections': secs}
    picked = set(v.get('picked', []))
    words = ''.join(
        ('<li class="vw-item" data-en="%s" data-pos="%s" data-zh="%s" data-ex="%s" data-exzh="%s"><div class="vw-head">'
         '<button type="button" class="vw-say" data-say="%s" title="發音">🔊</button> <b class="vw-en">%s</b>%s '
         '<span class="vw-pos">%s</span> <span class="vw-zh">%s</span></div>'
         '<div class="vw-ex"><button type="button" class="vw-say" data-say="%s" title="唸例句">🔊</button> %s<span class="zh">%s</span></div></li>')
        % (E(w), E(p), E(z), E(ex), E(exz), E(w), E(w), ' <span class="vw-pick" title="影片最後整理的精選字">⭐</span>' if w in picked else '',
           E(p), E(z), E(ex), E(ex), E(exz)) for w, p, z, ex, exz in v['words'])
    npick = sum(1 for w in v['words'] if w[0] in picked)
    # 重點片語：影片最後整理的片語；原句可跳回影片聽，說明、例句自編
    phrases = ''
    for ph in v.get('phrases', []):
        t0, t1, who, qen, qzh = ph['quote']
        exs = ''.join('<div class="vw-ex"><button type="button" class="vw-say" data-say="%s" title="唸例句">🔊</button> %s<span class="zh">%s</span></div>'
                      % (E(a), E(a), E(b)) for a, b in ph['ex'])
        phrases += ('<li class="vw-item vp-item" data-en="%s" data-pos="phr." data-zh="%s" data-ex="%s" data-exzh="%s"><div class="vw-head">'
                    '<button type="button" class="vw-say" data-say="%s" title="發音">🔊</button> <b class="vw-en">%s</b> <span class="vw-zh">%s</span></div>'
                    '<div class="vp-quote"><button type="button" class="vt-say" data-t="%d,%d" title="回到影片聽原句（%s）">🎬</button> '
                    '<b class="lt-tag">%s</b> <span class="en">%s</span><span class="zh">%s</span></div>'
                    '<div class="vp-note">💡 %s</div>%s</li>') % (
            E(ph['p']), E(ph['zh']), E(ph['ex'][0][0]), E(ph['ex'][0][1]), E(ph['p']), E(ph['p']), E(ph['zh']),
            t0, t1, fmt(t0), E(who), E(qen), E(qzh), ph['note'], exs)
    phr_sec = ('''  <section class="part vt-after">
    <h2>🔑 重點片語</h2>
    <p class="vt-lockmsg">🔒 這些片語就是題目裡的句子，<b>送出成績</b>後才會打開。</p>
    <div class="vt-after-body">
    <p class="lt-ldesc">影片最後整理的 %d 個片語。🎬 回到影片聽原句；說明和例句是本站自編，🔊 用這台裝置的語音唸。</p>
    <ol class="vt-words vt-phr">%s</ol>
    </div>
  </section>
''' % (len(v['phrases']), phrases)) if phrases else ''
    total = v['segments'][-1]['t'][1] - v['segments'][0]['t'][0]
    page = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>影片聽力｜%(title)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Noto+Sans+TC:wght@400;500;700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../grammar2/grammar.css?v=20261102">
<link rel="stylesheet" href="listening.css?v=20261128b">
</head>
<body>
<div class="wrap">
  <div class="top-links">
    <a class="home-link" href="index.html">← 聽力訓練目錄</a>
  </div>
  <div class="eyebrow">LISTENING · VIDEO · %(VID)s</div>
  <h1>影片聽力 <span class="zh">%(title)s</span></h1>
  <div class="subtitle">%(en)s・真人原速・%(level)s・%(nseg)d 段 %(n)d 題・約 %(mins)d 分鐘影片</div>
  <section class="part">
    <p>%(about)s</p>
  </section>
  <div class="vt-box">
      <div class="vt-frame"><div id="vtPlayer"></div><div class="vt-cover" id="vtCover"><div>🎧 只用聽的<br><small>影片畫面有中英字幕，作答時先遮住</small></div></div></div>
      <div class="vt-bar"><button type="button" class="btn" id="vtCoverBtn">👀 顯示畫面</button> <button type="button" class="btn" id="vtStop">⏹ 停止</button> <span id="vtStatus" class="vt-status"></span></div>
      <div class="vt-src">影片來源：YouTube「%(channel)s」頻道 <a href="https://www.youtube.com/watch?v=%(yt)s" target="_blank" rel="noopener">%(title)s</a>（%(kind)s從 %(start)s 開始）</div>
  </div>
  <section class="part lt-rules">
    <ul>
      <li>每一段按 <b>▶ 播放這一段</b>，影片會自己停在那一段的結尾。作答時每段最多聽 <b>%(plays)d 次</b>，可以先看題目再聽。</li>
      <li>全部作答才能送出；送出後看 <b>影片原文＋中文</b>，每一句都能按 🔊 回到影片那裡重聽，也可以改成慢速。</li>
      <li>錯的題目要訂正（訂正時可以一直重聽），全部訂正完再補送 1 點。</li>
    </ul>
    <div class="lt-speed">重聽速度：<button type="button" data-rate="1">一般</button><button type="button" data-rate="0.75">🐢 慢速</button></div>
  </section>
  <section class="part lt-quiz"><div id="gquiz"></div></section>
%(phr)s  <section class="part">
    <h2>📖 重點單字</h2>
    <p class="lt-ldesc">%(kind)s裡出現的字%(pick)s。中文、例句是本站自編；🔊 用這台裝置的語音唸。</p>
    <ol class="vt-words">%(words)s</ol>
  </section>
</div>
<script>
window.VT = %(vt)s;
window.GQUIZ = %(gq)s;
</script>
<script src="lt.js?v=20261125a"></script>
<script src="vt.js?v=20261128b"></script>
<script src="../grammar2/gquiz.js?v=20261125a"></script>
<script src="../points.js"></script>
</body>
</html>
''' % {'title': E(v['title']), 'VID': vid.upper(), 'en': E(v['en']), 'level': E(v['level']), 'nseg': len(secs), 'n': n,
       'mins': round(total / 60), 'about': v['about'], 'channel': E(v['channel']), 'yt': v['yt'], 'start': fmt(v['start']),
       'plays': v['plays'], 'words': words, 'kind': E(v.get('kind', '記者會')), 'phr': phr_sec,
       'pick': '（⭐＝影片最後整理的 %d 個精選字）' % npick if npick else '',
       'vt': json.dumps({'video': v['yt'], 'start': v['start'], 'plays': v['plays'], 'title': v['title']}, ensure_ascii=False),
       'gq': json.dumps(gq, ensure_ascii=False, indent=1)}
    out = os.path.join(ROOT, 'listening', vid + '.html')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(page)
    print('寫入', out, '%d 題' % n)


if __name__ == '__main__':
    for a in sys.argv[1:] or ['v01']:
        build(importlib.import_module('lt_' + a).VIDEO)
