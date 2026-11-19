# 主題 2000 字 Unit 29：Wh-words 疑問詞（字表依課本單元；詞性、中文、例句、題目為本站自編）
# 功能詞沒有適合的照片，全部用 emoji。
def W(w, pos, zh, note, ex, exzh, pic, exsay=None):
    d = {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}
    if exsay:
        d['exsay'] = exsay
    return d

UNIT = {
  'book': 'w2000', 'no': 29, 'en': 'Wh-words', 'zh': '疑問詞',
  'intro': '問「誰、什麼、哪裡、什麼時候、為什麼、怎樣」的 9 個字。看到疑問詞，就要想好回答要給什麼資訊。',
  'words': [
    W('how', 'adv.', '如何；怎樣；多麼', 'how old 幾歲、how many 多少', 'How do you go to school?', '你怎麼去上學？', '🤔'),
    W('what', 'pron./adj.', '什麼', '', 'What is your name?', '你叫什麼名字？', '❓'),
    W('which', 'pron./adj.', '哪一個', '從幾個裡面選', 'Which color do you like, red or blue?', '你喜歡哪個顏色，紅色還是藍色？', '🔴'),
    W('who', 'pron.', '誰', '', 'Who is that girl?', '那個女孩是誰？', '👤'),
    W('whose', 'pron./adj.', '誰的', '不要和 who\'s（＝who is）搞混', 'Whose bag is this?', '這是誰的包包？', '🎒'),
    W('when', 'adv./conj.', '什麼時候；當…的時候', '', 'When is your birthday?', '你的生日是什麼時候？', '📅'),
    W('where', 'adv.', '哪裡', '', 'Where do you live?', '你住在哪裡？', '📍'),
    W('whether', 'conj.', '是否', '常說 whether… or not', "I don't know whether he will come.", '我不知道他是否會來。', '⚖️'),
    W('why', 'adv.', '為什麼', '回答用 Because…', 'Why are you late?', '你為什麼遲到？', '⏰'),
  ],
  'focus': [
    {'title': '問什麼、答什麼', 'head': ('疑問詞', '問', '例句與回答'), 'rows': [
      ('who', '人', 'Who is he? — He is my uncle.'),
      ('whose', '誰的東西', 'Whose pen is this? — It\'s Sam\'s.'),
      ('what', '東西、事情', 'What are you doing? — I\'m cooking.'),
      ('which', '從幾個中選一個', 'Which one is yours? — The red one.'),
      ('when', '時間', 'When will you come? — Tomorrow.'),
      ('where', '地點', 'Where is he from? — England.'),
      ('why', '原因', 'Why are you late? — Because I got up late.'),
      ('how', '方法、狀況', 'How is the weather? — It\'s sunny.'),
    ], 'note': ''},
    {'title': 'how 家族', 'head': ('說法', '問', '例句'), 'rows': [
      ('how old', '年紀', 'How old is your sister?'),
      ('how many', '數量（可數）', 'How many books do you have?'),
      ('how much', '價錢；量（不可數）', 'How much is this shirt?'),
      ('how tall', '身高', 'How tall are you?'),
      ('how long', '多久；多長', 'How long is the movie?'),
      ('how often', '多常', 'How often do you play tennis?'),
    ], 'note': ''},
    {'title': '疑問詞放在句子中間', 'head': ('直接問', '放進句子裡', ''), 'rows': [
      ('Where does he live?', 'I don\'t know where he lives.', ''),
      ('Will it rain?', 'I don\'t know whether it will rain.', ''),
    ], 'note': '放進句子裡時，順序改回「主詞＋動詞」；沒有疑問詞的問句用 whether（是否）。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '誰的', 'opts': ['who', 'whose', "who's", 'which'], 'answer': 1, 'exp': 'whose 誰的。'},
    {'type': 'mc', 'q': '是否', 'opts': ['weather', 'whether', 'where', 'when'], 'answer': 1, 'exp': 'whether 是否；weather 是天氣。'},
    {'type': 'mc', 'q': '哪一個', 'opts': ['what', 'witch', 'which', 'why'], 'answer': 2, 'exp': 'which 哪一個；witch 是女巫。'},
  ]},
  {'title': '② 拼字：看中文，寫出疑問詞', 'items': [
    {'q': '哪裡：{0}', 'blanks': [['where']], 'exp': 'where。'},
    {'q': '為什麼：{0}', 'blanks': [['why']], 'exp': 'why。'},
    {'q': '什麼時候：{0}', 'blanks': [['when']], 'exp': 'when。'},
  ]},
  {'title': '③ 對話：選出正確的疑問詞', 'items': [
    {'type': 'mc', 'q': 'A: ______ are you late?  B: Because I missed the bus.', 'opts': ['Where', 'Why', 'What', 'Who'], 'answer': 1, 'exp': '回答 Because → 問原因 Why。'},
    {'type': 'mc', 'q': 'A: ______ is your birthday?  B: It\'s on May 5.', 'opts': ['When', 'Where', 'Which', 'How'], 'answer': 0, 'exp': '回答日期 → When。'},
    {'type': 'mc', 'q': 'A: ______ is that man?  B: He\'s my uncle.', 'opts': ['Whose', 'What', 'Who', 'Which'], 'answer': 2, 'exp': '問人 → Who。'},
    {'type': 'mc', 'q': 'A: ______ book is this?  B: It\'s Amy\'s.', 'opts': ['Who', 'Whose', 'Which', 'What'], 'answer': 1, 'exp': '回答誰的 → Whose。'},
    {'type': 'mc', 'q': 'A: ______ do you live?  B: In Taichung.', 'opts': ['Where', 'When', 'Why', 'How'], 'answer': 0, 'exp': '回答地點 → Where。'},
    {'type': 'mc', 'q': 'A: ______ do you go to school?  B: By bus.', 'opts': ['What', 'Where', 'How', 'Who'], 'answer': 2, 'exp': '回答方法 → How。'},
    {'type': 'mc', 'q': 'A: ______ are you doing?  B: I\'m reading.', 'opts': ['Which', 'What', 'Who', 'Whose'], 'answer': 1, 'exp': '問做什麼 → What。'},
    {'type': 'mc', 'q': 'A: ______ do you want, tea or coffee?  B: Tea, please.', 'opts': ['Which', 'Who', 'Where', 'Why'], 'answer': 0, 'exp': '從兩個中選 → Which。'},
  ]},
  {'title': '④ how 家族：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'A: How ______ is your brother?  B: He is ten.', 'opts': ['many', 'old', 'much', 'long'], 'answer': 1, 'exp': '問年紀 → how old。'},
    {'type': 'mc', 'q': 'A: How ______ is this cake?  B: It\'s 80 dollars.', 'opts': ['many', 'much', 'old', 'often'], 'answer': 1, 'exp': '問價錢 → how much。'},
    {'type': 'mc', 'q': 'A: How ______ pets do you have?  B: Three.', 'opts': ['much', 'many', 'long', 'tall'], 'answer': 1, 'exp': '可數的數量 → how many。'},
  ]},
  {'title': '⑤ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'I don\'t know ______ it will rain this afternoon.', 'opts': ['who', 'whose', 'whether', 'which'], 'answer': 2, 'exp': '是否 → whether。'},
    {'type': 'mc', 'q': 'Can you tell me where ______?', 'opts': ['does he live', 'he lives', 'lives he', 'he does live'], 'answer': 1, 'exp': '放進句子裡用「主詞＋動詞」：where he lives。'},
  ]},
]
