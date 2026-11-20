# LaLa Word Unit 11（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 119–131 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 11, 'en': 'More Light, Fewer Stars', 'zh': '一字多義（十一）',
  'intro': 'star 是星星，也是「明星」；light 是燈，也是「輕的」「淡的」。這個單元有 5 個主題單字、18 個更多單字，'
           '最後整理使役動詞 let／have／make。',
  'words': [
    W('star', '⭐', [
        S('n.', '星星；恆星', 'We can see many stars tonight.', '今晚可以看到很多星星。'),
        S('n.', '明星', 'She wants to be a movie star.', '她想當電影明星。', 'movie star 電影明星；rock star 搖滾明星'),
        S('n.', '星形', 'Draw a star on the card.', '在卡片上畫一顆星星。'),
        S('n.', '（等級的）星', 'We stayed at a five-star hotel.', '我們住五星級飯店。'),
        S('v.', '主演', 'Who stars in this movie?', '這部電影是誰主演的？'),
    ], 'star - starred - starred - starring', key=True),
    W('light', '💡', [
        S('n.', '燈', 'Please turn off the light.', '請關燈。'),
        S('n.', '光線', 'Plants need light to grow.', '植物需要光才能生長。'),
        S('adj.', '明亮的', 'It\'s still light outside at seven in summer.', '夏天七點外面還很亮。'),
        S('adj.', '淺色的；少量的', 'She is wearing a light blue shirt.', '她穿著淺藍色襯衫。', 'a light meal 清淡的一餐'),
        S('adj.', '輕的；輕鬆的', 'This bag is very light.', '這個包包很輕。'),
        S('v.', '點燃；照亮', 'Dad lit the candles on the cake.', '爸爸點了蛋糕上的蠟燭。', 'light up 照亮'),
    ], 'light - lighter - lightest；light - lit（lighted） - lit（lighted） - lighting', key=True),
    W('hard', '🪨', [
        S('adj.', '困難的', 'The math test was very hard.', '數學考試很難。'),
        S('adj.', '堅硬的', 'The bread is too hard to eat.', '麵包硬得吃不下。'),
        S('adj.', '嚴厲的', 'Don\'t be so hard on yourself.', '別對自己那麼嚴格。', 'be hard on 對…嚴厲'),
        S('adv.', '努力地', 'She studies hard every day.', '她每天都很用功。'),
        S('adv.', '猛烈地；用力地', 'It is raining hard.', '雨下得很大。'),
    ], 'hard - harder - hardest', key=True),
    W('clear', '🌤️', [
        S('adj.', '晴朗的；清澈的', 'The sky is clear today.', '今天天空很晴朗。'),
        S('adj.', '清楚的；明白的', 'Is that clear?', '這樣清楚嗎？', 'It is clear that… 很明顯…'),
        S('v.', '清理；收拾', 'Please clear the table after dinner.', '晚餐後請收拾餐桌。', 'clear one\'s throat 清喉嚨'),
        S('v.', '使（頭腦）清醒', 'A walk helps me clear my head.', '散步幫助我讓頭腦清醒。', 'clear one\'s head 讓頭腦清醒'),
    ], 'clear - clearer - clearest；clear - cleared - cleared - clearing', key=True),
    W('shine', '🌕', [
        S('v.', '（陽光、月光）照耀', 'The sun is shining.', '陽光普照。', 'rise and shine 起床囉'),
        S('v.', '發亮', 'Her eyes shone with joy.', '她的眼睛因為開心而發亮。'),
        S('v.', '表現出色', 'He really shines at basketball.', '他打籃球表現很出色。'),
        S('v.', '擦亮', 'Dad shined his shoes.', '爸爸把鞋子擦亮。'),
    ], 'shine - shone - shone - shining；（擦亮）shine - shined - shined'),
    W('blow', '🌬️', [
        S('v.', '吹', 'The wind blew my hat off.', '風把我的帽子吹走了。', 'blow out 吹熄；blow bubbles 吹泡泡；blow a kiss 送飛吻'),
        S('v.', '使驚嘆（blow away）', 'The show blew me away.', '這場表演讓我驚嘆不已。', 'blow + 人 + away 讓人驚豔'),
        S('v.', '爆炸（blow up）', 'The old building was blown up.', '那棟舊大樓被炸毀了。', 'blow up 爆炸'),
    ], 'blow - blew - blown - blowing'),
    W('duck', '🦆', [
        S('n.', '鴨子', 'The ducks are swimming in the pond.', '鴨子在池塘裡游泳。'),
        S('n.', '鴨肉', 'Have you tried Peking duck?', '你吃過北京烤鴨嗎？'),
        S('v.', '迅速低頭', 'Duck! The ball is coming!', '低頭！球飛過來了！'),
        S('v.', '躲避', 'The cat ducked under the bed.', '貓躲到床底下。', 'duck behind / under 躲到…後面／下面'),
    ], 'duck - ducked - ducked - ducking'),
    W('garden', '🌷', [
        S('n.', '花園；菜園', 'Grandma grows roses in her garden.', '奶奶在花園種玫瑰。'),
        S('v.', '從事園藝', 'My aunt loves gardening.', '我阿姨很喜歡園藝。'),
    ], 'garden - gardened - gardened - gardening'),
    W('giant', '🗿', [
        S('adj.', '巨大的', 'We saw a giant panda at the zoo.', '我們在動物園看到大貓熊。'),
        S('n.', '巨人', 'The giant lived in a castle.', '巨人住在城堡裡。'),
        S('n.', '巨頭；偉人', 'This company is a giant in the car business.', '這家公司是汽車業的巨頭。'),
    ], '複數 giants'),
    W('must', '❗', [
        S('aux.', '必須；一定要', 'You must wear a helmet.', '你一定要戴安全帽。', 'must not 不可以'),
        S('aux.', '一定（推測）', 'You must be tired after the long trip.', '長途旅行後你一定很累。'),
        S('n.', '必需品；必做的事', 'This museum is a must-see.', '這間博物館是必看的。', 'a must-see 必看；a must-have 必備'),
    ], 'must 沒有過去式（用 had to）'),
    W('news', '📰', [
        S('n.', '消息', 'I have some good news for you.', '我有好消息要告訴你。', 'No news is good news. 沒消息就是好消息'),
        S('n.', '新聞', 'Dad watches the news every evening.', '爸爸每天晚上看新聞。', 'on the news 在新聞上'),
    ], 'news 不可數（a piece of news）'),
    W('pick', '🍓', [
        S('v.', '挑選', 'Pick a card, any card.', '隨便挑一張牌。'),
        S('v.', '接人；撿起（pick up）', 'Mom will pick me up at five.', '媽媽五點會來接我。', 'pick up 接人；撿起'),
        S('v.', '摘（花、果）', 'We picked strawberries in Dahu.', '我們在大湖採草莓。'),
        S('v.', '挖；剔', 'Don\'t pick your nose!', '不要挖鼻孔！'),
        S('n.', '選擇；工具', 'Take your pick.', '你隨便挑。', 'toothpick 牙籤；guitar pick 吉他彈片'),
    ], 'pick - picked - picked - picking'),
    W('pound', '⚖️', [
        S('n.', '英鎊', 'The book costs ten pounds.', '這本書要十英鎊。'),
        S('n.', '磅（重量單位）', 'The baby weighs seven pounds.', '寶寶重七磅。'),
        S('v.', '連續敲打；（心）怦怦跳', 'My heart was pounding before the race.', '比賽前我的心怦怦跳。'),
    ], 'pound - pounded - pounded - pounding'),
    W('pretty', '🌸', [
        S('adj.', '漂亮的', 'What a pretty dress!', '好漂亮的洋裝！'),
        S('adv.', '相當；很', 'The test was pretty easy.', '考試相當簡單。', 'pretty much 差不多'),
    ], 'pretty - prettier - prettiest'),
    W('radio', '📻', [
        S('n.', '收音機', 'Can you turn on the radio?', '你可以打開收音機嗎？'),
        S('n.', '廣播', 'I heard the song on the radio.', '我在廣播上聽到這首歌。', 'listen to the radio 聽廣播'),
        S('n.', '無線電通訊', 'The pilots talk by radio.', '飛行員用無線電通話。'),
    ], '複數 radios'),
    W('reach', '🙌', [
        S('v.', '抵達', 'We reached the top of the mountain at noon.', '我們中午到達山頂。'),
        S('v.', '達到（年紀、溫度）', 'The temperature reached 38°C today.', '今天氣溫達到三十八度。'),
        S('v.', '伸手搆到；幫助', 'I can\'t reach the top shelf.', '我搆不到最上面那層架子。', 'reach out to 伸出援手'),
        S('v.', '聯絡上', 'You can reach me by phone.', '你可以打電話聯絡我。'),
    ], 'reach - reached - reached - reaching'),
    W('share', '🍕', [
        S('v.', '分享；共用', 'Let\'s share this pizza.', '我們一起分這個披薩吧。', 'share + 物 + with + 人'),
        S('v.', '分攤；分配', 'We shared the work.', '我們分攤工作。'),
        S('n.', '股票', 'He bought some shares of the company.', '他買了這家公司的一些股票。'),
    ], 'share - shared - shared - sharing'),
    W('sharp', '🔪', [
        S('adj.', '鋒利的', 'Be careful. The knife is sharp.', '小心，刀子很利。'),
        S('adj.', '嚴厲的；尖銳的（言語）', 'She gave me a sharp look.', '她狠狠地瞪了我一眼。'),
        S('adj.', '劇烈的；突然的', 'I felt a sharp pain in my leg.', '我的腿一陣劇痛。', 'a sharp turn 急轉彎'),
        S('adj.', '清楚的；明顯的', 'This photo is very sharp.', '這張照片很清楚。'),
        S('adj.', '敏銳的；聰明的', 'Grandpa still has a sharp mind.', '爺爺的頭腦還很靈光。', 'have a sharp eye for 對…有敏銳的眼光'),
    ], 'sharp - sharper - sharpest'),
    W('slow', '🐢', [
        S('adj.', '慢的', 'My watch is five minutes slow.', '我的錶慢了五分鐘。'),
        S('adj.', '遲鈍的', 'He is a little slow at math.', '他數學反應有點慢。'),
        S('adj.', '（生意）冷清的', 'Business is slow on rainy days.', '下雨天生意很冷清。'),
        S('v.', '減速', 'Slow down! You\'re driving too fast.', '慢一點！你開太快了。', 'slow down 減速'),
        S('adv.', '慢慢地', 'Go slow, please.', '請慢慢來。'),
    ], 'slow - slower - slowest'),
    W('space', '🚀', [
        S('n.', '空間', 'There isn\'t enough space for a sofa.', '沒有足夠的空間放沙發。'),
        S('n.', '空位', 'Is there a parking space?', '有停車位嗎？'),
        S('n.', '太空', 'Astronauts live in space for months.', '太空人在太空住好幾個月。'),
        S('v.', '隔開；留空', 'Space the chairs evenly.', '把椅子平均排開。'),
    ], 'space - spaced - spaced - spacing'),
    W('train', '🚆', [
        S('n.', '火車', 'Let\'s take the train to Hualien.', '我們搭火車去花蓮吧。', 'take a train 搭火車；get on / off the train 上／下火車'),
        S('n.', '（禮服的）拖尾', 'The bride\'s dress has a long train.', '新娘的禮服有長長的拖尾。'),
        S('v.', '訓練', 'He trains his dog to sit.', '他訓練他的狗坐下。', 'train + 人／動物 + to V 訓練…做'),
    ], 'train - trained - trained - training'),
    W('treat', '🍬', [
        S('v.', '對待', 'Don\'t treat me like a baby.', '別把我當小孩子。'),
        S('v.', '看待', 'She treated it as a joke.', '她把它當成玩笑。'),
        S('v.', '治療', 'The doctor treated his cut.', '醫生處理了他的傷口。'),
        S('v.', '請客；款待', 'Let me treat you to lunch.', '我請你吃午餐。', 'trick or treat 不給糖就搗蛋'),
        S('n.', '請客；好東西', 'This is my treat.', '這次我請客。'),
    ], 'treat - treated - treated - treating'),
    W('well', '👍', [
        S('adv.', '好地', 'She sings very well.', '她唱歌很好聽。', 'as well 也'),
        S('adj.', '健康的', 'I don\'t feel well today.', '我今天不太舒服。', 'get well soon 早日康復'),
        S('int.', '嗯；好吧', 'Well, let me think.', '嗯，讓我想想。'),
        S('n.', '井', 'The village gets water from a well.', '這個村子從井裡取水。'),
    ], 'well - better - best'),
  ],
  'focus': [
    {'title': '易混淆字：使役動詞 let／have／make', 'head': ('單字', '句型', '例句'), 'rows': [
      ('let', '允許：let + 受詞 + 原形動詞', 'Mom let me play games for an hour.'),
      ('have', '要求、安排：have + 人 + 原形動詞；have + 物 + p.p.（讓東西被處理）', 'I had my hair cut.'),
      ('make', '強迫、使得：make + 受詞 + 原形動詞／形容詞', 'The sad movie made me cry.'),
    ], 'note': '三個都是「受詞 + 原形動詞」，不加 to。'},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('light', '燈；光', '輕的；淺色的；點燃'),
      ('duck', '鴨子', '迅速低頭；躲避'),
      ('pound', '英鎊', '磅；（心）怦怦跳'),
      ('pretty', '漂亮的', '相當（pretty easy）'),
      ('share', '分享', '股票'),
      ('train', '火車', '訓練；禮服拖尾'),
      ('treat', '對待', '請客；治療'),
      ('well', '好地', '健康的；井'),
    ], 'note': ''},
    {'title': '常用片語', 'head': ('片語', '意思', '例句'), 'rows': [
      ('pick up', '接人；撿起', 'I\'ll pick you up at six.'),
      ('slow down', '減速', 'Slow down, please.'),
      ('blow out', '吹熄', 'Blow out the candles!'),
      ('be hard on', '對…嚴厲', 'Don\'t be so hard on him.'),
      ('get well soon', '早日康復', 'Get well soon!'),
      ('This is my treat.', '這次我請客', 'Put your money away. This is my treat.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'Tom Cruise <b>stars</b> in this action movie.', 'opts': ['星星', '明星', '主演', '星級'], 'answer': 2, 'exp': 'star 動詞：主演。'},
    {'type': 'mc', 'q': 'This box is <b>light</b>. I can carry it with one hand.', 'opts': ['燈', '明亮的', '淺色的', '輕的'], 'answer': 3, 'exp': '一隻手拿得動 → 輕的。'},
    {'type': 'mc', 'q': 'The teacher is <b>hard</b> on students who are late.', 'opts': ['困難的', '堅硬的', '嚴厲的', '努力地'], 'answer': 2, 'exp': 'be hard on 對…嚴厲。'},
    {'type': 'mc', 'q': 'Can you help me <b>clear</b> the table?', 'opts': ['晴朗的', '清楚的', '收拾', '清醒'], 'answer': 2, 'exp': 'clear the table 收拾餐桌。'},
    {'type': 'mc', 'q': '<b>Duck</b>! There\'s a low door here.', 'opts': ['鴨子', '鴨肉', '低頭', '跑'], 'answer': 2, 'exp': 'duck 動詞：迅速低頭。'},
    {'type': 'mc', 'q': 'My heart <b>pounded</b> when I went on stage.', 'opts': ['英鎊', '磅', '怦怦跳', '停止'], 'answer': 2, 'exp': '上台緊張 → 心怦怦跳。'},
    {'type': 'mc', 'q': 'The movie was <b>pretty</b> good.', 'opts': ['漂亮的', '相當', '一點也不', '可愛的'], 'answer': 1, 'exp': 'pretty + 形容詞：相當。'},
    {'type': 'mc', 'q': 'Dinner is my <b>treat</b> tonight.', 'opts': ['對待', '治療', '請客', '糖果'], 'answer': 2, 'exp': 'my treat 我請客。'},
    {'type': 'mc', 'q': 'People in the village get water from a <b>well</b>.', 'opts': ['好地', '健康的', '井', '河'], 'answer': 2, 'exp': 'well 名詞：井。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'Be careful. The knife is very ______.  ／  Grandma still has a ______ mind.', 'opts': ['sharp', 'clear', 'bright', 'hard'], 'answer': 0, 'exp': 'sharp 鋒利的／敏銳的。'},
    {'type': 'mc', 'q': 'We took the ______ to Taichung.  ／  The coach will ______ us every Saturday.', 'opts': ['bus', 'train', 'teach', 'plane'], 'answer': 1, 'exp': 'train 火車／訓練。'},
    {'type': 'mc', 'q': 'Is there any ______ for my bag?  ／  The astronaut flew into ______.', 'opts': ['room', 'space', 'sky', 'place'], 'answer': 1, 'exp': 'space 空間／太空。'},
    {'type': 'mc', 'q': 'Let\'s ______ the cake.  ／  He owns 500 ______s of the company.', 'opts': ['cut', 'share', 'stock', 'eat'], 'answer': 1, 'exp': 'share 分享／股票。'},
    {'type': 'mc', 'q': 'Turn on the ______. I want to hear the news.  ／  The ships talked by ______.', 'opts': ['TV', 'radio', 'phone', 'light'], 'answer': 1, 'exp': 'radio 收音機／無線電。'},
  ]},
  {'title': '③ 易混淆字：let／have／make', 'items': [
    {'type': 'mc', 'q': 'My parents ______ me stay up late on Saturdays.', 'opts': ['let', 'make', 'have to', 'lets'], 'answer': 0, 'exp': '允許 → let。'},
    {'type': 'mc', 'q': 'The joke ______ everyone laugh.', 'opts': ['let', 'made', 'had to', 'let to'], 'answer': 1, 'exp': '使得大家笑 → made。'},
    {'type': 'mc', 'q': 'I ______ my bike fixed yesterday.', 'opts': ['let', 'made', 'had', 'got to'], 'answer': 2, 'exp': 'have + 物 + p.p. 請人處理。'},
    {'type': 'mc', 'q': 'The teacher made us ______ the words ten times.', 'opts': ['write', 'to write', 'writing', 'wrote'], 'answer': 0, 'exp': 'make + 受詞 + 原形動詞。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Make a wish and blow {0} the candles. （吹熄）', 'blanks': [['out']], 'exp': 'blow out 吹熄。'},
    {'q': 'Dad will pick me {0} after school. （接）', 'blanks': [['up']], 'exp': 'pick up 接人。'},
    {'q': 'You {0} be hungry. You didn\'t eat lunch. （一定，推測）', 'blanks': [['must']], 'exp': 'must 表示肯定的推測。'},
    {'q': 'I heard some good {0} today. （消息）', 'blanks': [['news']], 'exp': 'news 不可數。'},
    {'q': 'Please slow {0}. The road is wet. （減速）', 'blanks': [['down']], 'exp': 'slow down 減速。'},
    {'q': 'I hope you get {0} soon. （健康的）', 'blanks': [['well']], 'exp': 'get well soon 早日康復。'},
  ]},
]
