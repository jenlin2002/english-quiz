# WORD UP 複習區 Unit 49（WORD UP「T-III」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 49, 'en': 'T-III', 'zh': 'T 開頭（三）',
  'intro': 'WORD UP「T-III」的 35 個字（tiny 到 train）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('tiny', 'adj.', '極小的', '', 'The baby has tiny hands.', '寶寶的手好小。', '🤏'),
    W('tip', 'n.', '小費；祕訣；尖端', '', 'Here are some tips for learning English.', '這裡有一些學英文的祕訣。', '💡'),
    W('tired', 'adj.', '累的；厭倦的', 'be tired of 厭倦', 'I\'m tired of eating noodles.', '我吃麵吃膩了。', '😫'),
    W('title', 'n.', '標題；頭銜', '', 'What\'s the title of the book?', '這本書的書名是什麼？', '🏷️'),
    W('toast', 'n.', '吐司', '不可數；a piece of toast', 'I had toast for breakfast.', '我早餐吃吐司。', '🍞'),
    W('today', 'adv./n.', '今天', '', 'What day is it today?', '今天星期幾？', '📅'),
    W('toe', 'n.', '腳趾', '', 'I hurt my toe.', '我傷到腳趾了。', '🦶'),
    W('tofu', 'n.', '豆腐', '', 'Stinky tofu smells bad but tastes good.', '臭豆腐聞起來臭但吃起來香。', '🧈'),
    W('together', 'adv.', '一起', '', 'Let\'s go together.', '我們一起去吧。', '🤝'),
    W('toilet', 'n.', '馬桶；廁所', '', 'Flush the toilet after use.', '用完馬桶要沖水。', '🚽'),
    W('tomato', 'n.', '番茄', '複數 tomatoes', 'I put tomatoes in the salad.', '我在沙拉裡放番茄。', '🍅'),
    W('tomorrow', 'adv./n.', '明天', '', 'See you tomorrow!', '明天見！', '🌅'),
    W('tongue', 'n.', '舌頭', 'ue 不發音', 'The dog stuck out its tongue.', '狗伸出舌頭。', '👅'),
    W('tonight', 'adv./n.', '今晚', '', 'What are you doing tonight?', '你今晚要做什麼？', '🌙'),
    W('too', 'adv.', '也；太', 'too + 形容詞 + to V 太…而不能', 'It\'s too hot to go out.', '太熱了，不能出門。', '➕'),
    W('tool', 'n.', '工具', '', 'A hammer is a useful tool.', '鐵鎚是很有用的工具。', '🧰'),
    W('tooth', 'n.', '牙齒', '複數 teeth', 'Brush your teeth twice a day.', '一天刷兩次牙。', '🦷'),
    W('toothache', 'n.', '牙痛', 'have a toothache', 'I have a toothache.', '我牙痛。', '😣'),
    W('toothbrush', 'n.', '牙刷', '', 'I need a new toothbrush.', '我需要一支新牙刷。', '🪥'),
    W('top', 'n./adj.', '頂端；最高的', 'on top of 在…上面', 'We climbed to the top of the hill.', '我們爬到山頂。', '🔝'),
    W('topic', 'n.', '主題；話題', '', 'What\'s the topic of your report?', '你報告的主題是什麼？', '💬'),
    W('total', 'adj./n.', '總計的；總數', 'in total 總共', 'The total cost is 500 dollars.', '總費用是 500 元。', '🧮'),
    W('touch', 'v./n.', '觸摸；接觸', 'keep in touch 保持聯絡', 'Let\'s keep in touch.', '我們保持聯絡吧。', '👆'),
    W('tour', 'n./v.', '旅遊；參觀', 'tour guide 導遊', 'We took a tour of the museum.', '我們參觀了博物館。', '🗺️'),
    W('towel', 'n.', '毛巾', '', 'Dry your hands with a towel.', '用毛巾擦乾手。', '🧻'),
    W('tower', 'n.', '塔', '', 'The tower is 500 meters tall.', '那座塔有 500 公尺高。', '🗼'),
    W('town', 'n.', '城鎮', '', 'I grew up in a small town.', '我在一個小鎮長大。', '🏘️'),
    W('toy', 'n.', '玩具', '', 'The kids are playing with toys.', '孩子們在玩玩具。', '🧸'),
    W('trace', 'n./v.', '痕跡；追蹤', '', 'The thief left no trace.', '小偷沒留下任何痕跡。', '👣'),
    W('track', 'n.', '跑道；軌道；足跡', '', 'The runners are on the track.', '跑者在跑道上。', '🏃'),
    W('trade', 'n./v.', '貿易；交換', '', 'Taiwan trades with many countries.', '台灣和很多國家貿易往來。', '🚢'),
    W('tradition', 'n.', '傳統', '', 'Eating dumplings is a tradition.', '吃餃子是一種傳統。', '🏮'),
    W('traditional', 'adj.', '傳統的', '', 'She wore a traditional dress.', '她穿著傳統服裝。', '👘'),
    W('traffic', 'n.', '交通；車流', '不可數；traffic jam 塞車', 'The traffic is heavy this morning.', '今天早上交通很擁擠。', '🚦'),
    W('train', 'n./v.', '火車；訓練', 'by train 搭火車', 'We went to Hualien by train.', '我們搭火車去花蓮。', '🚆'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('too + 形容詞 + to V', '太…而不能…', 'too tired to walk'),
      ('be tired of', '厭倦…', 'tired of waiting'),
      ('keep in touch', '保持聯絡', 'Keep in touch!'),
      ('on top of', '在…上面', 'on top of the box'),
      ('tradition / traditional', '傳統（名詞）／ 傳統的（形容詞）', 'an old tradition ／ traditional food'),
      ('traffic jam', '塞車', 'stuck in a traffic jam'),
      ('in total', '總共', '50 students in total'),
    ], 'note': 'tooth → teeth；tomato → tomatoes；traffic 不可數。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '舌頭', 'opts': ['toe', 'tongue', 'tooth', 'tool'], 'answer': 1, 'exp': 'tongue 舌頭。'},
    {'type': 'mc', 'q': '痕跡', 'opts': ['trace', 'track', 'trade', 'tour'], 'answer': 0, 'exp': 'trace 痕跡。'},
    {'type': 'mc', 'q': '毛巾', 'opts': ['tower', 'town', 'towel', 'toilet'], 'answer': 2, 'exp': 'towel 毛巾。'},
    {'type': 'mc', 'q': '標題', 'opts': ['tip', 'topic', 'total', 'title'], 'answer': 3, 'exp': 'title 標題。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '明天（t＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['tomorrow']], 'exp': 'tomorrow（一個 m、兩個 r）。'},
    {'q': '一起（t＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['together']], 'exp': 'together。'},
    {'q': '傳統（t＿＿＿＿＿＿＿＿，9 個字母）：{0}', 'blanks': [['tradition']], 'exp': 'tradition。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Brush your {0} before you go to bed. （牙齒，複數）', 'blanks': [['teeth']], 'exp': 'tooth 的複數 teeth。'},
    {'q': 'I\'m {0} of playing the same game. （厭倦的）', 'blanks': [['tired']], 'exp': 'be tired of 厭倦。'},
    {'q': 'The {0} is heavy. We will be late. （交通）', 'blanks': [['traffic']], 'exp': 'traffic 交通。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'The box is too heavy ______ me to carry.', 'opts': ['to', 'for', 'of', 'with'], 'answer': 1, 'exp': 'too + 形容詞 + for + 人 + to V。'},
    {'type': 'mc', 'q': 'Let\'s keep in ______ after you move.', 'opts': ['tour', 'top', 'touch', 'trace'], 'answer': 2, 'exp': 'keep in touch 保持聯絡。'},
    {'type': 'mc', 'q': 'We usually wear ______ clothes for the festival.', 'opts': ['traditional', 'tradition', 'traditions', 'trade'], 'answer': 0, 'exp': '形容詞 traditional 修飾 clothes。'},
    {'type': 'mc', 'q': 'There are 40 students ______ total.', 'opts': ['on', 'at', 'for', 'in'], 'answer': 3, 'exp': 'in total 總共。'},
  ]},
]
