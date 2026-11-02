"""用 Kokoro 錄投影片語音，直接用 soundfile 寫 mp3（不需要 ffmpeg；需要 libsndfile 1.1 以上）。
用法：python tools/grammar2_gen/tts_mp3.py tools/grammar2_gen/audio_jobs.json
模型檔放在環境變數 KOKORO_DIR 指定的資料夾（kokoro-v1.0.int8.onnx、voices-v1.0.bin），不要放進 git。
已經存在的 mp3 會跳過，要重錄就先刪掉。
"""
import json, os, sys
import soundfile as sf
from kokoro_onnx import Kokoro

MD = os.environ.get('KOKORO_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models'))
k = Kokoro(os.path.join(MD, 'kokoro-v1.0.int8.onnx'), os.path.join(MD, 'voices-v1.0.bin'))
with open(sys.argv[1], encoding='utf-8') as f:
    items = json.load(f)
for text, out in items:
    if os.path.exists(out):
        continue
    os.makedirs(os.path.dirname(out), exist_ok=True)
    samples, sr = k.create(text, voice='af_heart', speed=0.9, lang='en-us')
    sf.write(out, samples, sr, format='MP3', subtype='MPEG_LAYER_III', compression_level=0.7)
    print(os.path.basename(os.path.dirname(out)), os.path.basename(out), flush=True)
