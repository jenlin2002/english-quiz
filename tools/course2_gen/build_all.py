import json, importlib, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sl, qb
REPO=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'course2')
SP=os.path.dirname(os.path.abspath(__file__))
WEEKS={16:'比較結構與平行對等',17:'倒裝句與強調句（中高級入門）',18:'主詞動詞一致、代名詞與限定詞',19:'句型整合與英檢題型診斷'}
audio_jobs={}
for w,t in WEEKS.items():
    m=importlib.import_module('w%d_slides'%w)
    assert m.T==t
    says=sl.build(w,t,m.S,'%s/w%d'%(REPO,w))
    audio_jobs[w]=says
    qb.build(w,t,'w%d_data.js'%w,'%s/w%d'%(REPO,w))
    print(w,'slides',len(m.S),'audio',len(says))
qb.build(20,'全期總驗收與英檢模擬（第 1–19 週）','w20_data.js',REPO+'/w20',review=True)
json.dump(audio_jobs,open(SP+'/audio_jobs.json','w'),ensure_ascii=False,indent=0)
