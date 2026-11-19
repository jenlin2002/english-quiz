# 主題 2000 字 Unit 40：Other adverbs 其他副詞（字表依課本單元；詞性、中文、例句、題目為本站自編）
# 副詞沒有適合的照片，全部用 emoji。
def W(w, zh, note, ex, exzh, pic, pos='adv.'):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000', 'no': 40, 'en': 'Other adverbs', 'zh': '其他副詞',
  'intro': '頻率副詞（always、usually、often、sometimes、seldom、never）和其他常用副詞，共 36 個。頻率副詞放在 be 動詞後面、一般動詞前面。',
  'words': [
    W('always', '總是', '100%', 'Lily always wears red shoes.', 'Lily 總是穿紅色的鞋子。', '🔁'),
    W('ever', '曾經', '多用在問句', 'Have you ever been to Japan?', '你曾經去過日本嗎？', '❔'),
    W('never', '從不；絕不', '0%', 'Jay is never late for school.', 'Jay 上學從不遲到。', '🚫'),
    W('often', '時常', '', 'How often do you go to the movies?', '你多常去看電影？', '🔂'),
    W('seldom', '很少；不常', '', 'My grandpa seldom watches TV.', '我爺爺很少看電視。', '🤏'),
    W('sometimes', '有時候', '', 'I sometimes go swimming on weekends.', '我週末有時候會去游泳。', '🌗'),
    W('usually', '通常', '', 'He usually walks to school.', '他通常走路上學。', '🚶'),
    W('actually', '實際上；事實上', '', 'He looks scary, but actually he is very kind.', '他看起來很兇，但其實人很好。', '💡'),
    W('again', '再一次', '', 'Can you say that again?', '你可以再說一次嗎？', '🔄'),
    W('also', '也', '用在肯定句，放在動詞前', 'I like cats. I also like dogs.', '我喜歡貓，我也喜歡狗。', '➕'),
    W('away', '遠離地；離開', 'go away 走開', 'The school is far away from my house.', '學校離我家很遠。', '🏃'),
    W('too', '也；太', '肯定句句尾用 too', 'Your pen is blue, and mine is, too.', '你的筆是藍色的，我的也是。', '✌️'),
    W('almost', '幾乎；差一點', '', 'I almost missed the train.', '我差點錯過火車。', '🫣'),
    W('even', '甚至；連', '', 'He lied to everyone, even his family.', '他對所有人說謊，甚至是他的家人。', '😯'),
    W('finally', '最後；終於', '', 'Finally, I passed the exam.', '我終於通過考試了。', '🏁'),
    W('just', '正好；僅僅；剛剛', '', 'I just finished my homework.', '我剛寫完功課。', '⏱️'),
    W('least', '最少；最小', 'at least 至少', 'You should sleep at least eight hours.', '你應該至少睡八個小時。', '📉'),
    W('maybe', '也許', '放句首；may be 是「可能是」', 'Maybe it will rain tomorrow.', '也許明天會下雨。', '🤷'),
    W('perhaps', '也許', '比 maybe 正式', 'Perhaps she is on her way.', '也許她已經在路上了。', '🤔'),
    W('probably', '大概；很可能', '比 maybe 更確定', 'He will probably come tonight.', '他今晚很可能會來。', '📊'),
    W('really', '真正地；非常', '', 'I really like this song.', '我真的很喜歡這首歌。', '💯'),
    W('so', '如此地；非常', '也可當連接詞：所以', 'Snow White is so kind!', '白雪公主真善良！', '😍'),
    W('still', '仍然', '', 'Are you still hungry?', '你還餓嗎？', '⏳'),
    W('then', '然後；當時', '', 'He did his homework, and then he went to bed.', '他寫完功課，然後去睡覺。', '➡️'),
    W('together', '一起', '', 'Let\'s go shopping together.', '我們一起去逛街吧。', '👨‍👩‍👧'),
    W('twice', '兩次；兩倍', 'once 一次、three times 三次', 'I visit my grandparents twice a month.', '我一個月去看爺爺奶奶兩次。', '✌️'),
    W('very', '非常', '', 'The movie was very funny.', '這部電影非常好笑。', '‼️'),
    W('quite', '相當', '', 'He is quite tall.', '他相當高。', '📏'),
    W('yet', '尚未；已經（問句）', '用在否定句、問句', 'I haven\'t finished my homework yet.', '我還沒寫完功課。', '⌛'),
    W('abroad', '在國外；到國外', 'study abroad 出國留學', 'She wants to study abroad.', '她想出國留學。', '✈️'),
    W('ahead', '在前方；提前', 'go ahead 請便、繼續', 'The bus stop is just ahead.', '公車站就在前面。', '⏩'),
    W('somewhere', '某處', '', 'My keys must be somewhere in this room.', '我的鑰匙一定在這個房間的某個地方。', '📍'),
    W('either', '也（否定句）', '否定句句尾用 either', 'I don\'t like fish. My sister doesn\'t, either.', '我不喜歡魚，我妹妹也不喜歡。', '🙅'),
    W('no', '不；沒有', '', 'No, I\'m not tired.', '不，我不累。', '❌'),
    W('not', '不', '', 'Snoopy is a dog, not a cat.', '史努比是狗，不是貓。', '🚫'),
    W('yes', '是的', '', 'Yes, I love English.', '是的，我愛英文。', '✅'),
  ],
  'focus': [
    {'title': '頻率副詞', 'head': ('副詞', '頻率', '例句'), 'rows': [
      ('always', '100%', 'I always get up at six.'),
      ('usually', '80%', 'He usually walks to school.'),
      ('often', '60%', 'We often play basketball.'),
      ('sometimes', '40%', 'She sometimes cooks dinner.'),
      ('seldom', '10%', 'Grandpa seldom watches TV.'),
      ('never', '0%', 'Jay is never late.'),
    ], 'note': '位置：be 動詞、助動詞後面，一般動詞前面。問頻率用 How often…?'},
    {'title': '「也」的三種說法', 'head': ('副詞', '用在', '例句'), 'rows': [
      ('also', '肯定句，放動詞前', 'I also like dogs.'),
      ('too', '肯定句，放句尾', 'I like dogs, too.'),
      ('either', '否定句，放句尾', 'I don\'t like fish, either.'),
    ], 'note': ''},
    {'title': '也許、大概', 'head': ('副詞', '確定程度', '例句'), 'rows': [
      ('maybe', '一般', 'Maybe it will rain.'),
      ('perhaps', '一般（較正式）', 'Perhaps he is busy.'),
      ('probably', '比較確定', 'He will probably come.'),
    ], 'note': 'maybe（一個字，副詞）和 may be（助動詞＋be）不一樣：He may be a lawyer. ＝ Maybe he is a lawyer.'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '很少；不常', 'opts': ['seldom', 'sometimes', 'still', 'soon'], 'answer': 0, 'exp': 'seldom 很少。'},
    {'type': 'mc', 'q': '幾乎', 'opts': ['also', 'almost', 'always', 'already'], 'answer': 1, 'exp': 'almost 幾乎。'},
    {'type': 'mc', 'q': '兩次', 'opts': ['twice', 'twelve', 'twenty', 'together'], 'answer': 0, 'exp': 'twice 兩次。'},
    {'type': 'mc', 'q': '在國外', 'opts': ['ahead', 'abroad', 'about', 'away'], 'answer': 1, 'exp': 'abroad 在國外。'},
  ]},
  {'title': '② 頻率副詞：選出正確的答案', 'items': [
    {'type': 'mc', 'q': 'A: How ______ does Zoe walk to work?  B: Seldom.', 'opts': ['soon', 'fast', 'often', 'long'], 'answer': 2, 'exp': '問頻率 → How often。'},
    {'type': 'mc', 'q': 'Jay is ______ late for school. He gets up early every day.', 'opts': ['always', 'never', 'usually', 'often'], 'answer': 1, 'exp': '從不遲到 → never。'},
    {'type': 'mc', 'q': 'Which sentence is correct?', 'opts': ['He walks usually to school.', 'He usually walks to school.', 'Usually he walk to school.', 'He walks to usually school.'], 'answer': 1, 'exp': '頻率副詞放一般動詞前面。'},
    {'type': 'mc', 'q': 'Which sentence is correct?', 'opts': ['She always is happy.', 'She is always happy.', 'Always she happy is.', 'She is happy always is.'], 'answer': 1, 'exp': '頻率副詞放 be 動詞後面。'},
  ]},
  {'title': '③ also、too、either', 'items': [
    {'type': 'mc', 'q': 'I don\'t like fish. My sister doesn\'t, ______.', 'opts': ['too', 'also', 'either', 'so'], 'answer': 2, 'exp': '否定句的「也」→ either。'},
    {'type': 'mc', 'q': 'Your pen is blue, and mine is, ______.', 'opts': ['too', 'either', 'also', 'yet'], 'answer': 0, 'exp': '肯定句句尾 → too。'},
    {'type': 'mc', 'q': 'I ate an egg and ______ drank milk this morning.', 'opts': ['also', 'too', 'either', 'so'], 'answer': 0, 'exp': '放在動詞前 → also。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Can you say that {0}? （再一次）', 'blanks': [['again']], 'exp': 'again 再一次。'},
    {'q': 'Let\'s go shopping {0}. （一起）', 'blanks': [['together']], 'exp': 'together 一起。'},
    {'q': 'I haven\'t finished my homework {0}. （還沒）', 'blanks': [['yet']], 'exp': '否定句的「還沒」→ yet。'},
    {'q': 'Are you {0} hungry? （仍然）', 'blanks': [['still']], 'exp': 'still 仍然。'},
    {'q': 'You should sleep at {0} eight hours. （至少）', 'blanks': [['least']], 'exp': 'at least 至少。'},
  ]},
  {'title': '⑤ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'A: Have you ______ been to New York?  B: Yes, I\'ve been there twice.', 'opts': ['ever', 'never', 'already', 'yet'], 'answer': 0, 'exp': 'Have you ever…? 你曾經…嗎？'},
    {'type': 'mc', 'q': '______ it will rain tomorrow. Take an umbrella.', 'opts': ['May be', 'Maybe', 'Very', 'Quite'], 'answer': 1, 'exp': '句首的「也許」→ Maybe。'},
    {'type': 'mc', 'q': 'I ______ missed the train. I got on it just in time.', 'opts': ['almost', 'always', 'never', 'still'], 'answer': 0, 'exp': '差一點 → almost。'},
    {'type': 'mc', 'q': 'He did his homework, and ______ he went to bed.', 'opts': ['than', 'then', 'them', 'there'], 'answer': 1, 'exp': '然後 → then。'},
  ]},
]
