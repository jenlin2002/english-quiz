from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '把直接問句放進 Do you know…? 變成間接問句',
    '間接問句用「疑問詞 + 主詞 + 動詞」',
    '拿掉 do／does／did，把時態還給動詞',
    'Yes／No 問句改用 if／whether',
    '轉述別人說的話（said that、asked if）'])),
  card('暖身 3 題', qas([
    ('Do you know where ____? (is he / he is)', 'he is'),
    ('I don\'t know what ____. (does she want / she wants)', 'she wants'),
    ('I wonder ____ it will rain. (if / what)', 'if')]), 'o'))),

section('直接問句 vs 間接問句', table(['直接問句', '間接問句'], [
  [('Who <b>is the girl</b>?', '那女孩是誰？'), 'Do you know who the girl is?'],
  [('Where <b>is</b> the restroom?', '廁所在哪？'), 'Can you tell me where the restroom is?'],
  [('What time <b>will he</b> come?', '他幾點來？'), 'I don\'t know what time he will come.'],
], audio_col=0) + note('間接問句的語序：疑問詞 + 主詞 + 動詞（像直述句，不倒裝）')),

section('拿掉 do／does／did', cards(2,
  card('時態還給動詞', table(['直接問句', '間接問句'], [
    ['Where does he live?', 'where he lives'], ['What did she buy?', 'what she bought'], ['When do they leave?', 'when they leave']]), sub='does → -s；did → 過去式'),
  card('例句', ex('Do you know where he <i>lives</i>?', '→ 不是 where does he live', 'o') +
    ex('I wonder what she <i>bought</i>.', '→ 不是 what did she buy', 'o') +
    ex('Tell me when they <i>leave</i>.', '→ do 拿掉、原形', 'o'), 'o', sub='examples'), tight=True)),

section('Yes／No 問句與疑問詞當主詞', cards(2,
  card('Yes／No 問句：if / whether', ex('Is he a doctor? → I\'m not sure <b>if he is</b> a doctor.', '→ 是否') +
    ex('Did she pass? → I don\'t know <b>if she passed</b>.', '→ 拿掉 did') +
    ex('Will he come? → Nobody knows <b>whether he will come</b>.', '→ 是否：未來用 will'), sub='if = whether（是否）'),
  card('疑問詞當主詞：語序不變', ex('Who broke the window? → Do you know <i>who broke</i> the window?', '→ 不用改', 'o') +
    ex('What happened? → Tell me <i>what happened</i>.', '→ 不用改', 'o'), 'o', sub='Who / What + V'))),

section('問號還是句號？時態一致', cards(2,
  card('看前面的主要句子', ex('<b>Do you know</b> where he lives?', '→ 主要句子是問句：問號') +
    ex('<b>I don\'t know</b> where he lives.', '→ 直述句：句號') +
    ex('<b>Tell me</b> where it is.', '→ 祈使句：句號'), sub='? or .'),
  card('主要句子是過去式', ex('Where is the station? → He <i>asked</i> where the station <i>was</i>.', '→ is → was', 'o') +
    ex('Can you swim? → She <i>asked</i> if I <i>could</i> swim.', '→ can → could', 'o') +
    row('事實可保留現在式：', 'asked what the capital of Japan is'), 'o', sub='時態往過去退'))),

section('轉述別人說的話', table(['原本的話', '轉述'], [
  [('Amy said, "I am tired."', 'Amy 說：「我累了。」'), 'Amy said (that) she was tired.'],
  [('Ken said to me, "I like your bag."', 'Ken 對我說：「我喜歡你的包包。」'), 'Ken told me (that) he liked my bag.'],
  [('Mom asked, "Are you hungry?"', '媽媽問：「你餓嗎？」'), 'Mom asked me if I was hungry.'],
  [('He asked, "Where do you live?"', '他問：「你住哪？」'), 'He asked where I lived.'],
  [('The teacher said, "Be quiet."', '老師說：「安靜。」'), 'The teacher told us to be quiet.'],
], audio_col=0) + note('人稱跟著換（I → she、your → my），時態往過去退（am → was、can → could、will → would）。')),

section('學生最常錯的 5 句', top5([
  ('Do you know where is the post office?', 'Do you know where the post office is?', '主詞 + 動詞。'),
  ('I don\'t know where does he live.', 'I don\'t know where he lives.', '拿掉 does，加 -s。'),
  ('Can you tell me what did she buy?', 'Can you tell me what she bought?', '拿掉 did，改過去式。'),
  ('I wonder is he at home.', 'I wonder if he is at home.', 'Yes／No 問句加 if。'),
  ('I don\'t know where he lives?', 'I don\'t know where he lives.', '直述句用句號。'),
])),

section('快問快答 8 題', qas([
  ('Where is Ken? → I don\'t know where ____.', 'Ken is'),
  ('Who is she? → Do you know who ____?', 'she is'),
  ('Where does Amy work? → Tell me where ____.', 'Amy works'),
  ('What did he say? → I wonder what ____.', 'he said'),
  ('Is it true? → I\'m not sure ____ true.', 'if it is'),
  ('Who took it? → Do you know who ____ it?', 'took'),
  ('"I am busy," said Ben. → Ben said he ____ busy.', 'was'),
  ('"Sit down," said Mr. Lee. → He told us ____ down.', 'to sit'),
])),

section('改寫練習與下一步', two(div(lead('改成間接問句或轉述'), qas([
  ('What time does the shop open?（I don\'t know…）', 'I don\'t know what time the shop opens.'),
  ('Did they win?（Do you know…）', 'Do you know if they won?'),
  ('Mom asked, "Do you want milk?"', 'Mom asked me if I wanted milk.'),
  ('Lily said, "I am happy."', 'Lily said that she was happy.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '第一期 Week 15、16 的週測驗可以當綜合練習']), 'o'))),
]

UNIT = {'no': 19, 'zh': '直接問句與間接問句', 'en': 'Direct & Indirect Questions', 'c1': 'Where is he?', 'c2': 'where he is', 'slides': S}
