# WORD UP 複習區 Unit 21（WORD UP「G-I」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 21, 'en': 'G-I', 'zh': 'G 開頭（一）',
  'intro': 'WORD UP「G-I」的 34 個字（gain 到 gold）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('gain', 'v./n.', '獲得；增加', 'gain weight 變胖', 'He gained a lot of experience from the job.', '他從工作中得到很多經驗。', '📈'),
    W('game', 'n.', '遊戲；比賽', '', 'Let\'s play a game.', '我們來玩個遊戲吧。', '🎮'),
    W('garage', 'n.', '車庫', '', 'Dad parks the car in the garage.', '爸爸把車停在車庫。', '🚗'),
    W('garbage', 'n.', '垃圾', '不可數；take out the garbage 倒垃圾', 'It\'s my job to take out the garbage.', '倒垃圾是我的工作。', '🗑️'),
    W('garden', 'n.', '花園', '', 'Grandma grows roses in her garden.', '奶奶在花園種玫瑰。', '🌻'),
    W('gas', 'n.', '氣體；瓦斯；汽油', 'gas station 加油站', 'We stopped at a gas station.', '我們在加油站停下來。', '⛽'),
    W('gasoline', 'n.', '汽油', '= gas', 'The price of gasoline went up.', '油價漲了。', '🛢️'),
    W('gate', 'n.', '大門；登機門', '', 'Meet me at the school gate.', '在校門口跟我碰面。', '🚪'),
    W('gather', 'v.', '聚集；收集', '', 'The family gathered for dinner.', '全家人聚在一起吃晚餐。', '👪'),
    W('general', 'adj./n.', '一般的；將軍', 'in general 一般來說', 'In general, I go to bed at ten.', '一般來說，我十點睡覺。', '🎖️'),
    W('generation', 'n.', '世代；一代', '', 'Three generations live in this house.', '這棟房子住了三代人。', '👴'),
    W('generous', 'adj.', '慷慨的；大方的', '', 'It\'s very generous of you to help.', '你真慷慨，願意幫忙。', '🎁'),
    W('genius', 'n.', '天才', '', 'Einstein was a genius.', '愛因斯坦是天才。', '🧠'),
    W('gentle', 'adj.', '溫柔的；輕柔的', 'gently 輕輕地', 'Be gentle with the baby.', '對寶寶要溫柔。', '🤲'),
    W('gentleman', 'n.', '紳士；先生', '複數 gentlemen；Ladies and gentlemen 各位先生女士', 'Ladies and gentlemen, welcome!', '各位先生女士，歡迎！', '🎩'),
    W('geography', 'n.', '地理', '', 'We learn about maps in geography class.', '我們在地理課學地圖。', '🗺️'),
    W('German', 'adj./n.', '德國的；德國人；德文', '', 'My friend is learning German.', '我朋友在學德文。', '🥨'),
    W('Germany', 'n.', '德國', '', 'Berlin is the capital of Germany.', '柏林是德國的首都。', '🇩🇪'),
    W('gesture', 'n.', '手勢；姿態', '', 'He made a friendly gesture.', '他做了一個友善的手勢。', '👋'),
    W('get', 'v.', '得到；變得；到達', '三態 get-got-got／gotten', 'It\'s getting dark.', '天色漸漸變暗。', '🎯'),
    W('ghost', 'n.', '鬼', 'h 不發音', 'Do you believe in ghosts?', '你相信有鬼嗎？', '👻'),
    W('giant', 'n./adj.', '巨人；巨大的', '', 'There is a giant panda at the zoo.', '動物園裡有一隻大貓熊。', '🐼'),
    W('gift', 'n.', '禮物；天賦', '= present', 'This gift is for you.', '這份禮物是給你的。', '🎁'),
    W('girl', 'n.', '女孩', '', 'The girl in red is my sister.', '穿紅衣服的女孩是我妹妹。', '👧'),
    W('give', 'v.', '給', '三態 give-gave-given；give up 放棄', 'Never give up!', '永不放棄！', '🤲'),
    W('glad', 'adj.', '高興的', 'be glad to V', 'I\'m glad to see you.', '很高興見到你。', '😄'),
    W('glass', 'n.', '玻璃；玻璃杯', 'glasses 眼鏡', 'Can I have a glass of water?', '可以給我一杯水嗎？', '🥛'),
    W('glove', 'n.', '手套', '通常用複數 gloves', 'Wear your gloves. It\'s cold.', '戴上手套，天氣很冷。', '🧤'),
    W('glue', 'n./v.', '膠水；黏', '', 'Use glue to stick the paper on the card.', '用膠水把紙黏在卡片上。', '🧴'),
    W('go', 'v.', '去', '三態 go-went-gone', 'Let\'s go to the movies.', '我們去看電影吧。', '🚶'),
    W('goal', 'n.', '目標；（球賽）得分', '', 'My goal is to pass the GEPT.', '我的目標是通過全民英檢。', '🥅'),
    W('goat', 'n.', '山羊', 'sheep 綿羊', 'The goat is eating grass.', '山羊在吃草。', '🐐'),
    W('God', 'n.', '上帝；神', 'Oh my God! 天啊', 'Oh my God! I forgot my homework!', '天啊！我忘了帶作業！', '🙏'),
    W('gold', 'n./adj.', '金子；金的', 'golden 金色的', 'She won a gold medal.', '她贏得一面金牌。', '🥇'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('give up / give up + V-ing', '放棄', 'Don\'t give up studying.'),
      ('in general', '一般來說', 'In general, kids like candy.'),
      ('get + 形容詞', '變得…', 'get tired ／ get angry'),
      ('be glad to V', '很高興做…', 'I\'m glad to help.'),
      ('take out the garbage', '倒垃圾', 'take out the garbage every night'),
      ('glass / glasses', '玻璃杯 ／ 眼鏡', 'a glass of milk ／ wear glasses'),
      ('German / Germany', '德國的、德文 ／ 德國', 'speak German ／ live in Germany'),
    ], 'note': 'go 的過去式 went、過去分詞 gone；give 的過去式 gave、過去分詞 given。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '慷慨的', 'opts': ['gentle', 'generous', 'general', 'genius'], 'answer': 1, 'exp': 'generous 慷慨的。'},
    {'type': 'mc', 'q': '垃圾', 'opts': ['garbage', 'garage', 'garden', 'gasoline'], 'answer': 0, 'exp': 'garbage 垃圾。'},
    {'type': 'mc', 'q': '手勢', 'opts': ['gather', 'gate', 'gesture', 'goal'], 'answer': 2, 'exp': 'gesture 手勢。'},
    {'type': 'mc', 'q': '世代', 'opts': ['geography', 'gentleman', 'general', 'generation'], 'answer': 3, 'exp': 'generation 世代。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '地理（g＿＿＿＿＿＿＿＿，9 個字母）：{0}', 'blanks': [['geography']], 'exp': 'geography。'},
    {'q': '鬼（g＿＿＿＿，5 個字母）：{0}', 'blanks': [['ghost']], 'exp': 'ghost（h 不發音）。'},
    {'q': '手套（g＿＿＿＿，5 個字母）：{0}', 'blanks': [['glove']], 'exp': 'glove。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Don\'t {0} up. You can do it! （放棄）', 'blanks': [['give']], 'exp': 'give up 放棄。'},
    {'q': 'We {0} to the zoo last Saturday. （去，過去式）', 'blanks': [['went']], 'exp': 'go 的過去式 went。'},
    {'q': 'The students {0} in the hall for the meeting. （聚集，現在式）', 'blanks': [['gather']], 'exp': '主詞複數，gather 不加 s。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'It is ______ cold in the morning. Put on your coat.', 'opts': ['get', 'getting', 'got', 'gets'], 'answer': 1, 'exp': '現在進行式 is getting cold 漸漸變冷。'},
    {'type': 'mc', 'q': 'My grandma wears ______ when she reads.', 'opts': ['glass', 'a glass', 'glasses', 'glassy'], 'answer': 2, 'exp': '眼鏡 glasses。'},
    {'type': 'mc', 'q': 'I\'m ______ to hear that you passed the test.', 'opts': ['glad', 'gentle', 'giant', 'general'], 'answer': 0, 'exp': 'be glad to V 很高興…。'},
    {'type': 'mc', 'q': 'He gave ______ smoking last year.', 'opts': ['in', 'out', 'off', 'up'], 'answer': 3, 'exp': 'give up + V-ing 放棄、戒掉。'},
  ]},
]
