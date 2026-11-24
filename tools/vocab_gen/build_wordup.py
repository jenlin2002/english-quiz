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
jobs, tags = [], []
for k in keys:
    m = importlib.import_module('wordup_' + k)
    tag = m.UNIT.get('tag') or 'u%02d' % m.UNIT['no']
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
print('完成：' + ' '.join(tags))
