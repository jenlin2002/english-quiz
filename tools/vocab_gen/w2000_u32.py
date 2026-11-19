# 主題 2000 字 Unit 32：Conjunctions 連接詞（字表依課本單元；詞性、中文、例句、題目為本站自編）
# 功能詞沒有適合的照片，全部用 emoji。
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000', 'no': 32, 'en': 'Conjunctions', 'zh': '連接詞',
  'intro': '把兩個字或兩個句子接起來的字，共 12 個。注意：because 和 so、though 和 but 不能一起用。',
  'words': [
    W('and', 'conj.', '和；而且', '', 'I like apples and bananas.', '我喜歡蘋果和香蕉。', '➕'),
    W('as', 'conj./prep.', '當…時；因為；如同', 'as… as… 和…一樣', 'As I was walking home, it started to rain.', '我走路回家的時候，開始下雨了。', '🌦️'),
    W('because', 'conj.', '因為', '不和 so 一起用', 'I stayed home because I was sick.', '我待在家，因為我生病了。', '🤒'),
    W('but', 'conj.', '但是', '', 'The car is nice, but it\'s too expensive.', '這台車很好，但是太貴了。', '↩️'),
    W('however', 'adv.', '然而', '前後常加逗點', 'It was raining. However, we still went out.', '當時在下雨。然而我們還是出門了。', '🔀'),
    W('if', 'conj.', '如果；是否', '', 'If it rains tomorrow, we will stay home.', '如果明天下雨，我們就待在家。', '☔'),
    W('or', 'conj.', '或者；否則', '', 'Do you want tea or coffee?', '你要茶還是咖啡？', '🔁'),
    W('since', 'conj.', '自從；既然', '', 'Since you are here, let\'s start.', '既然你來了，我們就開始吧。', '📆'),
    W('than', 'conj.', '比', '比較級＋than', 'She is younger than I am.', '她比我年輕。', '📏'),
    W('that', 'conj.', '（引導名詞子句）', '常可以省略', 'I think that he is right.', '我認為他是對的。', '💭'),
    W('though', 'conj./adv.', '雖然；不過', '＝although，不和 but 一起用', 'Though he is old, he still runs every day.', '雖然他年紀大了，他還是每天跑步。', '🏃'),
    W('while', 'conj.', '當…的時候', '常接進行式', 'Mom called while I was taking a shower.', '我在洗澡的時候媽媽打電話來。', '🚿'),
  ],
  'focus': [
    {'title': '對等連接詞', 'head': ('連接詞', '關係', '例句'), 'rows': [
      ('and', '加上', 'He is tall and strong.'),
      ('but', '相反', 'He is tall but weak.'),
      ('or', '選擇；否則', 'Hurry up, or you\'ll be late.'),
      ('so', '結果', 'I was tired, so I went to bed.'),
    ], 'note': ''},
    {'title': '不能一起用的兩對', 'head': ('✗ 錯誤', '✓ 正確', ''), 'rows': [
      ('Because it rained, so we stayed home.', 'Because it rained, we stayed home. ／ It rained, so we stayed home.', ''),
      ('Though he is rich, but he is not happy.', 'Though he is rich, he is not happy. ／ He is rich, but he is not happy.', ''),
    ], 'note': 'because 和 so 選一個；though 和 but 選一個。'},
    {'title': '表示時間、條件的連接詞', 'head': ('連接詞', '意思', '例句'), 'rows': [
      ('when／as／while', '當…的時候', 'While I was reading, he came in.'),
      ('since', '自從；既然', 'I have known her since I was six.'),
      ('if', '如果', 'If you are free, call me.'),
    ], 'note': 'if、when 表示未來時，子句用現在式：If it rains tomorrow, …（不是 will rain）。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '然而', 'opts': ['however', 'whatever', 'because', 'though'], 'answer': 0, 'exp': 'however 然而。'},
    {'type': 'mc', 'q': '雖然', 'opts': ['through', 'though', 'thought', 'than'], 'answer': 1, 'exp': 'though 雖然。'},
    {'type': 'mc', 'q': '當…的時候', 'opts': ['which', 'white', 'while', 'whole'], 'answer': 2, 'exp': 'while 當…的時候。'},
  ]},
  {'title': '② 例句填空：寫出正確的連接詞', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'I stayed home {0} I was sick. （因為）', 'blanks': [['because']], 'exp': 'because 因為。'},
    {'q': 'Do you want tea {0} coffee? （或者）', 'blanks': [['or']], 'exp': 'or 或者。'},
    {'q': '{0} it rains tomorrow, we will stay home. （如果）', 'blanks': [['If', 'if']], 'exp': 'if 如果。'},
    {'q': 'The car is nice, {0} it\'s too expensive. （但是）', 'blanks': [['but']], 'exp': 'but 但是。'},
  ]},
  {'title': '③ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'He is tall, ______ he isn\'t strong.', 'opts': ['and', 'or', 'but', 'so'], 'answer': 2, 'exp': '前後相反 → but。'},
    {'type': 'mc', 'q': 'Hurry up, ______ you\'ll miss the bus.', 'opts': ['and', 'or', 'but', 'because'], 'answer': 1, 'exp': '否則 → or。'},
    {'type': 'mc', 'q': '______ he is old, he still runs every day.', 'opts': ['Though', 'Because', 'If', 'Or'], 'answer': 0, 'exp': '雖然 → Though（後面不加 but）。'},
    {'type': 'mc', 'q': 'Mom called ______ I was taking a shower.', 'opts': ['while', 'than', 'or', 'but'], 'answer': 0, 'exp': '正在…的時候 → while。'},
    {'type': 'mc', 'q': 'I have known her ______ I was six.', 'opts': ['for', 'since', 'if', 'than'], 'answer': 1, 'exp': '自從 → since。'},
    {'type': 'mc', 'q': 'She is younger ______ I am.', 'opts': ['that', 'then', 'than', 'as'], 'answer': 2, 'exp': '比較 → than。'},
    {'type': 'mc', 'q': 'I think ______ he is right.', 'opts': ['that', 'what', 'if', 'or'], 'answer': 0, 'exp': 'I think that… 我認為…。'},
    {'type': 'mc', 'q': 'Exercise takes time; ______, it\'s good for your health.', 'opts': ['and', 'however', 'because', 'if'], 'answer': 1, 'exp': '然而 → however。'},
    {'type': 'mc', 'q': 'Run ______ fast ______ you can!', 'opts': ['as… as', 'so… that', 'more… than', 'if… or'], 'answer': 0, 'exp': 'as fast as you can 盡你所能地快。'},
  ]},
]
