# LaLa Word Unit 6（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 61–70 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 6, 'en': 'The Way We Change', 'zh': '一字多義（六）',
  'intro': 'change 是改變，也是「零錢」；plant 是植物，也是「工廠」。這個單元有 8 個主題單字、12 個更多單字。',
  'words': [
    W('change', '🪙', [
        S('n.', '改變；變化', 'There are some changes to our class schedule.', '我們的課表有一些變動。'),
        S('n.', '零錢', 'Here is your change. Thank you!', '這是找您的零錢，謝謝！'),
        S('v.', '改變；更換', 'I changed my mind. I want the red one.', '我改變主意了，我要紅色的。', 'change one\'s mind 改變心意；change into 換成'),
    ], 'change - changed - changed - changing', key=True),
    W('lose', '🔍', [
        S('v.', '弄丟；失去', 'I lost my umbrella on the bus.', '我把雨傘掉在公車上了。', 'lose weight 減重；lose interest 失去興趣；lose one\'s voice 失聲'),
        S('v.', '輸', 'Our team lost the game 2 to 3.', '我們隊以二比三輸了比賽。'),
    ], 'lose - lost - lost - losing', key=True),
    W('learn', '📖', [
        S('v.', '學習', 'I want to learn to play the piano.', '我想學彈鋼琴。', 'learn to + V 學會；learn one\'s lesson 學到教訓'),
        S('v.', '得知', 'We learned about the news from TV.', '我們從電視得知這個消息。', 'learn about / of 得知'),
        S('v.', '記住；背熟', 'Learn these words by heart.', '把這些單字背起來。', 'learn… by heart 背熟'),
    ], 'learn - learned（learnt） - learned（learnt） - learning', key=True),
    W('live', '🏠', [
        S('v.', '生活；過活', 'People can\'t live without water.', '人沒有水無法生活。', 'live on 靠…過活'),
        S('v.', '居住', 'I live in Kaohsiung with my family.', '我和家人住在高雄。'),
        S('adj.', '活的', 'The shop sells live fish and crabs.', '這家店賣活魚和活螃蟹。'),
        S('adj.', '現場的', 'We watched a live show last night.', '我們昨晚看了一場現場表演。'),
    ], 'live - lived - lived - living（動詞唸 [lɪv]，形容詞唸 [laɪv]）', key=True),
    W('plant', '🪴', [
        S('n.', '植物', 'Plants need water and sunlight.', '植物需要水和陽光。'),
        S('n.', '工廠', 'My uncle works at a power plant.', '我叔叔在發電廠工作。'),
        S('v.', '種植', 'We planted a tree in the school garden.', '我們在學校花園種了一棵樹。'),
        S('v.', '輕放（親吻）', 'Mom planted a kiss on the baby\'s face.', '媽媽在寶寶臉上親了一下。', 'plant a kiss on 突然親一下'),
    ], 'plant - planted - planted - planting', key=True),
    W('way', '🛣️', [
        S('n.', '方法；方式', 'This is the best way to learn English.', '這是學英文最好的方法。', 'way to + V 做…的方法'),
        S('n.', '道路；方向', 'Can you tell me the way to the station?', '你可以告訴我去車站的路嗎？', 'lose one\'s way 迷路；the other way around 相反'),
        S('n.', '距離', 'The beach is a long way from here.', '海邊離這裡很遠。'),
    ], '複數 ways', key=True),
    W('rest', '🛋️', [
        S('v.', '休息', 'Let\'s stop and rest for a while.', '我們停下來休息一下吧。'),
        S('n.', '休息', 'You look tired. Take a rest.', '你看起來很累，休息一下吧。', 'take / have a rest 休息一下'),
        S('v.', '靠在；倚靠', 'She rested her head on my shoulder.', '她把頭靠在我的肩膀上。'),
        S('v.', '安息', 'May he rest in peace.', '願他安息。', 'rest in peace 安息'),
        S('n.', '其餘；剩下', 'I ate half of the pizza and saved the rest.', '我吃了半個披薩，剩下的留著。', 'the rest 其餘的'),
    ], 'rest - rested - rested - resting', key=True),
    W('miss', '🚌', [
        S('v.', '錯過；沒趕上', 'Hurry up, or we will miss the bus.', '快點，不然我們會趕不上公車。'),
        S('v.', '沒打中；沒接到', 'He kicked the ball but missed the goal.', '他踢了球但沒射進球門。'),
        S('v.', '想念', 'I miss my grandma a lot.', '我很想念奶奶。'),
        S('n.', '小姐；老師（Miss）', 'Miss Wang is our music teacher.', '王老師是我們的音樂老師。'),
        S('n.', '失誤；沒打中', 'That was a bad miss.', '那一球失誤得很可惜。'),
    ], 'miss - missed - missed - missing', key=True),
    W('age', '🎂', [
        S('n.', '年紀；年齡', 'He started swimming at the age of five.', '他五歲開始學游泳。', 'at the age of 在…歲時；act one\'s age 舉止符合年紀'),
        S('n.', '時代', 'We live in the age of the internet.', '我們生活在網路時代。'),
        S('n.', '很長的時間（ages）', 'I haven\'t seen you for ages!', '好久不見！'),
        S('v.', '變老；熟成', 'The cheese is aged for a year.', '這塊起司熟成了一年。'),
    ], 'age - aged - aged - aging'),
    W('camp', '⛺', [
        S('n.', '營隊', 'I went to an English camp last summer.', '我去年夏天參加英語營。'),
        S('n.', '營地', 'We set up camp near the lake.', '我們在湖邊紮營。'),
        S('v.', '露營', 'We camped in the mountains for two nights.', '我們在山上露營兩晚。', 'go camping 去露營'),
    ], 'camp - camped - camped - camping'),
    W('cool', '😎', [
        S('adj.', '涼爽的', 'It\'s cool in the morning.', '早上很涼爽。'),
        S('adj.', '冷靜的', 'Stay cool and think.', '保持冷靜，好好想想。', 'as cool as a cucumber 非常冷靜'),
        S('adj.', '酷的', 'Your new shoes look cool!', '你的新鞋看起來好酷！'),
        S('v.', '使冷卻', 'Let the soup cool down before you eat it.', '湯放涼一點再喝。', 'cool down 冷卻；冷靜下來'),
    ], 'cool - cooler - coolest；cool - cooled - cooled - cooling'),
    W('department', '🏬', [
        S('n.', '（公司的）部門；（百貨的）專櫃', 'Mom bought shoes at a department store.', '媽媽在百貨公司買了鞋子。', 'department store 百貨公司'),
        S('n.', '（大學的）系', 'My sister studies in the English Department.', '我姊姊讀英文系。'),
    ], '複數 departments'),
    W('just', '⏱️', [
        S('adv.', '剛才；剛剛', 'I just finished my homework.', '我剛寫完功課。', 'just now 剛才'),
        S('adv.', '只是；僅僅', 'It\'s just a joke.', '那只是個玩笑。'),
        S('adv.', '正好；恰好', 'This dress is just right for you.', '這件洋裝你穿剛剛好。'),
        S('adv.', '實在；很', 'The view is just beautiful.', '風景實在太美了。'),
        S('adj.', '公正的', 'The teacher is fair and just.', '這位老師很公平公正。'),
    ]),
    W('oil', '🛢️', [
        S('n.', '油；石油', 'Fry the eggs in a little oil.', '用一點油煎蛋。'),
        S('v.', '給…上油', 'Dad oiled the old bike.', '爸爸幫舊腳踏車上油。'),
        S('n.', '油畫', 'There are many famous oils in this museum.', '這間美術館有很多名畫（油畫）。'),
    ], 'oil - oiled - oiled - oiling'),
    W('roll', '🧻', [
        S('v.', '滾動；翻動', 'The ball rolled down the hill.', '球滾下山坡。', 'roll over 翻身'),
        S('v.', '捲', 'Roll up your sleeves before you wash the dishes.', '洗碗前把袖子捲起來。', 'roll up 捲起'),
        S('n.', '一捲', 'We need a new roll of toilet paper.', '我們需要一捲新的衛生紙。'),
        S('n.', '小圓麵包', 'I had a bread roll for breakfast.', '我早餐吃了一個小圓麵包。'),
        S('n.', '名單；名冊', 'The teacher called the roll.', '老師點名。'),
    ], 'roll - rolled - rolled - rolling'),
    W('station', '🚉', [
        S('n.', '車站；局', 'Let\'s meet at the train station.', '我們在火車站碰面。', 'police station 警察局；fire station 消防局；gas station 加油站'),
        S('n.', '電臺', 'This radio station plays great music.', '這個電臺播的音樂很好聽。'),
        S('v.', '駐紮', 'His dad was stationed on Kinmen.', '他爸爸以前駐守在金門。'),
    ], 'station - stationed - stationed - stationing'),
    W('stop', '🛑', [
        S('v.', '停止；停留', 'Stop talking and listen!', '別說話，注意聽！', 'stop + V-ing 停止做；stop to + V 停下來去做；stop by 順道拜訪'),
        S('v.', '阻止', 'Nobody can stop him from trying.', '沒有人能阻止他嘗試。', 'stop… from + V-ing 阻止…做'),
        S('n.', '停止', 'The car came to a stop.', '車子停下來了。'),
        S('n.', '車站；站牌', 'Get off at the next stop.', '在下一站下車。', 'bus stop 公車站'),
    ], 'stop - stopped - stopped - stopping'),
    W('story', '📕', [
        S('n.', '故事', 'Grandpa told us a funny story.', '爺爺說了一個好笑的故事給我們聽。', 'bedtime story 睡前故事；It\'s a long story. 說來話長'),
        S('n.', '說法；藉口', 'He made up a story about being sick.', '他編了一個生病的藉口。', 'make up a story 編藉口'),
        S('n.', '樓層', 'Our school building has five stories.', '我們的校舍有五層樓。'),
    ], '複數 stories'),
    W('trip', '🧳', [
        S('n.', '旅行；旅程', 'We went on a trip to Hualien.', '我們去花蓮旅行。', 'go on a trip 去旅行；field trip 校外教學；round-trip 來回'),
        S('v.', '絆倒', 'Be careful. Don\'t trip over the box.', '小心，別被箱子絆倒。', 'trip over 被…絆倒'),
    ], 'trip - tripped - tripped - tripping'),
    W('visit', '🧳', [
        S('v.', '參觀；拜訪', 'We visited the National Palace Museum.', '我們參觀了故宮博物院。'),
        S('v.', '瀏覽（網站）', 'Visit our website for more information.', '請瀏覽我們的網站了解更多。'),
        S('n.', '拜訪；參觀', 'Grandpa paid us a visit last Sunday.', '爺爺上星期天來看我們。', 'pay a visit 拜訪'),
    ], 'visit - visited - visited - visiting'),
  ],
  'focus': [
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('change', '改變', '零錢'),
      ('live', '住', '活的；現場的（唸 [laɪv]）'),
      ('plant', '植物；種植', '工廠'),
      ('rest', '休息', '其餘的'),
      ('miss', '錯過；想念', '小姐；老師'),
      ('just', '剛剛；只是', '公正的'),
      ('roll', '滾動', '一捲；小圓麵包；名單'),
      ('story', '故事', '樓層；藉口'),
      ('trip', '旅行', '絆倒'),
    ], 'note': ''},
    {'title': 'stop + V-ing 和 stop + to V', 'head': ('句型', '意思', '例句'), 'rows': [
      ('stop + V-ing', '停止正在做的事', 'He stopped playing games.（不玩了）'),
      ('stop + to V', '停下來，去做另一件事', 'He stopped to drink water.（停下來喝水）'),
      ('stop… from + V-ing', '阻止…做', 'The rain stopped us from going out.'),
    ], 'note': ''},
    {'title': '常用片語', 'head': ('片語', '意思', '例句'), 'rows': [
      ('change one\'s mind', '改變心意', 'She changed her mind.'),
      ('lose weight', '減重', 'Dad wants to lose weight.'),
      ('learn… by heart', '背熟', 'Learn the poem by heart.'),
      ('take a rest', '休息一下', 'Let\'s take a rest.'),
      ('pay a visit', '拜訪', 'We paid Grandma a visit.'),
      ('go on a trip', '去旅行', 'They went on a trip to Japan.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'Here\'s twenty dollars. Keep the <b>change</b>.', 'opts': ['改變', '零錢', '更換', '禮物'], 'answer': 1, 'exp': 'Keep the change. 不用找了。'},
    {'type': 'mc', 'q': 'My father works at a car <b>plant</b>.', 'opts': ['植物', '工廠', '花園', '種植'], 'answer': 1, 'exp': 'car plant 汽車工廠。'},
    {'type': 'mc', 'q': 'Amy ate one cookie and gave the <b>rest</b> to her friends.', 'opts': ['休息', '其餘的', '倚靠', '安息'], 'answer': 1, 'exp': 'the rest 剩下的。'},
    {'type': 'mc', 'q': 'I <b>miss</b> my old friends in Taichung.', 'opts': ['錯過', '沒打中', '想念', '失誤'], 'answer': 2, 'exp': '想念朋友。'},
    {'type': 'mc', 'q': 'We watched the game <b>live</b> on TV.', 'opts': ['居住', '生活', '活的', '現場直播'], 'answer': 3, 'exp': 'live 現場的（唸 [laɪv]）。'},
    {'type': 'mc', 'q': 'The building has thirty <b>stories</b>.', 'opts': ['故事', '藉口', '樓層', '房間'], 'answer': 2, 'exp': 'stories 樓層。'},
    {'type': 'mc', 'q': 'Watch out! Don\'t <b>trip</b> over the cable.', 'opts': ['旅行', '絆倒', '跳', '走'], 'answer': 1, 'exp': 'trip over 被…絆倒。'},
    {'type': 'mc', 'q': 'A good judge must be <b>just</b>.', 'opts': ['剛剛', '只是', '公正的', '恰好'], 'answer': 2, 'exp': 'just 形容詞：公正的。'},
    {'type': 'mc', 'q': 'I haven\'t seen Uncle Tom for <b>ages</b>.', 'opts': ['年紀', '時代', '很長一段時間', '熟成'], 'answer': 2, 'exp': 'for ages 很久。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'Get off the bus at the next ______.  ／  ______ talking! The baby is sleeping.', 'opts': ['station', 'stop', 'way', 'place'], 'answer': 1, 'exp': 'bus stop 公車站。'},
    {'type': 'mc', 'q': 'The ball ______ed under the sofa.  ／  Can you buy a ______ of paper towels?', 'opts': ['roll', 'kick', 'box', 'move'], 'answer': 0, 'exp': 'roll 滾動／一捲。'},
    {'type': 'mc', 'q': 'Is this the ______ to the museum?  ／  There is no ______ to finish it in one day.', 'opts': ['road', 'way', 'stop', 'trip'], 'answer': 1, 'exp': 'way 路／方法。'},
    {'type': 'mc', 'q': 'It\'s ______ outside. Bring a jacket.  ／  Wow, your skateboard is so ______!', 'opts': ['cold', 'cool', 'hot', 'nice'], 'answer': 1, 'exp': 'cool 涼的／酷的。'},
    {'type': 'mc', 'q': 'Hurry, or you\'ll ______ the train.  ／  ______ Chen is our new teacher.', 'opts': ['lose', 'miss', 'catch', 'Mrs.'], 'answer': 1, 'exp': 'miss 錯過／Miss 小姐、老師。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'I wanted pizza, but then I changed my {0}. （心意）', 'blanks': [['mind']], 'exp': 'change one\'s mind 改變心意。'},
    {'q': 'Grandpa wants to {0} weight. （減重）', 'blanks': [['lose']], 'exp': 'lose weight 減重。'},
    {'q': 'We go {0} by the lake every summer. （露營）', 'blanks': [['camping']], 'exp': 'go camping 去露營。'},
    {'q': 'Please learn this poem by {0}. （背熟）', 'blanks': [['heart']], 'exp': 'learn… by heart 背熟。'},
    {'q': 'Mom bought a new bag at the {0} store. （百貨公司）', 'blanks': [['department']], 'exp': 'department store 百貨公司。'},
    {'q': 'Let\'s pay Grandma a {0} this weekend. （拜訪）', 'blanks': [['visit']], 'exp': 'pay a visit 拜訪。'},
  ]},
]
