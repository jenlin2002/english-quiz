from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '分辨「可能成真」和「與事實相反」的假設',
    '寫出與現在相反（were、would + V）',
    '寫出與過去相反（had p.p.、would have p.p.）',
    '用 should 說「萬一」',
    '用 wish 說「真希望…」，分清楚 wish 和 hope'])),
  card('暖身 3 題', qas([
    ('If it ____ tomorrow, I\'ll stay home. (rains / will rain)', 'rains'),
    ('If I ____ you, I would rest. (am / were)', 'were'),
    ('I wish I ____ fly. (can / could)', 'could')]), 'o'))),

section('先看全貌：有可能嗎？', table(['種類', 'if 子句', '主要子句', '例句'], [
  ['事實、真理', '現在式', '現在式', ('If you heat ice, it <b>melts</b>.', '冰加熱就會融化')],
  ['可能成真', '現在式', 'will + V', ('If it <b>rains</b>, I <b>will stay</b> home.', '下雨的話我就待在家')],
  ['與現在相反', '過去式（were）', 'would + V', ('If I <b>were</b> rich, I <b>would buy</b> a house.', '如果我有錢就會買房子')],
  ['與過去相反', 'had + p.p.', 'would have + p.p.', ('If I <b>had studied</b>, I <b>would have passed</b>.', '如果我當時用功就會及格')],
], audio_col=3) + note('和事實相反時，動詞要往過去退一格。')),

section('有可能成真的假設', cards(2,
  card('事實、真理：兩邊現在式', ex('If you mix red and blue, you <b>get</b> purple.', '→ 永遠如此') +
    ex('If I drink coffee at night, I <b>can\'t</b> sleep.', '→ 每次都這樣'), sub='zero conditional'),
  card('未來可能：if 現在式 + will', ex('If it <i>is</i> sunny tomorrow, we <i>will go</i> on a picnic.', '→ 不是 if it will be', 'o') +
    ex('If you <i>need</i> help, <i>call</i> me.', '→ 也可以接祈使句', 'o'), 'o', sub='first conditional'))),

section('與現在事實相反', cards(2,
  card('If + 過去式, would + V', ex('If I <b>had</b> wings, I <b>would fly</b> to Japan.', '→ 事實：我沒有翅膀') +
    ex('If I <b>knew</b> her number, I <b>could call</b> her.', '→ 事實：我不知道') +
    ex('If I <b>were</b> you, I <b>would</b> take a break.', '→ be 一律用 were，常用來給建議'), sub='現在不是這樣'),
  card('事實怎麼說', ex('If I were taller, I could reach it.', '→ 假設', 'o') +
    ex('= I <i>am not</i> tall enough, so I <i>can\'t</i> reach it.', '→ 事實：現在式、肯否相反', 'o'), 'o', sub='假設 ⇄ 事實'))),

section('與過去事實相反', cards(2,
  card('If + had p.p., would have p.p.', ex('If you <b>had told</b> me, I <b>would have helped</b> you.', '→ 你當時沒說') +
    ex('If I <b>had left</b> earlier, I <b>wouldn\'t have missed</b> the bus.', '→ 我當時沒早點出門'), sub='過去已經發生'),
  card('事實怎麼說', ex('If he had studied, he would have passed.', '→ 假設', 'o') +
    ex('= He <i>didn\'t study</i>, so he <i>didn\'t pass</i>.', '→ 事實：過去式、肯否相反', 'o'), 'o', sub='假設 ⇄ 事實'))),

section('混合的假設與「萬一」', cards(2,
  card('過去沒做，影響現在', row('If + had p.p.（過去）, would + V + now（現在）', '') +
    ex('If I <b>had eaten</b> breakfast, I <b>wouldn\'t be</b> hungry now.', '→ 早上沒吃，現在很餓') +
    row('看時間線索：', 'if 子句 last week；主要子句 now'), sub='mixed'),
  card('萬一：If + should + V', ex('If it <i>should</i> rain, the game <i>will</i> be canceled.', '→ 萬一下雨', 'o') +
    ex('If you <i>should</i> see Ken, <i>tell</i> him to call me.', '→ 萬一看到 Ken', 'o'), 'o', sub='should'))),

section('wish：真希望…', table(['希望', '公式', '例句'], [
  ['現在', 'wish + 過去式（were）', ('I wish I <b>were</b> a bird.', '真希望我是一隻鳥')],
  ['現在（能力）', 'wish + could + V', ('I wish I <b>could</b> fly.', '真希望我會飛')],
  ['過去', 'wish + had + p.p.', ('I wish I <b>had studied</b> harder.', '真希望我當時更用功')],
  ['真的有可能 → hope', 'hope + will', ('I <b>hope</b> it will be sunny tomorrow.', '希望明天會放晴')],
], audio_col=2)),

section('學生最常錯的 5 句', top5([
  ('If it will rain tomorrow, we will stay home.', 'If it rains tomorrow, we will stay home.', 'if 子句現在代未來。'),
  ('If I am you, I would apologize.', 'If I were you, I would apologize.', '與現在相反用 were。'),
  ('If I had money, I will buy it.', 'If I had money, I would buy it.', '主要子句用 would。'),
  ('If you had called, I would come.（昨天）', 'If you had called, I would have come.', '與過去相反。'),
  ('I wish I can fly.', 'I wish I could fly.', 'wish 後面退一格。'),
])),

section('快問快答 8 題', qas([
  ('If it ____ sunny, we\'ll go. (is / will be)', 'is'),
  ('If I ____ you, I\'d go. (am / were)', 'were'),
  ('If I had time, I ____ help. (will / would)', 'would'),
  ('If I had known, I ____ come. (would / would have)', 'would have'),
  ('If she ____ studied, she would have passed. (has / had)', 'had'),
  ('I wish I ____ a cat. (have / had)', 'had'),
  ('I wish I ____ gone. (have / had)', 'had'),
  ('I ____ you get well soon. (wish / hope)', 'hope'),
])),

section('改寫練習與下一步', two(div(lead('依事實寫假設'), qas([
  ('I am not rich, so I can\'t travel.', 'If I were rich, I could travel.'),
  ('I don\'t have a dog.（wish）', 'I wish I had a dog.'),
  ('It rained, so we didn\'t go out.', 'If it hadn\'t rained, we would have gone out.'),
  ('I didn\'t bring my jacket.（wish）', 'I wish I had brought my jacket.'),
])), card('恭喜！20 個單元全部學完', ul([
  '回到「📘 講解」頁看完整的整理表',
  '準備好了就按右上角「📝 前往測驗」',
  '第一期 Week 14 的週測驗可以當綜合練習',
  '回國中文法目錄，挑錯最多的單元再複習一次']), 'o'))),
]

UNIT = {'no': 20, 'zh': '假設語氣', 'en': 'Conditionals & Wishes', 'c1': 'If I were…', 'c2': 'I wish…', 'slides': S}
