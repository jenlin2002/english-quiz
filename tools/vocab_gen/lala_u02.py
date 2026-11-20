# LaLa Word Unit 2（一字多義：字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本：115[翰林]國中英語 LaLa Word 小單字大視野（學用）PDF 印刷頁第 20–32 頁（PDF 頁序＝印刷頁碼－1）
# S(詞性, 中文, 例句, 例句中文, 片語)；W(單字, emoji, [意思…], 變化形, key=主題單字)

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 2, 'en': 'The Secret Clothes of Animals', 'zh': '一字多義（二）',
  'intro': '變色龍會「turn」green（變成綠色），不是「轉」綠色；party 除了派對還有「政黨」，fan 除了「粉絲」還是「電扇」。'
           '這個單元有 8 個主題單字、14 個更多單字，最後整理容易搞混的 look／watch／see／read。',
  'words': [
    W('time', '⏰', [
        S('n.', '時間；時光', 'Time flies when you are having fun.', '玩得開心時，時間過得特別快。', 'time flies 時光飛逝；take your time 慢慢來'),
        S('n.', '時刻；幾點', 'What time does the movie start?', '電影幾點開始？', 'Do you have the time? 現在幾點？'),
        S('n.', '（做某事的）時候', 'It\'s time to go to bed.', '該上床睡覺了。', 'It\'s time to… 該…了；on time 準時；in time 及時'),
        S('n.', '次；次數', 'I have been to Tainan three times.', '我去過臺南三次。', 'last time 上一次；next time 下一次'),
        S('v.', '計時', 'Can you time me when I swim?', '我游泳的時候你可以幫我計時嗎？'),
        S('prep.', '乘以（times）', 'Three times four is twelve.', '三乘以四等於十二。'),
    ], 'time - timed - timed - timing', key=True),
    W('turn', '↪️', [
        S('v.', '變成', 'The leaves turn yellow in autumn.', '秋天葉子變黃了。'),
        S('v.', '扭動（開關）', 'Please turn off the lights when you leave.', '離開時請關燈。', 'turn on 打開；turn off 關掉'),
        S('v.', '（使）轉身；轉向', 'She turned and smiled at me.', '她轉過身對我微笑。'),
        S('n.', '轉彎', 'Make a left turn at the bank.', '在銀行那裡左轉。', 'make a right / left turn 右轉／左轉'),
        S('n.', '輪到的機會', 'It\'s your turn to clean the board.', '輪到你擦黑板了。', 'take turns + V-ing 輪流'),
    ], 'turn - turned - turned - turning', key=True),
    W('magic', '🎩', [
        S('n.', '魔法；魔術', 'The witch used magic to turn the frog into a prince.', '女巫用魔法把青蛙變成王子。', 'work like magic 效果神奇'),
        S('n.', '魅力；神奇的力量', 'I love the magic of the night market.', '我愛夜市那種迷人的魅力。'),
        S('adj.', '有魔力的；魔術的', 'My uncle can do a magic trick with cards.', '我叔叔會用撲克牌變魔術。', 'magic trick 魔術'),
    ], key=True),
    W('party', '🎉', [
        S('n.', '派對；社交聚會', 'We are going to have a party for Mom\'s birthday.', '我們要為媽媽的生日辦一個派對。', 'have / throw a party 辦派對'),
        S('n.', '政黨', 'Which party will win the election?', '哪一個政黨會贏得選舉？'),
        S('v.', '狂歡；開派對', 'After the final exam, the students partied all night.', '期末考完後，學生們狂歡了一整晚。'),
    ], 'party - partied - partied - partying；複數 parties', key=True),
    W('use', '🛠️', [
        S('v.', '使用', 'May I use your phone?', '我可以用你的手機嗎？', 'use up 用完'),
        S('v.', '利用（別人）', 'He is not your friend. He is just using you.', '他不是你的朋友，他只是在利用你。'),
        S('v.', '說；寫（語言、字詞）', 'Don\'t use bad words.', '不要說髒話。'),
        S('n.', '使用', 'The elevator is out of use today.', '電梯今天停用。', 'out of use 停用；make use of 利用'),
        S('n.', '用途', 'Bamboo has many uses.', '竹子有很多用途。'),
    ], 'use - used - used - using', key=True),
    W('safe', '🔒', [
        S('adj.', '安全的', 'It\'s not safe to swim in this river.', '在這條河游泳不安全。'),
        S('adj.', '可靠的；謹慎的', 'Dad is a safe driver.', '爸爸開車很謹慎。'),
        S('adj.', '平安的；沒受傷的', 'The lost boy came home safe and sound.', '走失的男孩平安無事地回家了。', 'safe and sound 安然無恙'),
        S('n.', '保險箱', 'Grandma keeps her gold in a safe.', '奶奶把她的金子放在保險箱裡。'),
    ], 'safe - safer - safest；副詞 safely', key=True),
    W('walk', '🚶', [
        S('v.', '走路；步行', 'I walk to school every day.', '我每天走路上學。', 'walk away 走開'),
        S('v.', '遛（狗）', 'It\'s my job to walk the dog after dinner.', '晚餐後遛狗是我的工作。'),
        S('n.', '散步', 'Let\'s go for a walk in the park.', '我們去公園散步吧。', 'go for / take a walk 散步'),
        S('n.', '步行的路程', 'The MRT station is a ten-minute walk from here.', '捷運站離這裡走路十分鐘。'),
    ], 'walk - walked - walked - walking', key=True),
    W('picture', '🖼️', [
        S('n.', '圖畫', 'Kevin drew a picture of his family.', 'Kevin 畫了一張他家人的圖。', 'draw a picture of 畫一張…的圖'),
        S('n.', '照片', 'Can you take a picture of us?', '你可以幫我們拍一張照片嗎？', 'take a picture 拍照'),
        S('n.', '情況；了解', 'OK, I get the picture now.', '好，我現在懂了。', 'get the picture 了解情況'),
        S('v.', '想像', 'Picture yourself on a sunny beach.', '想像你自己在陽光燦爛的海灘上。'),
    ], 'picture - pictured - pictured - picturing', key=True),
    W('all', '💯', [
        S('pron.', '全部；所有', 'All of my friends came to my party.', '我所有的朋友都來參加我的派對。', 'all day 整天；all the time 一直'),
        S('adv.', '完全地', 'The dog got mud all over its body.', '狗弄得全身都是泥巴。', 'all alone 孤零零地；not… at all 一點也不'),
    ]),
    W('band', '🎸', [
        S('n.', '樂團', 'My cousin plays the drums in a band.', '我表哥在樂團裡打鼓。'),
        S('n.', '帶子；橡皮筋', 'She tied her hair with a rubber band.', '她用橡皮筋綁頭髮。', 'rubber band 橡皮筋'),
    ], '複數 bands'),
    W('can', '🥫', [
        S('aux.', '能；會', 'Can you ride a bike?', '你會騎腳踏車嗎？'),
        S('aux.', '可以（允許）', 'You can go out after you finish your homework.', '寫完功課你就可以出去。'),
        S('aux.', '可以…嗎（請求）', 'Could you pass me the salt?', '可以請你把鹽遞給我嗎？'),
        S('aux.', '有可能', 'It can be very cold here in winter.', '這裡冬天可能會很冷。'),
        S('n.', '罐頭；金屬罐', 'Please put the empty cans in the recycling bin.', '請把空罐子放進回收桶。'),
        S('v.', '把…裝罐', 'This factory cans tuna.', '這家工廠生產鮪魚罐頭。'),
    ], '助動詞過去式 could；動詞 can - canned - canned - canning'),
    W('class', '🏫', [
        S('n.', '班級；全班同學', 'There are 28 students in our class.', '我們班有 28 個學生。'),
        S('n.', '課；課程', 'We have a P.E. class this afternoon.', '我們今天下午有體育課。'),
        S('n.', '（車、機艙）等級', 'It costs a lot to fly first class.', '搭頭等艙很貴。'),
        S('n.', '社會階級', 'Many people in the working class work long hours.', '許多勞工階級的人工時很長。'),
    ], '複數 classes'),
    W('fan', '🪭', [
        S('n.', '狂熱愛好者；迷', 'My sister is a big fan of that singer.', '我姊姊是那位歌手的超級粉絲。', 'a big fan of 是…的大粉絲'),
        S('n.', '扇子；電風扇', 'It\'s hot. Can you turn on the fan?', '好熱。你可以開電風扇嗎？'),
        S('v.', '搧（風）', 'She fanned her face with a book.', '她用書搧臉。'),
    ], 'fan - fanned - fanned - fanning'),
    W('fight', '🥊', [
        S('v.', '打架；吵架；打仗', 'My two little brothers often fight over toys.', '我的兩個弟弟常常為了玩具吵架。', 'fight against 對抗；fight for 爭取'),
        S('n.', '打鬥；戰鬥', 'Two cats had a fight in the yard.', '兩隻貓在院子裡打了一架。'),
    ], 'fight - fought - fought - fighting'),
    W('free', '🆓', [
        S('adj.', '免費的', 'The drinks are free today.', '今天飲料免費。'),
        S('adj.', '有空的', 'Are you free this Sunday?', '你這個星期天有空嗎？', 'free time 空閒時間'),
        S('adj.', '自由的', 'The bird is free now. It can fly anywhere.', '這隻鳥現在自由了，牠可以飛到任何地方。', 'feel free to 儘管'),
        S('adj.', '沒有…的', 'This cake is sugar-free.', '這個蛋糕不含糖。', 'free of / from 沒有…的'),
        S('v.', '釋放', 'They freed the fish back into the sea.', '他們把魚放回海裡。'),
    ], 'free - freed - freed - freeing'),
    W('hand', '✋', [
        S('n.', '手；（鐘錶的）指針', 'The hour hand is on the six.', '時針指在六。'),
        S('n.', '幫忙', 'Can you give me a hand with these boxes?', '你可以幫我搬這些箱子嗎？', 'give / lend + 人 + a hand 幫忙'),
        S('n.', '掌聲', 'Let\'s give her a big hand!', '我們給她熱烈的掌聲！', 'give a big hand 鼓掌'),
        S('v.', '遞給；交', 'Please hand in your homework tomorrow.', '請明天交作業。', 'hand in 繳交'),
    ], 'hand - handed - handed - handing'),
    W('place', '📍', [
        S('n.', '地點；地方', 'This is a nice place for a picnic.', '這是野餐的好地方。'),
        S('n.', '名次', 'Amy won first place in the race.', 'Amy 賽跑得第一名。'),
        S('v.', '放置', 'Place the cup on the table, please.', '請把杯子放在桌上。'),
        S('v.', '舉行；發生（take place）', 'The concert will take place in the park.', '音樂會將在公園舉行。', 'take place 舉行；發生'),
        S('v.', '下（訂單）', 'I placed an order for two pizzas.', '我訂了兩個披薩。', 'place an order 下訂單'),
    ], 'place - placed - placed - placing'),
    W('please', '🙏', [
        S('int.', '請；拜託', 'Please close the door.', '請關門。'),
        S('int.', '好的，謝謝（接受時）', 'A: More juice?  B: Yes, please.', 'A：還要果汁嗎？ B：好，謝謝。'),
        S('v.', '使高興；取悅', 'It\'s hard to please everyone.', '要讓每個人都滿意很難。'),
    ], 'please - pleased - pleased - pleasing'),
    W('rule', '📏', [
        S('n.', '規則；習慣', 'Don\'t break the school rules.', '不要違反校規。', 'follow / break the rules 遵守／違反規則；make it a rule to 習慣'),
        S('n.', '經驗法則（a rule of thumb）', 'As a rule of thumb, drink eight glasses of water a day.', '一般來說，一天要喝八杯水。', 'a rule of thumb 經驗法則'),
        S('v.', '統治', 'The king ruled the country for forty years.', '國王統治這個國家四十年。'),
        S('v.', '支配；控制', 'Don\'t let your phone rule your life.', '別讓手機控制你的生活。'),
    ], 'rule - ruled - ruled - ruling'),
    W('shake', '🥤', [
        S('v.', '搖動；震動', 'The house shook during the earthquake.', '地震時房子在搖晃。', 'shake one\'s head 搖頭；shake hands 握手'),
        S('v.', '發抖', 'He was shaking with cold.', '他冷得發抖。', 'shake like a leaf 抖個不停'),
        S('v.', '擺脫（shake off）', 'I can\'t shake off this cold.', '我這個感冒一直好不了。', 'shake off 擺脫'),
        S('n.', '奶昔', 'I\'d like a chocolate shake, please.', '我要一杯巧克力奶昔。'),
    ], 'shake - shook - shaken - shaking'),
    W('study', '📚', [
        S('v.', '讀書；學習', 'She is studying for the test.', '她在準備考試。'),
        S('v.', '仔細研究', 'The scientist studies how bees talk to each other.', '這位科學家研究蜜蜂怎麼互相溝通。'),
        S('n.', '研究；調查', 'A new study shows that sleep helps memory.', '一項新研究顯示睡眠有助於記憶。'),
        S('n.', '書房', 'Dad is reading in his study.', '爸爸在書房看書。'),
    ], 'study - studied - studied - studying；複數 studies'),
    W('with', '🤝', [
        S('prep.', '和…一起', 'I went to the zoo with my cousins.', '我和表兄弟姊妹去動物園。'),
        S('prep.', '用（工具）', 'He cut the paper with scissors.', '他用剪刀剪紙。'),
        S('prep.', '有；帶著', 'Who is the girl with long hair?', '那個長頭髮的女孩是誰？'),
        S('prep.', '對於', 'Be careful with the knife.', '用刀子要小心。'),
        S('prep.', '支持；站在…這邊', 'Don\'t worry. I\'m with you.', '別擔心，我支持你。'),
    ]),
  ],
  'focus': [
    {'title': '易混淆字：都是「看」，有什麼不同？', 'head': ('單字', '用法', '例句'), 'rows': [
      ('look', '有意地把視線轉過去，常接 at；也可以當「看起來」＋形容詞', 'Look at the rainbow!／You look tired.'),
      ('watch', '專注地看一段時間（電視、比賽、會動的東西）', 'We watched a baseball game on TV.'),
      ('see', '不是刻意去看，自然「看到」；也表示「看得見」', 'I saw a cat on the roof.／I can\'t see the board.'),
      ('read', '看「文字」並了解意思（書、報紙、標誌）；也可以讀出別人的心思', 'She reads the news every morning.'),
    ], 'note': 'watch、see 後面可以接「受詞＋原形動詞／V-ing」：I saw him cross the street.／We watched the kids playing.'},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('turn', '轉彎；轉動', '變成；輪到'),
      ('party', '派對', '政黨'),
      ('safe', '安全的', '保險箱'),
      ('can', '能；會', '罐頭'),
      ('fan', '粉絲', '電扇；搧風'),
      ('free', '免費的', '有空的；不含…的'),
      ('hand', '手', '指針；幫忙；掌聲'),
      ('shake', '搖動', '奶昔'),
      ('study', '讀書', '書房；研究'),
    ], 'note': ''},
    {'title': '常用片語', 'head': ('片語', '意思', '例句'), 'rows': [
      ('take turns + V-ing', '輪流', 'We take turns washing the dishes.'),
      ('take place', '舉行；發生', 'The game took place last Friday.'),
      ('give + 人 + a hand', '幫某人忙', 'Can you give me a hand?'),
      ('hand in', '繳交', 'Hand in your test papers now.'),
      ('feel free to', '儘管…', 'Feel free to ask questions.'),
      ('safe and sound', '安然無恙', 'They got home safe and sound.'),
      ('out of use', '停用', 'This old road is out of use.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'The sky <b>turned</b> dark, and it started to rain.', 'opts': ['轉身', '變成', '輪到', '轉彎'], 'answer': 1, 'exp': 'turn + 形容詞：變成。'},
    {'type': 'mc', 'q': 'Mom keeps her rings in a <b>safe</b>.', 'opts': ['安全的', '盒子', '保險箱', '抽屜'], 'answer': 2, 'exp': 'a safe 名詞：保險箱。'},
    {'type': 'mc', 'q': 'It\'s hot in here. Let\'s turn on the <b>fan</b>.', 'opts': ['粉絲', '電扇', '燈', '音樂'], 'answer': 1, 'exp': 'turn on the fan 開電扇。'},
    {'type': 'mc', 'q': 'Are you <b>free</b> tomorrow afternoon? Let\'s go shopping.', 'opts': ['免費的', '自由的', '有空的', '不含…的'], 'answer': 2, 'exp': '問有沒有空 → 有空的。'},
    {'type': 'mc', 'q': 'The minute <b>hand</b> of the clock is broken.', 'opts': ['手', '指針', '幫忙', '掌聲'], 'answer': 1, 'exp': 'minute hand 分針。'},
    {'type': 'mc', 'q': 'The two <b>parties</b> don\'t agree on the new law.', 'opts': ['派對', '政黨', '朋友', '班級'], 'answer': 1, 'exp': '對法律有意見 → 政黨。'},
    {'type': 'mc', 'q': 'Grandpa is reading the newspaper in his <b>study</b>.', 'opts': ['研究', '課程', '書房', '學習'], 'answer': 2, 'exp': 'in his study 在他的書房。'},
    {'type': 'mc', 'q': 'I\'d like a strawberry <b>shake</b> and some fries.', 'opts': ['搖晃', '奶昔', '蛋糕', '握手'], 'answer': 1, 'exp': '點餐 → 奶昔。'},
    {'type': 'mc', 'q': 'OK, I get the <b>picture</b>. You don\'t need to explain again.', 'opts': ['照片', '圖畫', '情況；了解', '想像'], 'answer': 2, 'exp': 'get the picture 了解情況。'},
    {'type': 'mc', 'q': 'Our team won second <b>place</b> in the singing contest.', 'opts': ['地方', '名次', '座位', '舉行'], 'answer': 1, 'exp': 'second place 第二名。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'I\'m a big ______ of Jay Chou.  ／  It\'s so hot. Please turn on the ______.', 'opts': ['fan', 'friend', 'light', 'band'], 'answer': 0, 'exp': 'fan 粉絲／電扇。'},
    {'type': 'mc', 'q': 'My brother sings in a rock ______.  ／  Put a rubber ______ around the cards.', 'opts': ['group', 'band', 'ring', 'class'], 'answer': 1, 'exp': 'band 樂團／橡皮筋。'},
    {'type': 'mc', 'q': 'Please open this ______ of beans.  ／  ______ you help me with my homework?', 'opts': ['box', 'Will', 'can', 'bag'], 'answer': 2, 'exp': 'can 罐頭／能夠。'},
    {'type': 'mc', 'q': 'It\'s your ______ to sing.  ／  ______ right at the next corner.', 'opts': ['time', 'Go', 'turn', 'walk'], 'answer': 2, 'exp': 'turn 輪到／轉彎。'},
    {'type': 'mc', 'q': 'Two times three is six. Let\'s try one more ______.  ／  What ______ is it now?', 'opts': ['time', 'hour', 'turn', 'clock'], 'answer': 0, 'exp': 'time 次數／時間。'},
    {'type': 'mc', 'q': 'The park is a five-minute ______ from my house.  ／  Let\'s go for a ______ after dinner.', 'opts': ['ride', 'walk', 'run', 'trip'], 'answer': 1, 'exp': 'a five-minute walk 走路五分鐘／go for a walk 散步。'},
  ]},
  {'title': '③ 易混淆字：look／watch／see／read', 'items': [
    {'type': 'mc', 'q': '______ at that cute puppy!', 'opts': ['Look', 'Watch', 'See', 'Read'], 'answer': 0, 'exp': 'look at 看向某物。'},
    {'type': 'mc', 'q': 'We ______ a movie last night.', 'opts': ['looked', 'watched', 'read', 'saw at'], 'answer': 1, 'exp': '專注看電影一段時間 → watch。'},
    {'type': 'mc', 'q': 'I can\'t ______ anything. It\'s too dark.', 'opts': ['look', 'watch', 'see', 'read'], 'answer': 2, 'exp': '看得見 → see。'},
    {'type': 'mc', 'q': 'Can you ______ the sign? What does it say?', 'opts': ['look', 'watch', 'see at', 'read'], 'answer': 3, 'exp': '看文字並了解 → read。'},
    {'type': 'mc', 'q': 'You ______ happy today. Any good news?', 'opts': ['look', 'watch', 'see', 'read'], 'answer': 0, 'exp': 'look + 形容詞：看起來。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'The festival will take {0} in May. （舉行）', 'blanks': [['place']], 'exp': 'take place 舉行。'},
    {'q': 'Please hand {0} your reports by Friday. （繳交）', 'blanks': [['in']], 'exp': 'hand in 繳交。'},
    {'q': 'We take {0} feeding the fish. （輪流）', 'blanks': [['turns']], 'exp': 'take turns + V-ing 輪流。'},
    {'q': 'The two boys {0} on the playground yesterday. （打架，過去式）', 'blanks': [['fought']], 'exp': 'fight 的過去式 fought。'},
    {'q': 'The dog was {0} like a leaf during the storm. （發抖）', 'blanks': [['shaking']], 'exp': 'shake like a leaf 抖個不停。'},
    {'q': 'After the storm, everyone got home safe and {0}. （安然無恙）', 'blanks': [['sound']], 'exp': 'safe and sound 安然無恙。'},
  ]},
]
