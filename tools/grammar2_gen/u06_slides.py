from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '記住助動詞的四大特性',
    '分清楚 mustn\'t（禁止）和 don\'t have to（不必）',
    '用 should、had better、shall 給建議',
    '用 must、may、can\'t 推測「一定是／可能／不可能」',
    '用 could、would、may 客氣地請求'])),
  card('暖身 3 題', qas([
    ('She can ____ well. (sings / sing)', 'sing'),
    ('You ____ wear a seat belt. It\'s the law. (must / may)', 'must'),
    ('It\'s Sunday. You ____ get up early. (mustn\'t / don\'t have to)', 'don\'t have to')]), 'o'))),

section('助動詞的四大特性', cards(2,
  card('規則', ul([
    '① 後面一定接原形動詞',
    '② 不因主詞改變，沒有 -s',
    '③ 否定直接加 not：can\'t、shouldn\'t',
    '④ 問句把助動詞移到最前面']), sub='can、could、may、might、will、would、shall、should、must'),
  card('例句', ex('She <b>can swim</b>.', '→ 不是 can swims') +
    ex('He <i>shouldn\'t eat</i> so much.', '→ 否定加 not', 'o') +
    ex('<b>Can</b> you <b>swim</b>?', '→ 不用 Do you can') +
    ex('I <i>will be able to</i> go.', '→ 兩個助動詞不能連用', 'o'), 'o', sub='examples'))),

section('can、could、be able to', table(['用法', '說法', '例句'], [
  ['現在的能力', 'can = am / is / are able to', ('Mia <b>can</b> speak three languages.', 'Mia 會說三種語言')],
  ['過去的能力', 'could = was / were able to', ('I <b>could</b> read when I was four.', '我四歲就會讀書')],
  ['未來的能力', 'will be able to', ('You <b>will be able to</b> drive next year.', '你明年就能開車了')],
  ['允許', 'can', ('You <b>can</b> sit here.', '你可以坐這裡')],
  ['請求', 'can / could（較客氣）', ('<b>Could</b> you help me?', '可以請你幫我嗎？')],
], audio_col=2)),

section('must 和 have to', cards(2,
  card('肯定：必須', row('must：', '說話者覺得一定要（規定）') + row('have to：', '外在情況逼得非做不可') +
    ex('You <b>must</b> wear a seat belt.', '→ 規定') +
    ex('I <b>have to</b> get up at six tomorrow.', '→ 因為要出遊') +
    ex('I <b>had to</b> walk home yesterday.', '→ must 沒有過去式'), sub='must vs have to'),
  card('否定：意思完全不同', ex('You <i>mustn\'t</i> touch the paintings.', '→ 不可以（禁止）', 'o') +
    ex('You <i>don\'t have to</i> bring lunch.', '→ 不必（要帶也可以）', 'o') +
    row('回答 Must I…?', 'No, you don\'t have to. / No, you needn\'t.'), 'o', sub='最常考'))),

section('建議：should、had better、shall', table(['助動詞', '意思', '例句'], [
  ['should = ought to', '應該', ('You <b>should</b> drink more water.', '你應該多喝水')],
  ['had better', '最好（不然會有麻煩）', ('You\'<b>d better</b> take an umbrella.', '你最好帶把傘')],
  ['had better not', '最好不要', ('You\'<b>d better not</b> be late again.', '你最好別再遲到')],
  ['Shall I / we…?', '要不要…？', ('<b>Shall</b> we go for a walk?', '我們去散步好嗎？')],
  ['should have p.p.', '早該…（卻沒做）', ('You <b>should have told</b> me earlier.', '你早該告訴我')],
], audio_col=2) + note('had better 不是過去式；否定的 not 放在 better 後面。')),

