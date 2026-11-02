from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '分辨形容詞和副詞：修飾動詞要用副詞',
    '把形容詞變成副詞（-ly、well、fast、hard）',
    '頻率副詞放對位置，會問 How often',
    '用 too…to、enough to、so…that、such…that',
    '寫出副詞的比較級和最高級'])),
  card('暖身 3 題', qas([
    ('She sings ____. (beautiful / beautifully)', 'beautifully'),
    ('He plays soccer ____. (good / well)', 'well'),
    ('I ____ get up early. (always / am always)', 'always')]), 'o'))),

section('副詞的種類', table(['種類', '回答', '例子'], [
  ['狀態副詞', '怎麼做？', ('She sings <b>beautifully</b>.', '她唱得很好聽')],
  ['地方副詞', '在哪裡？', ('Come <b>here</b>.', '過來這裡')],
  ['時間副詞', '什麼時候？', ('I\'ll call you <b>tomorrow</b>.', '我明天打給你')],
  ['頻率副詞', '多常？', ('He <b>often</b> walks to school.', '他常走路上學')],
  ['程度副詞', '多麼？', ('The test was <b>really</b> hard.', '考試真的很難')],
  ['修飾整句', '看法', ('<b>Luckily</b>, nobody was hurt.', '幸好沒有人受傷')],
], audio_col=2) + note('形容詞修飾名詞；副詞修飾動詞、形容詞、副詞、整個句子。')),

section('副詞的形成', cards(2,
  card('形容詞 + -ly', table(['規則', '例子'], [
    ['一般加 -ly', 'quick → quickly'], ['子音 + y → -ily', 'happy → happily'],
    ['-le → -ly', 'gentle → gently'], ['不規則', 'good → well']]) +
    ex('He drives <b>carefully</b>.', '→ 不是 drives careful'), sub='-ly'),
  card('同形與意思不同', row('同形：', 'fast、hard、early、late、high') +
    ex('He runs <i>fast</i>.', '→ 沒有 fastly', 'o') +
    row('加 -ly 變意思：', 'hardly 幾乎不、lately 最近、nearly 幾乎') +
    ex('I can <i>hardly</i> hear you.', '→ 幾乎聽不到', 'o'), 'o', sub='注意 friendly、lovely 是形容詞'), tight=True)),

section('副詞的位置', cards(2,
  card('一般規則', row('① 狀態副詞在動詞或受詞後面', '') +
    ex('He finished his work <b>carefully</b>.', '→ 不放在動詞和受詞中間') +
    row('② 狀態 → 地方 → 時間', '') +
    ex('Bob studied <b>hard at home yesterday</b>.', '→ 怎樣、哪裡、何時'), sub='position'),
  card('遇到片語動詞', row('可拆開（take off）：副詞放前面或句尾', '') +
    ex('She <i>quickly</i> took off her coat.', '→ 不能塞中間', 'o') +
    row('不可拆開（look at）：中間可以放', '') +
    ex('Sam looked <i>carefully</i> at the map.', '→ look carefully at', 'o'), 'o', sub='Unit 7 複習'))),

section('頻率副詞', cards(2,
  card('由多到少', row('always → usually → often → sometimes → seldom → never', '') +
    ex('He <b>is always</b> on time.', '→ be 動詞後面') +
    ex('She <b>usually takes</b> the bus.', '→ 一般動詞前面') +
    ex('You <b>should always tell</b> the truth.', '→ 助動詞中間'), sub='be 後、一般前、助動詞中間'),
  card('How often 與否定', ex('<i>How often</i> do you exercise?', '→ 問頻率', 'o') +
    ex('Three times a week.', '→ once、twice、three times', 'o') +
    ex('He <i>never</i> eats breakfast.', '→ never 不再加 not', 'o'), 'o', sub='How often…?'))),

