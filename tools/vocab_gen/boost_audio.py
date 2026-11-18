"""把單字區的 mp3 音量放大（Kokoro 錄出來平均約 -22 dB，聽起來偏小聲）。
目標：平均音量（RMS）-16 dB，但最大音量不超過 -1 dB（不會破音）。
已經夠大聲的檔案（差不到 0.5 dB）會跳過，所以重跑不會越放越大。
用法：python tools/vocab_gen/boost_audio.py                 （預設處理 vocab/*/audio/ 底下全部）
      python tools/vocab_gen/boost_audio.py vocab/w2000/audio/u21   （只處理新錄的單元）
需要：numpy、soundfile（libsndfile 1.1 以上，和 tts_mp3.py 一樣）。
"""
import glob, os, sys
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
TARGET_MEAN = -16.0   # dB
PEAK_LIMIT = -1.0     # dB
SKIP_BELOW = 0.5      # 要放大的量小於這個就不動


def db(x):
    return 20 * np.log10(max(x, 1e-9))


def boost(path):
    data, sr = sf.read(path, dtype='float32')
    if data.ndim > 1:
        data = data.mean(axis=1)
    mean, peak = db(float(np.sqrt(np.mean(data ** 2)))), db(float(np.max(np.abs(data))))
    gain = min(TARGET_MEAN - mean, PEAK_LIMIT - peak)
    if gain < SKIP_BELOW:
        return path, 0.0
    data = np.clip(data * (10 ** (gain / 20)), -1.0, 1.0)
    tmp = path + '.tmp.mp3'
    sf.write(tmp, data, sr, format='MP3', subtype='MPEG_LAYER_III', compression_level=0.7)
    os.replace(tmp, path)
    return path, gain


if __name__ == '__main__':
    dirs = sys.argv[1:] or glob.glob(os.path.join(REPO, 'vocab', '*', 'audio', '*'))
    files = sorted(f for d in dirs for f in glob.glob(os.path.join(d, '*.mp3')))
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(boost, files))
    done = [g for _, g in res if g > 0]
    print('共 %d 個檔，放大 %d 個（平均 +%.1f dB），跳過 %d 個' % (len(res), len(done), sum(done) / max(len(done), 1), len(res) - len(done)))
