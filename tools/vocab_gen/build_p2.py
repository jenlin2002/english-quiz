"""主題 2000 字 PART 2：一次產生指定單元的頁面＋錄音＋放大音量＋合併音檔＋重跑 WORD UP 對照表。
用法（english-quiz 根目錄）：python tools/vocab_gen/build_p2.py 3 4 5      （要先設 KOKORO_DIR）
照片先放好在 vocab/w2000p2/img/uNN/<字>.jpg，沒有照片的字用資料檔的 emoji。"""
import importlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import build_vocab as B  # noqa: E402

nos = [int(x) for x in sys.argv[1:]]
jobs = []
for no in nos:
    m = importlib.import_module('w2000p2_u%02d' % no)
    j = B.build(m)
    print('PART 2 Unit %d：%d 個字、%d 個音檔' % (no, len(m.UNIT['words']), len(j)))
    jobs += j
jf = os.path.join(HERE, 'audio_jobs_p2.json')
json.dump(jobs, open(jf, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
py = sys.executable
subprocess.run([py, os.path.join(REPO, 'tools', 'grammar2_gen', 'tts_mp3.py'), jf], cwd=REPO, check=True, stdout=subprocess.DEVNULL)
for no in nos:
    subprocess.run([py, os.path.join(HERE, 'boost_audio.py'), 'vocab/w2000p2/audio/u%02d' % no], cwd=REPO, check=True, stdout=subprocess.DEVNULL)
    subprocess.run([py, os.path.join(HERE, 'sprite_audio.py'), 'vocab/w2000p2', 'u%02d' % no, '--delete'], cwd=REPO, check=True)
subprocess.run([py, os.path.join(HERE, 'build_wordup_index.py')], cwd=REPO, check=True)
os.remove(jf)
subprocess.run([py, os.path.join(HERE, 'p2_index.py')], cwd=REPO, check=True)
