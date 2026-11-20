# LaLa Word Unit 10（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 108–118 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 10, 'en': 'What Is Life Like in Space?', 'zh': '一字多義（十）',
  'intro': 'dish 是盤子，也是「一道菜」；fire 是火，也是「開除」。這個單元有 7 個主題單字、7 個更多單字，'
           '再整理 meet／meat、snack／snake、then／than、hear／listen／sound、a few／a little／few／little，和字尾 -ous（famous、dangerous）。',
  'words': [
    W('dish', '🍲', [
        S('n.', '盤子；碗盤', 'It\'s my turn to wash the dishes.', '輪到我洗碗了。', 'do / wash the dishes 洗碗'),
        S('n.', '一道菜', 'Beef noodles is my favorite dish.', '牛肉麵是我最喜歡的菜。', 'main dish 主菜；side dish 配菜'),
    ], '複數 dishes', key=True),
    W('taste', '👅', [
        S('v.', '嚐起來', 'This soup tastes good.', '這個湯很好喝。', 'taste + 形容詞；taste like + 名詞'),
        S('v.', '嚐；品嚐', 'Can I taste your ice cream?', '我可以嚐一口你的冰淇淋嗎？'),
        S('n.', '味道', 'I don\'t like the taste of bitter melon.', '我不喜歡苦瓜的味道。'),
        S('n.', '品味', 'She has good taste in music.', '她對音樂很有品味。'),
    ], 'taste - tasted - tasted - tasting', key=True),
    W('stay', '🏨', [
        S('v.', '保持（某狀態）', 'Drink water and stay healthy.', '多喝水，保持健康。', 'stay up 熬夜；stay away from 遠離'),
        S('v.', '暫住', 'We stayed at a hotel near the beach.', '我們住在海邊附近的飯店。', 'stay with + 人 暫住某人家'),
        S('v.', '待在；停留', 'It\'s raining. Let\'s stay home.', '在下雨，我們待在家吧。', 'stay home 待在家'),
        S('n.', '停留；住宿', 'Enjoy your stay in Taipei!', '祝你在臺北玩得愉快！'),
    ], 'stay - stayed - stayed - staying', key=True),
    W('raise', '✋', [
        S('v.', '提高（音量等）', 'Please don\'t raise your voice.', '請不要提高音量。'),
        S('v.', '舉起', 'Raise your hand if you know the answer.', '知道答案的人請舉手。', 'raise one\'s hand 舉手'),
        S('v.', '養育；飼養', 'Grandma raised six children.', '奶奶養大了六個孩子。'),
        S('v.', '提出', 'Amy raised a good question.', 'Amy 提出了一個好問題。'),
        S('v.', '募集（資金）', 'The students raised money for the poor.', '學生們為窮人募款。', 'raise money 募款'),
        S('n.', '加薪', 'Dad got a raise this year.', '爸爸今年加薪了。'),
    ], 'raise - raised - raised - raising', key=True),
    W('level', '📶', [
        S('n.', '含量', 'This drink has a high level of sugar.', '這杯飲料含糖量很高。'),
        S('n.', '程度；等級', 'This book is good for beginner level.', '這本書適合初級程度。'),
        S('n.', '高度', 'The water level of the river is rising.', '河水的水位在上升。', 'water level 水位；sea level 海平面'),
        S('n.', '（建築的）層', 'The food court is on level 4.', '美食街在四樓。'),
    ], '複數 levels', key=True),
    W('special', '🌟', [
        S('adj.', '特別的', 'Today is a special day for me.', '今天對我來說是特別的一天。', 'something special 特別的東西'),
        S('adj.', '專門的；特殊用途的', 'Divers wear special suits.', '潛水員穿著特殊的潛水衣。'),
        S('n.', '特餐；特別節目', 'Today\'s special is fried rice.', '今天的特餐是炒飯。'),
    ], 'special - more special - most special', key=True),
    W('smell', '👃', [
        S('v.', '聞起來', 'The flowers smell sweet.', '這些花聞起來很香。', 'smell + 形容詞；smell of / like 有…的味道'),
        S('v.', '聞到', 'I can smell something burning!', '我聞到有東西燒焦了！'),
        S('v.', '嗅覺；聞', 'Dogs can smell very well.', '狗的嗅覺很好。'),
        S('n.', '氣味', 'I love the smell of fresh bread.', '我喜歡剛出爐麵包的香味。'),
    ], 'smell - smelled（smelt） - smelled（smelt） - smelling', key=True),
    W('bite', '🦟', [
        S('n.', '一口', 'Can I have a bite of your sandwich?', '我可以吃一口你的三明治嗎？', 'have / take a bite 咬一口'),
        S('v.', '咬；叮', 'The mosquitoes bit me all night.', '蚊子咬了我一整晚。'),
        S('v.', '（魚）上鉤', 'The fish aren\'t biting today.', '今天魚都不上鉤。'),
    ], 'bite - bit - bitten - biting'),
    W('fire', '🔥', [
        S('n.', '火；火災', 'The firefighters put out the fire.', '消防員撲滅了火。', 'set fire to 放火；put out the fire 滅火；on fire 著火'),
        S('n.', '火堆', 'We sat around the fire and sang songs.', '我們圍著火堆唱歌。'),
        S('v.', '開槍', 'The soldier fired into the air.', '士兵朝空中開槍。'),
        S('v.', '解僱', 'He was fired for being late every day.', '他因為每天遲到被開除。', 'be / get fired 被開除'),
    ], 'fire - fired - fired - firing'),
    W('gas', '⛽', [
        S('n.', '氣體', 'Water can turn into a gas.', '水可以變成氣體。'),
        S('n.', '瓦斯；天然氣', 'Turn off the gas after cooking.', '煮完飯要關瓦斯。', 'gas stove 瓦斯爐'),
        S('n.', '腸胃脹氣', 'Eating beans gives me gas.', '吃豆子讓我脹氣。'),
        S('n.', '汽油', 'The car is out of gas.', '車子沒油了。', 'gas station 加油站'),
    ], '複數 gases（gasses）'),
    W('get', '🎁', [
        S('v.', '得到；買', 'Where did you get that cool bag?', '你那個酷包包在哪裡買的？'),
        S('v.', '收到', 'I got a letter from my pen pal.', '我收到筆友寄來的信。', 'get a call 接到電話'),
        S('v.', '上下車', 'Get on the bus at the next stop.', '在下一站上公車。', 'get on / off 上／下（公車、火車）；get in / out of 上／下（汽車）'),
        S('v.', '到達', 'What time did you get home?', '你幾點到家的？', 'get to + 地方 到達'),
        S('v.', '變得', 'It\'s getting dark.', '天色漸漸暗了。', 'get married 結婚；get used to 習慣'),
        S('v.', '了解', 'Sorry, I don\'t get it.', '抱歉，我不懂。'),
    ], 'get - got - got（gotten） - getting'),
    W('medium', '☕', [
        S('adj.', '中等的（尺寸）', 'I\'d like a medium coffee, please.', '我要一杯中杯咖啡。'),
        S('adj.', '（牛排）五分熟的', 'I\'d like my steak medium.', '我的牛排要五分熟。'),
        S('n.', '媒介', 'TV is a popular medium.', '電視是很普遍的媒體。'),
    ], '複數 media（mediums）'),
    W('rock', '🪨', [
        S('n.', '岩石；石塊', 'We sat on a big rock by the sea.', '我們坐在海邊的大石頭上。'),
        S('n.', '搖滾樂', 'My dad loves rock music.', '我爸爸很愛搖滾樂。', 'rock music 搖滾樂；rock star 搖滾明星'),
        S('v.', '搖晃', 'The boat rocked in the big waves.', '小船在大浪中搖晃。'),
    ], 'rock - rocked - rocked - rocking'),
    W('sound', '🔊', [
        S('n.', '聲音', 'I heard a strange sound outside.', '我聽到外面有奇怪的聲音。', 'make a sound 發出聲音'),
        S('n.', '音量', 'Can you turn the sound down?', '你可以把音量調小嗎？'),
        S('v.', '聽起來', 'That sounds like fun!', '聽起來很好玩！', 'sound + 形容詞；sound like + 名詞'),
        S('adj.', '完好無傷的', 'They came back safe and sound.', '他們平安歸來。', 'safe and sound 安然無恙'),
        S('adj.', '（睡得）很沉的', 'The baby is in a sound sleep.', '寶寶睡得很熟。'),
    ], 'sound - sounded - sounded - sounding'),
    W('famous', '🏆', [
        S('adj.', '有名的', 'Tainan is famous for its food.', '臺南以美食聞名。', 'be famous for 因…而有名'),
    ], 'fame 名聲 + -ous'),
    W('dangerous', '⚠️', [
        S('adj.', '危險的', 'It\'s dangerous to swim here.', '在這裡游泳很危險。'),
    ], 'danger 危險 + -ous'),
  ],
  'focus': [
    {'title': '發音或拼字很像的字', 'head': ('單字', '意思', '例句'), 'rows': [
      ('meet / meat', '遇見 ／ 肉（兩個字發音一樣）', 'Nice to meet you.／I don\'t eat meat.'),
      ('snack / snake', '點心 ／ 蛇', 'We had some snacks.／There\'s a snake!'),
      ('then / than', '當時；然後；那麼 ／ 比（比較級）', 'Then we went home.／He is taller than me.'),
    ], 'note': ''},
    {'title': '易混淆字：hear／listen／sound', 'head': ('單字', '用法', '例句'), 'rows': [
      ('hear', '聽到（不用刻意去聽）', 'I heard a dog bark.'),
      ('listen', '專心聽，後面要加 to', 'Listen to me, please.'),
      ('sound', '聽起來 + 形容詞；sound like + 名詞（沒有進行式）', 'That sounds great!'),
    ], 'note': ''},
    {'title': '易混淆字：a few／a little／few／little', 'head': ('單字', '用法', '例句'), 'rows': [
      ('a few', '一些（還有），接可數複數名詞', 'I have a few friends here.'),
      ('a little', '一些（還有），接不可數名詞', 'There is a little milk left.'),
      ('few', '很少、幾乎沒有，接可數複數名詞', 'Few people came to the party.'),
      ('little', '很少、幾乎沒有，接不可數名詞', 'There is little water in the bottle.'),
    ], 'note': '有 a 的偏正面（還有一些），沒有 a 的偏負面（幾乎沒有）。'},
    {'title': '字尾 -ous：「充滿…的；有…性質的」', 'head': ('原來的字', '加 -ous', '意思'), 'rows': [
      ('fame 名聲', 'famous', '有名的'),
      ('danger 危險', 'dangerous', '危險的'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'Stinky tofu is a famous Taiwanese <b>dish</b>.', 'opts': ['盤子', '一道菜', '碗', '點心'], 'answer': 1, 'exp': 'a Taiwanese dish 一道臺灣菜。'},
    {'type': 'mc', 'q': 'My mom has good <b>taste</b> in clothes.', 'opts': ['味道', '嚐', '品味', '吃起來'], 'answer': 2, 'exp': 'have good taste in 很有品味。'},
    {'type': 'mc', 'q': 'The farmer <b>raises</b> chickens and pigs.', 'opts': ['舉起', '提高', '飼養', '募集'], 'answer': 2, 'exp': 'raise animals 飼養動物。'},
    {'type': 'mc', 'q': 'The parking lot has three <b>levels</b>.', 'opts': ['含量', '程度', '高度', '層'], 'answer': 3, 'exp': '停車場的 levels → 層。'},
    {'type': 'mc', 'q': 'The cook was <b>fired</b> because the food was terrible.', 'opts': ['著火', '開槍', '被開除', '生火'], 'answer': 2, 'exp': 'be fired 被開除。'},
    {'type': 'mc', 'q': 'Let\'s stop at the next <b>gas</b> station. We need to fill up the car.', 'opts': ['氣體', '瓦斯', '汽油', '脹氣'], 'answer': 2, 'exp': 'gas station 加油站。'},
    {'type': 'mc', 'q': 'I don\'t <b>get</b> the joke. Can you explain it?', 'opts': ['得到', '到達', '變得', '了解'], 'answer': 3, 'exp': 'don\'t get it 不懂。'},
    {'type': 'mc', 'q': 'How would you like your steak? — <b>Medium</b>, please.', 'opts': ['中杯', '五分熟', '媒體', '中等身高'], 'answer': 1, 'exp': '牛排 medium 五分熟。'},
    {'type': 'mc', 'q': 'After a long day, I fell into a <b>sound</b> sleep.', 'opts': ['聲音', '音量', '聽起來', '很沉的'], 'answer': 3, 'exp': 'sound sleep 熟睡。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'Don\'t ______ up too late.  ／  We will ______ at Grandma\'s house this weekend.', 'opts': ['wake', 'stay', 'get', 'live'], 'answer': 1, 'exp': 'stay up 熬夜／stay 暫住。'},
    {'type': 'mc', 'q': 'The chicken soup ______s great.  ／  Do you want to ______ my cake?', 'opts': ['taste', 'smell', 'try', 'eat'], 'answer': 0, 'exp': 'taste 嚐起來／嚐。'},
    {'type': 'mc', 'q': 'I love the ______ of coffee.  ／  Can you ______ the smoke?', 'opts': ['taste', 'smell', 'sound', 'see'], 'answer': 1, 'exp': 'smell 氣味／聞到。'},
    {'type': 'mc', 'q': 'A dog may ______ you if you touch it.  ／  Can I have a ______ of your cookie?', 'opts': ['bite', 'piece', 'hit', 'taste'], 'answer': 0, 'exp': 'bite 咬／一口。'},
    {'type': 'mc', 'q': 'The kids sat on a big ______ by the river.  ／  I like ______ music.', 'opts': ['stone', 'rock', 'pop', 'tree'], 'answer': 1, 'exp': 'rock 石頭／搖滾樂。'},
  ]},
  {'title': '③ 易混淆字：選出正確的字', 'items': [
    {'type': 'mc', 'q': 'Nice to ______ you, Ms. Lin.', 'opts': ['meat', 'meet', 'met', 'make'], 'answer': 1, 'exp': '認識你 → meet。'},
    {'type': 'mc', 'q': 'My brother is taller ______ me.', 'opts': ['then', 'than', 'that', 'as'], 'answer': 1, 'exp': '比較級 + than。'},
    {'type': 'mc', 'q': 'Please ______ to the teacher carefully.', 'opts': ['hear', 'listen', 'sound', 'heard'], 'answer': 1, 'exp': 'listen to 專心聽。'},
    {'type': 'mc', 'q': 'Your idea ______ great!', 'opts': ['sounds', 'listens', 'hears', 'is sounding'], 'answer': 0, 'exp': 'sound + 形容詞：聽起來。'},
    {'type': 'mc', 'q': 'There is ______ milk in the bottle. Can you buy some more?', 'opts': ['few', 'little', 'a few', 'many'], 'answer': 1, 'exp': 'milk 不可數，幾乎沒有 → little。'},
    {'type': 'mc', 'q': 'I have ______ cookies. Do you want one?', 'opts': ['a few', 'a little', 'few', 'little'], 'answer': 0, 'exp': 'cookies 可數，還有一些 → a few。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'It\'s my turn to do the {0} tonight. （碗盤）', 'blanks': [['dishes']], 'exp': 'do the dishes 洗碗。'},
    {'q': 'Raise your {0} if you have a question. （手）', 'blanks': [['hand']], 'exp': 'raise one\'s hand 舉手。'},
    {'q': 'We need to get {0} the bus at the next stop. （下車）', 'blanks': [['off']], 'exp': 'get off 下車。'},
    {'q': 'The school is trying to {0} money for the library. （募集）', 'blanks': [['raise']], 'exp': 'raise money 募款。'},
    {'q': 'Taiwan is {0} for its bubble tea. （有名的）', 'blanks': [['famous']], 'exp': 'be famous for 因…有名。'},
    {'q': 'It is {0} to play with fire. （危險的）', 'blanks': [['dangerous']], 'exp': 'danger + -ous = dangerous。'},
  ]},
]
