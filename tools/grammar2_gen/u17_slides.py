from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '用 who、which、that、whose 把兩句合成一句',
    '分辨主格、受格（可省略）、所有格',
    '知道什麼時候一定用 that、什麼時候不能用 that',
    '用 what = the thing that',
    '用 where、when 說地方和時間'])),
  card('暖身 3 題', qas([
    ('The boy ____ sings well is Ken. (who / which)', 'who'),
    ('The book ____ I read is fun. (who / that)', 'that'),
    ('The girl ____ dog is big is Amy. (who / whose)', 'whose')]), 'o'))),

section('觀念：一個句子當形容詞', cards(2,
  card('形容詞子句放在名詞後面', ex('a <b>tall</b> boy', '→ 一個字：放前面') +
    ex('the boy <b>who is playing tennis</b>', '→ 一整句：放後面') +
    row('先行詞：', '被修飾的名詞（the boy）'), sub='who / which / that + 子句'),
  card('關係代名詞總表', table(['先行詞', '主格', '受格', '所有格'], [
    ['人', 'who / that', 'whom / that', 'whose'],
    ['物', 'which / that', 'which / that', 'whose'],
    ['人＋物', 'that', 'that', '—']]), 'o', sub='relative pronouns'), tight=True)),

section('合併兩句：三個步驟', cards(2,
  card('步驟', ul([
    '① 找出兩句相同的人或物',
    '② 第二句的那個字換成關係代名詞',
    '③ 整個子句放在先行詞後面']) +
    ex('The girl is my cousin. The girl sings well.', '→ 原本兩句'), sub='steps'),
  card('合併結果', ex('The girl <i>who sings well</i> is my cousin.', '→ 人、主格 → who', 'o') +
    ex('The bike <i>which my dad bought</i> is mine.', '→ 物、受格 → which，搬到子句前面', 'o'), 'o', sub='result'))),

section('主格與受格', cards(2,
  card('主格：後面接動詞', ex('I have a friend <b>who lives</b> in Japan.', '→ who 當主詞') +
    ex('the girls who <b>are</b>… / the girl who <b>is</b>…', '→ 動詞跟先行詞') +
    row('注意：', '主格關代不能省略'), sub='who / which / that + V'),
  card('受格：後面接主詞＋動詞', ex('The man <i>(whom) I met</i> is a doctor.', '→ 可以省略', 'o') +
    ex('The movie <i>(that) we watched</i> was boring.', '→ 可以省略', 'o') +
    row('注意：', '子句裡不能再有 it / him（關代已經代替）'), 'o', sub='(whom / which / that) + S + V'))),

section('介系詞 + whom / which 與 whose', cards(2,
  card('介系詞 + 關代', ex('The man <b>with whom</b> she works is kind.', '→ = The man she works with') +
    ex('This is the house <b>in which</b> I lived.', '→ = where I lived') +
    row('注意：', '介系詞後面不能用 that 或 who'), sub='with whom / in which'),
  card('所有格 whose：…的', ex('The girl <i>whose dog</i> is big is my classmate.', '→ whose 後面接名詞', 'o') +
    ex('I have a book <i>whose cover</i> is red.', '→ 物也可以用', 'o'), 'o', sub='whose + 名詞'))),

section('that 的特別規則', cards(2,
  card('一定（最好）用 that', ex('She is the kindest person <b>that</b> I know.', '→ 最高級') +
    ex('This is all <b>that</b> I have.', '→ all、the only、the first') +
    ex('the boy and his dog <b>that</b> are running', '→ 人＋物'), sub='must use that'),
  card('不能用 that', row('① 介系詞後面：', 'with whom（不是 with that）') +
    row('② 逗號後面（非限定）：', 'My dad, who is a cook, …') +
    row('③ 所有格：', '用 whose'), 'o', sub='can\'t use that'))),

section('what、限定與非限定', cards(2,
  card('what = the thing that', ex('<b>What</b> you said is true.', '→ 你說的話是真的') +
    ex('I don\'t understand <b>what</b> he means.', '→ 他的意思') +
    row('注意：', '前面有名詞就不能用 what：the book that I want'), sub='沒有先行詞'),
  card('逗號：補充說明', ex('The man <i>who is standing there</i> is my dad.', '→ 限定：指出是哪一個', 'o') +
    ex('My dad, <i>who loves hiking</i>, is a teacher.', '→ 非限定：補充，不能用 that', 'o'), 'o', sub='有沒有逗號'))),

section('關係副詞：where、when', table(['關係副詞', '代替', '例句'], [
  ['where', '地方（= in / at which）', ('This is the park <b>where</b> I often play.', '這是我常玩的公園')],
  ['when', '時間（= on / in which）', ('I remember the day <b>when</b> we first met.', '我記得我們初次見面那天')],
  ['which（比較）', '子句缺受詞', ('This is the park <b>which</b> I visited.', '這是我參觀過的公園')],
], audio_col=2) + note('看子句缺什麼：缺地方 → where；缺主詞或受詞 → which。')),

section('學生最常錯的 5 句', top5([
  ('The girl which sings well is Amy.', 'The girl who sings well is Amy.', '人用 who／that。'),
  ('The movie which we watched it was great.', 'The movie which we watched was great.', '不能重複 it。'),
  ('The girl who her dog is big is Amy.', 'The girl whose dog is big is Amy.', '「她的」用 whose。'),
  ('This is the book what I want.', 'This is the book that I want.', '有先行詞不用 what。'),
  ('This is the park which I often play.', 'This is the park where I often play.', '缺地方用 where。'),
])),

section('快問快答 8 題', qas([
  ('the man ____ lives here (who / which)', 'who'),
  ('the bag ____ I bought (who / that)', 'that'),
  ('the boy ____ mom is a nurse (who / whose)', 'whose'),
  ('the town ____ I grew up (which / where)', 'where'),
  ('the best song ____ I know (that / what)', 'that'),
  ('____ you need is sleep. (What / That)', 'What'),
  ('the friend with ____ I live (whom / that)', 'whom'),
  ('the day ____ we met (when / which)', 'when'),
])),

section('合併練習與下一步', two(div(lead('用關係詞合併'), qas([
  ('The lady is my aunt. She is wearing a hat.', 'The lady who is wearing a hat is my aunt.'),
  ('I lost the pen. I bought it yesterday.', 'I lost the pen (that) I bought yesterday.'),
  ('I know a boy. His dad is a pilot.', 'I know a boy whose dad is a pilot.'),
  ('This is the café. We met there.', 'This is the café where we met.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '第一期 Week 13 的週測驗可以當綜合練習']), 'o'))),
]

UNIT = {'no': 17, 'zh': '形容詞子句', 'en': 'Relative Clauses', 'c1': 'who・which', 'c2': 'that・whose', 'slides': S}
