# 主題 2000 字 Unit 21：Languages 語言（字表依課本單元；詞性、中文、例句、題目為本站自編）
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000', 'no': 21, 'en': 'Languages', 'zh': '語言',
  'intro': '兩個最常用的語言：Chinese 和 English。語言當名詞時不可數、前面不加 a；Chinese 還可以當「中國人」和「中國的」。',
  'words': [
    W('Chinese', 'n./adj.', '中文；中國人；中國的', '語言不可數；中國人單複數同形（two Chinese）',
      'My English teacher can speak a little Chinese.', '我的英文老師會說一點中文。', '🀄'),
    W('English', 'n./adj.', '英文；英語；英國的', '語言不可數，前面不加 a',
      'English is spoken in many countries.', '很多國家都說英語。', '🔤'),
  ],
  'focus': [
    {'title': 'Chinese、English 的三種用法', 'head': ('用法', '例句', '中文'), 'rows': [
      ('語言（名詞，不可數）', 'We have Chinese class every day.', '我們每天都有國文課。'),
      ('語言（名詞，不可數）', 'Can you write your name in English?', '你會用英文寫你的名字嗎？'),
      ('人（名詞）', 'Many Chinese live in Malaysia.', '很多華人住在馬來西亞。'),
      ('…的（形容詞）', 'Dumplings are a kind of Chinese food.', '餃子是一種中國食物。'),
      ('…的（形容詞）', 'I read an English storybook last night.', '我昨晚讀了一本英文故事書。'),
    ], 'note': '說語言不加 a／the：speak English（不是 speak an English）。in English＝用英文。'},
    {'title': '說語言的常用句', 'head': ('英文', '中文', ''), 'rows': [
      ('Do you speak English?', '你會說英文嗎？', ''),
      ('How do you say 「謝謝」 in English?', '「謝謝」用英文怎麼說？', ''),
      ('What does this word mean in Chinese?', '這個字的中文是什麼意思？', ''),
      ('Please say it again in English.', '請再用英文說一次。', ''),
      ('Chinese is hard to write, but it\'s fun.', '中文很難寫，但很有趣。', ''),
    ], 'note': '「用某種語言」說用 in：in English、in Chinese。'},
    {'title': '國家、人、語言（和 Unit 20 一起記）', 'head': ('國家', '人', '語言'), 'rows': [
      ('China', 'Chinese', 'Chinese'),
      ('England 英格蘭', 'English（英格蘭人；常說 the English）', 'English'),
      ('America', 'American', 'English'),
      ('Japan', 'Japanese', 'Japanese'),
    ], 'note': '語言、國籍的字第一個字母都要大寫：English、Chinese。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '中文；中國人', 'opts': ['China', 'Chinese', 'Taiwan', 'English'], 'answer': 1, 'exp': 'Chinese 中文、中國人；China 是中國這個國家。'},
    {'type': 'mc', 'q': '英文；英語', 'opts': ['England', 'America', 'English', 'Chinese'], 'answer': 2, 'exp': 'English 英文；England 是英格蘭。'},
  ]},
  {'title': '② 看英文選中文', 'items': [
    {'type': 'mc', 'q': 'English', 'opts': ['英文；英語', '美國', '英國人的國家', '日文'], 'answer': 0, 'exp': 'English 英文、英語。'},
    {'type': 'mc', 'q': 'Chinese', 'opts': ['中國', '臺灣', '中文；中國人；中國的', '日本人'], 'answer': 2, 'exp': 'Chinese 中文、中國人、中國的。'},
  ]},
  {'title': '③ 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數；語言第一個字母要大寫。', 'items': [
    {'q': '中文（C＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['Chinese']], 'exp': 'Chinese，C 大寫，結尾 -ese。'},
    {'q': '英文（E＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['English']], 'exp': 'English，E 大寫。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'We learn {0} in English class. （英文）', 'blanks': [['English']], 'exp': '英文課學英文 → English。'},
    {'q': 'My grandma can read {0}, but she can\'t read English. （中文）', 'blanks': [['Chinese']], 'exp': '中文 → Chinese。'},
    {'q': 'Dumplings and noodles are {0} food. （中國的）', 'blanks': [['Chinese']], 'exp': '中國的（形容詞）→ Chinese food。'},
    {'q': 'How do you say 「蘋果」 in {0}? — Apple. （英文）', 'blanks': [['English']], 'exp': '用英文 in English。'},
    {'q': 'People in China speak {0}. （中文）', 'blanks': [['Chinese']], 'exp': '中國人說中文 → Chinese。'},
  ]},
  {'title': '⑤ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Tom can speak ______ very well.', 'opts': ['a Chinese', 'Chinese', 'the Chineses', 'Chineses'], 'answer': 1, 'exp': '語言不可數，前面不加 a、不加 -s：speak Chinese。'},
    {'type': 'mc', 'q': 'Please write the answer ______ English.', 'opts': ['on', 'at', 'in', 'by'], 'answer': 2, 'exp': '用英文 in English。'},
    {'type': 'mc', 'q': 'A: Do you speak English?  B: Yes, ______.', 'opts': ['a little', 'a few', 'many', 'few'], 'answer': 0, 'exp': '語言不可數，用 a little（一點）。'},
    {'type': 'mc', 'q': 'There are two ______ in our class. They come from Beijing.', 'opts': ['Chinese', 'Chineses', 'China', 'Chinas'], 'answer': 0, 'exp': 'Chinese（中國人）單複數同形：two Chinese。'},
    {'type': 'mc', 'q': 'Which one is written correctly?', 'opts': ['english', 'English', 'ENGlish', 'Englich'], 'answer': 1, 'exp': '語言第一個字母要大寫：English。'},
  ]},
]
