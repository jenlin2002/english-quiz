from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '用 in、at、on 表示地方和時間',
    '用 in front of、between、across from 等說位置',
    '分清楚 for / since、until / by、in / into',
    '說交通方式：by bus、on foot',
    '記住片語裡的介系詞'])),
  card('暖身 3 題', qas([
    ('I get up ____ 6:30. (at / on)', 'at'),
    ('My birthday is ____ May. (on / in)', 'in'),
    ('I go to school ____ bus. (by / on)', 'by')]), 'o'))),

section('地方：in、at、on', table(['介系詞', '想像成', '例句'], [
  ['in', '空間、範圍裡面', ('The kids are playing <b>in</b> the park.', '孩子們在公園裡玩')],
  ['at', '一個點、地址', ('I\'ll meet you <b>at</b> the bus stop.', '我在公車站跟你碰面')],
  ['on', '一個面、一條線', ('There\'s a picture <b>on</b> the wall.', '牆上有一幅畫')],
  ['on', '大型交通工具', ('I saw Amy <b>on</b> the bus.', '我在公車上看到 Amy')],
], audio_col=2) + note('go home、come here、go downtown 不加介系詞；但 at home 要用 at。')),

section('位置與方向', cards(2,
  card('位置', table(['介系詞', '意思'], [
    ['in front of / behind', '前面／後面'], ['next to / beside', '旁邊'], ['between A and B', '兩者之間'],
    ['among', '三者以上之中'], ['across from', '對面'], ['under / above', '下面／上方']]), sub='where?'),
  card('方向、移動', ex('He ran <i>into</i> the room.', '→ 進入（移動）', 'o') +
    ex('She got <i>out of</i> the car.', '→ 從…出來', 'o') +
    ex('Walk <i>across</i> the street.', '→ 橫越', 'o') +
    ex('We walked <i>along</i> the river.', '→ 沿著', 'o'), 'o', sub='in 是狀態，into 是移動'), tight=True)),

section('時間：at、on、in', table(['介系詞', '用在', '例句'], [
  ['at', '時刻、noon、night、節日', ('The movie starts <b>at</b> 7:30.', '電影七點半開始')],
  ['on', '星期幾、日期、某一天', ('We have P.E. <b>on</b> Monday.', '我們星期一有體育課')],
  ['in', '月、季節、年、早上／晚上', ('I was born <b>in</b> 2013.', '我 2013 年出生')],
  ['on', '指定某天的早上', ('We left <b>on</b> Sunday morning.', '我們星期天早上出發')],
], audio_col=2) + note('口訣：at 點、on 天、in 長。this、next、last、every 前面不加介系詞：next week（不說 in next week）。')),

section('for、since、until、by、during', cards(2,
  card('持續多久', ex('I\'ve lived here <b>for</b> five years.', '→ for + 一段時間') +
    ex('I\'ve lived here <b>since</b> 2021.', '→ since + 起點') +
    ex('Don\'t talk <b>during</b> the test.', '→ 在…期間'), sub='for / since / during'),
  card('until 和 by', ex('I\'ll stay here <i>until</i> five.', '→ 一直待到五點', 'o') +
    ex('I\'ll be back <i>by</i> five.', '→ 五點前（最晚）會回來', 'o') +
    ex('Hand in your report <i>by</i> Friday.', '→ 最晚期限', 'o'), 'o', sub='持續 vs 期限'))),

section('by、with、in、for、about', table(['介系詞', '意思', '例句'], [
  ['by + 交通工具', '搭乘（不加 a / the）', ('I go to school <b>by bus</b>.', '我搭公車上學')],
  ['on foot', '走路', ('She goes to school <b>on foot</b>.', '她走路上學')],
  ['with', '和…一起；有…特徵', ('I live <b>with</b> my grandparents.', '我和爺爺奶奶住')],
  ['in', '穿著；用（語言）', ('Who is the man <b>in</b> the black coat?', '穿黑外套的人是誰？')],
  ['about', '關於', ('This is a book <b>about</b> dinosaurs.', '這是一本關於恐龍的書')],
], audio_col=2)),

section('片語中的介系詞', table(['介系詞', '常見片語'], [
  ['to', 'be kind to、listen to、belong to'],
  ['for', 'be ready for、be late for、wait for、thank … for'],
  ['with', 'be angry with、be patient with、What\'s wrong with you?'],
  ['of', 'be afraid of、be full of、be proud of、take care of'],
  ['about / at', 'be worried about、talk about / be good at、look at'],
  ['in / on', 'be interested in、in time（及時）/ on time（準時）、on sale'],
]) + note('介系詞後面接名詞、受格（with me）或 V-ing（before eating）。')),

section('學生最常錯的 5 句', top5([
  ('I was born on 2012.', 'I was born in 2012.', '年份用 in。'),
  ('See you in next week.', 'See you next week.', 'next 前面不加介系詞。'),
  ('I go to school by a bus.', 'I go to school by bus.', 'by + 交通工具不加 a。'),
  ('Let\'s go to home.', 'Let\'s go home.', 'go home 不加 to。'),
  ('Please finish it until Friday.', 'Please finish it by Friday.', '最晚期限用 by。'),
])),

section('快問快答 8 題', qas([
  ('____ Monday (in / on)', 'on'),
  ('____ the morning (in / on)', 'in'),
  ('____ midnight (at / in)', 'at'),
  ('____ summer (on / in)', 'in'),
  ('____ foot (by / on)', 'on'),
  ('for / since ____ 2019', 'since'),
  ('The cat ran ____ the house. (in / into)', 'into'),
  ('Sit between Ken and ____. (I / me)', 'me'),
])),

section('改寫練習與下一步', two(div(lead('同義改寫'), qas([
  ('I walk to school.', 'I go to school on foot.'),
  ('He takes the MRT to work.', 'He goes to work by MRT.'),
  ('The bank is opposite the park.', 'The bank is across from the park.'),
  ('I started living here in 2021.（現在還住）', 'I have lived here since 2021.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的介系詞表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '介系詞後接 V-ing 可以回 Unit 3 複習']), 'o'))),
]

UNIT = {'no': 12, 'zh': '介系詞', 'en': 'Prepositions', 'c1': '地方', 'c2': '時間', 'slides': S}
