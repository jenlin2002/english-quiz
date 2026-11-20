# LaLa Word Unit 13（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 144–154 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 13, 'en': 'Is It True?', 'zh': '一字多義（十三）',
  'intro': 'post 是網路上的貼文，也是「郵寄」；lie 是說謊，也是「躺」。這個單元有 5 個主題單字、16 個更多單字，'
           '再整理 wish／hope，和字尾 -er／-or、-ess、字首 inter-。',
  'words': [
    W('post', '📮', [
        S('n.', '貼文；公布的資訊', 'Her post got 500 likes.', '她的貼文有五百個讚。'),
        S('n.', '郵政；郵件', 'I sent the gift by post.', '我用郵寄的方式寄禮物。', 'post office 郵局'),
        S('v.', '發布（資訊）', 'Don\'t post your address online.', '不要把你的地址貼到網路上。'),
        S('v.', '寄出（信件、包裹）', 'Can you post this letter for me?', '你可以幫我寄這封信嗎？'),
    ], 'post - posted - posted - posting', key=True),
    W('lie', '🛏️', [
        S('n.', '謊言', 'Don\'t tell a lie.', '不要說謊。', 'tell a lie 說謊'),
        S('v.', '說謊', 'He lied to his mom about his grades.', '他對媽媽謊報成績。', 'lie - lied - lied - lying'),
        S('v.', '躺；臥', 'The cat is lying on the sofa.', '貓躺在沙發上。', 'lie - lay - lain - lying；lie down 躺下'),
    ], '說謊：lie - lied - lied；躺：lie - lay - lain', key=True),
    W('trick', '🃏', [
        S('n.', '惡作劇；騙局', 'They played a trick on their teacher.', '他們對老師惡作劇。', 'play a trick on 對…惡作劇'),
        S('v.', '欺騙', 'The man tricked me into buying a fake watch.', '那個男人騙我買了假手錶。', 'trick + 人 + into + V-ing 騙某人做'),
        S('n.', '技巧；訣竅', 'Here is a trick to remember new words.', '這是一個記新單字的訣竅。', 'magic trick 魔術'),
    ], 'trick - tricked - tricked - tricking', key=True),
    W('check', '✅', [
        S('v.', '檢查；確認', 'Check your answers before you hand in the test.', '交考卷前檢查你的答案。', 'check out 去看看'),
        S('n.', '檢查', 'The doctor gave me a quick check.', '醫生幫我做了簡單的檢查。'),
        S('n.', '支票', 'Can I pay by check?', '我可以用支票付款嗎？'),
        S('n.', '帳單', 'Waiter, can we have the check, please?', '服務生，請給我們帳單。'),
    ], 'check - checked - checked - checking', key=True),
    W('serious', '🧐', [
        S('adj.', '嚴肅的', 'Why do you look so serious?', '你為什麼看起來這麼嚴肅？'),
        S('adj.', '認真的', 'Are you serious? You\'re moving to Japan?', '你是認真的嗎？你要搬去日本？', 'be serious about 對…是認真的'),
        S('adj.', '嚴重的', 'Air pollution is a serious problem.', '空氣汙染是很嚴重的問題。'),
    ], 'serious - more serious - most serious', key=True),
    W('bat', '🦇', [
        S('n.', '蝙蝠', 'Bats sleep in the daytime.', '蝙蝠白天睡覺。', 'as blind as a bat 視力很差'),
        S('n.', '球棒', 'He hit the ball with a bat.', '他用球棒打球。'),
        S('v.', '用球棒擊球', 'It\'s your turn to bat.', '輪到你打擊了。'),
    ], 'bat - batted - batted - batting'),
    W('book', '📕', [
        S('n.', '書', 'I borrowed three books from the library.', '我從圖書館借了三本書。'),
        S('v.', '預訂', 'Dad booked a hotel room for us.', '爸爸幫我們訂了飯店房間。'),
    ], 'book - booked - booked - booking'),
    W('copy', '📄', [
        S('v.', '抄襲', 'Don\'t copy your classmate\'s homework.', '不要抄同學的功課。'),
        S('v.', '複製', 'Copy the file and send it to me.', '把檔案複製一份寄給我。', 'copy and paste 複製貼上'),
        S('v.', '模仿', 'My little sister copies everything I do.', '我妹妹什麼都學我。'),
        S('n.', '複製品；影本', 'This painting is just a copy.', '這幅畫只是複製品。'),
        S('n.', '一本；一份', 'The book sold a million copies.', '這本書賣了一百萬本。'),
    ], 'copy - copied - copied - copying；複數 copies'),
    W('crazy', '🤪', [
        S('adj.', '發瘋的', 'The noise is driving me crazy.', '那噪音快把我逼瘋了。', 'go crazy 發瘋'),
        S('adj.', '著迷的', 'My brother is crazy about basketball.', '我哥哥超迷籃球。', 'be crazy about 為…著迷'),
        S('adj.', '很生氣的', 'Mom will go crazy if she sees this mess.', '媽媽看到這團亂會氣炸。'),
        S('n.', '瘋子', 'Only a crazy would swim in this icy water.', '只有瘋子才會在這麼冰的水裡游泳。'),
    ], 'crazy - crazier - craziest'),
    W('gym', '🏀', [
        S('n.', '體育館', 'We play basketball in the gym on rainy days.', '下雨天我們在體育館打籃球。'),
        S('n.', '健身房', 'My aunt goes to the gym every morning.', '我阿姨每天早上去健身房。'),
        S('n.', '體操；體育課', 'Bring your shoes for gym class.', '體育課要帶運動鞋。'),
    ], '複數 gyms'),
    W('interest', '💵', [
        S('n.', '興趣', 'She has a strong interest in science.', '她對科學很有興趣。'),
        S('n.', '利益', 'The leader should think about the interests of everyone.', '領導者應該考慮每個人的利益。'),
        S('n.', '利息', 'The bank pays interest on your savings.', '銀行會為你的存款付利息。'),
        S('v.', '使感興趣', 'History doesn\'t interest me.', '歷史引不起我的興趣。', 'be interested in 對…有興趣'),
    ], 'interest - interested - interested - interesting'),
    W('nobody', '🙅', [
        S('pron.', '沒有人', 'Nobody knows the answer.', '沒有人知道答案。'),
        S('n.', '小人物', 'He was a nobody before he became famous.', '他成名前只是個無名小卒。'),
    ], '複數 nobodies'),
    W('pop', '🍿', [
        S('v.', '（使）爆開', 'The balloon popped.', '氣球破了。'),
        S('v.', '爆（玉米花）', 'Let\'s pop some corn for the movie.', '我們爆點爆米花配電影吧。'),
        S('n.', '流行音樂；流行歌曲', 'I like K-pop.', '我喜歡韓國流行音樂。'),
        S('adj.', '流行的；通俗的', 'She is a pop singer.', '她是流行歌手。'),
    ], 'pop - popped - popped - popping'),
    W('race', '🏃', [
        S('v.', '和…比賽速度', 'I\'ll race you to the gate!', '我們比賽看誰先跑到大門！'),
        S('n.', '比賽（速度）', 'Our class won the relay race.', '我們班贏了接力賽。'),
        S('n.', '種族；民族', 'We should respect people of every race.', '我們應該尊重每個種族的人。'),
    ], 'race - raced - raced - racing'),
    W('sentence', '✍️', [
        S('n.', '句子', 'Make a sentence with the word "happy."', '用 happy 造一個句子。'),
        S('n.', '判決；刑罰', 'The thief got a two-year sentence.', '小偷被判兩年徒刑。'),
        S('v.', '宣判', 'The judge sentenced him to two years in prison.', '法官判他兩年徒刑。'),
    ], 'sentence - sentenced - sentenced - sentencing'),
    W('since', '📆', [
        S('adv.', '從那時起', 'He moved away last year, and I haven\'t seen him since.', '他去年搬走，從那之後我就沒見過他。'),
        S('prep.', '自…以來', 'I have lived here since 2020.', '我從 2020 年起就住在這裡。'),
        S('conj.', '自從…', 'We have been friends since we were five.', '我們從五歲起就是朋友。'),
        S('conj.', '因為；既然', 'Since it\'s raining, let\'s stay home.', '既然在下雨，我們待在家吧。'),
    ]),
    W('slim', '🪄', [
        S('adj.', '苗條的', 'She is tall and slim.', '她又高又苗條。'),
        S('adj.', '渺茫的；微小的', 'We only have a slim chance of winning.', '我們贏的機會很渺茫。'),
        S('v.', '減輕體重', 'Dad is trying to slim down.', '爸爸正在努力減重。', 'slim down 減重'),
    ], 'slim - slimmer - slimmest；slim - slimmed - slimmed - slimming'),
    W('spell', '🔤', [
        S('v.', '拼字', 'How do you spell your name?', '你的名字怎麼拼？'),
        S('v.', '輪替；接手', 'Can I spell you for a while?', '我可以換手幫你一下嗎？'),
        S('n.', '一段時間', 'We had a spell of hot weather last week.', '上星期熱了一陣子。'),
        S('n.', '咒語；魔咒', 'The witch put a spell on the princess.', '巫婆對公主下了咒。'),
    ], 'spell - spelled（spelt） - spelled（spelt） - spelling'),
    W('tip', '💡', [
        S('v.', '給小費', 'In the U.S., people tip the waiter.', '在美國，人們會給服務生小費。'),
        S('n.', '小費', 'We left a tip on the table.', '我們在桌上留了小費。'),
        S('n.', '建議；訣竅', 'Here are some tips for learning English.', '這裡有一些學英文的訣竅。'),
        S('v.', '（使）傾斜；翻倒', 'Don\'t tip your chair back.', '不要把椅子往後翹。'),
    ], 'tip - tipped - tipped - tipping'),
    W('touch', '👆', [
        S('v.', '觸摸', 'Please don\'t touch the paintings.', '請勿觸摸畫作。'),
        S('n.', '觸覺', 'Babies learn about things by touch.', '嬰兒靠觸覺認識東西。', 'keep in touch 保持聯絡'),
        S('v.', '感動', 'Her story touched everyone.', '她的故事感動了每個人。'),
    ], 'touch - touched - touched - touching'),
    W('wish', '🌠', [
        S('v.', '希望（不太可能的事）', 'I wish I could fly.', '真希望我會飛。', 'I wish + 過去式：與現在事實相反'),
        S('n.', '願望', 'Close your eyes and make a wish.', '閉上眼睛許個願。', 'make a wish 許願'),
        S('v.', '祝福', 'We wish you a happy new year.', '祝你新年快樂。'),
        S('n.', '祝福（wishes）', 'Best wishes to you and your family.', '祝福你和你的家人。'),
    ], 'wish - wished - wished - wishing'),
    W('farmer', '👨‍🌾', [S('n.', '農夫', 'The farmer grows rice and corn.', '農夫種稻米和玉米。')], 'farm + -er'),
    W('actor', '🎭', [S('n.', '男演員；演員', 'He is a famous actor.', '他是有名的演員。')], 'act + -or'),
    W('waiter', '🤵', [S('n.', '男服務生', 'The waiter brought us some water.', '服務生端水給我們。')], 'wait + -er'),
    W('mail carrier', '📬', [S('n.', '郵差', 'The mail carrier comes at ten every morning.', '郵差每天早上十點來。')], 'carry + -er'),
    W('can opener', '🥫', [S('n.', '開罐器', 'I need a can opener to open the beans.', '我需要開罐器打開豆子罐頭。')], 'open + -er'),
    W('CD player', '💿', [S('n.', 'CD 播放器', 'Grandpa still uses a CD player.', '爺爺還在用 CD 播放器。')], 'play + -er'),
    W('actress', '👩‍🎤', [S('n.', '女演員', 'She won the Best Actress award.', '她得到最佳女主角獎。')], 'act + -ress'),
    W('waitress', '🙋‍♀️', [S('n.', '女服務生', 'The waitress took our order.', '女服務生幫我們點餐。')], 'wait + -ress'),
    W('princess', '👸', [S('n.', '公主', 'The princess lived in a big castle.', '公主住在一座大城堡裡。')], 'prince + -ess'),
    W('interview', '🎤', [
        S('n.', '面試；採訪', 'I have a job interview tomorrow.', '我明天有工作面試。'),
        S('v.', '採訪；面試', 'The reporter interviewed the singer.', '記者採訪了那位歌手。'),
    ], 'inter- + view'),
    W('Internet', '🌐', [S('n.', '網際網路', 'You can find a lot of information on the Internet.', '你可以在網路上找到很多資訊。', 'surf the Internet 上網')], 'inter- + net'),
  ],
  'focus': [
    {'title': '易混淆字：wish 和 hope', 'head': ('單字', '用法', '例句'), 'rows': [
      ('wish', '希望不太可能或不會發生的事：I wish + 過去式；也用來祝福', 'I wish I were taller.／I wish you good luck.'),
      ('hope', '希望「有可能」發生的事：hope + to V／hope + that 子句', 'I hope I can pass the test.'),
    ], 'note': ''},
    {'title': '字尾 -er／-or：做某件事的人或東西', 'head': ('原來的字', '加字尾', '意思'), 'rows': [
      ('farm 耕作', 'farmer', '農夫'),
      ('act 演戲', 'actor', '演員'),
      ('wait 等候', 'waiter', '服務生'),
      ('carry 搬運', 'mail carrier', '郵差'),
      ('open 打開', 'can opener', '開罐器'),
      ('play 播放', 'CD player', 'CD 播放器'),
    ], 'note': ''},
    {'title': '字尾 -ess：女性', 'head': ('原來的字', '加 -ess', '意思'), 'rows': [
      ('actor 男演員', 'actress', '女演員'),
      ('waiter 男服務生', 'waitress', '女服務生'),
      ('prince 王子', 'princess', '公主'),
    ], 'note': ''},
    {'title': '字首 inter-：在…之間；互相', 'head': ('原來的字', '加 inter-', '意思'), 'rows': [
      ('view 看法', 'interview', '面試；採訪'),
      ('net 網子', 'Internet', '網際網路'),
    ], 'note': ''},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('lie', '說謊', '躺（lie - lay - lain）'),
      ('check', '檢查', '支票；帳單'),
      ('bat', '球棒', '蝙蝠'),
      ('book', '書', '預訂'),
      ('race', '比賽', '種族'),
      ('sentence', '句子', '判決'),
      ('spell', '拼字', '咒語；一段時間'),
      ('tip', '小費', '訣竅；傾斜'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'The dog is <b>lying</b> under the table.', 'opts': ['說謊', '躺著', '玩耍', '吃東西'], 'answer': 1, 'exp': 'lie 躺，lying 正在躺著。'},
    {'type': 'mc', 'q': 'Mom <b>booked</b> two tickets for the concert.', 'opts': ['讀', '預訂', '寫', '賣'], 'answer': 1, 'exp': 'book 動詞：預訂。'},
    {'type': 'mc', 'q': 'Can we have the <b>check</b>, please?', 'opts': ['檢查', '支票', '帳單', '菜單'], 'answer': 2, 'exp': '餐廳要 the check → 帳單。'},
    {'type': 'mc', 'q': 'The banks pay <b>interest</b> on your money.', 'opts': ['興趣', '利益', '利息', '注意'], 'answer': 2, 'exp': '銀行付給你的 → 利息。'},
    {'type': 'mc', 'q': 'The witch cast a <b>spell</b> on the prince.', 'opts': ['拼字', '一段時間', '咒語', '接手'], 'answer': 2, 'exp': 'cast a spell 下咒。'},
    {'type': 'mc', 'q': 'Here\'s a <b>tip</b>: drink water before you feel thirsty.', 'opts': ['小費', '建議；訣竅', '傾斜', '尖端'], 'answer': 1, 'exp': '一個建議。'},
    {'type': 'mc', 'q': 'We were all <b>touched</b> by the movie.', 'opts': ['摸', '觸覺', '感動', '聯絡'], 'answer': 2, 'exp': 'be touched 被感動。'},
    {'type': 'mc', 'q': 'There is only a <b>slim</b> chance of rain today.', 'opts': ['苗條的', '渺茫的；微小的', '很大的', '減重'], 'answer': 1, 'exp': 'slim chance 機會渺茫。'},
    {'type': 'mc', 'q': '<b>Since</b> you are tired, you can go to bed early.', 'opts': ['自從', '從那時起', '既然', '雖然'], 'answer': 2, 'exp': 'since 表示原因：既然。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'A ______ is flying in the dark cave.  ／  He hit the ball with his ______.', 'opts': ['bird', 'bat', 'club', 'stick'], 'answer': 1, 'exp': 'bat 蝙蝠／球棒。'},
    {'type': 'mc', 'q': 'Can you ______ this letter for me?  ／  I liked your ______ on Instagram.', 'opts': ['send', 'post', 'mail', 'share'], 'answer': 1, 'exp': 'post 寄出／貼文。'},
    {'type': 'mc', 'q': 'Don\'t ______ my homework.  ／  The library has two ______s of this book.', 'opts': ['copy', 'read', 'print', 'steal'], 'answer': 0, 'exp': 'copy 抄／一本。'},
    {'type': 'mc', 'q': 'The bubble will ______ if you touch it.  ／  Do you like K-______ music?', 'opts': ['pop', 'break', 'rock', 'jazz'], 'answer': 0, 'exp': 'pop 爆開／流行音樂。'},
    {'type': 'mc', 'q': 'Who won the 100-meter ______?  ／  People of every ______ should be treated fairly.', 'opts': ['game', 'race', 'country', 'run'], 'answer': 1, 'exp': 'race 比賽／種族。'},
  ]},
  {'title': '③ 易混淆字與字首字尾', 'items': [
    {'type': 'mc', 'q': 'I ______ I had a million dollars.', 'opts': ['hope', 'wish', 'want', 'think'], 'answer': 1, 'exp': '不太可能的事 → wish + 過去式。'},
    {'type': 'mc', 'q': 'I ______ to see you again soon.', 'opts': ['wish', 'hope', 'wishes', 'hoping'], 'answer': 1, 'exp': 'hope + to V。'},
    {'type': 'mc', 'q': 'The woman in the movie is a famous ______.', 'opts': ['actor', 'actress', 'waiter', 'prince'], 'answer': 1, 'exp': '女演員 actress。'},
    {'type': 'mc', 'q': 'A person who brings letters to your house is a ______.', 'opts': ['farmer', 'waiter', 'mail carrier', 'can opener'], 'answer': 2, 'exp': '郵差 mail carrier。'},
    {'type': 'mc', 'q': 'The reporter wants to ______ the new mayor.', 'opts': ['internet', 'interview', 'interest', 'invite'], 'answer': 1, 'exp': 'interview 採訪。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Don\'t play a {0} on your little brother. （惡作劇）', 'blanks': [['trick']], 'exp': 'play a trick on 對…惡作劇。'},
    {'q': 'Are you {0} about learning to fly a plane? （認真的）', 'blanks': [['serious']], 'exp': 'be serious about 對…認真。'},
    {'q': 'My sister is {0} about K-pop. （著迷的）', 'blanks': [['crazy']], 'exp': 'be crazy about 為…著迷。'},
    {'q': '{0} knows where the key is. （沒有人）', 'blanks': [['Nobody', 'nobody']], 'exp': 'nobody 沒有人。'},
    {'q': 'Let\'s keep in {0} after graduation. （聯絡）', 'blanks': [['touch']], 'exp': 'keep in touch 保持聯絡。'},
    {'q': 'Blow out the candles and make a {0}! （願望）', 'blanks': [['wish']], 'exp': 'make a wish 許願。'},
  ]},
]
