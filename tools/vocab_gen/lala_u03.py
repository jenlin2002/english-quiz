# LaLa Word Unit 3（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 33–41 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 3, 'en': 'Sports Day', 'zh': '一字多義（三）',
  'intro': '運動會上，跑第二名是 second，跑完也可以說 The race is over。這個單元有 5 個主題單字、6 個更多單字，'
           '再整理 date／day、on／above／over、they\'re／their／there，和字首 un-（unhappy、unlucky）。',
  'words': [
    W('around', '🔄', [
        S('prep.', '圍繞', 'The moon goes around the Earth.', '月亮繞著地球轉。'),
        S('adv.', '轉身；轉過來', 'Turn around and look at me.', '轉過來看著我。', 'turn around 轉身'),
        S('adv.', '到處', 'We walked around the night market.', '我們在夜市到處逛。', 'look around 到處看；show… around 帶…參觀'),
        S('adv.', '在附近', 'Is there a bank around here?', '這附近有銀行嗎？', 'around the corner 在轉角；即將到來'),
        S('adv.', '大約', 'I get up around six o\'clock.', '我大約六點起床。'),
    ], key=True),
    W('back', '🔙', [
        S('adv.', '向後', 'Please step back from the door.', '請從門邊往後退。'),
        S('adv.', '回到原來的樣子', 'My hair will grow back soon.', '我的頭髮很快就會長回來。', 'give back 歸還；pay back 還錢'),
        S('adv.', '回覆；返回', 'I\'ll call you back later.', '我等一下再回你電話。'),
        S('n.', '背部', 'My back hurts after playing basketball.', '打完籃球我的背好痛。', 'back to back 背靠背；連續地'),
        S('v.', '倒退', 'Dad backed the car out of the garage.', '爸爸把車倒出車庫。'),
        S('v.', '支持', 'Don\'t worry. We will back you up.', '別擔心，我們會支持你。', 'back up 支持；備份'),
    ], 'back - backed - backed - backing', key=True),
    W('second', '🥈', [
        S('adj.', '第二的；再一次的', 'This is my second time in Japan.', '這是我第二次來日本。', 'a second time 再一次；second-hand 二手的'),
        S('n.', '第二名', 'Tom came second in the race.', 'Tom 賽跑得第二名。'),
        S('adv.', '其次', 'First, wash your hands. Second, set the table.', '首先洗手，其次擺好餐具。'),
        S('n.', '秒', 'Wait a second, please.', '請等一下。', 'in seconds 一下子；馬上'),
        S('v.', '贊成', 'A: Let\'s order pizza.  B: I second that!', 'A：我們叫披薩吧。 B：我贊成！'),
    ], 'second - seconded - seconded - seconding', key=True),
    W('only', '☝️', [
        S('adv.', '只；僅；才', 'I have only ten dollars.', '我只有十塊錢。', 'only + 數字 才…；only when 只有在…的時候'),
        S('adv.', '剛剛（only just）', 'The movie has only just started.', '電影才剛開始。', 'only just 才剛…'),
        S('adj.', '唯一的', 'Lucy is an only child.', 'Lucy 是獨生女。', 'only child 獨生子女；the only way 唯一的方法'),
    ], key=True),
    W('over', '🏁', [
        S('adj.', '結束的', 'The game is over. We won!', '比賽結束了，我們贏了！'),
        S('prep.', '超過', 'Over 300 students came to the show.', '超過三百個學生來看表演。'),
        S('prep.', '在…上方；覆蓋', 'A bird flew over our heads.', '一隻鳥從我們頭上飛過。'),
        S('prep.', '在…期間', 'What did you do over the summer?', '你暑假做了什麼？'),
        S('prep.', '從（病、難過）恢復', 'He is over his cold now.', '他感冒已經好了。'),
        S('adv.', '到（某處）', 'Come over here and sit with us.', '過來這裡和我們一起坐。', 'come over 過來；over there 那邊'),
        S('adv.', '再一次；反覆', 'I made a mistake, so I started over.', '我寫錯了，所以重新來過。', 'over and over 一再；start over 重新來'),
    ], key=True),
    W('bear', '🐻', [
        S('n.', '熊', 'The bear is catching fish in the river.', '熊在河裡抓魚。'),
        S('v.', '忍受', 'I can\'t bear the noise anymore.', '我再也受不了這個噪音了。'),
        S('v.', '生（孩子）；結（果實）', 'This apple tree bears a lot of fruit.', '這棵蘋果樹結很多果實。'),
        S('v.', '承受（重量）', 'Can this old bridge bear a heavy truck?', '這座舊橋撐得住重型卡車嗎？'),
    ], 'bear - bore - born（borne） - bearing'),
    W('clean', '🧽', [
        S('adj.', '乾淨的', 'Keep your room clean.', '保持你的房間乾淨。'),
        S('adj.', '俐落的；漂亮的', 'He made a clean shot and scored.', '他漂亮地一投得分。'),
        S('v.', '把…弄乾淨', 'Let\'s clean up the classroom.', '我們來打掃教室吧。', 'clean up 清理'),
    ], 'clean - cleaner - cleanest；clean - cleaned - cleaned - cleaning'),
    W('date', '📅', [
        S('n.', '日期', 'What\'s the date today?', '今天幾月幾號？', 'set a date 訂日期'),
        S('n.', '約會；約會對象', 'He has a date with Amy on Friday.', '他星期五和 Amy 有約會。', 'have a date with 和…約會'),
        S('v.', '在…寫上日期', 'Please date the letter before you send it.', '寄信前請寫上日期。'),
        S('v.', '和…交往', 'They have been dating for two years.', '他們已經交往兩年了。'),
        S('v.', '使過時', 'Those old phones really date the movie.', '那些舊手機讓這部電影顯得很過時。'),
    ], 'date - dated - dated - dating'),
    W('example', '💡', [
        S('n.', '例子', 'Can you give me an example?', '你可以給我舉個例子嗎？', 'for example 例如；follow the example 照範例'),
        S('n.', '榜樣', 'Big brothers should set a good example.', '哥哥們應該樹立好榜樣。', 'set an example 樹立榜樣'),
        S('n.', '警惕（make an example of）', 'The teacher made an example of the boy who cheated.', '老師拿作弊的男孩來殺雞儆猴。', 'make an example of 以…為戒'),
    ], '複數 examples'),
    W('next', '⏭️', [
        S('adj.', '下一個的', 'See you next week!', '下星期見！', 'next time / week / year 下次／下星期／明年'),
        S('adj.', '旁邊的', 'Come and sit next to me.', '來坐我旁邊。', 'next to 在旁邊；next door 隔壁'),
        S('adv.', '接下來', 'What should I do next?', '我接下來該做什麼？'),
    ]),
    W('right', '👉', [
        S('adj.', '正確的', 'You got the right answer!', '你答對了！', 'be right about 判斷正確'),
        S('adj.', '右邊的', 'Raise your right hand.', '舉起你的右手。'),
        S('adv.', '向右', 'Turn right at the corner.', '在轉角右轉。'),
        S('adv.', '立刻；正好', 'Come here right now!', '馬上過來！', 'right now 現在；立刻；right away 立刻'),
        S('n.', '權利', 'Every child has the right to go to school.', '每個孩子都有上學的權利。'),
    ], '複數 rights'),
    W('unhappy', '😞', [
        S('adj.', '不快樂的；不滿意的', 'She was unhappy about her test score.', '她對考試分數不滿意。', 'be unhappy about 對…不滿'),
    ], 'unhappy - unhappier - unhappiest'),
    W('unlucky', '🐈‍⬛', [
        S('adj.', '不幸的；倒楣的', 'Some people think 13 is an unlucky number.', '有些人認為 13 是不吉利的數字。'),
    ], 'unlucky - unluckier - unluckiest'),
  ],
  'focus': [
    {'title': '易混淆字：date 和 day', 'head': ('單字', '用法', '例句'), 'rows': [
      ('date', '幾月幾號（特定的日期）', 'What\'s the date today? It\'s May 20.'),
      ('day', '一天、星期幾', 'What day is it today? It\'s Wednesday.'),
    ], 'note': ''},
    {'title': '易混淆字：on／above／over', 'head': ('單字', '用法', '例句'), 'rows': [
      ('on', '在…上面，有接觸', 'The cup is on the table.'),
      ('above', '在…上方，沒有接觸；也可以表示「高於」', 'The lamp is above the table.／kids aged 7 and above'),
      ('over', '在…正上方；常有「越過、覆蓋」的動作感', 'The cat jumped over the table.'),
    ], 'note': ''},
    {'title': '發音一樣：they\'re／their／there', 'head': ('單字', '意思', '例句'), 'rows': [
      ('they\'re', '＝ they are 他們是', 'They\'re my classmates.'),
      ('their', '他們的（後面接名詞）', 'Their dog is very cute.'),
      ('there', '那裡；There is / are 有…', 'There are two cats over there.'),
    ], 'note': ''},
    {'title': '字首 un-：「不」或「相反」', 'head': ('原來的字', '加 un-', '意思'), 'rows': [
      ('happy 快樂的', 'unhappy', '不快樂的'),
      ('lucky 幸運的', 'unlucky', '不幸的'),
      ('kind 親切的', 'unkind', '不親切的'),
      ('lock 鎖上', 'unlock', '打開（鎖）'),
    ], 'note': 'unhappy、unlucky 的比較級要把 y 改成 i：unhappier、unluckiest。'},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'The movie is <b>over</b>. Let\'s go home.', 'opts': ['超過', '結束的', '在上方', '再一次'], 'answer': 1, 'exp': 'be over 結束了。'},
    {'type': 'mc', 'q': 'I can\'t <b>bear</b> this hot weather.', 'opts': ['熊', '忍受', '生（孩子）', '結果實'], 'answer': 1, 'exp': 'can\'t bear 受不了。'},
    {'type': 'mc', 'q': 'Everyone has the <b>right</b> to be happy.', 'opts': ['右邊', '正確的', '權利', '立刻'], 'answer': 2, 'exp': 'have the right to 有…的權利。'},
    {'type': 'mc', 'q': 'Ann is going on a <b>date</b> with her boyfriend tonight.', 'opts': ['日期', '約會', '旅行', '派對'], 'answer': 1, 'exp': 'go on a date 去約會。'},
    {'type': 'mc', 'q': 'Wait a <b>second</b>. I\'ll get my coat.', 'opts': ['第二', '其次', '秒；一下子', '贊成'], 'answer': 2, 'exp': 'wait a second 等一下。'},
    {'type': 'mc', 'q': 'There are <b>around</b> forty people in the room.', 'opts': ['圍繞', '到處', '大約', '在附近'], 'answer': 2, 'exp': 'around + 數字：大約。'},
    {'type': 'mc', 'q': 'My mom is my best <b>example</b>. She works hard every day.', 'opts': ['例子', '榜樣', '警告', '題目'], 'answer': 1, 'exp': '值得學習的人 → 榜樣。'},
    {'type': 'mc', 'q': 'Kevin is an <b>only</b> child. He has no brothers or sisters.', 'opts': ['只', '才剛', '唯一的', '孤單的'], 'answer': 2, 'exp': 'only child 獨生子女。'},
    {'type': 'mc', 'q': 'I hurt my <b>back</b> when I picked up the heavy box.', 'opts': ['背部', '向後', '回來', '支持'], 'answer': 0, 'exp': 'hurt my back 背受傷。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'Turn ______ at the bank.  ／  You are ______. The answer is C.', 'opts': ['left', 'right', 'back', 'around'], 'answer': 1, 'exp': 'right 右轉／正確的。'},
    {'type': 'mc', 'q': 'I\'ll call you ______ later.  ／  I sat in the ______ of the bus.', 'opts': ['back', 'again', 'end', 'over'], 'answer': 0, 'exp': 'call back 回電／the back of 後面。'},
    {'type': 'mc', 'q': 'There are sixty ______ in a minute.  ／  May won ______ place in the contest.', 'opts': ['times', 'second', 'seconds / second', 'hours / first'], 'answer': 2, 'exp': 'second 秒／第二。'},
    {'type': 'mc', 'q': 'What\'s the ______ today?  ／  He asked her out on a ______.', 'opts': ['day', 'time', 'date', 'party'], 'answer': 2, 'exp': 'date 日期／約會。'},
    {'type': 'mc', 'q': 'The ______ is sleeping in the cave.  ／  I can\'t ______ the pain.', 'opts': ['lion', 'bear', 'stand', 'dog'], 'answer': 1, 'exp': 'bear 熊／忍受。'},
  ]},
  {'title': '③ 易混淆字：選出正確的字', 'items': [
    {'type': 'mc', 'q': 'What ______ is it today? It\'s Friday.', 'opts': ['date', 'day', 'time', 'week'], 'answer': 1, 'exp': '問星期幾用 day。'},
    {'type': 'mc', 'q': 'The plane flew ______ the mountains.', 'opts': ['on', 'over', 'in', 'at'], 'answer': 1, 'exp': '從上方飛越 → over。'},
    {'type': 'mc', 'q': 'There is a picture ______ the wall.', 'opts': ['on', 'above', 'over', 'up'], 'answer': 0, 'exp': '掛在牆面上（有接觸）→ on。'},
    {'type': 'mc', 'q': '______ my cousins. They live in Tainan.', 'opts': ['There', 'Their', 'They\'re', 'Them'], 'answer': 2, 'exp': 'They\'re = They are。'},
    {'type': 'mc', 'q': 'The kids put ______ bags on the desks.', 'opts': ['there', 'their', 'they\'re', 'they'], 'answer': 1, 'exp': '後面接名詞 → their 他們的。'},
    {'type': 'mc', 'q': 'I lost my wallet today. I\'m so ______.', 'opts': ['lucky', 'unlucky', 'happy', 'kind'], 'answer': 1, 'exp': '掉錢包 → unlucky 倒楣的。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Please clean {0} your desk before you go. （清理）', 'blanks': [['up']], 'exp': 'clean up 清理。'},
    {'q': 'My grandparents live next {0}. （隔壁）', 'blanks': [['door']], 'exp': 'next door 隔壁。'},
    {'q': 'Many animals, for {0}, cats and dogs, can hear very well. （例如）', 'blanks': [['example']], 'exp': 'for example 例如。'},
    {'q': 'Let me show you {0} our school. （到處）', 'blanks': [['around']], 'exp': 'show… around 帶…參觀。'},
    {'q': 'I wrote it wrong, so I had to start {0}. （重新）', 'blanks': [['over']], 'exp': 'start over 重新來過。'},
    {'q': 'The boy was {0} because he lost the game. （不快樂的）', 'blanks': [['unhappy']], 'exp': 'un + happy = unhappy。'},
  ]},
]
