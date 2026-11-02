from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '用 and、but、or、so 連接句子',
    '祈使句 + and（就會）／ or（否則）',
    'both…and、either…or、neither…nor 的動詞一致',
    'because／so、although／but 只能用一個',
    '時間、條件子句用現在式代替未來式'])),
  card('暖身 3 題', qas([
    ('I was hungry, ____ I ate a sandwich. (so / but)', 'so'),
    ('____ it was cold, we went out. (Although / Because)', 'Although'),
    ('Hurry, ____ you\'ll be late. (and / or)', 'or')]), 'o'))),

section('對等連接詞：and、but、or、so', table(['連接詞', '關係', '例句'], [
  ['and', '加上', ('I like cats, <b>and</b> my sister likes dogs.', '我喜歡貓，我妹妹喜歡狗')],
  ['but', '相反', ('The bag is nice, <b>but</b> it\'s too expensive.', '包包很好看，但太貴了')],
  ['or', '選擇', ('Do you want tea <b>or</b> coffee?', '你要茶還是咖啡？')],
  ['so', '結果', ('It was raining, <b>so</b> we stayed home.', '下雨了，所以我們待在家')],
], audio_col=2) + '<div style="height:calc(var(--u)*1.4)"></div>' + cards(2,
  card('祈使句 + and：就會', ex('Study hard, <b>and</b> you will pass.', '→ 用功就會及格')),
  card('祈使句 + or：否則', ex('Hurry up, <i>or</i> you will be late.', '→ 快一點，否則會遲到', 'o'), 'o'), tight=True)),

section('成對的連接詞', table(['句型', '意思', '動詞跟誰'], [
  ['both A and B', 'A 和 B 都', '複數'],
  ['either A or B', '不是 A 就是 B', '靠近的 B'],
  ['neither A nor B', 'A 和 B 都不', '靠近的 B'],
  ['not only A but also B', '不但 A 而且 B', '靠近的 B'],
  ['A as well as B', 'A 和 B 都', '前面的 A'],
]) + '<div style="height:calc(var(--u)*1.4)"></div>' + cards(2,
  card('例句', ex('<b>Both</b> Ken and Amy <b>are</b> here.', '→ 複數')),
  card('就近原則', ex('Neither my parents nor <i>I am</i> home.', '→ 看靠近的 I', 'o'), 'o'), tight=True)),

section('附屬連接詞：帶出子句', table(['用途', '連接詞', '例句'], [
  ['原因', 'because, since, as', ('I stayed home <b>because</b> I was sick.', '我因為生病待在家')],
  ['讓步', 'although, though', ('<b>Although</b> it was cold, we went swimming.', '雖然很冷，我們還是去游泳')],
  ['時間', 'when, while, before, after, until', ('Call me <b>as soon as</b> you arrive.', '你一到就打給我')],
  ['條件', 'if, unless, as long as', ('You can go <b>as long as</b> you finish your homework.', '只要寫完功課就可以去')],
  ['目的', 'so that', ('He got up early <b>so that</b> he could catch the bus.', '他早起為了趕公車')],
], audio_col=2) + note('子句在前加逗號：When I got home, …；子句在後不加：… when I got home.')),

section('不能一起用：because／so、although／but', cards(2,
  card('只能選一個', ex('<b>Because</b> it rained, we stayed home.', '→ 不能再加 so') +
    ex('It rained, <b>so</b> we stayed home.', '→ 或只用 so') +
    ex('<b>Although</b> he is rich, he is not happy.', '→ 不能再加 but'), sub='中文「因為…所以」英文只用一個'),
  card('連接詞 vs 介系詞', table(['子句（主詞＋動詞）', '名詞'], [
    ['because it rained', 'because of the rain'], ['although it rained', 'in spite of the rain'],
    ['while I was sleeping', 'during the night']]) +
    ex('The game was canceled <i>because of</i> the typhoon.', '→ 後面是名詞', 'o'), 'o', sub='看後面接什麼'))),

section('時間與條件子句：現在代未來', cards(2,
  card('子句用現在式', ex('I\'ll call you when I <b>get</b> home.', '→ 不是 will get') +
    ex('If it <b>rains</b> tomorrow, we\'ll stay in.', '→ 主要子句才用 will') +
    ex('You\'ll be late <b>unless</b> you hurry.', '→ unless = if … not'), sub='when / if / unless / before / after'),
  card('例外：if = 是否', ex('I don\'t know <i>if</i> he <i>will come</i>.', '→ 我不知道他會不會來', 'o') +
    row('判斷：', 'if 放在 know、ask 後面，意思是「是否」，未來就用 will'), 'o', sub='名詞子句'))),

section('not … until 與 since 的兩個意思', cards(2,
  card('not … until：直到…才', ex('I <b>didn\'t</b> go to bed <b>until</b> midnight.', '→ 直到半夜才睡') +
    ex('She <b>didn\'t</b> know <b>until</b> her friend told her.', '→ 朋友說了她才知道'), sub='not … until'),
  card('since：自從／既然', ex('I\'ve lived here <i>since</i> I was five.', '→ 自從（時間）', 'o') +
    ex('<i>Since</i> you\'re here, let\'s start.', '→ 既然（原因）', 'o'), 'o', sub='since'))),

section('學生最常錯的 5 句', top5([
  ('Because I was sick, so I stayed home.', 'Because I was sick, I stayed home.', 'because 和 so 只用一個。'),
  ('Although it was late, but he worked.', 'Although it was late, he worked.', 'although 和 but 只用一個。'),
  ('We stayed home because the rain.', 'We stayed home because of the rain.', '名詞前用 because of。'),
  ('I\'ll call you when I will arrive.', 'I\'ll call you when I arrive.', '時間子句用現在式。'),
  ('Unless you don\'t hurry, you\'ll be late.', 'Unless you hurry, you\'ll be late.', 'unless 不再加 not。'),
])),

section('快問快答 8 題', qas([
  ('It was hot, ____ I turned on the fan. (so / but)', 'so'),
  ('Try again, ____ you\'ll do it. (and / or)', 'and'),
  ('Both Amy and I ____ ready. (am / are)', 'are'),
  ('Either you or he ____ wrong. (is / are)', 'is'),
  ('____ the rain, we stayed in. (Because / Because of)', 'Because of'),
  ('If it ____ tomorrow, I\'ll stay home. (rains / will rain)', 'rains'),
  ('I\'ll wait ____ you come back. (until / unless)', 'until'),
  ('____ she was tired, she kept working. (Although / Because)', 'Although'),
])),

section('改寫練習與下一步', two(div(lead('同義改寫'), qas([
  ('Because it was noisy, I couldn\'t sleep.', 'It was noisy, so I couldn\'t sleep.'),
  ('If you don\'t hurry, you\'ll be late.', 'Hurry, or you\'ll be late.'),
  ('If you don\'t study, you won\'t pass.', 'Unless you study, you won\'t pass.'),
  ('We stayed home because it rained.', 'We stayed home because of the rain.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整說明和整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '第一期 Week 8 的週測驗可以當綜合練習']), 'o'))),
]

UNIT = {'no': 13, 'zh': '連接詞', 'en': 'Conjunctions', 'c1': 'and・but', 'c2': 'because', 'slides': S}
