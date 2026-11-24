"""WORD UP 複習區：一次產生指定單元的頁面＋錄音＋放大音量＋合併音檔＋重跑 WORD UP 對照表（2026-11-24）。
用法（english-quiz 根目錄）：python tools/vocab_gen/build_wordup.py u03 u04 u05     （也可寫 3 4 5；要先設 KOKORO_DIR）
資料檔 tools/vocab_gen/wordup_uNN.py（字表照 vocab/wordup/status.json 的 units.uNN；中文、例句、題目自編）。
照片可放 vocab/wordup/img/uNN/<字>.jpg，沒有照片的字用資料檔的 emoji。
做完記得在 vocab/wordup/units.html 加卡片。"""
import importlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import build_vocab as B  # noqa: E402

keys = [a if a.startswith('u') else 'u%02d' % int(a) for a in sys.argv[1:]]
STATUS = json.load(open(os.path.join(REPO, 'vocab', 'wordup', 'status.json'), encoding='utf-8'))['units']
UNITS_HTML = os.path.join(REPO, 'vocab', 'wordup', 'units.html')
jobs, tags = [], []
for k in keys:
    m = importlib.import_module('wordup_' + k)
    tag = m.UNIT.get('tag') or 'u%02d' % m.UNIT['no']
    mine = [w['w'] for w in m.UNIT['words']]
    if mine != STATUS[tag]['words']:   # 字表一定要和 WORD UP 一模一樣（順序也一樣）
        raise SystemExit('%s 字表和 status.json 不同：多 %s／少 %s' % (tag, sorted(set(mine) - set(STATUS[tag]['words'])), sorted(set(STATUS[tag]['words']) - set(mine))))
    j = B.build(m)
    print('WORD UP %s：%d 個字、%d 個音檔' % (tag, len(m.UNIT['words']), len(j)), flush=True)
    jobs += j; tags.append(tag)
jf = os.path.join(HERE, 'audio_jobs_wordup.json')
json.dump(jobs, open(jf, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
py = sys.executable
subprocess.run([py, os.path.join(REPO, 'tools', 'grammar2_gen', 'tts_mp3.py'), jf], cwd=REPO, check=True, stdout=subprocess.DEVNULL)
for tag in tags:
    subprocess.run([py, os.path.join(HERE, 'boost_audio.py'), 'vocab/wordup/audio/' + tag], cwd=REPO, check=True, stdout=subprocess.DEVNULL)
    subprocess.run([py, os.path.join(HERE, 'sprite_audio.py'), 'vocab/wordup', tag, '--delete'], cwd=REPO, check=True)
subprocess.run([py, os.path.join(HERE, 'build_wordup_index.py')], cwd=REPO, check=True)
os.remove(jf)
# WORD UP 目錄 units.html：還沒有卡片的單元自動加在最後（說明＝字數＋重點整理前幾項）
html = open(UNITS_HTML, encoding='utf-8').read()
for k in keys:
    m = importlib.import_module('wordup_' + k)
    u, tag = m.UNIT, m.UNIT.get('tag') or 'u%02d' % m.UNIT['no']
    if 'href="%s.html"' % tag in html:
        continue
    ws = u['words']
    sub = '%d 字；%s' % (len(ws), '、'.join(r[0] for r in u['focus'][0]['rows'][:4]))
    card = ('    <div class="card">\n      <div class="card-week">WORD UP %s</div>\n      <div class="card-title">%s%s～%s</div>\n'
            '      <div class="card-sub">%s</div>\n      <div class="card-links"><a class="link-read" href="%s.html">📗 單字卡</a>'
            '<a class="link-slides" href="%s-slides.html">📊 投影片</a><a class="link-quiz" href="%s-quiz.html">📝 測驗</a></div>\n    </div>\n'
            % (u['en'], u['zh'], ws[0]['w'], ws[-1]['w'], sub.replace('<', '&lt;'), tag, tag, tag))
    i = html.rindex('  </div>\n</div>\n<script')   # 複習單元 grid 的結尾
    html = html[:i] + card + html[i:]
open(UNITS_HTML, 'w', encoding='utf-8').write(html)
print('完成：' + ' '.join(tags))
