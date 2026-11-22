"""重寫 vocab/index.html 裡「主題 2000 字 PART 2」那一區（P2-START～P2-END 之間），卡片依 w2000p2_uNN.py 資料檔產生。
資料檔 UNIT 可加 'card': '卡片說明'；沒有就自動列前 5 個字＋字數。用法：python tools/vocab_gen/p2_index.py"""
import glob, html, importlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
E = html.escape
cards = []
for f in sorted(glob.glob(os.path.join(HERE, 'w2000p2_u[0-9][0-9].py'))):
    m = importlib.import_module(os.path.basename(f)[:-3])
    u = m.UNIT
    tag = 'u%02d' % u['no']
    if not os.path.exists(os.path.join(REPO, 'vocab', 'w2000p2', tag + '.html')):
        continue
    ws = u['words']
    sub = u.get('card') or '%s%s 共 %d 字' % ('、'.join(w['w'] for w in ws[:5]), '…' if len(ws) > 5 else '', len(ws))
    cards.append('''    <div class="card">
      <div class="card-week">PART 2 · UNIT %d</div>
      <div class="card-title">%s %s</div>
      <div class="card-sub">%s</div>
      <div class="card-links"><a class="link-read" href="w2000p2/%s.html">📗 單字卡</a><a class="link-slides" href="w2000p2/%s-slides.html">📊 投影片</a><a class="link-quiz" href="w2000p2/%s-quiz.html">📝 測驗</a></div>
    </div>''' % (u['no'], E(u['en']), E(u['zh']), E(sub), tag, tag, tag))
block = ('<!-- P2-START：這一區由 tools/vocab_gen/p2_index.py 產生，不要手改 -->\n'
         '  <div class="section-title">主題 2000 字 PART 2：1201～2000 字（進階字，同樣照主題分單元；課本 PART 2 沒有 Unit 7）</div>\n'
         '  <div class="grid">\n%s\n  </div>\n\n<!-- P2-END -->' % '\n'.join(cards))
p = os.path.join(REPO, 'vocab', 'index.html')
s = open(p, encoding='utf-8').read()
s = re.sub(r'<!-- P2-START.*?<!-- P2-END -->', lambda _: block, s, flags=re.S)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('PART 2 卡片', len(cards))
