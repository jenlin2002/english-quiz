from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '用三個規則寫出附加問句',
    '依照 be 動詞、一般動詞、助動詞、完成式選對字',
    '處理 this、there、everyone 等特別的主詞',
    'never、nothing 句子的附加問句、Let\'s 和祈使句',
    '正確回答附加問句（看事實說 Yes / No）'])),
  card('暖身 3 題', qas([
    ('It\'s cold, ____? (isn\'t it / is it)', 'isn\'t it'),
    ('You like music, ____? (aren\'t you / don\'t you)', 'don\'t you'),
    ('He can\'t swim, ____? (can he / can\'t he)', 'can he')]), 'o'))),

section('附加問句的三個規則', cards(2,
  card('規則', ul([
    '① 前肯後否、前否後肯',
    '② 主詞換成代名詞（Ken → he）',
    '③ 用原句的 be／助動詞；一般動詞借 do / does / did',
    '④ 否定一律縮寫：isn\'t、don\'t、can\'t']), sub='rules'),
  card('例句', ex('Ken is your classmate, <b>isn\'t he</b>?', '→ 前肯後否') +
    ex('Amy isn\'t here, <i>is she</i>?', '→ 前否後肯', 'o') +
    ex('Your parents like fish, <b>don\'t they</b>?', '→ 一般動詞借 do') +
    ex('Ben lost his key, <i>didn\'t he</i>?', '→ 過去式借 did', 'o'), 'o', sub='examples'))),

section('各種時態與助動詞', table(['前面的句子', '附加問句', '例句'], [
  ['was / were', '同一個 be 動詞', ('It was cold, <b>wasn\'t it</b>?', '那時很冷，對吧？')],
  ['現在式一般動詞', 'do / does', ('She plays tennis, <b>doesn\'t she</b>?', '她打網球，對吧？')],
  ['can / will / should', '同一個助動詞', ('It will rain, <b>won\'t it</b>?', '會下雨，對吧？')],
  ['have / has + p.p.', 'have / has', ('They have finished, <b>haven\'t they</b>?', '他們做完了，對吧？')],
  ['have（擁有）', 'do / does', ('You have a dog, <b>don\'t you</b>?', '你有養狗，對吧？')],
  ['I am', 'aren\'t I（較正式 am I not）', ('I\'m late, <b>aren\'t I</b>?', '我遲到了，對吧？')],
], audio_col=2)),

section('特別的主詞', table(['主詞', '附加問句用', '例句'], [
  ['this / that', 'it', ('This is your pen, <b>isn\'t it</b>?', '這是你的筆，對吧？')],
  ['these / those', 'they', ('Those are your shoes, <b>aren\'t they</b>?', '那些是你的鞋，對吧？')],
  ['everything / nothing', 'it', ('Everything is ready, <b>isn\'t it</b>?', '都準備好了，對吧？')],
  ['everyone / nobody', 'they', ('Everyone likes her, <b>don\'t they</b>?', '大家都喜歡她，對吧？')],
  ['There is / are', 'there', ('There is a park nearby, <b>isn\'t there</b>?', '附近有公園，對吧？')],
], audio_col=2)),

section('句子裡有否定的字', cards(2,
  card('never、nothing、seldom…', row('雖然沒有 not，句子已經是否定 → 附加問句用肯定', '') +
    ex('She <b>never</b> eats meat, <b>does she</b>?', '→ 她從不吃肉，對吧？') +
    ex('There is <b>nothing</b> in the box, <b>is there</b>?', '→ 箱子裡沒東西，對吧？'), sub='negative words'),
  card('字裡面的否定不算', ex('He is <i>unhappy</i>, <i>isn\'t he</i>?', '→ unhappy 仍算肯定句', 'o') +
    ex('Nobody came, <i>did they</i>?', '→ nobody 用 they', 'o'), 'o', sub='unhappy、dislike'))),

section('祈使句與 Let\'s', table(['句型', '附加問句', '例句'], [
  ['Let\'s …', 'shall we?', ('Let\'s go to the movies, <b>shall we</b>?', '我們去看電影好嗎？')],
  ['祈使句（請對方做）', 'will you?', ('Close the door, <b>will you</b>?', '把門關上好嗎？')],
  ['否定祈使句', 'will you?', ('Don\'t be late, <b>will you</b>?', '別遲到喔')],
  ['邀請', 'won\'t you?', ('Have some cake, <b>won\'t you</b>?', '吃塊蛋糕吧！')],
], audio_col=2)),

section('含子句的句子與怎麼回答', cards(2,
  card('跟著主要子句', ex('You know where he lives, <b>don\'t you</b>?', '→ 主要子句 You know') +
    ex('She was sleeping when you called, <b>wasn\'t she</b>?', '→ 主要子句 She was sleeping') +
    row('例外：', 'I think … 跟著後面的子句：I think Ken is right, isn\'t he?'), sub='main clause'),
  card('回答：看事實說 Yes / No', ex('— You aren\'t hungry, are you?', '→ 問句', 'o') +
    ex('— <i>Yes, I am.</i>', '→ 我餓（事實是肯定）', 'o') +
    ex('— <i>No, I\'m not.</i>', '→ 我不餓（事實是否定）', 'o'), 'o', sub='和中文的「對／不對」不同'))),

section('學生最常錯的 5 句', top5([
  ('Amy is your sister, isn\'t Amy?', 'Amy is your sister, isn\'t she?', '主詞換成代名詞。'),
  ('You like pizza, aren\'t you?', 'You like pizza, don\'t you?', '一般動詞借 do。'),
  ('He went home, doesn\'t he?', 'He went home, didn\'t he?', '過去式借 did。'),
  ('He never lies, doesn\'t he?', 'He never lies, does he?', 'never 是否定 → 後面肯定。'),
  ('Let\'s have lunch, don\'t we?', 'Let\'s have lunch, shall we?', 'Let\'s → shall we。'),
])),

section('快問快答 8 題', qas([
  ('She is tall, ____?', 'isn\'t she'),
  ('They don\'t know, ____?', 'do they'),
  ('You saw it, ____?', 'didn\'t you'),
  ('Ken will come, ____?', 'won\'t he'),
  ('This is fun, ____?', 'isn\'t it'),
  ('There are two cats, ____?', 'aren\'t there'),
  ('Let\'s dance, ____?', 'shall we'),
  ('He seldom cries, ____?', 'does he'),
])),

section('合併練習與下一步', two(div(lead('改成附加問句'), qas([
  ('Jay is good at math. Right?', 'Jay is good at math, isn\'t he?'),
  ('You didn\'t lock the door. Right?', 'You didn\'t lock the door, did you?'),
  ('Close the window, please.', 'Close the window, will you?'),
  ('Everyone is here. Right?', 'Everyone is here, aren\'t they?'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '時態和助動詞不熟，可以回 Unit 1、Unit 6 複習']), 'o'))),
]

UNIT = {'no': 14, 'zh': '附加問句', 'en': 'Tag Questions', 'c1': 'isn\'t it?', 'c2': 'do you?', 'slides': S}
