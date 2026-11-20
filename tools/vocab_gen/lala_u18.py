# LaLa Word Unit 18（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 196–206 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 18, 'en': 'A Day Off for Your Mind', 'zh': '一字多義（十八）',
  'intro': 'tire 是輪胎，也是「使疲倦」；tear 唸 [tɪr] 是眼淚，唸 [tɛr] 是「撕開」。這個單元有 5 個主題單字、16 個更多單字，'
           '是 LaLa Word 的最後一個單元。',
  'words': [
    W('tire', '🛞', [
        S('v.', '使疲倦', 'The long walk tired me out.', '走了那麼久讓我累壞了。', 'tire + 人 + out 使筋疲力盡；feel tired 覺得累'),
        S('n.', '輪胎', 'My bike has a flat tire.', '我的腳踏車爆胎了。'),
    ], 'tire - tired - tired - tiring', key=True),
    W('guide', '🧭', [
        S('v.', '引導；帶領', 'The teacher guided us through the museum.', '老師帶我們參觀博物館。'),
        S('n.', '指南', 'This book is a guide to Japanese food.', '這本書是日本料理指南。'),
        S('n.', '嚮導；導遊', 'Our tour guide speaks three languages.', '我們的導遊會說三種語言。'),
    ], 'guide - guided - guided - guiding', key=True),
    W('beat', '🥁', [
        S('v.', '打敗', 'Our class beat Class 3 in the final.', '我們班在決賽打敗了三班。', 'beat the record 打破紀錄；It beats me. 我不知道'),
        S('v.', '打；拍打；攪拌', 'Beat the eggs and sugar together.', '把蛋和糖一起打勻。', 'beat the drum 打鼓'),
        S('v.', '（心臟）跳動', 'My heart was beating fast.', '我的心跳得很快。'),
        S('n.', '心跳', 'My heart skipped a beat when I saw the test score.', '看到考試分數時我心跳漏了一拍。', 'skip a beat 心跳漏一拍'),
        S('n.', '節拍', 'Clap your hands to the beat.', '跟著節拍拍手。'),
    ], 'beat - beat - beaten - beating', key=True),
    W('state', '🇺🇸', [
        S('n.', '情況；狀態', 'The old house is in a bad state.', '那棟老房子狀況很差。', 'in a state of 處於…的狀態'),
        S('n.', '國家；政府', 'The state pays for the new railway.', '政府出資興建新鐵路。'),
        S('n.', '州', 'Texas is a big state in the U.S.', '德州是美國很大的一州。', 'the States 美國'),
    ], '複數 states', key=True),
    W('tear', '💧', [
        S('n.', '眼淚', 'Tears ran down her face.', '眼淚從她的臉上流下來。', 'be in tears 哭了；（眼淚唸 [tɪr]）'),
        S('v.', '撕開', 'Don\'t tear the paper.', '不要撕紙。', '（撕開唸 [tɛr]）tear apart 撕碎；be torn 內心掙扎'),
        S('v.', '狂奔', 'The kids tore out of the classroom at lunchtime.', '午餐時間孩子們衝出教室。'),
    ], 'tear - tore - torn - tearing', key=True),
    W('active', '🏃‍♀️', [
        S('adj.', '活躍的', 'My grandma is still very active.', '我奶奶還是很活躍。', 'stay active 保持活躍'),
        S('adj.', '積極參與的', 'She is active in the student council.', '她積極參與學生會。', 'play an active role in 在…扮演積極的角色'),
        S('adj.', '（火山）活的', 'This is an active volcano.', '這是一座活火山。'),
    ], 'active - more active - most active'),
    W('base', '⚾', [
        S('n.', '基地', 'The climbers returned to their base.', '登山者回到基地。'),
        S('n.', '底部；基座', 'The lamp has a heavy base.', '這盞燈的底座很重。'),
        S('n.', '壘（棒球）', 'He ran to second base.', '他跑上二壘。'),
        S('v.', '以…為根據', 'This movie is based on a true story.', '這部電影是根據真實故事改編的。', 'be based on 以…為根據'),
    ], 'base - based - based - basing'),
    W('beauty', '🌸', [
        S('n.', '美人', 'She was a beauty when she was young.', '她年輕時是個美人。'),
        S('n.', '美麗', 'We enjoyed the beauty of the mountains.', '我們欣賞山的美景。', 'Beauty is only skin deep. 美貌只是外表'),
    ], '複數 beauties'),
    W('charge', '🔌', [
        S('v.', '收費', 'The shop charged me 100 dollars.', '這家店向我收了一百元。'),
        S('n.', '費用', 'There is no charge for kids under six.', '六歲以下兒童免費。'),
        S('v.', '充電', 'I need to charge my phone.', '我要幫手機充電。'),
        S('v.', '猛衝', 'The dog charged at the ball.', '狗朝球衝過去。'),
        S('n.', '控訴；罪名', 'He faces a charge of stealing.', '他被控偷竊。'),
        S('n.', '負責', 'Who is in charge of this class?', '誰負責這個班？', 'in charge of 負責；take charge of 掌管'),
    ], 'charge - charged - charged - charging'),
    W('crowd', '👥', [
        S('n.', '一群人；人群', 'There was a big crowd at the concert.', '演唱會上人山人海。'),
        S('v.', '擠滿', 'The night market is crowded with people.', '夜市擠滿了人。', 'be crowded with 擠滿'),
        S('v.', '擠進', 'We all crowded into the small elevator.', '我們全都擠進小電梯。'),
    ], 'crowd - crowded - crowded - crowding'),
    W('flat', '🏢', [
        S('adj.', '平的；扁平的', 'The road is flat and easy to ride on.', '這條路很平，很好騎。'),
        S('adj.', '固定的（價錢）', 'The taxi charges a flat fee to the airport.', '計程車到機場收固定的費用。'),
        S('adj.', '平淡無趣的', 'The ending of the movie was a bit flat.', '電影的結局有點平淡。'),
        S('adj.', '沒氣的；沒電的', 'This soda has gone flat.', '這罐汽水沒氣了。', 'flat tire 爆胎'),
        S('adj.', '（音）偏低的', 'He sang a little flat.', '他唱得有點走音偏低。'),
        S('adj.', '斷然的', 'She gave me a flat "no."', '她斷然拒絕我。'),
        S('adj.', '沒有成長的', 'Sales have been flat this year.', '今年的銷售量沒有成長。'),
        S('n.', '公寓（英式）', 'They live in a small flat in London.', '他們住在倫敦的一間小公寓。'),
    ], 'flat - flatter - flattest'),
    W('hall', '🏛️', [
        S('n.', '大廳；禮堂', 'The graduation was held in the school hall.', '畢業典禮在學校禮堂舉行。', 'concert hall 音樂廳'),
        S('n.', '走廊', 'Don\'t run in the hall.', '不要在走廊奔跑。'),
    ], '複數 halls'),
    W('jam', '🍓', [
        S('n.', '果醬', 'I like strawberry jam on my toast.', '我喜歡在吐司上抹草莓果醬。'),
        S('n.', '塞車', 'We were stuck in a traffic jam.', '我們被困在車陣中。', 'traffic jam 塞車'),
        S('n.', '堵塞', 'There is a paper jam in the printer.', '印表機卡紙了。'),
        S('v.', '卡住', 'The door is jammed.', '門卡住了。'),
        S('v.', '塞滿', 'She jammed her clothes into the bag.', '她把衣服硬塞進包包裡。'),
    ], 'jam - jammed - jammed - jamming'),
    W('judge', '⚖️', [
        S('n.', '法官；評審', 'She was a judge in the singing contest.', '她是歌唱比賽的評審。'),
        S('v.', '判斷', 'Don\'t judge people by their looks.', '不要以貌取人。', 'judge by 根據…判斷'),
        S('v.', '批評', 'Please don\'t judge me.', '請不要批評我。'),
    ], 'judge - judged - judged - judging'),
    W('lamb', '🐑', [
        S('n.', '小羊；羊肉', 'The little lamb is very cute.', '小羊好可愛。'),
        S('v.', '生小羊', 'The sheep lamb in spring.', '母羊在春天生小羊。'),
    ], '複數 lambs'),
    W('model', '✈️', [
        S('n.', '模特兒', 'She works as a model.', '她當模特兒。'),
        S('n.', '模型', 'My brother built a model plane.', '我哥哥做了一架模型飛機。'),
        S('n.', '榜樣', 'My mom is my role model.', '我媽媽是我的榜樣。', 'role model 榜樣'),
        S('n.', '（車、手機）款式', 'This is the newest model of the phone.', '這是這支手機的最新款。'),
    ], '複數 models'),
    W('nut', '🥜', [
        S('n.', '堅果', 'Nuts are good for your health.', '堅果對健康很好。'),
        S('n.', '螺帽', 'Tighten the nut with a wrench.', '用扳手把螺帽鎖緊。'),
        S('n.', '怪人', 'He dances like a nut.', '他跳舞像個瘋子一樣。'),
        S('n.', '迷；熱衷者', 'My dad is a baseball nut.', '我爸爸是個棒球迷。'),
    ], '複數 nuts'),
    W('patient', '🏥', [
        S('n.', '病人', 'The doctor saw thirty patients today.', '醫生今天看了三十個病人。'),
        S('adj.', '有耐心的', 'Be patient with your little brother.', '對你弟弟要有耐心。', 'be patient with 對…有耐心'),
    ], 'patient - more patient - most patient'),
    W('sheet', '🛏️', [
        S('n.', '床單', 'Let\'s change the sheets today.', '我們今天換床單吧。'),
        S('n.', '一張（紙）', 'Write your name on the answer sheet.', '在答案紙上寫你的名字。', 'a sheet of paper 一張紙'),
        S('n.', '薄片；薄層', 'There is a sheet of ice on the lake.', '湖面上結了一層薄冰。'),
    ], '複數 sheets'),
    W('shoot', '🏀', [
        S('v.', '射擊；射（箭）', 'He shot an arrow at the target.', '他朝靶子射了一支箭。'),
        S('v.', '注射', 'The nurse shot the medicine into my arm.', '護理師把藥打進我的手臂。'),
        S('v.', '投籃；射門', 'Let\'s go shoot some hoops.', '我們去投籃吧。'),
        S('v.', '快速上升', 'Prices shot up last month.', '上個月物價暴漲。', 'shoot up 暴漲'),
        S('n.', '拍攝活動', 'The model is ready for the photo shoot.', '模特兒準備好拍照了。'),
        S('n.', '新芽', 'Bamboo shoots grow fast after rain.', '雨後竹筍長得很快。', 'bamboo shoot 竹筍'),
    ], 'shoot - shot - shot - shooting'),
    W('wild', '🦁', [
        S('n.', '荒野；野外', 'Lions live in the wild.', '獅子生活在野外。', 'in the wild 在野外'),
        S('adj.', '野生的', 'We saw wild monkeys on the mountain.', '我們在山上看到野生猴子。'),
        S('adj.', '瘋狂的', 'The fans went wild when the singer came out.', '歌手出場時粉絲瘋狂了。'),
        S('adj.', '荒涼的', 'They hiked across the wild land.', '他們徒步穿越荒涼的土地。'),
    ], 'wild - wilder - wildest'),
  ],
  'focus': [
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('tire', '輪胎', '使疲倦（tired 累的）'),
      ('beat', '打敗', '心跳；節拍'),
      ('state', '狀態', '州；國家'),
      ('tear', '眼淚 [tɪr]', '撕開 [tɛr]'),
      ('charge', '收費', '充電；負責'),
      ('flat', '平的', '爆胎；公寓；沒氣的'),
      ('jam', '果醬', '塞車；卡住'),
      ('nut', '堅果', '螺帽；迷'),
      ('patient', '有耐心的', '病人'),
      ('shoot', '射擊', '投籃；竹筍；拍攝'),
    ], 'note': ''},
    {'title': '常用片語', 'head': ('片語', '意思', '例句'), 'rows': [
      ('tire + 人 + out', '使筋疲力盡', 'The game tired me out.'),
      ('be based on', '以…為根據', 'The book is based on a true story.'),
      ('in charge of', '負責', 'She is in charge of the party.'),
      ('be crowded with', '擠滿', 'The beach is crowded with people.'),
      ('traffic jam', '塞車', 'We were late because of a traffic jam.'),
      ('be patient with', '對…有耐心', 'Be patient with the new students.'),
      ('in the wild', '在野外', 'Pandas live in the wild in China.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'The long trip <b>tired</b> us out.', 'opts': ['輪胎', '使疲倦', '修理', '休息'], 'answer': 1, 'exp': 'tire out 使筋疲力盡。'},
    {'type': 'mc', 'q': 'Our tour <b>guide</b> told us about the old temple.', 'opts': ['指南', '導遊', '引導', '地圖'], 'answer': 1, 'exp': 'tour guide 導遊。'},
    {'type': 'mc', 'q': 'Everyone danced to the <b>beat</b> of the music.', 'opts': ['打敗', '心跳', '節拍', '攪拌'], 'answer': 2, 'exp': '跟著音樂的節拍跳舞。'},
    {'type': 'mc', 'q': 'California is the biggest <b>state</b> by population in the U.S.', 'opts': ['狀態', '國家', '州', '城市'], 'answer': 2, 'exp': '美國的 state → 州。'},
    {'type': 'mc', 'q': 'Be careful. Don\'t <b>tear</b> the map.', 'opts': ['眼淚', '撕破', '狂奔', '弄濕'], 'answer': 1, 'exp': 'tear 撕開。'},
    {'type': 'mc', 'q': 'Mr. Lee is in <b>charge</b> of the school trip.', 'opts': ['收費', '充電', '負責', '控訴'], 'answer': 2, 'exp': 'in charge of 負責。'},
    {'type': 'mc', 'q': 'This cola has gone <b>flat</b>.', 'opts': ['平的', '沒氣的', '公寓', '固定的'], 'answer': 1, 'exp': '汽水 go flat → 沒氣。'},
    {'type': 'mc', 'q': 'The printer has a paper <b>jam</b> again.', 'opts': ['果醬', '塞車', '堵塞；卡紙', '塞滿'], 'answer': 2, 'exp': 'paper jam 卡紙。'},
    {'type': 'mc', 'q': 'The nurse is taking care of the <b>patients</b>.', 'opts': ['病人', '有耐心的', '家人', '醫生'], 'answer': 0, 'exp': 'patients 病人。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'Pandas eat bamboo ______s.  ／  Let\'s go ______ some hoops after school.', 'opts': ['leaf', 'shoot', 'throw', 'play'], 'answer': 1, 'exp': 'shoot 竹筍／投籃。'},
    {'type': 'mc', 'q': 'My dad is a basketball ______.  ／  Almonds and cashews are ______s.', 'opts': ['fan', 'nut', 'seed', 'bean'], 'answer': 1, 'exp': 'nut 迷／堅果。'},
    {'type': 'mc', 'q': 'I need to ______ my phone.  ／  Is there any ______ for using the gym?', 'opts': ['fix', 'charge', 'fee', 'pay'], 'answer': 1, 'exp': 'charge 充電／費用。'},
    {'type': 'mc', 'q': 'Mom changed the ______s on my bed.  ／  Write the answers on this ______.', 'opts': ['sheet', 'cover', 'paper', 'blanket'], 'answer': 0, 'exp': 'sheet 床單／一張紙。'},
    {'type': 'mc', 'q': 'Don\'t ______ a book by its cover.  ／  The ______ gave her a high score.', 'opts': ['read', 'judge', 'teacher', 'see'], 'answer': 1, 'exp': 'judge 判斷／評審。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'This movie is {0} on a true story. （以…為根據）', 'blanks': [['based']], 'exp': 'be based on 以…為根據。'},
    {'q': 'The MRT was {0} with people after the fireworks. （擠滿）', 'blanks': [['crowded']], 'exp': 'be crowded with 擠滿。'},
    {'q': 'We were stuck in a traffic {0} for an hour. （塞車）', 'blanks': [['jam']], 'exp': 'traffic jam 塞車。'},
    {'q': 'Please be {0} with your little sister. （有耐心的）', 'blanks': [['patient']], 'exp': 'be patient with 對…有耐心。'},
    {'q': 'My aunt is my role {0}. （榜樣）', 'blanks': [['model']], 'exp': 'role model 榜樣。'},
    {'q': 'Tigers live in the {0}. （野外）', 'blanks': [['wild']], 'exp': 'in the wild 在野外。'},
  ]},
]
