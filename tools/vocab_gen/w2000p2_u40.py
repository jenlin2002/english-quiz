# 主題 2000 字 PART 2 Unit 40：Other adverbs 其他副詞（字表依課本 PART 2 印刷頁 187–188，10 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 40, 'en': 'Other adverbs', 'zh': '其他副詞',
  'card': 'altogether、especially、hardly、nearly、rather、aloud、everywhere、neither、nor… 共 10 字',
  'intro': '其他副詞，共 10 個。hardly 是「幾乎不」（本身就是否定，不要再加 not）；neither…nor… 是「既不…也不…」；would rather 是「寧願」。',
  'words': [
    W('altogether', 'adv.', '總共；完全', 'all together 是「全部一起」', 'There are thirty students altogether.', '總共有三十個學生。', '🧮'),
    W('especially', 'adv.', '尤其；特別', 'special → especially', 'I love fruit, especially mangoes.', '我喜歡水果，尤其是芒果。', '⭐'),
    W('hardly', 'adv.', '幾乎不', '本身是否定，不再加 not；hard 是「努力地」', 'I can hardly hear you.', '我幾乎聽不到你說話。', '🤏'),
    W('nearly', 'adv.', '幾乎；差不多', '= almost', 'It\'s nearly ten o\'clock.', '快十點了。', '⏳'),
    W('rather', 'adv.', '寧願；相當', 'would rather + 原形動詞 寧願…', 'I\'d rather stay home tonight.', '我今晚寧願待在家。', '🏠'),
    W('aloud', 'adv.', '大聲地；出聲地', 'read aloud 朗讀', 'Please read the story aloud.', '請把故事大聲唸出來。', '📢'),
    W('everywhere', 'adv.', '到處', 'every + where', 'I looked everywhere for my cat.', '我到處找我的貓。', '🔍'),
    W('anywhere', 'adv.', '任何地方', '多用在否定句和問句', 'I can\'t find my keys anywhere.', '我到處都找不到我的鑰匙。', '❓'),
    W('neither', 'adv.', '也不', 'Neither do I. 我也不', '"I don\'t like snakes." "Neither do I."', '「我不喜歡蛇。」「我也不喜歡。」', '🙅'),
    W('nor', 'conj.', '也不', 'neither A nor B 既不 A 也不 B', 'He can neither swim nor ride a bike.', '他既不會游泳也不會騎腳踏車。', '🚫'),
  ],
  'focus': [
    {'title': '容易用錯的副詞', 'head': ('句子', '說明', ''),
     'rows': [('I can hardly see.', 'hardly 已經是否定，不說 can\'t hardly', ''), ('I\'d rather walk.', 'would rather + 原形動詞', ''), ('Neither do I.', '附和否定句「我也不」', ''), ('neither A nor B', '既不 A 也不 B', '')],
     'note': 'nearly = almost；especially 用在「尤其是…」。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=40, n_ce=6, n_ec=5, n_sp=5, fill=[
  F('It\'s so dark. I can ______ see anything.', ['hardly', 'hard', 'nearly', 'rather'], 0, '幾乎看不到 → hardly。'),
  F('I\'d ______ walk than take the bus.', ['rather', 'hardly', 'nearly', 'neither'], 0, 'would rather 寧願。'),
  F('"I don\'t eat meat." "______ do I."', ['Neither', 'Nor', 'So', 'Either'], 0, '附和否定句 → Neither do I.'),
  F('She likes all sports, ______ basketball.', ['especially', 'altogether', 'aloud', 'anywhere'], 0, '尤其是 → especially。'),
  F('He neither called ______ wrote to me.', ['nor', 'or', 'neither', 'and'], 0, 'neither A nor B。'),
  F('There are flowers ______ in the park.', ['everywhere', 'anywhere', 'altogether', 'nearly'], 0, '到處都是 → everywhere。'),
  F('It\'s ______ midnight. Go to bed!', ['nearly', 'hardly', 'aloud', 'rather'], 0, '快半夜了 → nearly = almost。'),
])
