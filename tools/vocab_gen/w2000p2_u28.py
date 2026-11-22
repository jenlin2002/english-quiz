# 主題 2000 字 PART 2 Unit 28：Pronouns & reflexives 代名詞與反身代名詞（字表依課本 PART 2 印刷頁 167：none；中文、例句、題目自編）
# 課本 PART 2 沒有 Unit 27、29。
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 28, 'en': 'Pronouns & reflexives', 'zh': '代名詞與反身代名詞',
  'intro': 'PART 2 的代名詞只有一個字：none「一個也沒有」。用在三者以上；兩者之間用 neither。',
  'words': [
    W('none', 'pron.', '一個也沒有；一點也沒有', 'none of + 名詞（三者以上）；兩者用 neither', 'None of my friends can swim.', '我的朋友沒有一個會游泳。', '🚫'),
  ],
  'focus': [
    {'title': 'none、neither、no one', 'head': ('字', '用法', ''),
     'rows': [('none', '三者以上「一個也沒有」：None of the students…', ''), ('neither', '兩者「都不」：Neither of my parents…', ''), ('no one', '「沒有人」，只指人：No one knows.', '')],
     'note': '問 How many…? 回答「一個都沒有」說 None.；問 Who…? 回答「沒有人」說 No one.'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=28, n_ce=0, n_ec=0, n_sp=1, fill=[
  F('I have three sisters, but ______ of them can cook.', ['none', 'neither', 'no one', 'nothing'], 0, '三個以上 → none。'),
  F('I have two brothers. ______ of them likes math.', ['Neither', 'None', 'No one', 'Nothing'], 0, '兩個 → neither。'),
  F('"How many apples are left?" "______. We ate them all."', ['None', 'Neither', 'No one', 'Nobody'], 0, '問數量，一個都沒有 → None.'),
  F('"Who is in the classroom?" "______. Everyone went home."', ['No one', 'None', 'Neither', 'Nothing'], 0, '問人，沒有人 → No one.'),
])
