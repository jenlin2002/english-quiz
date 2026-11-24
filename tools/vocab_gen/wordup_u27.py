# WORD UP 複習區 Unit 27（WORD UP「L-I」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 27, 'en': 'L-I', 'zh': 'L 開頭（一）',
  'intro': 'WORD UP「L-I」的 37 個字（lack 到 library）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('lack', 'n./v.', '缺乏', 'lack of + 名詞', 'Lack of sleep makes me tired.', '睡眠不足讓我很累。', '🪫'),
    W('lady', 'n.', '女士；淑女', '複數 ladies', 'Ladies and gentlemen, welcome!', '各位女士先生，歡迎！', '👩'),
    W('lake', 'n.', '湖', 'Sun Moon Lake 日月潭', 'We rode bikes around Sun Moon Lake.', '我們騎腳踏車環日月潭。', '🏞️'),
    W('lamb', 'n.', '小羊；羊肉', 'b 不發音', 'The lamb is following its mother.', '小羊跟著媽媽走。', '🐑'),
    W('lamp', 'n.', '燈；檯燈', '', 'Turn on the lamp. It\'s dark.', '打開檯燈，好暗。', '💡'),
    W('land', 'n./v.', '陸地；土地；降落', '', 'The plane landed safely.', '飛機安全降落。', '🛬'),
    W('language', 'n.', '語言', '', 'How many languages can you speak?', '你會說幾種語言？', '🗣️'),
    W('large', 'adj.', '大的', '= big', 'Can I have a large Coke?', '我可以要一杯大可樂嗎？', '🔝'),
    W('last', 'adj./v.', '最後的；上一個；持續', 'last night 昨晚', 'The meeting lasted two hours.', '會議持續了兩小時。', '🔚'),
    W('late', 'adj./adv.', '遲的；晚的', 'be late for 遲到', 'Don\'t be late for school.', '上學不要遲到。', '⏰'),
    W('later', 'adv.', '稍後；後來', 'See you later. 待會見', 'See you later!', '待會見！', '⏭️'),
    W('latest', 'adj.', '最新的', '', 'Have you seen the latest phone?', '你看過最新款的手機嗎？', '🆕'),
    W('laugh', 'v./n.', '笑', 'laugh at 嘲笑；gh 唸 /f/', 'Don\'t laugh at others.', '不要嘲笑別人。', '😂'),
    W('law', 'n.', '法律', '', 'Everyone must obey the law.', '每個人都必須守法。', '⚖️'),
    W('lawyer', 'n.', '律師', '', 'My aunt is a lawyer.', '我阿姨是律師。', '👩‍⚖️'),
    W('lay', 'v.', '放；下（蛋）', '三態 lay-laid-laid', 'The hen laid three eggs.', '母雞下了三顆蛋。', '🥚'),
    W('lazy', 'adj.', '懶惰的', '', 'Don\'t be lazy. Get up!', '別懶惰了，起床！', '🦥'),
    W('lead', 'v.', '帶領；導致', '三態 lead-led-led；lead to 導致', 'Hard work leads to success.', '努力帶來成功。', '🧭'),
    W('leader', 'n.', '領導者', 'class leader 班長', 'Who is your class leader?', '誰是你們班長？', '🧑‍✈️'),
    W('leadership', 'n.', '領導能力', '', 'She has great leadership.', '她很有領導能力。', '🏅'),
    W('leaf', 'n.', '葉子', '複數 leaves', 'The leaves turn yellow in fall.', '葉子秋天變黃。', '🍃'),
    W('learn', 'v.', '學習', 'learn to V', 'I\'m learning to swim.', '我正在學游泳。', '📖'),
    W('least', 'adj./adv.', '最少的', 'at least 至少', 'Drink at least eight glasses of water a day.', '一天至少喝八杯水。', '🔻'),
    W('leave', 'v.', '離開；留下', '三態 leave-left-left；leave for 前往', 'The train leaves at nine.', '火車九點開。', '🚪'),
    W('left', 'adj./n.', '左邊的；左邊', 'turn left 左轉', 'Turn left at the corner.', '在轉角左轉。', '⬅️'),
    W('leg', 'n.', '腿', '', 'A spider has eight legs.', '蜘蛛有八隻腳。', '🦵'),
    W('legal', 'adj.', '合法的', 'illegal 違法的', 'Is it legal to park here?', '在這裡停車合法嗎？', '📜'),
    W('lemon', 'n.', '檸檬', '', 'I like tea with lemon.', '我喜歡加檸檬的茶。', '🍋'),
    W('lend', 'v.', '借（出）', '三態 lend-lent-lent；lend A to B', 'Can you lend me your pen?', '你可以借我你的筆嗎？', '🤲'),
    W('length', 'n.', '長度', 'long 的名詞', 'What is the length of this room?', '這個房間的長度是多少？', '📏'),
    W('less', 'adj./adv.', '較少的', 'little 的比較級；接不可數名詞', 'Eat less sugar.', '少吃糖。', '➖'),
    W('lesson', 'n.', '課；教訓', '', 'I have piano lessons on Fridays.', '我星期五上鋼琴課。', '📚'),
    W('let', 'v.', '讓', '三態都是 let；let + 人 + 原形', 'Let me help you.', '讓我幫你。', '🙌'),
    W('letter', 'n.', '信；字母', '', 'I wrote a letter to my grandma.', '我寫了一封信給奶奶。', '✉️'),
    W('lettuce', 'n.', '萵苣；生菜', '', 'Put some lettuce in the sandwich.', '在三明治裡放些生菜。', '🥬'),
    W('level', 'n.', '程度；等級', '', 'This book is at my reading level.', '這本書符合我的閱讀程度。', '📶'),
    W('library', 'n.', '圖書館', '', 'I borrow books from the library.', '我從圖書館借書。', '🏛️'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('lend / borrow', '借出 ／ 借入', 'lend me a pen ／ borrow a pen from you'),
      ('let + 人 + 原形動詞', '讓某人…', 'Let me go.'),
      ('laugh at', '嘲笑', 'laugh at his mistake'),
      ('at least', '至少', 'at least ten minutes'),
      ('be late for', '…遲到', 'late for class'),
      ('lead to', '導致', 'lead to problems'),
      ('leaf → leaves', '葉子的複數', 'green leaves'),
    ], 'note': 'leave 的過去式 left；lay（放、下蛋）的過去式 laid。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '律師', 'opts': ['leader', 'lawyer', 'lady', 'letter'], 'answer': 1, 'exp': 'lawyer 律師。'},
    {'type': 'mc', 'q': '缺乏', 'opts': ['lack', 'lake', 'lamb', 'lamp'], 'answer': 0, 'exp': 'lack 缺乏。'},
    {'type': 'mc', 'q': '合法的', 'opts': ['lazy', 'latest', 'legal', 'level'], 'answer': 2, 'exp': 'legal 合法的。'},
    {'type': 'mc', 'q': '長度', 'opts': ['lesson', 'least', 'leaf', 'length'], 'answer': 3, 'exp': 'length 長度。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '圖書館（l＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['library']], 'exp': 'library。'},
    {'q': '語言（l＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['language']], 'exp': 'language。'},
    {'q': '檸檬（l＿＿＿＿，5 個字母）：{0}', 'blanks': [['lemon']], 'exp': 'lemon。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'The {0} fell from the tree. （葉子，複數）', 'blanks': [['leaves']], 'exp': 'leaf 的複數 leaves。'},
    {'q': 'He {0} home at seven this morning. （離開，過去式）', 'blanks': [['left']], 'exp': 'leave 的過去式 left。'},
    {'q': 'You should sleep at {0} eight hours. （至少）', 'blanks': [['least']], 'exp': 'at least 至少。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Could you ______ me your eraser?', 'opts': ['borrow', 'lend', 'let', 'leave'], 'answer': 1, 'exp': '借給我：lend me。'},
    {'type': 'mc', 'q': 'Mom let me ______ TV after dinner.', 'opts': ['to watch', 'watching', 'watch', 'watched'], 'answer': 2, 'exp': 'let + 人 + 原形。'},
    {'type': 'mc', 'q': 'Don\'t laugh ______ him. He is trying his best.', 'opts': ['at', 'to', 'with', 'for'], 'answer': 0, 'exp': 'laugh at 嘲笑。'},
    {'type': 'mc', 'q': 'Hurry up, or you\'ll be late ______ the bus.', 'opts': ['to', 'at', 'in', 'for'], 'answer': 3, 'exp': 'be late for 趕不上、遲到。'},
  ]},
]
