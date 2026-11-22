# 主題 2000 字 PART 2 Unit 5：Forms of address 稱謂的形式（字表依課本 PART 2 印刷頁 148：ma'am／madam；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 5, 'en': 'Forms of address', 'zh': '稱謂的形式',
  'intro': '對女士有禮貌的稱呼：ma\'am 和 madam（對男士說 sir）。在商店、餐廳常聽到。',
  'words': [
    W('ma\'am', 'n.', '女士；夫人（禮貌稱呼）', '= madam 的口語縮寫；對男士說 sir', 'Can I help you, ma\'am?', '女士，需要幫忙嗎？', '🙋‍♀️', say='mam'),
    W('madam', 'n.', '女士；夫人（禮貌稱呼）', '比 ma\'am 正式；Dear Madam 敬啟者（寫信）', 'Excuse me, madam. Is this your bag?', '不好意思，女士，這是您的包包嗎？', '👜'),
  ],
  'focus': [
    {'title': '禮貌的稱呼', 'head': ('對誰', '稱呼', ''),
     'rows': [('女士', 'ma\'am／madam', ''), ('先生', 'sir', ''), ('知道姓氏時', 'Mr. Lin／Ms. Lin', '')],
     'note': '不知道對方名字時，用 sir 或 ma\'am 最禮貌。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=5, n_ce=0, n_ec=0, n_sp=1, fill=[
  F('A waiter says to a woman: "Here is your coffee, ______."', ['ma\'am', 'sir', 'Mr.', 'boy'], 0, '對女士 → ma\'am。'),
  F('A clerk says to a man: "Can I help you, ______?"', ['madam', 'ma\'am', 'sir', 'lady'], 2, '對男士 → sir。'),
  F('"Dear ______," is a polite way to start a letter to a woman you don\'t know.', ['Madam', 'Sir', 'Mr.', 'Kid'], 0, 'Dear Madam 用在給不認識的女士的信。'),
])
