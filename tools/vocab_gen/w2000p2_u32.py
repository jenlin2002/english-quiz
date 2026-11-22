# 主題 2000 字 PART 2 Unit 32：Conjunctions 連接詞（字表依課本 PART 2 印刷頁 168：besides、therefore；中文、例句、題目自編）
# 課本 PART 2 沒有 Unit 33。
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 32, 'en': 'Conjunctions', 'zh': '連接詞',
  'intro': '兩個用來連接句意的副詞：besides（而且、此外）和 therefore（因此）。注意 besides 和 beside（在旁邊）只差一個 s。',
  'words': [
    W('besides', 'adv. / prep.', '而且；此外；除了…還有', 'beside 是「在旁邊」', 'I\'m too tired to go out. Besides, it\'s raining.', '我太累了不想出門，而且外面在下雨。', '➕'),
    W('therefore', 'adv.', '因此；所以', '= so（比較正式）', 'He studied hard; therefore, he passed the exam.', '他很用功，因此通過了考試。', '∴'),
  ],
  'focus': [
    {'title': '容易搞混', 'head': ('字', '意思', ''),
     'rows': [('besides', '而且；除了…之外還有', ''), ('beside', '在…旁邊', ''), ('therefore', '因此（結果）', ''), ('because', '因為（原因）', '')],
     'note': 'therefore 前面常用分號或句號，後面加逗號：…; therefore, …'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=32, n_ce=0, n_ec=0, n_sp=2, fill=[
  F('I don\'t want to go to the movies. ______, I have homework to do.', ['Besides', 'Therefore', 'Beside', 'Because'], 0, '再加一個理由 → Besides 而且。'),
  F('It was raining hard; ______, the game was canceled.', ['therefore', 'besides', 'beside', 'because'], 0, '前面是原因，後面是結果 → therefore。'),
  F('Come and sit ______ me.', ['beside', 'besides', 'therefore', 'because'], 0, '在旁邊 → beside（沒有 s）。'),
  F('______ English, she can speak Japanese and Korean.', ['Besides', 'Beside', 'Therefore', 'Because'], 0, '除了英文還會… → Besides。'),
])
