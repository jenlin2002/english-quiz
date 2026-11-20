# LaLa Word Unit 15（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 165–178 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 15, 'en': 'The Power of Music', 'zh': '一字多義（十五）',
  'intro': 'cover 是蓋子，也是「翻唱」；ring 是戒指，也是「（電話）響」。這個單元有 4 個主題單字、21 個更多單字，'
           '再整理 probably／possible／perhaps、except／besides／beside，和字首 im-、字尾 -less。',
  'words': [
    W('play', '🎻', [
        S('v.', '演奏（樂器）', 'My sister plays the violin.', '我姊姊拉小提琴。', 'play + the + 樂器'),
        S('v.', '播放', 'Can you play that song again?', '你可以再播一次那首歌嗎？'),
        S('v.', '玩；從事運動', 'Let\'s play basketball after school.', '放學後我們去打籃球吧。', 'play + 球類'),
        S('n.', '戲劇；劇本', 'Our class put on a play.', '我們班演了一齣戲。'),
        S('n.', '比賽（態度）', 'Fair play is more important than winning.', '公平比賽比贏更重要。'),
    ], 'play - played - played - playing', key=True),
    W('cover', '📘', [
        S('v.', '覆蓋', 'The mountain is covered with snow.', '山上覆蓋著雪。', 'be covered with 被…覆蓋'),
        S('n.', '蓋子；封面', 'I like the cover of this book.', '我喜歡這本書的封面。', 'Don\'t judge a book by its cover. 人不可貌相'),
        S('v.', '包含；涵蓋', 'The test will cover Units 1 to 4.', '這次考試範圍是第一到第四課。'),
        S('v.', '翻唱', 'The band covered an old song.', '樂團翻唱了一首老歌。'),
        S('n.', '掩護；遮蔽', 'We took cover under a tree when it rained.', '下雨時我們在樹下躲雨。', 'take cover 躲避'),
    ], 'cover - covered - covered - covering', key=True),
    W('rise', '🌅', [
        S('v.', '增加；上漲', 'Prices keep rising.', '物價一直上漲。'),
        S('n.', '上升；增加', 'There is a rise in the number of tourists.', '觀光客人數增加了。'),
        S('v.', '起身；站起來', 'Please rise for the national anthem.', '請起立唱國歌。'),
        S('v.', '（太陽、月亮）升起', 'The sun rises in the east.', '太陽從東方升起。'),
    ], 'rise - rose - risen - rising', key=True),
    W('public', '🏛️', [
        S('adj.', '公開的', 'Don\'t shout in public.', '不要在公共場所大叫。', 'in public 公開地；當眾'),
        S('adj.', '公共的', 'There is a public library near my house.', '我家附近有一間公立圖書館。'),
        S('n.', '大眾；民眾', 'The museum is open to the public.', '這間博物館開放給大眾參觀。', 'the public 大眾'),
    ], key=True),
    W('appear', '🌈', [
        S('v.', '出現', 'A rainbow appeared after the rain.', '雨後出現了一道彩虹。'),
        S('v.', '登場', 'The singer will appear on stage at eight.', '歌手八點登台。'),
        S('v.', '看起來；似乎', 'He appears to be tired.', '他看起來很累。', 'appear to 似乎'),
    ], 'appear - appeared - appeared - appearing'),
    W('bottom', '⬇️', [
        S('adj.', '底部的', 'The socks are in the bottom drawer.', '襪子在最下面的抽屜裡。'),
        S('n.', '底部', 'There is some sugar at the bottom of the cup.', '杯底有一些糖。', 'from the bottom of one\'s heart 打從心底'),
        S('n.', '末端；最後一名', 'Our team is at the bottom of the list.', '我們隊排在最後。'),
        S('n.', '屁股', 'The baby fell on his bottom.', '寶寶一屁股跌坐在地上。'),
    ], '複數 bottoms'),
    W('bow', '🎀', [
        S('v.', '鞠躬', 'The students bowed to the teacher.', '學生們向老師鞠躬。', '（鞠躬唸 [baʊ]）'),
        S('n.', '鞠躬', 'The actors took a bow at the end.', '演員們最後鞠躬謝幕。', 'take a bow 鞠躬致意'),
        S('v.', '使彎曲', 'The trees bowed in the strong wind.', '樹在強風中彎下腰。'),
        S('n.', '弓', 'He shot an arrow with his bow.', '他用弓射了一支箭。', '（弓、蝴蝶結唸 [bo]）'),
        S('n.', '蝴蝶結', 'She wears a red bow in her hair.', '她頭上綁著紅色蝴蝶結。'),
    ], 'bow - bowed - bowed - bowing'),
    W('character', '🦸', [
        S('n.', '角色', 'Who is your favorite cartoon character?', '你最喜歡的卡通人物是誰？'),
        S('n.', '性格', 'He has a kind character.', '他的個性很善良。'),
        S('n.', '字', 'How many Chinese characters can you write?', '你會寫幾個中文字？'),
    ], '複數 characters'),
    W('draw', '✏️', [
        S('v.', '畫', 'Can you draw a cat?', '你會畫貓嗎？'),
        S('v.', '拉；抽（籤）', 'Draw the curtains, please.', '請拉上窗簾。', 'draw lots 抽籤'),
        S('v.', '吸引', 'The show drew a big crowd.', '這場表演吸引了一大群人。', 'draw attention 吸引注意'),
        S('n.', '平手', 'The game ended in a draw.', '比賽以平手結束。'),
    ], 'draw - drew - drawn - drawing'),
    W('fool', '🤡', [
        S('n.', '傻瓜', 'I felt like a fool.', '我覺得自己像個傻瓜。'),
        S('v.', '愚弄；欺騙', 'You can\'t fool me!', '你騙不了我的！'),
        S('v.', '胡鬧（fool around）', 'Stop fooling around and do your homework.', '別再胡鬧了，快去寫功課。', 'fool around 鬼混；胡鬧'),
    ], 'fool - fooled - fooled - fooling'),
    W('fry', '🍟', [
        S('v.', '煎；炸；炒', 'Dad fried some eggs for breakfast.', '爸爸煎了幾顆蛋當早餐。', 'fried rice 炒飯；fried chicken 炸雞'),
        S('v.', '曬傷', 'I got fried at the beach.', '我在海邊曬傷了。'),
        S('n.', '薯條（fries）', 'I\'d like a burger and fries.', '我要一個漢堡和薯條。'),
    ], 'fry - fried - fried - frying；複數 fries'),
    W('heat', '🔥', [
        S('v.', '加熱', 'Heat the milk before you drink it.', '牛奶熱一下再喝。', 'heat up 加熱'),
        S('n.', '熱；高溫', 'I can\'t stand the summer heat.', '我受不了夏天的炎熱。'),
        S('n.', '火力', 'Cook the soup on low heat.', '用小火煮湯。'),
    ], 'heat - heated - heated - heating'),
    W('joke', '😂', [
        S('v.', '開玩笑', 'Don\'t worry. I\'m only joking.', '別擔心，我只是開玩笑的。'),
        S('n.', '笑話', 'Grandpa told us a funny joke.', '爺爺講了一個好笑的笑話。', 'tell a joke 說笑話'),
        S('n.', '荒唐可笑的事物', 'The test was so easy. It was a joke!', '考試簡單得像開玩笑一樣！'),
    ], 'joke - joked - joked - joking'),
    W('line', '➖', [
        S('n.', '線條', 'Draw a straight line.', '畫一條直線。'),
        S('n.', '車道', 'Drivers should stay between the lines.', '駕駛應該待在自己的車道裡。'),
        S('n.', '隊伍', 'There is a long line at the ice cream shop.', '冰淇淋店前大排長龍。'),
        S('n.', '臺詞（lines）', 'I need to learn my lines for the play.', '我要背戲劇的臺詞。'),
        S('v.', '排隊（line up）', 'Please line up at the door.', '請在門口排隊。', 'line up 排隊'),
    ], 'line - lined - lined - lining'),
    W('mark', '❌', [
        S('v.', '標記', 'Mark the right answers with a pen.', '用筆標出正確答案。'),
        S('v.', '紀念', 'We had a party to mark Grandma\'s 80th birthday.', '我們開派對慶祝奶奶八十歲生日。'),
        S('n.', '記號；痕跡', 'There are dirty marks on the wall.', '牆上有髒髒的痕跡。'),
        S('n.', '分數', 'She got full marks in English.', '她英文考滿分。', 'full marks 滿分'),
    ], 'mark - marked - marked - marking'),
    W('notice', '📢', [
        S('v.', '注意到', 'Did you notice his new haircut?', '你有注意到他的新髮型嗎？'),
        S('n.', '通知；告示', 'Read the notice on the board.', '看一下公布欄上的通知。'),
    ], 'notice - noticed - noticed - noticing'),
    W('paper', '📄', [
        S('n.', '紙', 'Can I have a piece of paper?', '可以給我一張紙嗎？', 'a piece of paper 一張紙'),
        S('n.', '報紙；報告', 'Dad reads the paper every morning.', '爸爸每天早上看報紙。'),
        S('v.', '貼壁紙', 'We papered the bedroom walls.', '我們在臥室牆上貼了壁紙。'),
    ], 'paper - papered - papered - papering'),
    W('pin', '📌', [
        S('v.', '釘住；別住', 'Pin the poster on the board.', '把海報釘在布告欄上。'),
        S('v.', '弄清楚（pin down）', 'We can\'t pin down the problem.', '我們找不出問題在哪裡。', 'pin down 弄清楚'),
        S('n.', '別針；圖釘', 'She wears a flower pin on her coat.', '她外套上別著一個花朵別針。'),
    ], 'pin - pinned - pinned - pinning'),
    W('ring', '💍', [
        S('v.', '（電話、鈴）響', 'The phone is ringing.', '電話在響。'),
        S('v.', '打電話', 'I\'ll ring you tonight.', '我今晚打電話給你。'),
        S('n.', '戒指', 'She wears a gold ring.', '她戴著一枚金戒指。'),
        S('n.', '圓圈；環', 'The kids danced in a ring.', '孩子們圍成一圈跳舞。'),
    ], 'ring - rang - rung - ringing'),
    W('round', '🔵', [
        S('v.', '繞行', 'The bus rounded the corner.', '公車轉過街角。'),
        S('prep.', '繞著；圍著', 'We sat round the table.', '我們圍著桌子坐。', '同 around'),
        S('n.', '回合', 'She won the first round.', '她贏了第一回合。'),
        S('adj.', '圓的', 'The earth is round.', '地球是圓的。'),
    ], 'round - rounded - rounded - rounding'),
    W('slide', '🛝', [
        S('n.', '溜滑梯', 'The kids are playing on the slide.', '孩子們在玩溜滑梯。'),
        S('v.', '滑動；滑落', 'The book slid off the desk.', '書從桌上滑下來。'),
        S('v.', '悄悄地移動', 'The cat slid into the room.', '貓悄悄溜進房間。'),
    ], 'slide - slid - slid - sliding'),
    W('smoke', '💨', [
        S('n.', '煙', 'Smoke is coming out of the kitchen!', '廚房冒出煙來了！', 'There\'s no smoke without fire. 無風不起浪'),
        S('v.', '冒煙', 'The old car is smoking.', '那台老車在冒煙。'),
        S('v.', '抽菸', 'Smoking is bad for your health.', '抽菸對健康有害。'),
    ], 'smoke - smoked - smoked - smoking'),
    W('square', '🟥', [
        S('n.', '正方形', 'Cut the paper into squares.', '把紙剪成正方形。'),
        S('n.', '廣場', 'There is a big tree in the square.', '廣場上有一棵大樹。'),
        S('adj.', '平方的', 'The room is 20 square meters.', '這個房間二十平方公尺。'),
        S('v.', '使成正方形', 'Square the corners of the box.', '把盒子的角弄方正。'),
        S('v.', '與…一致', 'His story doesn\'t square with the facts.', '他的說法和事實不符。', 'square with 與…一致'),
    ], 'square - squared - squared - squaring'),
    W('string', '🧵', [
        S('n.', '細繩', 'Tie the box with some string.', '用細繩把盒子綁起來。', 'a piece of string 一段繩子'),
        S('n.', '一串', 'She bought a string of beads.', '她買了一串珠子。'),
        S('n.', '一連串', 'He asked a string of questions.', '他問了一連串的問題。'),
        S('n.', '（樂器的）弦', 'A guitar has six strings.', '吉他有六根弦。'),
        S('v.', '串起', 'We strung lights across the yard.', '我們在院子裡掛起一串燈。'),
    ], 'string - strung - strung - stringing'),
    W('tape', '📼', [
        S('v.', '用膠帶黏', 'Tape the note to the door.', '用膠帶把紙條貼在門上。'),
        S('n.', '膠帶', 'I need some tape to fix this.', '我需要膠帶來修這個。'),
        S('n.', '錄音帶；錄影帶', 'The thief was caught on tape.', '小偷被錄影機拍到了。', 'on tape 被錄下來'),
    ], 'tape - taped - taped - taping'),
    W('impossible', '🚫', [S('adj.', '不可能的', 'Nothing is impossible.', '沒有不可能的事。')], 'im- + possible'),
    W('impolite', '🙊', [S('adj.', '不禮貌的', 'It\'s impolite to talk with your mouth full.', '嘴裡有食物還說話是不禮貌的。')], 'im- + polite'),
    W('careless', '🫨', [S('adj.', '粗心的', 'I made a careless mistake on the test.', '我考試時犯了一個粗心的錯誤。')], 'care + -less'),
    W('useless', '🗑️', [S('adj.', '沒用的', 'This old phone is useless now.', '這支舊手機現在沒用了。')], 'use + -less'),
    W('worthless', '🪙', [S('adj.', '沒有價值的', 'The fake coin is worthless.', '這枚假硬幣一文不值。')], 'worth + -less'),
  ],
  'focus': [
    {'title': '易混淆字：probably／possible／perhaps', 'head': ('單字', '用法', '例句'), 'rows': [
      ('probably', '（副詞）很可能；大概，把握比較大', 'He will probably be late.'),
      ('possible', '（形容詞）可能的：It\'s possible (that)…／It\'s possible for + 人 + to V', 'It\'s possible that it will snow.'),
      ('perhaps', '（副詞）或許，把握比較小，語氣委婉', 'Perhaps she forgot.'),
    ], 'note': ''},
    {'title': '易混淆字：except／besides／beside', 'head': ('單字', '意思', '例句'), 'rows': [
      ('except', '除了…之外（不包括）', 'Everyone came except Tom.（Tom 沒來）'),
      ('besides', '除了…之外還有（包括在內）', 'Besides English, she speaks Japanese.'),
      ('beside', '在…旁邊（只差一個 s，意思完全不同）', 'The cat is sitting beside me.'),
    ], 'note': ''},
    {'title': '字首 im-、字尾 -less', 'head': ('原來的字', '加字首／字尾', '意思'), 'rows': [
      ('possible 可能的', 'impossible', '不可能的'),
      ('polite 有禮貌的', 'impolite', '不禮貌的'),
      ('care 小心', 'careless', '粗心的'),
      ('use 使用', 'useless', '沒用的'),
      ('worth 價值', 'worthless', '沒有價值的'),
    ], 'note': 'im-＝不；-less＝沒有（without）。'},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('cover', '蓋子；覆蓋', '翻唱；涵蓋（考試範圍）'),
      ('bow', '鞠躬（[baʊ]）', '弓；蝴蝶結（[bo]）'),
      ('character', '角色', '性格；字'),
      ('draw', '畫', '平手；吸引'),
      ('line', '線', '隊伍；臺詞'),
      ('ring', '戒指', '（電話）響'),
      ('square', '正方形', '廣場'),
      ('string', '細繩', '樂器的弦；一連串'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'The singer <b>covered</b> a famous English song.', 'opts': ['覆蓋', '包含', '翻唱', '躲避'], 'answer': 2, 'exp': '歌手 cover 一首歌 → 翻唱。'},
    {'type': 'mc', 'q': 'Everyone <b>rose</b> when the principal came in.', 'opts': ['上漲', '升起', '站起來', '增加'], 'answer': 2, 'exp': 'rise 起身。'},
    {'type': 'mc', 'q': 'She tied the gift with a pink <b>bow</b>.', 'opts': ['鞠躬', '弓', '蝴蝶結', '彎曲'], 'answer': 2, 'exp': '綁禮物 → 蝴蝶結。'},
    {'type': 'mc', 'q': 'Learning Chinese <b>characters</b> takes time.', 'opts': ['角色', '性格', '字', '故事'], 'answer': 2, 'exp': 'Chinese characters 中文字。'},
    {'type': 'mc', 'q': 'The soccer game ended in a 1–1 <b>draw</b>.', 'opts': ['畫', '平手', '抽籤', '吸引'], 'answer': 1, 'exp': '1 比 1 → 平手。'},
    {'type': 'mc', 'q': 'The actor forgot his <b>lines</b> on stage.', 'opts': ['線條', '隊伍', '臺詞', '車道'], 'answer': 2, 'exp': '演員忘了 lines → 臺詞。'},
    {'type': 'mc', 'q': 'We met in the town <b>square</b>.', 'opts': ['正方形', '廣場', '平方', '一致'], 'answer': 1, 'exp': 'town square 廣場。'},
    {'type': 'mc', 'q': 'One of the guitar <b>strings</b> broke.', 'opts': ['細繩', '一串', '弦', '一連串'], 'answer': 2, 'exp': '吉他的弦。'},
    {'type': 'mc', 'q': 'The robbery was caught on <b>tape</b>.', 'opts': ['膠帶', '錄影帶', '繩子', '照片'], 'answer': 1, 'exp': 'on tape 被錄下來。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'My phone is ______ing. Can you answer it?  ／  He gave her a diamond ______.', 'opts': ['call', 'ring', 'sound', 'bell'], 'answer': 1, 'exp': 'ring 響／戒指。'},
    {'type': 'mc', 'q': 'Turn down the ______, or the soup will burn.  ／  I can\'t stand the summer ______.', 'opts': ['fire', 'heat', 'sun', 'hot'], 'answer': 1, 'exp': 'heat 火力／炎熱。'},
    {'type': 'mc', 'q': 'There is a dirty ______ on your shirt.  ／  I got full ______s on the test.', 'opts': ['spot', 'mark', 'point', 'score'], 'answer': 1, 'exp': 'mark 痕跡／分數。'},
    {'type': 'mc', 'q': 'Please ______ up in front of the classroom.  ／  Draw a straight ______.', 'opts': ['stand', 'line', 'queue', 'row'], 'answer': 1, 'exp': 'line up 排隊／線。'},
    {'type': 'mc', 'q': 'Did you read the ______ on the door?  ／  Did you ______ anything strange?', 'opts': ['sign', 'notice', 'see', 'note'], 'answer': 1, 'exp': 'notice 告示／注意到。'},
  ]},
  {'title': '③ 易混淆字與字首字尾', 'items': [
    {'type': 'mc', 'q': 'It\'s ______ that the train will be late.', 'opts': ['probably', 'possible', 'perhaps', 'maybe'], 'answer': 1, 'exp': 'It\'s possible that…'},
    {'type': 'mc', 'q': 'I like all vegetables ______ carrots. I hate carrots.', 'opts': ['except', 'besides', 'beside', 'expect'], 'answer': 0, 'exp': '不包括胡蘿蔔 → except。'},
    {'type': 'mc', 'q': '______ math, he is also good at music.', 'opts': ['Except', 'Besides', 'Beside', 'Expect'], 'answer': 1, 'exp': '除了數學之外還有 → besides。'},
    {'type': 'mc', 'q': 'Come and sit ______ me.', 'opts': ['besides', 'except', 'beside', 'probably'], 'answer': 2, 'exp': '在旁邊 → beside。'},
    {'type': 'mc', 'q': 'I forgot to write my name. I was so ______.', 'opts': ['useless', 'careless', 'impolite', 'worthless'], 'answer': 1, 'exp': '粗心的 careless。'},
    {'type': 'mc', 'q': 'It\'s ______ to finish this huge puzzle in one hour.', 'opts': ['impolite', 'impossible', 'useless', 'careless'], 'answer': 1, 'exp': '不可能的 impossible。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Don\'t pick your nose in {0}. （公開地）', 'blanks': [['public']], 'exp': 'in public 公開地。'},
    {'q': 'A rainbow {0} after the rain. （出現，過去式）', 'blanks': [['appeared']], 'exp': 'appear 的過去式。'},
    {'q': 'Thank you from the {0} of my heart. （底部）', 'blanks': [['bottom']], 'exp': 'from the bottom of one\'s heart 打從心底。'},
    {'q': 'Stop fooling {0} and clean your room. （胡鬧）', 'blanks': [['around']], 'exp': 'fool around 胡鬧。'},
    {'q': 'Please {0} up the soup before dinner. （加熱）', 'blanks': [['heat']], 'exp': 'heat up 加熱。'},
    {'q': 'I\'m just {0}. Don\'t take it seriously. （開玩笑）', 'blanks': [['joking']], 'exp': 'I\'m just joking.'},
  ]},
]
