from sl import *

W = 16
T = '比較結構與平行對等'

S = [
title(W, T, 'Comparisons &amp; Parallel Structure', 'as…as', 'not only…but also'),

section('本週目標與暖身', cards(2,
  card('本週目標', ul([
    '用 as…as、not as / so…as 做同級比較，會說倍數（twice as…as）',
    '會用 the 比較級…, the 比較級… 和 比較級 and 比較級',
    '用比較級說出最高級：than any other、no other',
    '用 both…and、either…or、neither…nor、not only…but also，動詞和誰一致',
    '平行結構：and、or、but 前後的形式要一樣'])),
  card('暖身 3 題', qas([
    ('My bag is as ____ as yours. (heavy / heavier)', 'heavy'),
    ('The more you practice, the ____ you get. (better / best)', 'better'),
    ('Neither Tom nor his sisters ____ here. (is / are)', 'are')]), 'o'))),

section('回收：第 14 週的分詞構句與連接詞', lead('上週把兩個句子接起來；這週把兩樣東西「拿來比」或「並排放」。') + cards(2,
  card('第 14 週回顧',
    ex('<b>Having finished</b> my homework, I went out.', '→ 分詞構句：比主句更早發生') +
    ex('<i>Despite</i> the rain, we went to the park.', '→ despite + 名詞', 'o')),
  card('這週的延伸',
    ex('My room is <b>twice as big as</b> yours.', '→ 倍數 + as…as') +
    ex('She is <i>not only</i> smart <i>but also</i> kind.', '→ 對等連接詞：前後形式一致', 'o'), 'o'))),

section('同級比較：as…as 與 not as / so…as', cards(2,
  card('as + 原級 + as', row('公式：', 'A + be/V + as + 形容詞/副詞原級 + as + B') + row('意思：', '「A 和 B 一樣…」') +
    ex('Tom is <b>as tall as</b> his father.', '→ Tom 和他爸爸一樣高') +
    ex('She runs <b>as fast as</b> her brother.', '→ 修飾動詞 runs，用副詞 fast'), sub='一樣…'),
  card('not as / so + 原級 + as', row('公式：', 'A + not + as / so + 原級 + as + B') + row('意思：', '「A 沒有 B 那麼…」= A 比 B 更不…') +
    ex('This test is <i>not as difficult as</i> the last one.', '→ 這次考試沒有上次那麼難', 'o') +
    ex('I can\'t swim <i>so well as</i> you.', '→ 否定句才可以用 so…as', 'o'), 'o', sub='沒有那麼…')) +
  note('as…as 中間一定是「原級」：as taller as、as tallest as 都是錯的。也可以說 as many books as、as much money as。')),

section('倍數與比較級的修飾語', cards(2,
  card('倍數的兩種說法', row('公式 1：', '倍數 + as + 原級 + as') + row('公式 2：', '倍數 + 比較級 + than（三倍以上較常用）') +
    ex('My room is <b>twice as big as</b> yours.', '→ 我的房間是你的兩倍大') +
    ex('This bag costs <b>three times as much as</b> that one.', '→ 這個包包的價錢是那個的三倍') +
    ex('The new road is <b>three times longer than</b> the old one.', '→ 新路比舊路長三倍'), sub='twice、three times、half'),
  card('強調比較級：much、far、even、a lot', row('可以用：', 'much、far、even、a lot、still') + row('不能用：', '<span class="bad">very</span> + 比較級') +
    ex('This phone is <i>much cheaper</i> than that one.', '→ 便宜得多', 'o') +
    ex('Today is <i>even hotter</i> than yesterday.', '→ 今天比昨天還要熱', 'o') +
    ex('She is <i>far better</i> at math than I am.', '→ 她數學好得多', 'o'), 'o', sub='「…得多」'), tight=True)),

section('the 比較級…, the 比較級… 與 比較級 and 比較級', cards(2,
  card('越…就越…', row('公式：', 'The + 比較級 + S + V, the + 比較級 + S + V') +
    ex('<b>The more</b> you practice, <b>the better</b> you get.', '→ 你練習越多，就變得越好') +
    ex('<b>The older</b> he gets, <b>the wiser</b> he becomes.', '→ 他年紀越大，就越有智慧') +
    ex('<b>The sooner</b>, <b>the better</b>.', '→ 越快越好（慣用語，可省略主詞動詞）'), sub='the + 比較級，兩邊都要有 the'),
  card('越來越…', row('公式：', '比較級 + and + 比較級 / more and more + 原級') +
    ex('It is getting <i>colder and colder</i>.', '→ 天氣越來越冷', 'o') +
    ex('English is becoming <i>more and more</i> important.', '→ 英文變得越來越重要', 'o') +
    ex('<i>Fewer and fewer</i> people write letters now.', '→ 越來越少人寫信了', 'o'), 'o', sub='get / become / grow + 比較級 and 比較級'))),

section('用比較級說出最高級', table(['句型', '意思', '例句'], [
  ['than any other + 單數名詞', '比其他任何…都', ('Mount Jade is higher <b>than any other mountain</b> in Taiwan.', '玉山比台灣其他任何一座山都高')],
  ['No other + 單數名詞 + 比較級 + than', '沒有其他…比…更', ('<b>No other</b> mountain in Taiwan <b>is higher than</b> Mount Jade.', '台灣沒有別的山比玉山高')],
  ['one of the + 最高級 + 複數名詞', '最…的之一', ('She is <b>one of the best students</b> in our class.', '她是我們班最好的學生之一')],
  ['最高級 + (that) S + have ever p.p.', '我…過最…的', ('This is <b>the funniest movie I have ever seen</b>.', '這是我看過最好笑的電影')],
], audio_col=2) + note('than any other 後面接「單數名詞」，而且要有 other（不能和自己比）；one of the 後面接「複數名詞」。')),

section('比較的對象要一致，與不用 than 的比較', cards(2,
  card('比較對象要對等', row('規則：', '拿「東西」比「東西」，不能拿「東西」比「人」') +
    ex('The weather in Taipei is hotter than <b>that</b> in Tokyo.', '→ that = the weather（單數）') +
    ex('The prices here are higher than <b>those</b> in my town.', '→ those = the prices（複數）') +
    ex('My bike is newer than <b>my brother\'s</b>.', '→ my brother\'s = my brother\'s bike'), sub='that / those / 所有格'),
  card('不用 than 的比較', row('superior / inferior to：', '比…優秀／差') + row('prefer A to B：', '比起 B 更喜歡 A') + row('would rather A than B：', '寧願 A 也不要 B（接原形）') +
    ex('This phone is <i>superior to</i> that one.', '→ 這支手機比那支好', 'o') +
    ex('I <i>prefer</i> tea <i>to</i> coffee.', '→ 比起咖啡我更喜歡茶', 'o') +
    ex('I would <i>rather</i> stay home <i>than</i> go out.', '→ 我寧願待在家也不要出門', 'o'), 'o', sub='to / than 的特別用法'))),

section('對等相關連接詞：both、either、neither、not only', table(['句型', '意思', '動詞跟誰', '例句'], [
  ['both A and B', 'A 和 B 都', '複數', ('<b>Both</b> Tom <b>and</b> Amy <b>are</b> students.', 'Tom 和 Amy 都是學生')],
  ['either A or B', '不是 A 就是 B', '靠近的 B', ('<b>Either</b> you <b>or</b> he <b>has</b> to go.', '不是你就是他得去')],
  ['neither A nor B', 'A 和 B 都不', '靠近的 B', ('<b>Neither</b> Tom <b>nor</b> his sisters <b>are</b> here.', 'Tom 和他姊妹都不在')],
  ['not only A but also B', '不但 A 而且 B', '靠近的 B', ('<b>Not only</b> the students <b>but also</b> the teacher <b>was</b> late.', '不但學生，連老師也遲到了')],
  ['not A but B', '不是 A 而是 B', 'B', ('He is <b>not</b> a doctor <b>but</b> a nurse.', '他不是醫生，而是護理師')],
], audio_col=3) + note('口訣：both 一定用複數；either…or、neither…nor、not only…but also 都是「就近原則」，動詞看最靠近的那個主詞。')),

section('平行結構：and、or、but 前後要一樣', cards(2,
  card('形式要一致', row('名詞 & 名詞：', 'reading, music, and sports') + row('V-ing & V-ing：', 'I like reading and swimming.') + row('to V & to V：', 'I want to learn and (to) grow.') + row('形容詞 & 形容詞：', 'smart, kind, and funny') +
    ex('She likes <b>reading</b>, <b>swimming</b>, and <b>dancing</b>.', '→ 三個都是 V-ing') +
    ex('He is <b>smart</b>, <b>kind</b>, and <b>funny</b>.', '→ 三個都是形容詞'), sub='Parallel Structure'),
  card('相關連接詞也要平行', row('規則：', 'both、either、neither、not only 後面接的東西，要和 and、or、nor、but also 後面的形式一樣') +
    ex('She is <i>not only</i> smart <i>but also</i> hardworking.', '→ 形容詞對形容詞', 'o') +
    ex('You can <i>either</i> walk <i>or</i> take the bus.', '→ 原形對原形', 'o') +
    '<div class="ex o"><div class="en"><span class="bad">She likes to swim and dancing.</span></div><div class="zh">→ to swim 和 dancing 不平行，要改成 swimming and dancing</div></div>', 'o', sub='前後對稱'))),

section('對比頁：容易搞混的四組', two(
  card('as…as 與 than', ex('He is <b>as tall as</b> me.', '→ 一樣高，中間用原級') + ex('He is <i>taller than</i> me.', '→ 比較高，用比較級 + than', 'o')),
  card('much taller 與 very tall', ex('He is <b>much taller</b> than me.', '→ 比較級用 much 加強') + ex('He is <i>very tall</i>.', '→ 原級才用 very', 'o'), 'o'), tight=True) + two(
  card('both…and 與 either…or', ex('<b>Both</b> he <b>and</b> I <b>are</b> ready.', '→ 兩個都，動詞用複數') + ex('<i>Either</i> he <i>or</i> I <i>am</i> wrong.', '→ 其中一個，動詞看 I', 'o')),
  card('prefer A to B 與 would rather A than B', ex('I <b>prefer</b> walking <b>to</b> driving.', '→ to 是介系詞，接 V-ing') + ex('I would <i>rather</i> walk <i>than</i> drive.', '→ 接原形動詞', 'o'), 'o'), tight=True)),

section('學生最常錯的 5 句', top5([
  ('He is as taller as his father.', 'He is as tall as his father.', 'as…as 中間用原級。'),
  ('This book is very better than that one.', 'This book is much better than that one.', '比較級要用 much、far、even 加強，不能用 very。'),
  ('Mount Jade is higher than any mountain in Taiwan.', 'Mount Jade is higher than any other mountain in Taiwan.', '玉山本身就在台灣，要加 other，不能和自己比。'),
  ('Neither my brother nor I are hungry.', 'Neither my brother nor I am hungry.', 'neither…nor 動詞看最靠近的主詞 I。'),
  ('I like swimming, to read, and play games.', 'I like swimming, reading, and playing games.', '並列的東西形式要一樣（平行結構）。'),
])),

section('快問快答 8 題', qas([
  ('She is as ____ as her mother. (beautiful / more beautiful)', 'beautiful'),
  ('This box is ____ heavier than that one. (very / much)', 'much'),
  ('My room is ____ as big as yours. (two times / twice)', 'twice'),
  ('The harder you work, ____ you will be. (the more successful / more successful)', 'the more successful'),
  ('It is getting ____. (warmer and warmer / warm and warm)', 'warmer and warmer'),
  ('She is one of the best ____ in our school. (singer / singers)', 'singers'),
  ('Both my father and my mother ____ teachers. (is / are)', 'are'),
  ('Either you or Tom ____ to clean the room. (has / have)', 'has'),
])),

section('挑錯練習與句型轉換', two(div(lead('挑錯：每句有一個錯'), qas([
  ('The weather in Taipei is hotter than Tokyo.', 'Tokyo → that in Tokyo'),
  ('She is not only kind but also she is smart.', '改成 not only kind but also smart'),
  ('I prefer tea than coffee.', 'than → to'),
])), div(lead('改寫成指定句型'), qas([
  ('Tom is taller than any other boy in his class.（用 No other）', 'No other boy in his class is taller than Tom.'),
  ('You eat more; you get fatter.（用 The…, the…）', 'The more you eat, the fatter you get.'),
  ('Tom is not here. Mary is not here.（用 Neither…nor）', 'Neither Tom nor Mary is here.'),
])))),

section('在閱讀與聽力裡找到它', passage(
  'Is city life <span class="hl">better than</span> country life? In the city, buses come <span class="hl">much more often</span>, and shops stay open <span class="hl">later</span>. However, rent in the city can be <span class="hl">twice as high as</span> it is in the country. <span class="hl2">The bigger</span> a city grows, <span class="hl2">the busier</span> its streets become. Country life is <span class="hl2">not only</span> quiet <span class="hl2">but also</span> healthy.') +
  cards(2,
    card('閱讀怎麼用', ul(['看到 than、as…as，先找「誰和誰比」', 'the + 比較級, the + 比較級：前面是條件，後面是結果', 'not only A but also B：B 通常是作者要強調的新資訊'])),
    card('聽力怎麼用', ul(['聽到 twice、three times，題目常考倍數或價錢', '聽到 not as…as，代表前者「比較不…」', '聽到 neither…nor，表示兩個都沒有'], ), 'o'))),

section('口說句型跟讀', lead('先按 🔊 聽，再跟著大聲念，最後換成自己的句子。') + two(div(
  ex('My sister is <b>not as tall as</b> I am.', '→ not as…as'),
  ex('<b>The more</b> I read, <b>the more</b> I learn.', '→ the 比較級, the 比較級'),
  ex('Taipei 101 is taller <b>than any other building</b> in Taiwan.', '→ 比較級表最高級')), div(
  ex('I like <i>both</i> basketball <i>and</i> swimming.', '→ both…and', 'o'),
  ex('My best friend is <i>not only</i> funny <i>but also</i> helpful.', '→ not only…but also', 'o')))),

section('重點整理與測驗說明', two(div(
  table(['重點', '規則'], [
    ['as…as', '中間用原級；否定 not as / so…as'],
    ['倍數', 'twice / three times + as…as 或 + 比較級 than'],
    ['the 比較級, the 比較級', '越…就越…，兩邊都要 the'],
    ['than any other', '後面接單數名詞，要有 other'],
    ['neither…nor / either…or', '動詞看最靠近的主詞'],
    ['平行結構', 'and、or、but 前後形式相同']]),
  note('口訣：as 中間放原級，比較加強用 much；both 複數、either 就近；並排的東西要長得一樣。')), div(
  card('本週測驗：64 題', row('題型：', '文法 20．閱讀 10．克漏字 4．單字 10．聽力 15．口說 5') + ul(['文法 20 題中，16 題是本週新教，4 題回收第 14 週分詞構句與連接詞']), 'o'),
  card('回家作業', ol(['用 as…as 和 not as…as 各寫一句比較你和家人。', '用 The more…, the more… 寫一句學習心得。', '用 not only…but also 介紹你的好朋友，注意平行結構。']))))),
]