section('may、might 與 may be／maybe', cards(2,
  card('可能、允許', ex('It <b>may</b> rain this afternoon.', '→ 可能會下雨') +
    ex('Ken <b>might</b> come to the party.', '→ 也許會來（可能性更低）') +
    ex('<b>May</b> I use your phone?', '→ 客氣地請求允許'), sub='may / might'),
  card('may be 和 maybe', row('may be：', '助動詞 + be，當句子的動詞') + row('maybe：', '副詞（= perhaps），常放句首') +
    ex('He <i>may be</i> at home now.', '→ 句中', 'o') +
    ex('<i>Maybe</i> he <i>is</i> at home now.', '→ 句首，還要有動詞 is', 'o'), 'o', sub='分開寫還是連在一起？'))),

section('will、would、need、used to', cards(2,
  card('will、would', ex('<b>Would</b> you open the window, please?', '→ 比 Will you 客氣') +
    ex('I\'<b>d like</b> a glass of water.', '→ would like = want，較禮貌') +
    ex('Dad said he <b>would</b> buy me a bike.', '→ 轉述時 will 變 would'), sub='未來、請求'),
  card('need、used to', row('need 當助動詞：', '只用在否定和問句，後接原形') +
    ex('He <i>needn\'t</i> worry. = He <i>doesn\'t need to</i> worry.', '→ 兩種不能混用', 'o') +
    ex('I <i>used to</i> be afraid of dogs.', '→ 以前常常，現在不會', 'o') +
    ex('<i>Did</i> you <i>use to</i> live here?', '→ 問句變 use to', 'o'), 'o', sub='兩種身分'))),

section('用助動詞推測：有多確定？', table(['把握度', '助動詞', '例句'], [
  ['一定是', 'must + V', ('The lights are on. They <b>must be</b> home.', '燈亮著，他們一定在家')],
  ['有可能', 'may / might / could + V', ('She <b>may be</b> in the library.', '她可能在圖書館')],
  ['不可能', 'can\'t + V', ('He just ate. He <b>can\'t be</b> hungry.', '他剛吃過，不可能餓')],
  ['過去一定', 'must have p.p.', ('It <b>must have rained</b> last night.', '昨晚一定下過雨')],
  ['過去不可能', 'can\'t have p.p.', ('You <b>can\'t have seen</b> her here.', '你不可能在這裡看到她')],
], audio_col=2) + note('推測「一定不是」用 can\'t，不用 mustn\'t。')),

section('學生最常錯的 5 句', top5([
  ('She can speaks English.', 'She can speak English.', '助動詞後面接原形。'),
  ('You should to see a doctor.', 'You should see a doctor.', 'should 後面直接接原形。'),
  ('I will can go with you.', 'I will be able to go with you.', '兩個助動詞不能連用。'),
  ('Must I go? — No, you mustn\'t.', 'No, you don\'t have to.', 'mustn\'t 是禁止，不必用 don\'t have to。'),
  ('He just ate. He mustn\'t be hungry.', 'He can\'t be hungry.', '推測「不可能」用 can\'t。'),
])),

section('快問快答 8 題', qas([
  ('I ____ swim when I was five. (can / could)', 'could'),
  ('You ____ park here. It\'s a fire lane. (mustn\'t / don\'t have to)', 'mustn\'t'),
  ('We ____ wear uniforms on Fridays. (don\'t have to / mustn\'t)', 'don\'t have to'),
  ('You\'d better ____ late. (not be / not to be)', 'not be'),
  ('____ he is sick. (Maybe / May be)', 'Maybe'),
  ('She ____ be tired. She slept all day. (can\'t / mustn\'t)', 'can\'t'),
  ('I ____ finish it yesterday. (must / had to)', 'had to'),
  ('____ you pass the salt, please? (Could / Must)', 'Could'),
])),

section('改寫練習與下一步', two(div(lead('同義改寫'), qas([
  ('Sam can speak French.', 'Sam is able to speak French.'),
  ('You should rest.', 'You ought to rest.'),
  ('Maybe she is busy.', 'She may be busy.'),
  ('I\'m sure he is the new coach.', 'He must be the new coach.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整說明和整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '第一期 Week 6 的週測驗可以當綜合練習']), 'o'))),
]

UNIT = {'no': 6, 'zh': '助動詞', 'en': 'Modal Verbs', 'c1': '能力・義務', 'c2': '推測・請求', 'slides': S}
