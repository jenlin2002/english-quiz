from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '知道什麼是倒裝、為什麼要倒裝',
    'never、seldom、little 放句首時，改成問句句型',
    '地方片語放句首時，動詞搬到主詞前',
    'Here comes the bus. 和 Here he comes. 的差別',
    '說 Here you are. / Here we are.'])),
  card('暖身 3 題', qas([
    ('Is he late? / He is late. 哪一句是問句句型？', 'Is he late?'),
    ('Look! Here ____ the bus. (come / comes)', 'comes'),
    ('— The salt, please. — Here ____. (you are / are you)', 'you are')]), 'o'))),

section('什麼是倒裝？', table(['種類', '怎麼倒', '例句'], [
  ['否定副詞放句首', '後面改成問句的樣子', ('Never <b>is he</b> late.', '他從不遲到')],
  ['地方片語放句首', '動詞搬到主詞前面', ('Under the tree <b>sat a cat</b>.', '樹下坐著一隻貓')],
  ['Here / There 放句首', '名詞主詞倒裝', ('Here <b>comes the bus</b>.', '公車來了')],
], audio_col=2) + note('倒裝是為了強調放在句首的字。原句：He is never late. → 強調 never → Never is he late.')),

section('否定副詞放句首：改成問句句型', table(['原句的動詞', '倒裝公式', '例句'], [
  ['be 動詞', 'Never + be + 主詞', ('Never <b>is he</b> late.', '他從不遲到')],
  ['一般動詞', 'Seldom + do / does / did + 主詞 + 原形', ('Seldom <b>does Ken go</b> to the movies.', 'Ken 很少去看電影')],
  ['助動詞', 'Never + will / can + 主詞 + 原形', ('Never <b>will I forget</b> this day.', '我永遠不會忘記這一天')],
  ['完成式', 'Never + have / has + 主詞 + p.p.', ('Never <b>have I seen</b> such a big fish.', '我從沒看過這麼大的魚')],
], audio_col=2) + note('否定副詞：never、seldom、rarely、hardly、little、few + 名詞')),

section('一般動詞的倒裝：借 do / does / did', cards(2,
  card('步驟', ul([
    '① 看原句時態：現在 → do / does；過去 → did',
    '② 把 do / does / did 放到主詞前面',
    '③ 原本的動詞變回原形']) +
    ex('He seldom <b>goes</b> out. → Seldom <b>does</b> he <b>go</b> out.', '→ goes 變 go'), sub='steps'),
  card('例句', ex('<i>Little did she know</i> the truth.', '→ knew 變 know', 'o') +
    ex('<i>Few books did he read</i> last summer.', '→ few + 名詞一起搬', 'o') +
    ex('<i>Rarely do they eat</i> fast food.', '→ 主詞 they → do', 'o'), 'o', sub='examples'))),

section('地方片語放句首', cards(2,
  card('動詞直接搬到主詞前', row('不用借 do；時態不變', '') +
    ex('<b>On the table is</b> a pen.', '→ 桌上有一支筆') +
    ex('<b>In the water are</b> five coins.', '→ 動詞看 five coins') +
    ex('<b>At the door stood</b> an old man.', '→ 門口站著一位老先生'), sub='place + V + S'),
  card('代名詞不倒裝', ex('Under the tree <i>she sat</i>.', '→ 不說 sat she', 'o') +
    row('判斷：', '主詞是名詞才倒裝；是代名詞就照原本順序'), 'o', sub='pronoun → no inversion'))),

section('Here、There 放句首', cards(2,
  card('名詞 vs 代名詞', ex('Here <b>comes the bus</b>.', '→ 名詞：倒裝') +
    ex('Here <b>it comes</b>.', '→ 代名詞：不倒裝') +
    ex('There <b>goes the train</b>. / There <b>she goes</b>.', '→ 同樣規則'), sub='Here / There'),
  card('常用說法', ex('— Two tickets, please. — <i>Here you are</i>.', '→ 給你', 'o') +
    ex('<i>Here we are</i>! This is the museum.', '→ 我們到了', 'o') +
    ex('<i>Here it is</i>! I found my key.', '→ 找到了', 'o'), 'o', sub='useful phrases'))),

section('學生最常錯的 5 句', top5([
  ('Never he is late.', 'Never is he late.', '要倒裝成問句句型。'),
  ('Seldom does he goes swimming.', 'Seldom does he go swimming.', '借了 does 用原形。'),
  ('Never I have seen a whale.', 'Never have I seen a whale.', 'have 移到主詞前。'),
  ('Here comes he.', 'Here he comes.', '代名詞不倒裝。'),
  ('On the desk is two books.', 'On the desk are two books.', '動詞看後面的主詞。'),
])),

section('快問快答 8 題', qas([
  ('Never ____ late. (he is / is he)', 'is he'),
  ('Seldom ____ TV. (does she watch / she watches)', 'does she watch'),
  ('Never ____ there. (have I been / I have been)', 'have I been'),
  ('Little ____ know. (did he / he did)', 'did he'),
  ('Here ____ the teacher. (comes / come)', 'comes'),
  ('Here ____. (she comes / comes she)', 'she comes'),
  ('In the box ____ two cats. (is / are)', 'are'),
  ('Hardly ____ hear you. (can I / I can)', 'can I'),
])),

section('改寫練習與下一步', two(div(lead('改成倒裝句'), qas([
  ('He never forgets my birthday.', 'Never does he forget my birthday.'),
  ('I have never tasted such sweet mangoes.', 'Never have I tasted such sweet mangoes.'),
  ('A little girl stood at the bus stop.', 'At the bus stop stood a little girl.'),
  ('The bus comes here.', 'Here comes the bus.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  'So do I（Unit 15）也是倒裝，可以一起複習']), 'o'))),
]

UNIT = {'no': 16, 'zh': '倒裝句', 'en': 'Inversion', 'c1': 'Never is he', 'c2': 'Here comes', 'slides': S}
