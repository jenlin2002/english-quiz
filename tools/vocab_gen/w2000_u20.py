# 主題 2000 字 Unit 20：Countries and areas 國家與區域（字表依課本單元；詞性、中文、例句、題目為本站自編）
def W(w, pos, zh, note, ex, exzh, pic, say=None, exsay=None):
    d = {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}
    if say:
        d['say'] = say      # 語音唸法（縮寫要一個字母一個字母唸）
    if exsay:
        d['exsay'] = exsay
    return d

UNIT = {
  'book': 'w2000', 'no': 20, 'en': 'Countries and areas', 'zh': '國家與區域',
  'intro': '國家、世界和常見的國名縮寫，共 7 個字。注意國名、國家的人、語言怎麼說，以及 R.O.C.、U.S.A. 是哪幾個字的縮寫。',
  'words': [
    W('country', 'n.', '國家；鄉下', '複數 countries', 'Japan and Korea are both Asian countries.', '日本和韓國都是亞洲國家。', '🗺️'),
    W('world', 'n.', '世界', 'all over the world 全世界', 'People all over the world love music.', '全世界的人都喜歡音樂。', '🌍'),
    W('America', 'n.', '美國；美洲', '美國人、美國的：American', 'My cousin lives in America.', '我表哥住在美國。', '🗽'),
    W('China', 'n.', '中國', '中文、中國人：Chinese', 'The Great Wall is in China.', '長城在中國。', '🏯'),
    W('Taiwan', 'n.', '臺灣', '臺灣人、臺灣的：Taiwanese', 'I come from Taiwan.', '我來自臺灣。', '🏝️'),
    W('R.O.C.', 'n.', '中華民國', 'the Republic of China 的縮寫；也寫 ROC', 'R.O.C. is short for the Republic of China.', 'R.O.C. 是中華民國的縮寫。', '🏛️',
      say='R O C', exsay='R O C is short for the Republic of China.'),
    W('U.S.A.', 'n.', '美國', 'the United States of America 的縮寫；也寫 USA', 'The U.S.A. is a very big country.', '美國是一個很大的國家。', '🗽',
      say='U S A', exsay='The U S A is a very big country.'),
  ],
  'focus': [
    {'title': '國家、人、語言', 'head': ('國家', '人；…的', '語言'), 'rows': [
      ('Taiwan 臺灣', 'Taiwanese', 'Chinese（中文）、Taiwanese（臺語）'),
      ('China 中國', 'Chinese', 'Chinese'),
      ('America／the U.S.A. 美國', 'American', 'English'),
      ('Japan 日本', 'Japanese', 'Japanese'),
      ('Korea 韓國', 'Korean', 'Korean'),
    ], 'note': '國名、國家的人、語言第一個字母都要大寫。Taiwanese、Chinese、Japanese 單數複數同形：two Taiwanese。'},
    {'title': '常見的國名縮寫', 'head': ('縮寫', '全名', '中文'), 'rows': [
      ('R.O.C.', 'the Republic of China', '中華民國'),
      ('U.S.A.', 'the United States of America', '美國（美利堅合眾國）'),
      ('U.S.', 'the United States', '美國'),
      ('U.K.', 'the United Kingdom', '英國'),
    ], 'note': 'the United States、the United Kingdom 前面要加 the。'},
    {'title': '問別人從哪裡來', 'head': ('英文', '中文', ''), 'rows': [
      ('Where are you from?', '你從哪裡來？', ''),
      ('I\'m from Taiwan. / I come from Taiwan.', '我來自臺灣。', ''),
      ('He is American.', '他是美國人。', ''),
      ('How many countries are there in the world?', '世界上有幾個國家？', ''),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '世界', 'opts': ['word', 'world', 'country', 'America'], 'answer': 1, 'exp': 'world 世界；word 是「字」。'},
    {'type': 'mc', 'q': '國家', 'opts': ['city', 'town', 'country', 'world'], 'answer': 2, 'exp': 'country 國家。'},
    {'type': 'mc', 'q': '中國', 'opts': ['China', 'Chinese', 'Taiwan', 'America'], 'answer': 0, 'exp': 'China 中國；Chinese 中文、中國人。'},
    {'type': 'mc', 'q': '美國（縮寫）', 'opts': ['R.O.C.', 'U.K.', 'U.S.A.', 'Taiwan'], 'answer': 2, 'exp': 'U.S.A. = the United States of America。'},
  ]},
  {'title': '② 看英文選中文', 'items': [
    {'type': 'mc', 'q': 'R.O.C.', 'opts': ['中華民國', '美國', '英國', '中國'], 'answer': 0, 'exp': 'R.O.C. = the Republic of China 中華民國。'},
    {'type': 'mc', 'q': 'Taiwan', 'opts': ['泰國', '臺灣', '日本', '中國'], 'answer': 1, 'exp': 'Taiwan 臺灣。'},
    {'type': 'mc', 'q': 'America', 'opts': ['非洲', '亞洲', '歐洲', '美國；美洲'], 'answer': 3, 'exp': 'America 美國；美洲。'},
  ]},
  {'title': '③ 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數；國名第一個字母要大寫。', 'items': [
    {'q': '世界（w＿＿＿＿，5 個字母）：{0}', 'blanks': [['world']], 'exp': 'world。'},
    {'q': '國家（c＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['country']], 'exp': 'country。'},
    {'q': '美國（A＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['America']], 'exp': 'America，A 大寫。'},
    {'q': '臺灣（T＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['Taiwan']], 'exp': 'Taiwan，T 大寫。'},
  ]},
  {'title': '④ 國家、人、語言', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'I\'m from Taiwan. I\'m {0}. （臺灣人）', 'blanks': [['Taiwanese']], 'exp': 'Taiwanese 臺灣人。'},
    {'q': 'He comes from America. He is {0}. （美國人）', 'blanks': [['American']], 'exp': 'American 美國人。'},
    {'q': 'People in China speak {0}. （中文）', 'blanks': [['Chinese']], 'exp': 'Chinese 中文。'},
    {'q': 'country → (複數) {0}', 'blanks': [['countries']], 'exp': '子音 + y → countries。'},
    {'q': 'R.O.C. is short for the Republic of {0}. （中國）', 'blanks': [['China']], 'exp': 'R.O.C. = the Republic of China。'},
    {'q': 'U.S.A. is short for the United States of {0}. （美洲）', 'blanks': [['America']], 'exp': 'U.S.A. = the United States of America。'},
  ]},
  {'title': '⑤ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Where are you ______? — I\'m from Taiwan.', 'opts': ['from', 'in', 'at', 'to'], 'answer': 0, 'exp': 'Where are you from? 你從哪裡來？'},
    {'type': 'mc', 'q': '______ United States is a big country.', 'opts': ['The', 'A', 'An', '（不填）'], 'answer': 0, 'exp': 'the United States 要加 the。'},
    {'type': 'mc', 'q': 'There are about 200 ______ in the world.', 'opts': ['country', 'countries', 'countrys', 'world'], 'answer': 1, 'exp': '200 個國家 → countries。'},
    {'type': 'mc', 'q': 'People all over the ______ love music.', 'opts': ['world', 'worlds', 'a world', 'world\'s'], 'answer': 0, 'exp': 'all over the world 全世界。'},
    {'type': 'mc', 'q': 'Mary is from New York. She is ______.', 'opts': ['America', 'American', 'Chinese', 'Taiwan'], 'answer': 1, 'exp': '她是美國人 → American。'},
  ]},
]
