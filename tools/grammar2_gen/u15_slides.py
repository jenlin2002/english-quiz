from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '用 too 和 so 說「…也是」',
    '用 either、neither、nor 說「…也不」',
    '選對助動詞（be、do、did、can、have）',
    '在對話裡附和或表示不同意'])),
  card('暖身 3 題', qas([
    ('— I like cats. — ____ do I. (So / Neither)', 'So'),
    ('— I can\'t swim. — ____ can I. (So / Neither)', 'Neither'),
    ('I don\'t eat fish, and he doesn\'t, ____. (too / either)', 'either')]), 'o'))),

section('肯定的附和句：…也是', cards(2,
  card('too：放句尾', row('主詞 + 助動詞, too', '') +
    ex('Ken likes cats, and <b>I do, too</b>.', '→ 我也是') +
    ex('My dad was at home, and <b>I was, too</b>.', '→ 我也在家'), sub='… , too'),
  card('so：倒裝', row('so + 助動詞 + 主詞', '') +
    ex('Ken likes cats, and <i>so do I</i>.', '→ 不是 so I do', 'o') +
    ex('My dad was at home, and <i>so was I</i>.', '→ 倒裝', 'o'), 'o', sub='so + 助動詞 + 主詞'))),

section('否定的附和句：…也不', cards(2,
  card('either：放句尾', row('主詞 + 助動詞 + not, either', '') +
    ex('I can\'t swim, and <b>Amy can\'t, either</b>.', '→ Amy 也不會') +
    row('注意：', '否定句用 either，不用 too'), sub='… , either'),
  card('neither / nor：倒裝', row('neither + 助動詞 + 主詞', '') +
    ex('I can\'t swim, and <i>neither can Amy</i>.', '→ 不再加 not', 'o') +
    ex('I can\'t swim, <i>nor can Amy</i>.', '→ nor 也可以', 'o') +
    ex('Tom never cries, and <i>neither does</i> his sister.', '→ never 是否定', 'o'), 'o', sub='neither + 助動詞 + 主詞'))),

section('助動詞怎麼選？', table(['前面用', '附和句用', '例句'], [
  ['be 動詞', 'be 動詞', ('She is tired, and <b>so am I</b>.', '她累了，我也是')],
  ['現在式一般動詞', 'do / does', ('I love pizza, and <b>so does my brother</b>.', '我愛披薩，我哥也是')],
  ['過去式一般動詞', 'did', ('Leo went to the zoo, and <b>so did Amy</b>.', 'Leo 去了動物園，Amy 也是')],
  ['can / will', '同一個', ('Mia can\'t drive, and <b>neither can her dad</b>.', 'Mia 不會開車，她爸也不會')],
  ['have / has + p.p.', 'have / has', ('I\'ve been to Japan, and <b>so has Ken</b>.', '我去過日本，Ken 也去過')],
], audio_col=2) + note('時態要和前面相同；單複數看「新的主詞」：My parents like jazz, and so does my uncle.')),

section('對話裡的附和與不同意', table(['對方說', '我也是／我也不', '我不一樣'], [
  [('I like spicy food.', '我喜歡辣'), 'So do I. / Me too.', 'Oh, I don\'t.'],
  [('I\'m not tired.', '我不累'), 'Neither am I. / Me neither.', 'Really? I am.'],
  [('I can\'t sing.', '我不會唱歌'), 'Neither can I.', 'I can.'],
  [('I went to the party.', '我去了派對'), 'So did I.', 'I didn\'t.'],
], audio_col=0) + note('Me too／Me neither 是口語；寫句子時多用 So do I／Neither do I。')),

section('學生最常錯的 5 句', top5([
  ('Amy likes dogs, and so am I.', 'Amy likes dogs, and so do I.', 'likes 是一般動詞 → do。'),
  ('I don\'t eat fish, and Ken doesn\'t, too.', '…, and Ken doesn\'t, either.', '否定句用 either。'),
  ('He can\'t swim, and neither can\'t I.', '…, and neither can I.', 'neither 不再加 not。'),
  ('She went home, and so does Tom.', 'She went home, and so did Tom.', '時態要相同。'),
  ('Ella never eats meat, and so does Lily.', '…, and neither does Lily.', 'never 是否定。'),
])),

section('快問快答 8 題', qas([
  ('— I\'m happy. — So ____ I.', 'am'),
  ('— I like tea. — So ____ I.', 'do'),
  ('— I went home. — So ____ I.', 'did'),
  ('— I can\'t cook. — Neither ____ I.', 'can'),
  ('— I haven\'t eaten. — Neither ____ I.', 'have'),
  ('He isn\'t here, and she isn\'t, ____.', 'either'),
  ('My sisters sing, and so ____ my brother.', 'does'),
  ('— I never lie. — ____ do I.', 'Neither'),
])),

section('改寫練習與下一步', two(div(lead('換一種說法'), qas([
  ('Ken is tall, and I am, too.', 'Ken is tall, and so am I.'),
  ('Amy can\'t swim, and Ben can\'t, either.', 'Amy can\'t swim, and neither can Ben.'),
  ('Both my mom and I like cooking.', 'My mom likes cooking, and so do I.'),
  ('Neither Tom nor Jay went.', 'Tom didn\'t go, and neither did Jay.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '助動詞的選法和 Unit 14 附加問句一樣，可以一起複習']), 'o'))),
]

UNIT = {'no': 15, 'zh': '附和句', 'en': 'So do I / Neither do I', 'c1': '我也是', 'c2': '我也不', 'slides': S}
