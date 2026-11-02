from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '把直述句改成 Yes／No 問句',
    '用「疑問詞 + 問句」問時間、地點、人、原因…',
    '知道問主詞時不借 do（Who broke it?）',
    '分清楚 How many / much / often / long / soon / far',
    '依畫線部分造問句'])),
  card('暖身 3 題', qas([
    ('— ____ do you live? — In Taipei. (Where / When)', 'Where'),
    ('— ____ is it? — NT$100. (How many / How much)', 'How much'),
    ('____ she like cats? (Does / Is)', 'Does')]), 'o'))),

section('Yes／No 問句', table(['原句', '問句', '簡答'], [
  ['She is a nurse.', ('<b>Is</b> she a nurse?', '她是護理師嗎？'), 'Yes, she is.'],
  ['They can swim.', ('<b>Can</b> they swim?', '他們會游泳嗎？'), 'Yes, they can.'],
  ['He likes cats.', ('<b>Does</b> he <b>like</b> cats?', '他喜歡貓嗎？'), 'No, he doesn\'t.'],
  ['You went out.', ('<b>Did</b> you <b>go</b> out?', '你出門了嗎？'), 'Yes, I did.'],
], audio_col=1) + note('選擇問句（A or B?）不能用 Yes／No 回答：Do you want tea or coffee? — Tea, please.')),

section('疑問詞問句：疑問詞 + 問句', cards(2,
  card('公式', row('疑問詞 + be／助動詞／do + 主詞 + …?', '') +
    ex('Will you graduate next year? → <b>When will you</b> graduate?', '→ 問時間') +
    ex('Is he studying in the library? → <b>Where is he</b> studying?', '→ 問地點'), sub='Wh- + question'),
  card('問主詞：不借 do', ex('<i>Who broke</i> the window?', '→ Who 是主詞', 'o') +
    ex('<i>Who(m) did</i> you see?', '→ Who 是受詞，要借 did', 'o') +
    ex('<i>What happened</i>?', '→ What 是主詞', 'o'), 'o', sub='Who / What as subject'))),

section('各個疑問詞', table(['疑問詞', '問', '例句'], [
  ['when / where', '時間／地點', ('<b>When</b> did she arrive? / <b>Where</b> does Tom live?', '她何時到？／Tom 住哪？')],
  ['who / whom', '人', ('<b>Who</b> is that man?', '那個人是誰？')],
  ['whose', '誰的', ('<b>Whose</b> bag is this?', '這是誰的包包？')],
  ['what / which', '什麼／哪一個', ('<b>Which</b> color do you like, red or blue?', '你喜歡紅色還是藍色？')],
  ['why', '原因', ('<b>Why</b> are you late?', '你為什麼遲到？')],
  ['how', '方法、狀況', ('<b>How</b> do you go to school?', '你怎麼去上學？')],
], audio_col=2) + note('Who is he? 問身分；What does he do? 問職業。')),

section('How 家族', table(['問句', '問', '回答'], [
  ['How many + 複數', '數量（可數）', 'Twenty.'],
  ['How much', '數量（不可數）／價錢', 'NT$300.'],
  ['How often', '頻率', 'Twice a week.'],
  ['How long', '多久（for + 一段時間）', 'For five years.'],
  ['How soon', '還要多久（in + 一段時間）', 'In ten minutes.'],
  ['How far', '距離', 'About two kilometers.'],
  ['How old / tall', '年紀／身高', 'She\'s ten.'],
])),

section('常用的 What 問句', table(['問句', '問', '回答'], [
  [('<b>What time</b> is it?', '現在幾點？'), '幾點', 'It\'s three o\'clock.'],
  [('<b>What day</b> is today?', '今天星期幾？'), '星期幾', 'It\'s Monday.'],
  [('What\'s the <b>weather like</b>?', '天氣如何？'), '天氣', 'It\'s sunny.'],
  [('<b>What does</b> he <b>do</b>?', '他做什麼工作？'), '職業', 'He\'s a lawyer.'],
  [('What does she <b>look like</b>?', '她長什麼樣子？'), '外表', 'She\'s tall.'],
], audio_col=0) + note('提議：Why don\'t we go? = How about going?　回應：Why not?（好啊！）')),

section('依畫線部分造問句', cards(2,
  card('三個步驟', ul([
    '① 看畫線部分 → 選疑問詞',
    '② 畫線是主詞 → 疑問詞直接取代',
    '③ 不是主詞 → 改成 Yes／No 問句，刪掉畫線部分，疑問詞放最前面']), sub='steps'),
  card('例子', ex('Ken bought <u>a bike</u>. → <i>What did Ken buy</i>?', '→ 受詞：借 did', 'o') +
    ex('<u>Amy</u> broke the cup. → <i>Who broke</i> the cup?', '→ 主詞：直接換', 'o') +
    ex('They swim <u>twice a week</u>. → <i>How often do they swim</i>?', '→ 頻率', 'o'), 'o', sub='examples'))),

section('學生最常錯的 5 句', top5([
  ('Where you live?', 'Where do you live?', '一般動詞要借 do。'),
  ('What did you bought?', 'What did you buy?', '借了 did 用原形。'),
  ('Who did break the window?', 'Who broke the window?', '問主詞不借 did。'),
  ('How many water do you drink?', 'How much water do you drink?', 'water 不可數。'),
  ('How long do you swim? — Twice a week.', 'How often do you swim?', '回答次數用 How often。'),
])),

section('快問快答 8 題', qas([
  ('— ____? — At 7. (When / Where)', 'When'),
  ('— ____ is this? — It\'s mine. (Whose / Who)', 'Whose'),
  ('— ____ are you sad? — I lost my cat.', 'Why'),
  ('— ____ books? — Five. (How many / How much)', 'How many'),
  ('— ____ do you swim? — Every day.', 'How often'),
  ('— ____ will you be back? — In an hour.', 'How soon'),
  ('— ____ called you? — My mom. (Who / Whom did)', 'Who'),
  ('— ____ does he do? — He\'s a cook.', 'What'),
])),

section('造問句練習與下一步', two(div(lead('依畫線造問句'), qas([
  ('Ken visited his uncle last Sunday.（last Sunday）', 'When did Ken visit his uncle?'),
  ('Lisa cleaned the room.（Lisa）', 'Who cleaned the room?'),
  ('They are playing in the gym.（in the gym）', 'Where are they playing?'),
  ('Mia has three brothers.（three）', 'How many brothers does Mia have?'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '接著學 Unit 19 間接問句：Do you know where he lives?']), 'o'))),
]

UNIT = {'no': 18, 'zh': '疑問句', 'en': 'Questions', 'c1': 'Yes / No', 'c2': 'Wh- / How', 'slides': S}
