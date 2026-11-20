# LaLa Word Unit 7（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 71–81 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 7, 'en': 'Too Good to Be True', 'zh': '一字多義（七）',
  'intro': 'fall 是秋天，也是「掉下來」；spring 是春天，也是「彈簧」和「泉水」。這個單元有 4 個主題單字、12 個更多單字，'
           '再整理 hear／here、lend／borrow，和都是「說」的 talk／say／speak／tell。',
  'words': [
    W('tell', '🗣️', [
        S('v.', '告訴；說', 'Please tell me about your trip.', '請告訴我你這趟旅行的事。', 'tell a story / joke / lie 說故事／笑話／說謊；tell on 告狀'),
        S('v.', '顯示', 'Her smile told me she was happy.', '她的微笑告訴我她很開心。'),
        S('v.', '分辨', 'I can\'t tell the twins apart.', '我分不出這對雙胞胎。', 'tell A from B 分辨 A 和 B'),
    ], 'tell - told - told - telling', key=True),
    W('start', '🚦', [
        S('v.', '開始', 'School starts at eight.', '八點開始上課。', 'start to V / V-ing 開始做；start over 重新開始'),
        S('n.', '開始；開端', 'We had a good start this year.', '我們今年有個好的開始。', 'make a fresh start 重新開始'),
        S('v.', '創立', 'Her parents started a small restaurant.', '她爸媽開了一家小餐廳。', 'start a business 創業'),
    ], 'start - started - started - starting', key=True),
    W('call', '📞', [
        S('n.', '通話；電話', 'I got a call from my uncle.', '我接到叔叔打來的電話。', 'make a call 打電話；return a call 回電'),
        S('v.', '打電話', 'Call me when you get home.', '到家的時候打電話給我。', 'call back 回電'),
        S('v.', '叫；喊', 'Mom is calling us for dinner.', '媽媽在叫我們吃晚飯。', 'call for help 呼救；call off 取消'),
        S('v.', '稱呼；取名', 'We call our cat Mimi.', '我們叫我們的貓咪咪。'),
    ], 'call - called - called - calling', key=True),
    W('lesson', '📝', [
        S('n.', '教訓；經驗', 'I learned my lesson. I will never be late again.', '我學到教訓了，再也不會遲到。', 'learn a lesson 學到教訓'),
        S('n.', '課', 'She takes piano lessons every Friday.', '她每個星期五上鋼琴課。', 'take lessons 上課'),
    ], '複數 lessons', key=True),
    W('club', '🎾', [
        S('n.', '社團；俱樂部', 'I joined the chess club at school.', '我參加了學校的西洋棋社。'),
        S('n.', '夜店', 'They went dancing at a club.', '他們去夜店跳舞。'),
        S('n.', '棍棒；球桿', 'He hit the golf ball with a club.', '他用球桿打高爾夫球。'),
    ], '複數 clubs'),
    W('fall', '🍂', [
        S('n.', '秋天', 'The leaves turn red in fall.', '秋天葉子變紅。'),
        S('n.', '瀑布（falls）', 'We saw the beautiful falls in the mountains.', '我們在山裡看到美麗的瀑布。'),
        S('v.', '掉下；跌倒', 'Be careful! Don\'t fall down.', '小心！別跌倒。', 'fall down 跌倒'),
        S('v.', '下降', 'The temperature fell to 10°C last night.', '昨晚氣溫降到十度。'),
        S('v.', '變成（某種狀態）', 'The baby fell asleep in my arms.', '寶寶在我懷裡睡著了。', 'fall asleep 睡著；fall in love 墜入愛河'),
    ], 'fall - fell - fallen - falling'),
    W('heavy', '🏋️', [
        S('adj.', '重的', 'This box is too heavy for me.', '這個箱子對我來說太重了。'),
        S('adj.', '繁重的；大量的', 'There is heavy traffic in the morning.', '早上交通很擁擠。', 'heavy rain 大雨；heavy traffic 交通擁擠'),
        S('adj.', '厚實的', 'Wear a heavy coat. It\'s very cold.', '穿件厚外套，天氣很冷。'),
    ], 'heavy - heavier - heaviest'),
    W('kind', '🤗', [
        S('adj.', '親切的；好心的', 'It\'s very kind of you to help me.', '你幫我真是太好心了。', 'be kind to 對…好'),
        S('n.', '種類', 'What kind of music do you like?', '你喜歡哪一種音樂？', 'all kinds of 各式各樣的'),
    ], 'kind - kinder - kindest；複數 kinds'),
    W('mean', '😠', [
        S('v.', '意思是', 'What does this word mean?', '這個字是什麼意思？'),
        S('v.', '故意；打算', 'Sorry, I didn\'t mean to hurt you.', '對不起，我不是故意要傷害你。'),
        S('v.', '有意義；很重要', 'Your letter means a lot to me.', '你的信對我意義重大。'),
        S('adj.', '刻薄的；兇的', 'Don\'t be mean to your little sister.', '不要對妹妹那麼兇。', 'be mean to 對…很兇'),
        S('adj.', '小氣的', 'He is mean with his money.', '他對錢很小氣。'),
    ], 'mean - meant - meant - meaning；mean - meaner - meanest'),
    W('mine', '⛏️', [
        S('pron.', '我的（東西）', 'This pen is not mine.', '這支筆不是我的。'),
        S('n.', '礦坑', 'The workers dig for gold in the mine.', '工人在礦坑裡挖金子。'),
        S('n.', '地雷', 'Mines are very dangerous.', '地雷非常危險。'),
    ]),
    W('order', '🧾', [
        S('v.', '點餐；訂購', 'Are you ready to order?', '您準備好點餐了嗎？'),
        S('n.', '訂單；點的餐', 'The waiter took our order.', '服務生幫我們點餐。', 'take one\'s order 幫…點餐；place an order 下訂單'),
        S('v.', '命令', 'The coach ordered us to run five laps.', '教練命令我們跑五圈。', 'order + 人 + to V 命令某人做'),
        S('n.', '順序', 'Put the words in the right order.', '把這些字排成正確的順序。', 'in order to 為了'),
    ], 'order - ordered - ordered - ordering'),
    W('own', '🔑', [
        S('adj.', '自己的', 'I have my own room now.', '我現在有自己的房間了。', 'on one\'s own 獨自'),
        S('v.', '擁有', 'My uncle owns a big farm.', '我叔叔擁有一座大農場。'),
    ], 'own - owned - owned - owning'),
    W('poor', '🥺', [
        S('adj.', '貧窮的', 'The family was too poor to buy a car.', '那家人窮得買不起車。'),
        S('adj.', '可憐的', 'The poor dog was left in the rain.', '那隻可憐的狗被丟在雨中。'),
        S('adj.', '不擅長的', 'I\'m poor at math.', '我數學不好。', 'be poor at 不擅長'),
        S('adj.', '不好的；差的', 'He is in poor health.', '他身體不好。', 'poor health 健康不佳'),
    ], 'poor - poorer - poorest'),
    W('season', '🍁', [
        S('n.', '季節', 'Which season do you like best?', '你最喜歡哪個季節？'),
        S('n.', '季；時期', 'Mangoes are in season now.', '現在是芒果的產季。', 'in season 當季；rainy season 雨季'),
        S('v.', '調味', 'Season the soup with a little salt.', '在湯裡加一點鹽調味。'),
    ], 'season - seasoned - seasoned - seasoning'),
    W('snow', '❄️', [
        S('n.', '雪', 'The kids made a snowman in the snow.', '孩子們在雪地裡堆雪人。'),
        S('v.', '下雪', 'It snowed on Hehuan Mountain last night.', '昨晚合歡山下雪了。'),
    ], 'snow - snowed - snowed - snowing'),
    W('spring', '🌸', [
        S('n.', '春天', 'Flowers bloom in spring.', '花在春天盛開。'),
        S('n.', '彈簧', 'This old bed has a broken spring.', '這張舊床有一根彈簧壞了。'),
        S('n.', '泉水', 'We went to Beitou to enjoy the hot springs.', '我們去北投泡溫泉。', 'hot spring 溫泉'),
        S('v.', '跳起；突然出現', 'The cat sprang onto the table.', '貓一躍跳上桌子。', 'spring up 快速出現'),
    ], 'spring - sprang - sprung - springing'),
  ],
  'focus': [
    {'title': '易混淆字：hear 和 here（發音一樣）', 'head': ('單字', '意思', '例句'), 'rows': [
      ('hear', '（動詞）聽到', 'Can you hear me?'),
      ('here', '（副詞）這裡；Here you are. 給你', 'Come here, please.'),
    ], 'note': '聽力題兩個字發音一樣，要看上下文判斷。'},
    {'title': '易混淆字：lend 和 borrow', 'head': ('單字', '用法', '例句'), 'rows': [
      ('lend', '借出（主詞是借給別人的人）：lend + 物 + to + 人', 'Can you lend me your eraser?'),
      ('borrow', '借入（主詞是向別人借的人）：borrow + 物 + from + 人', 'Can I borrow your eraser?'),
    ], 'note': 'lend - lent - lent；borrow - borrowed - borrowed。'},
    {'title': '易混淆字：talk／say／speak／tell', 'head': ('單字', '用法', '例句'), 'rows': [
      ('talk', '聊天、討論：talk to / with + 人、talk about + 事', 'We talked about the movie.'),
      ('say', '說的「內容」；告示、時鐘也可以 say', 'The sign says "No Smoking."'),
      ('speak', '說某種語言；比較正式的說話', 'Can you speak Japanese?'),
      ('tell', '告訴某人：tell + 人 + 事；tell a story / a lie', 'Tell me the truth.'),
    ], 'note': ''},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('fall', '秋天', '掉下；falls 瀑布'),
      ('spring', '春天', '彈簧；泉水'),
      ('mean', '意思是', '刻薄的；小氣的'),
      ('mine', '我的', '礦坑；地雷'),
      ('club', '社團', '球桿'),
      ('kind', '親切的', '種類'),
      ('season', '季節', '調味'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'I can\'t <b>tell</b> the difference between the two bags.', 'opts': ['告訴', '顯示', '分辨', '說謊'], 'answer': 2, 'exp': 'tell the difference 分辨差異。'},
    {'type': 'mc', 'q': 'My mom and her friend <b>started</b> a flower shop.', 'opts': ['開始', '創立', '跑步', '打開'], 'answer': 1, 'exp': 'start a shop 開店。'},
    {'type': 'mc', 'q': 'The game was <b>called</b> off because of the typhoon.', 'opts': ['打電話', '叫喊', '取消', '取名'], 'answer': 2, 'exp': 'call off 取消。'},
    {'type': 'mc', 'q': 'The price of eggs <b>fell</b> last month.', 'opts': ['秋天', '跌倒', '下降', '睡著'], 'answer': 2, 'exp': '價格 fall → 下降。'},
    {'type': 'mc', 'q': 'What <b>kind</b> of food do you like?', 'opts': ['親切的', '種類', '味道', '份量'], 'answer': 1, 'exp': 'what kind of 哪一種。'},
    {'type': 'mc', 'q': 'The girl was <b>mean</b> to the new student.', 'opts': ['意思是', '刻薄的', '故意', '重要的'], 'answer': 1, 'exp': 'be mean to 對…很兇。'},
    {'type': 'mc', 'q': 'My grandfather used to work in a coal <b>mine</b>.', 'opts': ['我的', '礦坑', '地雷', '工廠'], 'answer': 1, 'exp': 'coal mine 煤礦。'},
    {'type': 'mc', 'q': 'Please line up in <b>order</b> of height.', 'opts': ['點餐', '訂單', '命令', '順序'], 'answer': 3, 'exp': 'in order of height 依身高順序。'},
    {'type': 'mc', 'q': 'The pen doesn\'t work because the <b>spring</b> is broken.', 'opts': ['春天', '彈簧', '泉水', '跳起'], 'answer': 1, 'exp': '筆裡的彈簧。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'I\'m in the school music ______.  ／  He hit the ball with a golf ______.', 'opts': ['team', 'club', 'band', 'stick'], 'answer': 1, 'exp': 'club 社團／球桿。'},
    {'type': 'mc', 'q': 'The leaves fall in ______.  ／  Be careful not to ______ off the bike.', 'opts': ['autumn', 'winter', 'fall', 'drop'], 'answer': 2, 'exp': 'fall 秋天／跌落。'},
    {'type': 'mc', 'q': 'Mangoes are in ______ in summer.  ／  ______ the meat with salt and pepper.', 'opts': ['season', 'time', 'Cook', 'Salt'], 'answer': 0, 'exp': 'season 季節／調味。'},
    {'type': 'mc', 'q': 'I learned a ______ from my mistake.  ／  I have a swimming ______ today.', 'opts': ['class', 'lesson', 'story', 'course'], 'answer': 1, 'exp': 'lesson 教訓／課。'},
    {'type': 'mc', 'q': 'That family is very ______. They don\'t have enough food.  ／  I\'m ______ at singing.', 'opts': ['rich', 'poor', 'bad', 'mean'], 'answer': 1, 'exp': 'poor 貧窮的／不擅長的。'},
  ]},
  {'title': '③ 易混淆字：選出正確的字', 'items': [
    {'type': 'mc', 'q': 'Speak louder. I can\'t ______ you.', 'opts': ['here', 'hear', 'listen', 'say'], 'answer': 1, 'exp': '聽到 → hear。'},
    {'type': 'mc', 'q': 'Can I ______ your umbrella?', 'opts': ['lend', 'borrow', 'give', 'lent'], 'answer': 1, 'exp': '我向你借 → borrow。'},
    {'type': 'mc', 'q': 'Jack ______ me his comic book yesterday.', 'opts': ['borrowed', 'lent', 'lend', 'took'], 'answer': 1, 'exp': '借給我 → lend 的過去式 lent。'},
    {'type': 'mc', 'q': 'My friend can ______ three languages.', 'opts': ['talk', 'say', 'speak', 'tell'], 'answer': 2, 'exp': '說某種語言 → speak。'},
    {'type': 'mc', 'q': 'Grandpa often ______ us funny stories.', 'opts': ['says', 'talks', 'speaks', 'tells'], 'answer': 3, 'exp': 'tell + 人 + stories。'},
    {'type': 'mc', 'q': 'What did the teacher ______ about the test?', 'opts': ['say', 'tell', 'speak', 'talk'], 'answer': 0, 'exp': '說了什麼內容 → say。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'I\'ll call you {0} later. （回電）', 'blanks': [['back']], 'exp': 'call back 回電。'},
    {'q': 'The baby fell {0} on the sofa. （睡著）', 'blanks': [['asleep']], 'exp': 'fall asleep 睡著。'},
    {'q': 'There was {0} rain last night. （大量的）', 'blanks': [['heavy']], 'exp': 'heavy rain 大雨。'},
    {'q': 'She finished the work on her {0}. （自己的；獨自）', 'blanks': [['own']], 'exp': 'on one\'s own 獨自。'},
    {'q': 'We got up early in {0} to see the sunrise. （為了）', 'blanks': [['order']], 'exp': 'in order to 為了。'},
    {'q': 'Your gift {0} a lot to me. （有意義，現在式）', 'blanks': [['means']], 'exp': 'mean a lot to 對…很重要。'},
  ]},
]
