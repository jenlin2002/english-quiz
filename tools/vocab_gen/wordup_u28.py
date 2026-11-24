# WORD UP 複習區 Unit 28（WORD UP「L-II」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 28, 'en': 'L-II', 'zh': 'L 開頭（二）',
  'intro': 'WORD UP「L-II」的 37 個字（lick 到 lunch）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('lick', 'v.', '舔', '', 'The dog licked my hand.', '狗舔了我的手。', '👅'),
    W('lid', 'n.', '蓋子', '', 'Put the lid on the pot.', '把鍋蓋蓋上。', '🫕'),
    W('lie', 'v./n.', '說謊；躺；謊話', '說謊 lie-lied-lied；躺 lie-lay-lain', 'Don\'t tell a lie.', '不要說謊。', '🤥'),
    W('life', 'n.', '生活；生命', '複數 lives', 'Life is beautiful.', '人生很美好。', '🌱'),
    W('lift', 'v./n.', '舉起；搭便車；電梯', '', 'Can you lift this heavy box?', '你舉得起這個重箱子嗎？', '🏋️'),
    W('light', 'n./adj./v.', '光；燈；輕的；點燃', '', 'Turn off the light.', '關燈。', '💡'),
    W('lightning', 'n.', '閃電', 'thunder 雷聲', 'I saw lightning in the sky.', '我看到天空有閃電。', '⚡'),
    W('like', 'v./prep.', '喜歡；像', 'like + V-ing／to V；look like 看起來像', 'You look like your mom.', '你長得像你媽媽。', '👍'),
    W('likely', 'adj.', '可能的', 'be likely to V', 'It is likely to rain tomorrow.', '明天可能會下雨。', '🌦️'),
    W('limit', 'n./v.', '限制', 'speed limit 速限', 'There is a time limit for the test.', '這個考試有時間限制。', '🚧'),
    W('line', 'n.', '線；行；隊伍', 'stand in line 排隊', 'Please stand in line.', '請排隊。', '📏'),
    W('link', 'n./v.', '連結；連接', '', 'Click on the link.', '點那個連結。', '🔗'),
    W('lion', 'n.', '獅子', '', 'The lion is the king of animals.', '獅子是萬獸之王。', '🦁'),
    W('lip', 'n.', '嘴唇', '', 'My lips are dry in winter.', '冬天我的嘴唇很乾。', '👄'),
    W('liquid', 'n./adj.', '液體；液體的', 'solid 固體', 'Water is a liquid.', '水是液體。', '💧'),
    W('list', 'n.', '清單', 'shopping list 購物清單', 'Make a shopping list before you go.', '出門前先列購物清單。', '📝'),
    W('listen', 'v.', '聽', 'listen to + 東西；t 不發音', 'Listen to the teacher.', '聽老師說。', '🎧'),
    W('little', 'adj./adv.', '小的；少的', 'a little 一點；little 幾乎沒有；接不可數名詞', 'I have a little money.', '我有一點錢。', '🤏'),
    W('live', 'v./adj.', '居住；活的；現場的', 'live in + 地點', 'I live in Taipei.', '我住在台北。', '🏠'),
    W('loaf', 'n.', '一條（麵包）', '複數 loaves', 'Mom bought a loaf of bread.', '媽媽買了一條吐司。', '🍞'),
    W('local', 'adj.', '當地的', '', 'Let\'s try some local food.', '我們來吃點當地美食吧。', '📍'),
    W('lock', 'v./n.', '鎖', '', 'Did you lock the door?', '你鎖門了嗎？', '🔒'),
    W('London', 'n.', '倫敦', '', 'London is the capital of the UK.', '倫敦是英國的首都。', '🎡'),
    W('lonely', 'adj.', '寂寞的', 'alone 獨自（事實）', 'He felt lonely after his friends moved away.', '朋友們搬走後他覺得很寂寞。', '😔'),
    W('long', 'adj./adv.', '長的；長久', 'How long…? 多久', 'How long have you lived here?', '你住在這裡多久了？', '📐'),
    W('look', 'v.', '看；看起來', 'look at／look for 找／look after 照顧', 'I\'m looking for my glasses.', '我在找我的眼鏡。', '👀'),
    W('lose', 'v.', '遺失；輸', '三態 lose-lost-lost', 'Our team lost the game.', '我們隊輸了比賽。', '😞'),
    W('loser', 'n.', '輸家', 'winner 贏家', 'There is always a winner and a loser.', '總會有贏家和輸家。', '🥈'),
    W('loss', 'n.', '損失；喪失', '', 'The fire caused a big loss.', '那場火災造成很大的損失。', '📉'),
    W('lot', 'n.', '許多', 'a lot of = lots of', 'I have a lot of friends.', '我有很多朋友。', '🔢'),
    W('loud', 'adj.', '大聲的', 'loudly 大聲地', 'The music is too loud.', '音樂太大聲了。', '🔊'),
    W('love', 'v./n.', '愛', 'love + V-ing／to V', 'I love playing basketball.', '我超愛打籃球。', '❤️'),
    W('lovely', 'adj.', '可愛的；美好的', '-ly 結尾但是形容詞', 'What a lovely day!', '多美好的一天！', '🌸'),
    W('lover', 'n.', '愛好者；情人', 'music lover 音樂愛好者', 'He is a big book lover.', '他很愛看書。', '💕'),
    W('low', 'adj.', '低的', 'high 高的', 'The price is very low.', '價格很低。', '⬇️'),
    W('lucky', 'adj.', '幸運的', 'luck 運氣', 'You are so lucky!', '你真幸運！', '🍀'),
    W('lunch', 'n.', '午餐', 'have lunch', 'What did you have for lunch?', '你午餐吃什麼？', '🍱'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('look at / look for / look after', '看 ／ 找 ／ 照顧', 'look for my key'),
      ('alone / lonely', '獨自 ／ 寂寞的', 'live alone but not lonely'),
      ('a little / little', '一點 ／ 幾乎沒有（不可數）', 'a little milk'),
      ('lose / loser / loss', '輸、遺失 ／ 輸家 ／ 損失', 'lose the game'),
      ('a lot of / lots of', '許多', 'a lot of books'),
      ('stand in line', '排隊', 'stand in line for tickets'),
      ('be likely to V', '可能會…', 'likely to snow'),
    ], 'note': 'life → lives、loaf → loaves：f 結尾的名詞複數常變成 -ves。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '閃電', 'opts': ['light', 'lightning', 'likely', 'liquid'], 'answer': 1, 'exp': 'lightning 閃電。'},
    {'type': 'mc', 'q': '蓋子', 'opts': ['lid', 'lip', 'lick', 'link'], 'answer': 0, 'exp': 'lid 蓋子。'},
    {'type': 'mc', 'q': '當地的', 'opts': ['lonely', 'lovely', 'local', 'lucky'], 'answer': 2, 'exp': 'local 當地的。'},
    {'type': 'mc', 'q': '損失', 'opts': ['loser', 'lose', 'lot', 'loss'], 'answer': 3, 'exp': 'loss 損失。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '寂寞的（l＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['lonely']], 'exp': 'lonely。'},
    {'q': '液體（l＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['liquid']], 'exp': 'liquid。'},
    {'q': '幸運的（l＿＿＿＿，5 個字母）：{0}', 'blanks': [['lucky']], 'exp': 'lucky。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'I {0} my umbrella on the bus yesterday. （遺失，過去式）', 'blanks': [['lost']], 'exp': 'lose 的過去式 lost。'},
    {'q': 'Please {0} to me carefully. （聽）', 'blanks': [['listen']], 'exp': 'listen to 聽。'},
    {'q': 'I\'m {0} for my cat. Have you seen it? （尋找）', 'blanks': [['looking']], 'exp': 'look for 尋找，進行式 looking。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'There is only ______ milk in the bottle. Let\'s buy some more.', 'opts': ['a few', 'little', 'few', 'many'], 'answer': 1, 'exp': 'milk 不可數，「幾乎沒有」用 little。'},
    {'type': 'mc', 'q': 'Who will look ______ your dog when you are away?', 'opts': ['at', 'for', 'after', 'like'], 'answer': 2, 'exp': 'look after 照顧。'},
    {'type': 'mc', 'q': 'It is ______ to rain this afternoon. Take an umbrella.', 'opts': ['likely', 'like', 'lovely', 'lonely'], 'answer': 0, 'exp': 'be likely to V 可能會…。'},
    {'type': 'mc', 'q': 'The boy ______ to his mom about the broken vase.', 'opts': ['lay', 'laid', 'lain', 'lied'], 'answer': 3, 'exp': '說謊 lie 的過去式 lied。'},
  ]},
]
