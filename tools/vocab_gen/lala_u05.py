# LaLa Word Unit 5（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 51–60 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 5, 'en': 'A Small Mask, A Big Change', 'zh': '一字多義（五）',
  'intro': 'mask 是面具，也是口罩；chicken 是雞，也可以笑人「膽小鬼」。這個單元有 4 個主題單字、14 個更多單字，'
           '最後整理都是「很多」的 many／much／a lot of。',
  'words': [
    W('chicken', '🐔', [
        S('n.', '雞', 'Grandma keeps ten chickens on her farm.', '奶奶的農場養了十隻雞。'),
        S('n.', '雞肉', 'I\'d like chicken rice, please.', '我要一份雞肉飯。'),
        S('n.', '膽小鬼', 'Come on, jump in! Don\'t be a chicken.', '快跳下來！別當膽小鬼。'),
    ], '複數 chickens', key=True),
    W('dark', '🌃', [
        S('adj.', '天黑的；昏暗的', 'It gets dark early in winter.', '冬天天黑得早。'),
        S('adj.', '深色的', 'He is wearing a dark blue jacket.', '他穿著一件深藍色外套。'),
        S('n.', '天黑', 'Come home before dark.', '天黑前回家。'),
        S('n.', '黑暗', 'My little sister is afraid of the dark.', '我妹妹怕黑。', 'in the dark 在黑暗中；被蒙在鼓裡'),
    ], 'dark - darker - darkest', key=True),
    W('bright', '☀️', [
        S('adj.', '明亮的；鮮豔的', 'The sun is very bright today.', '今天陽光很亮。'),
        S('adj.', '聰明的', 'Lily is a bright student.', 'Lily 是個聰明的學生。', '(as) bright as a button 非常聰明'),
        S('adj.', '樂觀的；開心的', 'Always look on the bright side.', '凡事要往好處想。', 'look on the bright side 往好處想'),
    ], 'bright - brighter - brightest', key=True),
    W('mask', '😷', [
        S('n.', '面具', 'The kids wore animal masks at the party.', '孩子們在派對上戴動物面具。'),
        S('n.', '口罩', 'Please wear a mask on the bus.', '搭公車請戴口罩。'),
        S('n.', '掩飾', 'His smile was a mask. He was really sad.', '他的微笑只是掩飾，他其實很難過。'),
    ], '複數 masks', key=True),
    W('glass', '🥛', [
        S('n.', '玻璃', 'The window is made of glass.', '窗戶是玻璃做的。'),
        S('n.', '玻璃杯', 'Can I have a glass of water?', '可以給我一杯水嗎？', 'a glass of 一杯'),
        S('n.', '眼鏡（glasses）', 'I can\'t see well without my glasses.', '沒戴眼鏡我看不清楚。'),
    ], '複數 glasses'),
    W('hot', '🌶️', [
        S('adj.', '熱的', 'It\'s so hot today. Let\'s go swimming.', '今天好熱，我們去游泳吧。'),
        S('adj.', '辣的', 'This curry is too hot for me.', '這個咖哩對我來說太辣了。'),
        S('adj.', '熱門的', 'This game is the hot new toy this year.', '這個遊戲是今年最熱門的新玩具。'),
    ], 'hot - hotter - hottest'),
    W('kid', '🧒', [
        S('n.', '小孩', 'The kids are playing in the park.', '孩子們在公園玩。'),
        S('n.', '年輕人', 'He was just a kid when he started his company.', '他開公司的時候還只是個年輕人。'),
        S('v.', '開玩笑', 'I\'m just kidding. Don\'t be angry.', '我只是開玩笑，別生氣。'),
        S('v.', '嘲笑；拿…開玩笑', 'My brother always kids me about my short hair.', '我哥哥老是拿我的短髮開玩笑。', 'kid + 人 + about 拿…開某人玩笑'),
    ], 'kid - kidded - kidded - kidding'),
    W('last', '🔚', [
        S('adj.', '上一個的', 'I went to Kenting last summer.', '我去年夏天去墾丁。', 'last night / week / year 昨晚／上週／去年'),
        S('adj.', '最後的', 'December is the last month of the year.', '十二月是一年的最後一個月。', 'last name 姓'),
        S('adj.', '最不可能的', 'He is the last person to tell a lie.', '他是最不可能說謊的人。'),
        S('v.', '持續；維持', 'The rain lasted for three days.', '雨下了三天。'),
    ], 'last - lasted - lasted - lasting'),
    W('milk', '🥛', [
        S('n.', '牛奶；奶', 'I drink a glass of milk every morning.', '我每天早上喝一杯牛奶。'),
        S('n.', '（植物的）白色汁液', 'Soy milk is popular in Taiwan.', '豆漿在臺灣很受歡迎。', 'soy milk 豆漿；coconut milk 椰奶'),
        S('v.', '擠奶', 'The farmer milks the cows every morning.', '農夫每天早上擠牛奶。'),
        S('v.', '榨取（利益）', 'Some shops milk tourists for money.', '有些店家專門坑觀光客的錢。'),
    ], 'milk - milked - milked - milking'),
    W('part', '🧩', [
        S('n.', '部分', 'Part of the cake is gone.', '蛋糕少了一部分。', 'in part 部分地'),
        S('n.', '零件', 'The car needs some new parts.', '這輛車需要一些新零件。'),
        S('n.', '角色', 'Tom played the part of the king in the play.', 'Tom 在戲裡演國王。'),
        S('v.', '分開；離別', 'The two friends parted at the train station.', '兩個朋友在火車站分別。'),
    ], 'part - parted - parted - parting'),
    W('plate', '🍽️', [
        S('n.', '盤子；一盤', 'She ate a plate of fried noodles.', '她吃了一盤炒麵。', 'a plate of 一盤…'),
        S('n.', '板子；車牌', 'Can you see the car\'s license plate?', '你看得到那台車的車牌嗎？', 'license plate 車牌'),
        S('v.', '裝盤', 'The chef plated the steak with some vegetables.', '主廚把牛排和蔬菜一起裝盤。'),
    ], 'plate - plated - plated - plating'),
    W('shop', '🏪', [
        S('v.', '購物；買東西', 'Mom shops for food every Saturday.', '媽媽每週六去買菜。', 'shop for 購買；window-shopping 逛街只看不買'),
        S('n.', '商店', 'There is a coffee shop near my school.', '我學校附近有一家咖啡店。'),
        S('n.', '工作坊；修理廠', 'Dad took the car to the shop.', '爸爸把車送去修車廠。'),
    ], 'shop - shopped - shopped - shopping'),
    W('show', '🎭', [
        S('v.', '給…看；展示', 'Show me your new phone.', '給我看你的新手機。', 'show + 人 + 物 = show + 物 + to + 人'),
        S('v.', '顯示；證明', 'The test shows that you studied hard.', '這次考試證明你很用功。'),
        S('v.', '出現（show up）', 'He didn\'t show up for the party.', '他沒有出現在派對上。', 'show up 出現'),
        S('n.', '節目；表演', 'My favorite TV show starts at eight.', '我最愛的電視節目八點開始。'),
        S('n.', '展覽', 'We went to a car show last weekend.', '我們上週末去看車展。'),
    ], 'show - showed - shown（showed） - showing'),
    W('sick', '🤒', [
        S('adj.', '生病的', 'I can\'t go to school. I\'m sick.', '我不能去上學，我生病了。'),
        S('adj.', '想吐的；噁心的', 'I feel sick on long bus rides.', '坐長途公車我會想吐。', 'carsick 暈車；seasick 暈船；homesick 想家'),
        S('n.', '病假', 'Ms. Lin is on sick leave today.', '林老師今天請病假。', 'on sick leave 請病假'),
        S('n.', '病人（the sick）', 'Doctors and nurses take care of the sick.', '醫生和護理師照顧病人。'),
    ], 'sick - sicker - sickest'),
    W('still', '🧘', [
        S('adv.', '仍然；還', 'Are you still hungry?', '你還餓嗎？'),
        S('adv.', '儘管如此', 'It rained hard. Still, we had fun.', '雨下得很大，但我們還是玩得很開心。'),
        S('adv.', '更加', 'The second test was still harder.', '第二次考試更難。'),
        S('adj.', '靜止的', 'Sit still and listen.', '坐好別動，注意聽。', 'keep / stay still 保持不動'),
    ]),
    W('sweet', '🍭', [
        S('adj.', '甜的', 'This watermelon is very sweet.', '這顆西瓜很甜。', 'have a sweet tooth 愛吃甜食'),
        S('adj.', '貼心的', 'It\'s sweet of you to help me.', '你幫我真貼心。'),
        S('adj.', '美好的', 'Winning the game felt so sweet.', '贏得比賽的感覺真美好。'),
        S('n.', '糖果', 'Don\'t eat too many sweets.', '不要吃太多糖果。'),
    ], 'sweet - sweeter - sweetest'),
    W('thirsty', '🥤', [
        S('adj.', '口渴的', 'I\'m thirsty. Can I have some water?', '我口渴了，可以喝點水嗎？'),
        S('adj.', '渴望的', 'The boy is thirsty for his parents\' love.', '那個男孩渴望父母的愛。', 'be thirsty for 渴望'),
    ], 'thirsty - thirstier - thirstiest'),
    W('water', '💧', [
        S('n.', '水', 'Drink more water on hot days.', '天氣熱要多喝水。'),
        S('n.', '水域（waters）', 'Many fish live in these waters.', '很多魚住在這片水域。'),
        S('v.', '澆水', 'Can you water the plants for me?', '你可以幫我澆花嗎？'),
        S('v.', '流口水', 'The smell of the food made my mouth water.', '食物的香味讓我流口水。'),
        S('v.', '流眼淚', 'Cutting onions makes my eyes water.', '切洋蔥讓我流眼淚。'),
    ], 'water - watered - watered - watering'),
  ],
  'focus': [
    {'title': '易混淆字：都是「很多」', 'head': ('單字', '用法', '例句'), 'rows': [
      ('many', '接可數名詞（複數）；比較級 more、最高級 most', 'How many apples do you want?'),
      ('much', '接不可數名詞；也可以修飾動詞、比較級', 'How much milk is there?／It\'s much hotter today.'),
      ('a lot of', '可數、不可數都可以接（＝ lots of）', 'I have a lot of homework.'),
      ('a lot', '副詞，放在動詞後面', 'She talks a lot.'),
    ], 'note': '否定句、疑問句常用 many／much；肯定句口語常用 a lot of。'},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('chicken', '雞；雞肉', '膽小鬼'),
      ('mask', '面具；口罩', '掩飾'),
      ('bright', '明亮的', '聰明的'),
      ('glass', '玻璃；玻璃杯', 'glasses 眼鏡'),
      ('hot', '熱的', '辣的；熱門的'),
      ('kid', '小孩', '開玩笑'),
      ('last', '最後的', '持續'),
      ('part', '部分', '角色；分開'),
      ('still', '仍然', '靜止的'),
      ('water', '水', '澆水；流口水'),
    ], 'note': ''},
    {'title': '常用片語', 'head': ('片語', '意思', '例句'), 'rows': [
      ('in the dark', '在黑暗中；被蒙在鼓裡', 'Nobody told me. I was in the dark.'),
      ('look on the bright side', '往好處想', 'Look on the bright side. You learned a lot.'),
      ('just kidding', '開玩笑的', 'I\'m just kidding!'),
      ('show up', '出現', 'She showed up at ten.'),
      ('have a sweet tooth', '愛吃甜食', 'My dad has a sweet tooth.'),
      ('stay still', '保持不動', 'Stay still for the photo.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'Jump! Don\'t be such a <b>chicken</b>.', 'opts': ['雞', '雞肉', '膽小鬼', '小孩'], 'answer': 2, 'exp': '叫人別怕 → 膽小鬼。'},
    {'type': 'mc', 'q': 'Jenny is a <b>bright</b> girl. She learns everything fast.', 'opts': ['明亮的', '聰明的', '鮮豔的', '開心的'], 'answer': 1, 'exp': '學得快 → 聰明的。'},
    {'type': 'mc', 'q': 'This soup is too <b>hot</b>. I put too much pepper in it.', 'opts': ['熱的', '辣的', '熱門的', '甜的'], 'answer': 1, 'exp': '放太多胡椒 → 辣的。'},
    {'type': 'mc', 'q': 'The movie <b>lasted</b> three hours.', 'opts': ['最後', '上一次', '持續', '最不可能'], 'answer': 2, 'exp': 'last 動詞：持續。'},
    {'type': 'mc', 'q': 'Ben got the <b>part</b> of the wolf in the school play.', 'opts': ['部分', '零件', '角色', '分開'], 'answer': 2, 'exp': '在戲裡演狼 → 角色。'},
    {'type': 'mc', 'q': 'I feel <b>sick</b>. I think I ate too much.', 'opts': ['想吐的', '病假', '病人', '想家的'], 'answer': 0, 'exp': '吃太多 → 想吐。'},
    {'type': 'mc', 'q': 'Please sit <b>still</b> while I cut your hair.', 'opts': ['仍然', '儘管如此', '更加', '靜止不動'], 'answer': 3, 'exp': 'sit still 坐著不動。'},
    {'type': 'mc', 'q': 'Thanks for the card. It\'s so <b>sweet</b> of you.', 'opts': ['甜的', '貼心的', '糖果', '美好的'], 'answer': 1, 'exp': 'It\'s sweet of you. 你真貼心。'},
    {'type': 'mc', 'q': 'The smell of fried chicken made my mouth <b>water</b>.', 'opts': ['水', '澆水', '流口水', '流眼淚'], 'answer': 2, 'exp': 'make one\'s mouth water 讓人流口水。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'She drank a ______ of orange juice.  ／  Grandpa needs his ______es to read.', 'opts': ['cup', 'glass', 'bottle', 'mask'], 'answer': 1, 'exp': 'a glass of 一杯／glasses 眼鏡。'},
    {'type': 'mc', 'q': 'Wear a ______ when you have a cold.  ／  The thief wore a black ______.', 'opts': ['hat', 'mask', 'coat', 'glove'], 'answer': 1, 'exp': 'mask 口罩／面具。'},
    {'type': 'mc', 'q': 'Can you ______ me the way to the station?  ／  We watched a magic ______.', 'opts': ['tell', 'show', 'play', 'film'], 'answer': 1, 'exp': 'show 指給…看／表演。'},
    {'type': 'mc', 'q': 'December is the ______ month of the year.  ／  How long will the meeting ______?', 'opts': ['final', 'end', 'last', 'take'], 'answer': 2, 'exp': 'last 最後的／持續。'},
    {'type': 'mc', 'q': 'Please ______ the flowers.  ／  I\'m thirsty. Can I have some ______?', 'opts': ['milk', 'water', 'juice', 'wash'], 'answer': 1, 'exp': 'water 澆水／水。'},
  ]},
  {'title': '③ 易混淆字：many／much／a lot of／a lot', 'items': [
    {'type': 'mc', 'q': 'How ______ students are in your class?', 'opts': ['much', 'many', 'a lot', 'lot of'], 'answer': 1, 'exp': 'students 可數 → many。'},
    {'type': 'mc', 'q': 'We don\'t have ______ time. Hurry up!', 'opts': ['many', 'much', 'a lot', 'lots'], 'answer': 1, 'exp': 'time 不可數 → much。'},
    {'type': 'mc', 'q': 'He eats ______. He is always hungry.', 'opts': ['a lot', 'a lot of', 'many', 'much of'], 'answer': 0, 'exp': '放在動詞後面 → a lot。'},
    {'type': 'mc', 'q': 'Today is ______ colder than yesterday.', 'opts': ['many', 'much', 'a lot of', 'more'], 'answer': 1, 'exp': 'much + 比較級：…得多。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Come home before {0}. （天黑）', 'blanks': [['dark']], 'exp': 'before dark 天黑以前。'},
    {'q': 'I\'m just {0}. Don\'t be angry. （開玩笑）', 'blanks': [['kidding']], 'exp': 'just kidding 開玩笑的。'},
    {'q': 'Mom went to the market to {0} for vegetables. （購物）', 'blanks': [['shop']], 'exp': 'shop for 購買。'},
    {'q': 'After the long run, I was very {0}. （口渴的）', 'blanks': [['thirsty']], 'exp': 'thirsty 口渴的。'},
    {'q': 'He didn\'t show {0} at the meeting. （出現）', 'blanks': [['up']], 'exp': 'show up 出現。'},
    {'q': 'We ordered a {0} of dumplings. （一盤）', 'blanks': [['plate']], 'exp': 'a plate of 一盤。'},
  ]},
]
