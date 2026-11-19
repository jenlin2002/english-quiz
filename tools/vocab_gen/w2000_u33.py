# 主題 2000 字 Unit 33：Interjections 感嘆詞（字表依課本單元；詞性、中文、例句、題目為本站自編）
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000', 'no': 33, 'en': 'Interjections', 'zh': '感嘆詞',
  'intro': '打招呼、說再見的 4 個字。打電話、見面、道別都會用到。',
  'words': [
    W('hello', 'interj.', '哈囉；你好；（電話）喂', '', 'Hello, may I speak to Amy, please?', '喂，請問 Amy 在嗎？', '📞'),
    W('hey', 'interj.', '嘿', '叫人注意、比較隨便', 'Hey! Wait for me!', '嘿！等等我！', '🙋'),
    W('hi', 'interj.', '嗨；你好', '比 hello 輕鬆', 'Hi, Tom! Long time no see!', '嗨，湯姆！好久不見！', '👋'),
    W('good-bye', 'interj.', '再見', '＝goodbye、bye', 'Good-bye! See you tomorrow.', '再見！明天見。', '🫡'),
  ],
  'focus': [
    {'title': '見面和道別', 'head': ('情境', '說法', '回答'), 'rows': [
      ('見面', 'Hi! / Hello! How are you?', 'I\'m fine, thank you.'),
      ('好久不見', 'Long time no see!', 'Yeah! How have you been?'),
      ('道別', 'Good-bye! / Bye! See you later.', 'See you!'),
      ('打電話', 'Hello, may I speak to…?', 'Hold on, please. ／ Speaking.'),
    ], 'note': 'hey 比較隨便，用在朋友之間或叫人注意。'},
  ],
}

QUIZ = [
  {'title': '① 選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'A: ______ May I speak to Iris, please?  B: Hold on.', 'opts': ['Hello!', 'Good-bye!', 'Good night!', 'Sorry!'], 'answer': 0, 'exp': '打電話開頭說 Hello。'},
    {'type': 'mc', 'q': 'A: ______ See you tomorrow.  B: Bye!', 'opts': ['Hi!', 'Good-bye!', 'Hello!', 'Hey!'], 'answer': 1, 'exp': '道別 → Good-bye。'},
    {'type': 'mc', 'q': '______! Wait for me!', 'opts': ['Hey', 'Bye', 'Thanks', 'Sorry'], 'answer': 0, 'exp': '叫人注意 → Hey。'},
    {'type': 'mc', 'q': 'A: Hi, Tom! Long time no see!  B: ______', 'opts': ['Good-bye!', 'Hi! How have you been?', 'Speaking.', 'No, thanks.'], 'answer': 1, 'exp': '見面回 Hi。'},
  ]},
  {'title': '② 拼字：寫出單字', 'items': [
    {'q': '再見（g＿＿＿－＿＿＿，有一個連字號）：{0}', 'blanks': [['good-bye', 'goodbye']], 'exp': 'good-bye（也可寫 goodbye）。'},
    {'q': '哈囉（h＿＿＿＿，5 個字母）：{0}', 'blanks': [['hello']], 'exp': 'hello。'},
  ]},
]