section('still、already、yet', table(['副詞', '意思', '例句'], [
  ['still', '仍然', ('It\'s <b>still</b> raining.', '還在下雨')],
  ['still（否定）', '放 not 前面', ('He <b>still</b> can\'t swim.', '他還是不會游泳')],
  ['already', '已經（肯定句）', ('I\'ve <b>already</b> eaten.', '我已經吃過了')],
  ['yet', '還沒（否定句，句尾）', ('I haven\'t eaten <b>yet</b>.', '我還沒吃')],
  ['yet', '已經…了嗎（問句，句尾）', ('Have you eaten <b>yet</b>?', '你吃過了嗎？')],
], audio_col=2)),

section('程度副詞：too、enough、so、such', table(['句型', '意思', '例句'], [
  ['too + adj. + to V', '太…而不能', ('The soup is <b>too hot to</b> eat.', '湯太燙不能喝')],
  ['adj. + enough + to V', '夠…可以', ('He ran <b>fast enough to</b> win.', '他跑得夠快，贏了')],
  ['so + adj. + that', '如此…以致於', ('It was <b>so cold that</b> we stayed home.', '太冷了，我們待在家')],
  ['such + a + adj. + N + that', '如此…的（名詞）', ('It was <b>such a cold day that</b> we stayed home.', '那天好冷，我們待在家')],
], audio_col=2) + note('後面沒有名詞用 so；後面有名詞用 such。too…to = so…that + can\'t。')),

section('副詞的比較級與最高級', cards(2,
  card('變化規則', table(['規則', '例子'], [
    ['同形單音節：-er / -est', 'fast → faster → fastest'], ['early', 'earlier → earliest'],
    ['-ly 副詞：more / most', 'slowly → more slowly'], ['不規則', 'well → better → best']]), sub='forms'),
  card('例句', ex('Amy runs <b>faster than</b> Ben.', '→ 比較級') +
    ex('Please drive <i>more slowly</i>.', '→ 不說 slowlier', 'o') +
    ex('Steve works <b>the hardest</b> in the company.', '→ 副詞最高級，the 可省略') +
    ex('She sings <i>better than</i> me.', '→ well 的比較級', 'o'), 'o', sub='examples'), tight=True)),

section('學生最常錯的 5 句', top5([
  ('She speaks English very good.', 'She speaks English very well.', '修飾動詞用副詞 well。'),
  ('He runs very fastly.', 'He runs very fast.', 'fast 沒有 -ly。'),
  ('I studied hardly for the test.', 'I studied hard for the test.', 'hardly 是「幾乎不」。'),
  ('He goes always to school by bus.', 'He always goes to school by bus.', '頻率副詞放一般動詞前。'),
  ('It was so a nice day.', 'It was such a nice day.', '有名詞用 such。'),
])),

section('快問快答 8 題', qas([
  ('He drives ____. (careful / carefully)', 'carefully'),
  ('She swims ____. (good / well)', 'well'),
  ('I can ____ believe it! (hard / hardly)', 'hardly'),
  ('She ____ late. (is never / never is)', 'is never'),
  ('____ do you play tennis? (How often / How long)', 'How often'),
  ('I haven\'t finished ____. (already / yet)', 'yet'),
  ('It was ____ a funny movie. (so / such)', 'such'),
  ('Please speak ____. (more slowly / slowlier)', 'more slowly'),
])),

section('改寫練習與下一步', two(div(lead('同義改寫'), qas([
  ('He is a careful driver.', 'He drives carefully.'),
  ('She is a good swimmer.', 'She swims well.'),
  ('The tea is too hot to drink.', 'The tea is so hot that I can\'t drink it.'),
  ('She is so kind a girl.', 'She is such a kind girl.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整說明和整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '形容詞的比較可以回 Unit 10 複習']), 'o'))),
]

UNIT = {'no': 11, 'zh': '副詞', 'en': 'Adverbs', 'c1': '怎樣・多常', 'c2': '多麼', 'slides': S}
