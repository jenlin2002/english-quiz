import sys, json, subprocess, os, soundfile as sf
from kokoro_onnx import Kokoro
MD = os.environ.get("KOKORO_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "models"))
k = Kokoro(os.path.join(MD, "kokoro-v1.0.int8.onnx"), os.path.join(MD, "voices-v1.0.bin"))
# args: json file of [[text, outpath], ...]
items = json.load(open(sys.argv[1]))
for text, out in items:
    samples, sr = k.create(text, voice="af_heart", speed=0.9, lang="en-us")
    wav = out + ".wav"
    sf.write(wav, samples, sr)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",wav,"-ac","1","-ar","24000","-b:a","48k",out], check=True)
    os.remove(wav)
    print(out, flush=True)
