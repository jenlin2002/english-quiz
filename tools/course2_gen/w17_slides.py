from sl import *

W = 17
T = '倒裝句與強調句（中高級入門）'

S = [
title(W, T, 'Inversion &amp; Emphasis', 'Never have I…', 'It is…that…'),

section('本週目標與暖身', cards(2,
  card('本週目標', ul([
    '認識倒裝：否定副詞放句首 → 助動詞搬到主詞前面',
    '會用 So do I、Neither can she 回應別人',
    '會用 Not until…、Only then…、No sooner…than、Hardly…when',
    '條件句省略 if 的倒裝：Had I known、Should you need、Were I you',
    '強調句 It is…that…、What I need is…、助動詞 do / did 加強語氣'])),
  card('暖身 3 題', qas([
    ('Never ____ such a big dog. (I have seen / have I seen)', 'have I seen'),
    ('A: I like pizza. B: So ____ I. (am / do)', 'do'),
    ('It was Tom ____ broke the window. (that / what)', 'that')]), 'o'))),

section('回收：第 16 週的比較與平行結構', lead('上週學「比」和「並排」；這週學把重點「搬到前面」或「特別強調」。') + cards(2,
  card('第 16 週回顧',
    ex('<b>The more</b> you practice, <b>the better</b> you get.', '→ the 比較級, the 比較級') +
    ex('She is <i>not only</i> smart <i>but also</i> kind.', '→ not only…but also', 'o')),
  card('這週的延伸',
    ex('<b>Not only</b> is she smart, <b>but</b> she is also kind.', '→ Not only 放句首要倒裝') +
    ex('<i>It is</i> practice <i>that</i> makes you better.', '→ 強調句：強調 practice', 'o'), 'o'))),

section('什麼是倒裝？否定副詞放句首', cards(2,
  card('倒裝的規則', row('一般：', '主詞 + 助動詞 + 動詞') + row('倒裝：', '否定副詞 + 助動詞 + 主詞 + 動詞') + row('沒有助動詞：', '借 do / does / did') +
    ex('I have <b>never</b> seen such a big dog.', '→ 一般語序') +
    ex('<b>Never have I seen</b> such a big dog.', '→ 倒裝：我從來沒看過這麼大的狗') +
    ex('<b>Seldom does he</b> eat breakfast.', '→ 借 does：他很少吃早餐'), sub='Negative Inversion'),
  card('常見的否定副詞', row('never：', '從不') + row('seldom / rarely：', '很少') + row('little：', '一點也不（Little did I know…）') +
    ex('<i>Rarely do we</i> see snow in Taipei.', '→ 台北很少下雪', 'o') +
    ex('<i>Little did I know</i> that he was the boss.', '→ 我一點也不知道他是老闆', 'o') +
    note('倒裝像疑問句的語序：Have I…? Does he…? Did I…?'), 'o', sub='放句首就要倒裝'), tight=True)),

section('So / Neither / Nor + 助動詞 + 主詞', cards(2,
  card('So：我也是（肯定）', row('公式：', 'So + 助動詞 / be + 主詞') +
    ex('A: I like pizza. B: <b>So do I</b>.', '→ 我也喜歡（like 是一般動詞 → do）') +
    ex('A: She is tired. B: <b>So am I</b>.', '→ 我也累（is → am）') +
    ex('A: Tom has finished. B: <b>So has Amy</b>.', '→ Amy 也做完了（has → has）'), sub='前面是肯定句'),
  card('Neither / Nor：我也不（否定）', row('公式：', 'Neither / Nor + 助動詞 / be + 主詞') +
    ex('A: I can\'t swim. B: <i>Neither can I</i>.', '→ 我也不會', 'o') +
    ex('A: He didn\'t go. B: <i>Nor did she</i>.', '→ 她也沒去', 'o') +
    '<div class="ex o"><div class="en"><span class="bad">So I do.</span> → <span class="good">So do I.</span></div><div class="zh">→ So I do 是「我確實如此」，意思不一樣</div></div>', 'o', sub='前面是否定句')) +
  note('助動詞要跟著前一句：前一句用 can → can；用 is → am / is / are；用一般動詞過去式 → did。')),

section('Not until、Only、No sooner、Hardly', table(['句型', '意思', '例句'], [
  ['Not until + 時間 / 子句 + 倒裝', '直到…才', ('<b>Not until</b> midnight <b>did he</b> go to bed.', '他直到半夜才去睡')],
  ['Only + 副詞 / 介系詞片語 + 倒裝', '只有…才', ('<b>Only then did I</b> understand the problem.', '那時我才明白這個問題')],
  ['Only when / if + 子句 + 倒裝', '只有當…才', ('<b>Only when</b> you work hard <b>will you</b> succeed.', '只有努力才會成功')],
  ['No sooner + had + S + p.p. + than', '一…就…', ('<b>No sooner had I</b> arrived <b>than</b> it began to rain.', '我一到就開始下雨')],
  ['Hardly / Scarcely + had + S + p.p. + when', '一…就…', ('<b>Hardly had she</b> sat down <b>when</b> the phone rang.', '她一坐下電話就響了')],
], audio_col=2) + note('Not until 和 Only 的句子，倒裝放在「主要子句」：Not until he came <b>did we</b> start（不是 did he come）。')),

section('Not only 句首倒裝與地方副詞倒裝', cards(2,
  card('Not only…but (also)…', row('一般：', 'She is not only smart but also kind.') + row('倒裝：', 'Not only + 助動詞 + 主詞…, but + 主詞 + also…') +
    ex('<b>Not only is she</b> smart, but she is also kind.', '→ 她不但聰明，而且善良') +
    ex('<b>Not only did he</b> win, but he also broke the record.', '→ 他不但贏了，還破了紀錄'), sub='只有前半句倒裝'),
  card('地方副詞放句首', row('公式：', '地方副詞 + 動詞 + 名詞主詞') + row('注意：', '主詞是代名詞時「不」倒裝') +
    ex('<i>Here comes</i> the bus!', '→ 公車來了！', 'o') +
    ex('<i>On the hill stands</i> an old temple.', '→ 山丘上矗立著一座老廟', 'o') +
    ex('<i>Here it comes</i>!', '→ 代名詞 it 不倒裝', 'o'), 'o', sub='Here / There / On the hill…'))),

section('條件句的倒裝：省略 if', table(['原句', '倒裝（省略 if）', '例句'], [
  ['If I had known…', 'Had I known…', ('<b>Had I known</b> the truth, I would have told you.', '如果我早知道真相，我就會告訴你了')],
  ['If I were you…', 'Were I you…', ('<b>Were I</b> you, I would take the job.', '如果我是你，我會接受這份工作')],
  ['If you should need…', 'Should you need…', ('<b>Should you need</b> help, please call me.', '萬一你需要幫忙，請打給我')],
], audio_col=2) + note('第 7、8 週學過條件句與假設語氣；把 if 拿掉後，had、were、should 就要搬到主詞前面。這種寫法在英檢中級閱讀很常見。')),

section('強調句：It is / was … that …', cards(2,
  card('把要強調的部分放進 It is…that', row('原句：', 'Tom broke the window yesterday.') +
    ex('<b>It was Tom that</b> broke the window yesterday.', '→ 強調人：是 Tom 打破的') +
    ex('<b>It was the window that</b> Tom broke yesterday.', '→ 強調物：打破的是窗戶') +
    ex('<b>It was yesterday that</b> Tom broke the window.', '→ 強調時間：是昨天打破的'), sub='Cleft Sentence'),
  card('小提醒', row('人：', '可以用 who 代替 that') + row('時態：', '現在用 It is，過去用 It was') + row('怎麼檢查：', '拿掉 It is / was 和 that，句子還要完整') +
    ex('<i>It is</i> my mother <i>who</i> cooks dinner every day.', '→ 每天煮晚餐的是我媽媽', 'o') +
    ex('<i>It was</i> in 2020 <i>that</i> we moved here.', '→ 我們是在 2020 年搬來的', 'o'), 'o', sub='that / who'))),

section('What 強調句與助動詞 do 加強語氣', cards(2,
  card('What…is…', row('公式：', 'What + S + V + is / was + 重點') +
    ex('<b>What I need is</b> a good rest.', '→ 我需要的是好好休息') +
    ex('<b>What he said was</b> true.', '→ 他說的是真的') +
    ex('<b>All I want is</b> a cup of coffee.', '→ 我只想要一杯咖啡'), sub='第 12 週的複合關代 what'),
  card('do / does / did + 原形', row('用途：', '加強語氣「真的、確實」') +
    ex('I <i>do</i> like your new hairstyle.', '→ 我真的很喜歡你的新髮型', 'o') +
    ex('She <i>does</i> work hard.', '→ 她確實很努力', 'o') +
    ex('He <i>did</i> call you yesterday.', '→ 他昨天真的有打給你', 'o'), 'o', sub='後面一定接原形'))),

section('對比頁：容易搞混的四組', two(
  card('So do I 與 So I do', ex('A: I love music. B: <b>So do I</b>.', '→ 我也是') + ex('A: You love music! B: Yes, <i>so I do</i>.', '→ 我確實是（同意對方說的）', 'o')),
  card('一般語序與倒裝', ex('I <b>have never</b> seen it.', '→ 否定副詞在中間，不倒裝') + ex('<i>Never have I</i> seen it.', '→ 否定副詞在句首，要倒裝', 'o'), 'o'), tight=True) + two(
  card('Here comes he 與 Here he comes', ex('<b>Here comes</b> the teacher.', '→ 名詞主詞要倒裝') + ex('<i>Here he comes</i>.', '→ 代名詞主詞不倒裝', 'o')),
  card('It is…that 與 It is…to V', ex('<b>It is</b> Amy <b>that</b> won the prize.', '→ 強調句，拿掉後句子完整') + ex('<i>It is</i> important <i>to</i> exercise.', '→ 虛主詞 it，不是強調句', 'o'), 'o'), tight=True)),

section('學生最常錯的 5 句', top5([
  ('Never I have seen such a thing.', 'Never have I seen such a thing.', '否定副詞放句首，助動詞要放到主詞前面。'),
  ('Seldom he eats breakfast.', 'Seldom does he eat breakfast.', '沒有助動詞時要借 does，動詞改回原形。'),
  ('A: I can\'t swim. B: So can\'t I.', 'A: I can\'t swim. B: Neither can I.', '否定句的「我也不」用 Neither / Nor。'),
  ('Not until he came home he started dinner.', 'Not until he came home did he start dinner.', 'Not until 放句首，主要子句要倒裝。'),
  ('It was Tom what broke the window.', 'It was Tom that broke the window.', '強調句是 It is / was…that（人也可用 who）。'),
])),

section('快問快答 8 題', qas([
  ('Rarely ____ late for school. (he is / is he)', 'is he'),
  ('Little ____ that it was a trick. (I knew / did I know)', 'did I know'),
  ('A: I am hungry. B: So ____ I. (do / am)', 'am'),
  ('A: She didn\'t come. B: Neither ____ I. (did / was)', 'did'),
  ('Not until ten ____ home. (did he get / he got)', 'did he get'),
  ('No sooner had I left ____ it rained. (when / than)', 'than'),
  ('____ I you, I would say sorry. (Were / Was)', 'Were'),
  ('____ I need is more time. (What / That)', 'What'),
])),

section('挑錯練習與句型轉換', two(div(lead('挑錯：每句有一個錯'), qas([
  ('Only then I understood the lesson.', 'I understood → did I understand'),
  ('Hardly had he sat down than the bell rang.', 'than → when'),
  ('Here comes it!', '改成 Here it comes!'),
])), div(lead('改寫成指定句型'), qas([
  ('I have never been so happy.（用 Never 開頭）', 'Never have I been so happy.'),
  ('If I had known, I would have come.（省略 if）', 'Had I known, I would have come.'),
  ('My dad fixed the bike.（強調 my dad）', 'It was my dad that / who fixed the bike.'),
])))),

section('在閱讀與聽力裡找到它', passage(
  '<span class="hl">Never had</span> the village <span class="hl">seen</span> so much snow. <span class="hl">Not until</span> noon <span class="hl">did</span> the roads open again. <span class="hl2">It was</span> an old farmer <span class="hl2">who</span> cleared the main road first. <span class="hl">Hardly had</span> he finished <span class="hl">when</span> the children ran out to play. <span class="hl2">What</span> the village needed <span class="hl2">was</span> a hero, and he was one.') +
  cards(2,
    card('閱讀怎麼用', ul(['句首看到 Never、Not until、Hardly，主詞在助動詞後面，要往後找', 'It was…who / that 中間夾的就是作者要強調的重點', 'What…was… 後半部才是答案的關鍵'])),
    card('聽力怎麼用', ul(['聽到 So do I、Neither can I，表示說話者「也一樣」', 'Not until… 表示「直到那時才」，題目常考時間', 'No sooner…than、Hardly…when 表示兩件事緊接著發生']), 'o'))),

section('口說句型跟讀', lead('先按 🔊 聽，再跟著大聲念，最後換成自己的句子。') + two(div(
  ex('<b>Never have I</b> seen such a beautiful sunset.', '→ 否定副詞倒裝'),
  ex('A: I love bubble tea. B: <b>So do I</b>!', '→ So + 助動詞 + 主詞'),
  ex('<b>Not until</b> I got home <b>did I</b> notice my phone was gone.', '→ Not until 倒裝')), div(
  ex('<i>It was</i> my grandmother <i>who</i> taught me to cook.', '→ 強調句', 'o'),
  ex('<i>What I need</i> most <i>is</i> a long holiday.', '→ What 強調句', 'o')))),

section('重點整理與測驗說明', two(div(
  table(['重點', '規則'], [
    ['否定副詞倒裝', 'Never / Seldom / Little + 助動詞 + 主詞'],
    ['So / Neither', 'So do I（肯定）、Neither can I（否定）'],
    ['Not until / Only', '主要子句倒裝'],
    ['No sooner / Hardly', 'had + S + p.p. + than / when'],
    ['條件句倒裝', 'Had I…、Were I…、Should you…'],
    ['強調句', 'It is / was…that（who）、What…is…、do + 原形']]),
  note('口訣：否定放前頭，助動詞往前走；So 肯定 Neither 否；強調句拿掉 It is 和 that，句子還完整。')), div(
  card('本週測驗：64 題', row('題型：', '文法 20．閱讀 10．克漏字 4．單字 10．聽力 15．口說 5') + ul(['文法 20 題中，16 題是本週新教，4 題回收第 16 週比較與平行結構']), 'o'),
  card('回家作業', ol(['用 Never have I… 寫一句你沒做過的事。', '和家人練習三組 So do I / Neither can I 的對話。', '用 It was…who… 寫一句感謝某個人的話。']))))),
]
