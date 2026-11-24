# WORD UP 複習區 Unit 15（WORD UP「D-III」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 15, 'en': 'D-III', 'zh': 'D 開頭（三）',
  'intro': 'WORD UP「D-III」的 37 個字（dog 到 duty）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('dog', 'n.', '狗', '', 'Our dog barks at strangers.', '我們的狗會對陌生人叫。', '🐕'),
    W('doll', 'n.', '洋娃娃', '', 'My sister has a lot of dolls.', '我妹妹有很多洋娃娃。', '🪆'),
    W('dollar', 'n.', '元（貨幣）', 'NT$ 新台幣', 'The ticket costs 100 dollars.', '這張票 100 元。', '💵'),
    W('dolphin', 'n.', '海豚', '', 'Dolphins are very smart animals.', '海豚是很聰明的動物。', '🐬'),
    W('donkey', 'n.', '驢子', '', 'The donkey carried the heavy bags.', '驢子背著重重的袋子。', '🫏'),
    W('door', 'n.', '門', 'next door 隔壁', 'Someone is knocking on the door.', '有人在敲門。', '🚪'),
    W('dot', 'n.', '點；圓點', '', 'Connect the dots to draw a star.', '把點連起來畫出星星。', '⚫'),
    W('double', 'adj./v.', '雙倍的；加倍', 'double room 雙人房', 'The price has doubled.', '價格變成兩倍了。', '✖️'),
    W('Double Tenth Day', 'n.', '雙十節（國慶日）', '10 月 10 日', 'There are fireworks on Double Tenth Day.', '國慶日有煙火。', '🎆'),
    W('doubt', 'n./v.', '懷疑', 'b 不發音；no doubt 無疑地', 'I doubt that he will come.', '我懷疑他會不會來。', '🤨'),
    W('doughnut', 'n.', '甜甜圈', '= donut', 'I had a chocolate doughnut.', '我吃了一個巧克力甜甜圈。', '🍩'),
    W('down', 'adv./prep.', '向下', 'sit down 坐下', 'Please sit down.', '請坐下。', '⬇️'),
    W('downstairs', 'adv.', '在樓下；到樓下', 'upstairs 樓上', 'Mom is downstairs in the kitchen.', '媽媽在樓下廚房。', '🔽'),
    W('downtown', 'adv./n.', '在市中心；市區', '', 'Let\'s go shopping downtown.', '我們去市中心逛街吧。', '🌆'),
    W('dozen', 'n.', '一打（12 個）', 'a dozen eggs（不加 of）', 'Mom bought a dozen eggs.', '媽媽買了一打雞蛋。', '🥚'),
    W('Dr.', 'n.', '醫生；博士（稱呼）', 'Doctor 的縮寫', 'Dr. Lin is a kind doctor.', '林醫師是一位親切的醫生。', '👨‍⚕️'),
    W('dragon', 'n.', '龍', '', 'The dragon is a symbol of power in Chinese culture.', '在中華文化裡，龍是力量的象徵。', '🐉'),
    W('Dragon-Boat Festival', 'n.', '端午節', '農曆五月五日', 'We eat rice dumplings during the Dragon-Boat Festival.', '端午節我們吃粽子。', '🛶'),
    W('drama', 'n.', '戲劇；連續劇', '', 'My mom loves Korean dramas.', '我媽媽很愛看韓劇。', '🎭'),
    W('draw', 'v.', '畫（線條）；拉', '三態 draw-drew-drawn', 'Can you draw a cat?', '你會畫貓嗎？', '✏️'),
    W('drawer', 'n.', '抽屜', '', 'The scissors are in the top drawer.', '剪刀在最上面的抽屜。', '🗃️'),
    W('dream', 'n./v.', '夢；做夢；夢想', 'dream of／about', 'My dream is to be a pilot.', '我的夢想是當飛行員。', '💭'),
    W('dress', 'n./v.', '洋裝；穿衣服', 'get dressed 穿好衣服', 'She is wearing a red dress.', '她穿著紅色洋裝。', '👗'),
    W('dresser', 'n.', '梳妝台；五斗櫃', '', 'There is a mirror on the dresser.', '梳妝台上有一面鏡子。', '🪞'),
    W('drink', 'v./n.', '喝；飲料', '三態 drink-drank-drunk', 'Drink more water every day.', '每天多喝水。', '🥤'),
    W('drive', 'v.', '開車', '三態 drive-drove-driven', 'My dad drives me to school.', '爸爸開車載我上學。', '🚗'),
    W('driver', 'n.', '駕駛；司機', '', 'The bus driver is very careful.', '公車司機很小心。', '🚌'),
    W('drop', 'v./n.', '掉落；一滴', '過去式 dropped', 'I dropped my phone on the floor.', '我把手機掉在地上。', '💧'),
    W('drug', 'n.', '藥；毒品', '', 'Say no to drugs.', '對毒品說不。', '💊'),
    W('drugstore', 'n.', '藥局', '', 'You can buy medicine at the drugstore.', '你可以在藥局買藥。', '🏪'),
    W('drum', 'n.', '鼓', 'play the drums', 'He plays the drums in the band.', '他在樂團打鼓。', '🥁'),
    W('dry', 'adj./v.', '乾的；把…弄乾', '過去式 dried', 'Dry your hair before you go to bed.', '睡前把頭髮吹乾。', '🏜️'),
    W('dryer', 'n.', '烘乾機；吹風機', 'hair dryer 吹風機', 'Put the clothes in the dryer.', '把衣服放進烘乾機。', '🌀'),
    W('duck', 'n.', '鴨子', '', 'The ducks are swimming in the pond.', '鴨子在池塘裡游泳。', '🦆'),
    W('dumb', 'adj.', '笨的；啞的', 'b 不發音', 'Sorry, that was a dumb question.', '抱歉，那是個笨問題。', '🙊'),
    W('dumpling', 'n.', '餃子', 'rice dumpling 粽子', 'Grandma makes the best dumplings.', '奶奶包的餃子最好吃。', '🥟'),
    W('duty', 'n.', '責任；職責', 'on duty 值班', 'It is our duty to protect the earth.', '保護地球是我們的責任。', '🛡️'),
  ],
  'focus': [
    {'title': '容易搞混的字', 'head': ('字', '用法', '例子'), 'rows': [
      ('draw / drawer', '畫 ／ 抽屜', 'draw a map ／ open the drawer'),
      ('dress / dresser', '洋裝、穿衣 ／ 梳妝台', 'a long dress ／ a wooden dresser'),
      ('drug / drugstore', '藥、毒品 ／ 藥局', 'take drugs ／ go to the drugstore'),
      ('dry / dryer', '乾的、弄乾 ／ 烘乾機、吹風機', 'dry the dishes ／ a hair dryer'),
      ('downstairs / downtown', '樓下 ／ 市中心', 'go downstairs ／ work downtown'),
    ], 'note': 'dozen 前面有數字時不加 s、不加 of：two dozen eggs。'},
    {'title': '不規則動詞三態', 'head': ('原形', '過去式', '過去分詞'), 'rows': [
      ('draw', 'drew', 'drawn'),
      ('drink', 'drank', 'drunk'),
      ('drive', 'drove', 'driven'),
      ('dream', 'dreamed／dreamt', 'dreamed／dreamt'),
      ('drop', 'dropped', 'dropped'),
      ('dry', 'dried', 'dried'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '抽屜', 'opts': ['dresser', 'drawer', 'dryer', 'driver'], 'answer': 1, 'exp': 'drawer 抽屜。'},
    {'type': 'mc', 'q': '藥局', 'opts': ['drugstore', 'downtown', 'drum', 'drama'], 'answer': 0, 'exp': 'drugstore 藥局。'},
    {'type': 'mc', 'q': '懷疑', 'opts': ['double', 'dozen', 'doubt', 'dot'], 'answer': 2, 'exp': 'doubt 懷疑（b 不發音）。'},
    {'type': 'mc', 'q': '責任', 'opts': ['dumb', 'dream', 'drop', 'duty'], 'answer': 3, 'exp': 'duty 責任。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '海豚（d＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['dolphin']], 'exp': 'dolphin。'},
    {'q': '餃子（d＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['dumpling']], 'exp': 'dumpling。'},
    {'q': '樓下（d＿＿＿＿＿＿＿＿＿，10 個字母）：{0}', 'blanks': [['downstairs']], 'exp': 'downstairs。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Dad {0} us to the beach last Sunday. （開車，過去式）', 'blanks': [['drove']], 'exp': 'drive 的過去式 drove。'},
    {'q': 'Be careful! Don\'t {0} the glass. （掉落）', 'blanks': [['drop']], 'exp': 'Don\'t + 原形：drop。'},
    {'q': 'I need a {0} eggs to make the cake. （一打）', 'blanks': [['dozen']], 'exp': 'a dozen eggs 一打雞蛋。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Mom bought two ______ apples.', 'opts': ['dozen', 'dozens', 'dozen of', 'dozens of'], 'answer': 0, 'exp': '數字 + dozen，不加 s 也不加 of。'},
    {'type': 'mc', 'q': 'Last night I ______ about flying in the sky.', 'opts': ['dream', 'dreamed', 'dreaming', 'dreams'], 'answer': 1, 'exp': 'last night 用過去式 dreamed。'},
    {'type': 'mc', 'q': 'My brother plays ______ drums very well.', 'opts': ['a', '（不填）', 'the', 'an'], 'answer': 2, 'exp': 'play the + 樂器。'},
    {'type': 'mc', 'q': 'Our class leader is ______ duty today.', 'opts': ['in', 'at', 'for', 'on'], 'answer': 3, 'exp': 'on duty 值班。'},
  ]},
]
