# 主題 2000 字 PART 2 Unit 26：Animals & insects 動物與昆蟲（字表依課本 PART 2 印刷頁 165–167，30 字；中文、例句、題目自編）
# shrimp 已在 Unit 10 食物出現（蝦仁），這裡用動物「蝦子」的意思。
from p2kit import W, F, auto_quiz

N = 'n.'
UNIT = {
  'book': 'w2000p2', 'no': 26, 'en': 'Animals & insects', 'zh': '動物與昆蟲',
  'card': 'deer、dinosaur、kangaroo、koala、ox、wolf、mosquito、dolphin、swallow… 共 30 字；不規則複數',
  'intro': '陸地動物、鳥、昆蟲、海洋動物，還有動物的叫聲和翅膀，共 30 個。注意不規則複數：deer → deer、ox → oxen、wolf → wolves。',
  'words': [
    W('deer', N, '鹿', '單複數同形 deer', 'We saw a group of deer in the mountains.', '我們在山上看到一群鹿。', '🦌'),
    W('dinosaur', N, '恐龍', '', 'Dinosaurs lived millions of years ago.', '恐龍生活在幾百萬年前。', '🦕'),
    W('donkey', N, '驢子', '複數 donkeys', 'The donkey carried heavy bags up the hill.', '驢子把重重的袋子揹上山坡。', '🫏'),
    W('eagle', N, '老鷹', 'an eagle', 'The eagle flew high above the mountain.', '老鷹在山上高高飛翔。', '🦅'),
    W('hippo', N, '河馬', '= hippopotamus', 'The hippo spends most of the day in the water.', '河馬一天大部分時間都待在水裡。', '🦛'),
    W('kangaroo', N, '袋鼠', '', 'A baby kangaroo lives in its mother\'s pouch.', '小袋鼠住在媽媽的育兒袋裡。', '🦘'),
    W('kitten', N, '小貓', 'cat → kitten；dog → puppy', 'The kitten is playing with a ball of yarn.', '小貓在玩毛線球。', '🐱'),
    W('koala', N, '無尾熊', '', 'Koalas sleep about 20 hours a day.', '無尾熊一天睡大約二十個小時。', '🐨'),
    W('lamb', N, '小羊；羊肉', 'b 不發音', 'The little lamb followed its mother.', '小羊跟著媽媽走。', '🐑'),
    W('monster', N, '怪物；妖怪', '', 'The kids dressed up as monsters for Halloween.', '孩子們萬聖節打扮成怪物。', '👹'),
    W('ox', N, '公牛；牛', '複數 oxen', 'Long ago, farmers used oxen to work in the fields.', '很久以前，農夫用牛在田裡工作。', '🐂'),
    W('panda', N, '貓熊', '', 'Pandas love to eat bamboo.', '貓熊愛吃竹子。', '🐼'),
    W('parrot', N, '鸚鵡', '', 'Our parrot can say "Hello!"', '我們家的鸚鵡會說「哈囉！」。', '🦜'),
    W('pigeon', N, '鴿子', 'dove 白鴿（象徵和平）', 'Many pigeons are looking for food in the square.', '很多鴿子在廣場上找食物。', '🕊️'),
    W('swan', N, '天鵝', 'The Ugly Duckling 醜小鴨長大變天鵝', 'The swan swam gracefully on the lake.', '天鵝在湖上優雅地游著。', '🦢'),
    W('turkey', N, '火雞；（大寫）土耳其', 'Turkey 土耳其', 'Americans eat turkey on Thanksgiving.', '美國人感恩節吃火雞。', '🦃'),
    W('wolf', N, '狼', '複數 wolves', 'Wolves hunt in groups.', '狼成群打獵。', '🐺'),
    W('cockroach', N, '蟑螂', '複數 cockroaches；口語 roach', 'There\'s a cockroach in the kitchen!', '廚房裡有一隻蟑螂！', '🪳'),
    W('dragon', N, '龍', 'Dragon Boat Festival 端午節', 'In Chinese stories, dragons bring rain.', '在中國故事裡，龍會帶來雨。', '🐲'),
    W('mosquito', N, '蚊子', '複數 mosquitoes／mosquitos', 'A mosquito bit me on the arm.', '一隻蚊子叮了我的手臂。', '🦟'),
    W('snail', N, '蝸牛', 'at a snail\'s pace 非常慢', 'The snail moves very slowly.', '蝸牛爬得很慢。', '🐌'),
    W('worm', N, '蟲；蠕蟲', 'The early bird catches the worm. 早起的鳥兒有蟲吃', 'The bird caught a worm.', '那隻鳥抓到一隻蟲。', '🪱'),
    W('crab', N, '螃蟹', '', 'We saw many small crabs on the beach.', '我們在海灘上看到很多小螃蟹。', '🦀'),
    W('dolphin', N, '海豚', '', 'Dolphins are friendly and smart.', '海豚友善又聰明。', '🐬'),
    W('shark', N, '鯊魚', '', 'Sharks have many sharp teeth.', '鯊魚有很多尖牙。', '🦈'),
    W('shrimp', N, '蝦子', '複數 shrimp／shrimps', 'A shrimp has ten legs.', '蝦子有十隻腳。', '🦐'),
    W('whale', N, '鯨魚', 'killer whale 虎鯨', 'The whale is the largest animal in the world.', '鯨魚是世界上最大的動物。', '🐋'),
    W('bark', 'v. / n.', '（狗）吠叫；樹皮', 'Barking dogs seldom bite. 會叫的狗不咬人', 'The dog barks at every stranger.', '那隻狗對每個陌生人吠叫。', '🐕'),
    W('swallow', 'n. / v.', '燕子；吞下', 'swallow the pill 把藥吞下', 'Swallows build nests under the roof.', '燕子在屋簷下築巢。', '🐦'),
    W('wing', N, '翅膀', '', 'The bird hurt its wing and couldn\'t fly.', '那隻鳥傷了翅膀，飛不起來。', '🪽'),
  ],
  'focus': [
    {'title': '不規則複數', 'head': ('單數', '複數', ''),
     'rows': [('deer', 'deer', ''), ('ox', 'oxen', ''), ('wolf', 'wolves', ''), ('shrimp', 'shrimp／shrimps', ''), ('mosquito', 'mosquitoes', '')],
     'note': '動物寶寶：cat → kitten、sheep → lamb、dog → puppy。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=26, n_ce=7, n_ec=6, n_sp=6, fill=[
  F('I saw five ______ in the forest.', ['deer', 'deers', 'deeres', 'dear'], 0, 'deer 單複數同形。'),
  F('The farmer has two ______.', ['oxen', 'oxes', 'ox', 'oxs'], 0, 'ox 的複數是 oxen。'),
  F('A pack of ______ was howling at the moon.', ['wolves', 'wolfs', 'wolf', 'wolfes'], 0, 'wolf → wolves。'),
  F('A baby cat is called a ______.', ['kitten', 'lamb', 'puppy', 'swan'], 0, '小貓 → kitten。'),
  F('The dog next door ______ all night. I couldn\'t sleep.', ['barked', 'swallowed', 'winged', 'flew'], 0, '狗叫 → bark。'),
  F('This bird can talk like a person. It\'s a ______.', ['parrot', 'pigeon', 'swan', 'eagle'], 0, '會說話的鳥 → parrot 鸚鵡。'),
  F('______ lived on Earth long before people did.', ['Dinosaurs', 'Kittens', 'Koalas', 'Pigeons'], 0, '很久以前 → dinosaurs 恐龍。'),
  F('Chew your food well before you ______ it.', ['swallow', 'bark', 'wing', 'crab'], 0, '吞下 → swallow。'),
])
