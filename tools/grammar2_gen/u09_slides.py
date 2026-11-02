from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '正確選用主格、受格、所有格、所有代名詞、反身代名詞',
    '分清楚 one … the other、another、others、the others',
    '知道什麼時候用 it、什麼時候用 one',
    '用 both、either、neither、all、any、none 並配對動詞',
    '看懂部分否定 not all、not both'])),
  card('暖身 3 題', qas([
    ('This book is ____. (my / mine)', 'mine'),
    ('She hurt ____. (her / herself)', 'herself'),
    ('I have two pens. One is red; ____ is blue. (another / the other)', 'the other')]), 'o'))),

section('人稱代名詞總表', table(['人稱', '主格', '受格', '所有格', '所有代名詞', '反身'], [
  ['我', 'I', 'me', 'my', 'mine', 'myself'],
  ['你', 'you', 'you', 'your', 'yours', 'yourself'],
  ['他／她', 'he / she', 'him / her', 'his / her', 'his / hers', 'himself / herself'],
  ['它', 'it', 'it', 'its', '—', 'itself'],
  ['我們', 'we', 'us', 'our', 'ours', 'ourselves'],
  ['你們', 'you', 'you', 'your', 'yours', 'yourselves'],
  ['他們', 'they', 'them', 'their', 'theirs', 'themselves'],
]) + note('動詞前當主詞用主格；動詞、介系詞後面用受格。its（它的）沒有撇號，it\'s = it is。')),

section('所有代名詞', cards(2,
  card('後面不接名詞', ex('This is <b>my</b> bag. = This bag is <b>mine</b>.', '→ 不能說 mine bag') +
    ex('I found my umbrella, but Sara can\'t find <b>hers</b>.', '→ hers = her umbrella'), sub='所有格 + 名詞 = 所有代名詞'),
  card('比較同類、雙重所有格', ex('My phone is newer than <i>yours</i>.', '→ 手機比手機，不是 than you', 'o') +
    ex('Kevin is <i>a friend of mine</i>.', '→ 不說 a my friend', 'o'), 'o', sub='常考'))),

section('反身代名詞', cards(2,
  card('兩種用法', row('① 主詞＝受詞', '') +
    ex('Don\'t cut <b>yourself</b>.', '→ 別割到自己') +
    row('② 強調「親自」', '') +
    ex('I made this cake <b>myself</b>.', '→ 我自己做的'), sub='-self / -selves'),
  card('常用片語', table(['片語', '意思'], [
    ['by oneself', '獨自'], ['enjoy oneself', '玩得愉快'], ['help oneself (to)', '自己拿'], ['teach oneself', '自學']]) +
    ex('We <i>enjoyed ourselves</i> at the party.', '→ 玩得很開心', 'o'), 'o', sub='不能當主詞'), tight=True)),

section('one、another、the other、others', table(['情況', '句型', '例句'], [
  ['兩個', 'one … the other', ('I have two cats. One is black, and <b>the other</b> is white.', '一隻黑、另一隻白')],
  ['三個', 'one … another … the other', ('One is red, <b>another</b> is blue, and <b>the other</b> is green.', '紅、藍、最後一個綠')],
  ['其餘全部', 'one / some … the others', ('Some walk to school; <b>the others</b> take the bus.', '其餘的人搭公車')],
  ['另一些（沒說完）', 'some … others', ('Some people like coffee; <b>others</b> like tea.', '有些人喜歡茶')],
  ['再一個', 'another', ('Can I try <b>another</b>?', '我可以試另一件嗎？')],
], audio_col=2) + note('有 the＝範圍固定、說完就沒了：the other（最後一個）、the others（剩下全部）。')),

section('one、ones 和 it', cards(2,
  card('it：就是那一個', ex('I lost my pen. I can\'t find <b>it</b>.', '→ 找的是原本那支') +
    ex('Do you like the red bike? I want to buy <b>it</b>.', '→ 就是那台'), sub='同一個東西'),
  card('one / ones：同類的任一個', ex('I need to buy a new <i>one</i>.', '→ 另一支筆', 'o') +
    ex('These shoes are small. I want bigger <i>ones</i>.', '→ 複數用 ones', 'o'), 'o', sub='同一類，不是同一個'))),

section('both、either、neither、all、any、none', table(['', '全部都是', '其中任一個', '全部都不是'], [
  ['兩個', 'both（複數動詞）', 'either（單數動詞）', 'neither（單數動詞）'],
  ['三個以上', 'all', 'any', 'none'],
]) + '<div style="height:calc(var(--u)*1.4)"></div>' + cards(2,
  card('兩個', ex('<b>Both</b> of my sisters <b>are</b> teachers.', '→ 都是') +
    ex('<b>Neither</b> of the answers <b>is</b> correct.', '→ 都不對')),
  card('三個以上', ex('— Apple or banana or grape? — <i>Any</i> will do.', '→ 任一個都可以', 'o') +
    ex('<i>None</i> of my friends knows it.', '→ 一個都不知道', 'o'), 'o'), tight=True)),

section('部分否定與數量代名詞', cards(2,
  card('部分否定：不是全部都', ex('<b>Not all</b> students like math.', '→ 有些喜歡、有些不喜歡') +
    ex('I don\'t know <b>both</b> of them.', '→ 只認識其中一個') +
    row('全部都不：', '兩個 neither；三個以上 none'), sub='not all / not every / not both'),
  card('數量 + of + 名詞', ex('<i>Most of</i> my classmates <i>have</i> phones.', '→ 動詞看 of 後面的名詞', 'o') +
    ex('<i>Each of</i> the students <i>has</i> a locker.', '→ each 一定單數', 'o') +
    ex('<i>One of</i> my friends <i>lives</i> in Japan.', '→ 主詞是 one', 'o'), 'o', sub='most / some / each / one of'))),

section('學生最常錯的 5 句', top5([
  ('This is mine book.', 'This is my book.', 'mine 後面不接名詞。'),
  ('My bike is faster than you.', 'My bike is faster than yours.', '腳踏車和腳踏車比。'),
  ('She cut her when cooking.', 'She cut herself.', '主詞＝受詞用反身代名詞。'),
  ('I have two brothers. One is tall, and another is short.', 'One is tall, and the other is short.', '兩個中的最後一個用 the other。'),
  ('Each of the boys have a bike.', 'Each of the boys has a bike.', 'each 用單數動詞。'),
])),

section('快問快答 8 題', qas([
  ('Is this ____ cap? (your / yours)', 'your'),
  ('Come with ____. (we / us)', 'us'),
  ('Help ____, kids! (yourself / yourselves)', 'yourselves'),
  ('Some like red; ____ like blue. (others / the other)', 'others'),
  ('I lost my key. I need a new ____. (it / one)', 'one'),
  ('____ of my parents work. (Both / Either)', 'Both'),
  ('____ of the two answers is right. (Neither / None)', 'Neither'),
  ('Each of us ____ a book. (have / has)', 'has'),
])),

section('改寫練習與下一步', two(div(lead('同義改寫'), qas([
  ('This is her umbrella.', 'This umbrella is hers.'),
  ('He went camping alone.', 'He went camping by himself.'),
  ('Ken isn\'t here. Leo isn\'t here.', 'Neither of them is here.'),
  ('He is my friend.（雙重所有格）', 'He is a friend of mine.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的代名詞總表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '名詞的所有格可以回 Unit 8 複習']), 'o'))),
]

UNIT = {'no': 9, 'zh': '代名詞', 'en': 'Pronouns', 'c1': 'me・mine', 'c2': 'the other', 'slides': S}
