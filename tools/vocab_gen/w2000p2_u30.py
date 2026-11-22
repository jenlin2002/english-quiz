# 主題 2000 字 PART 2 Unit 30：Be & auxiliaries be 動詞與助動詞（字表依課本 PART 2 印刷頁 167：shall；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 30, 'en': 'Be & auxiliaries', 'zh': 'be 動詞與助動詞',
  'intro': 'PART 2 的助動詞只有 shall。現在最常用在提議：Shall we…?（我們…好嗎？）、Shall I…?（要我…嗎？）。',
  'words': [
    W('shall', 'aux.', '將會；（問句）…好嗎', 'Shall we…? 我們…好嗎？；Shall I…? 要我…嗎？', 'Shall we go to the park after lunch?', '午餐後我們去公園好嗎？', '🤝'),
  ],
  'focus': [
    {'title': 'Shall 的用法', 'head': ('句型', '意思', ''),
     'rows': [('Shall we + 原形動詞?', '我們…好嗎？（提議）', ''), ('Shall I + 原形動詞?', '要我…嗎？（主動幫忙）', ''), ('Let\'s…, shall we?', '我們…吧，好嗎？', '')],
     'note': 'shall 後面接原形動詞，和 will、can 一樣。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=30, n_ce=0, n_ec=0, n_sp=1, fill=[
  F('It\'s a nice day. ______ we go for a walk?', ['Shall', 'Do', 'Are', 'Does'], 0, '提議 → Shall we…?'),
  F('Your bag looks heavy. Shall I ______ it for you?', ['carry', 'carries', 'carrying', 'to carry'], 0, 'shall 後面接原形動詞 carry。'),
  F('Let\'s sing a song, ______ we?', ['shall', 'will', 'do', 'are'], 0, 'Let\'s…, shall we? 附加問句。'),
])
