# 主題 2000 字 PART 2 Unit 12：Clothing & accessories 衣服和裝飾品（字表依課本 PART 2 印刷頁 151–153，23 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

N = 'n.'
UNIT = {
  'book': 'w2000p2', 'no': 12, 'en': 'Clothing & accessories', 'zh': '衣服和裝飾品',
  'card': 'blouse、pajamas、swimsuit、necklace、slippers、diamond… 共 23 字；a pair of',
  'intro': '衣服、配件和材質，共 23 個。成雙成對的東西（trousers、slippers、sneakers、pajamas）要用 a pair of。',
  'words': [
    W('blouse', N, '女用襯衫', '', 'She wore a white blouse and a blue skirt.', '她穿白色襯衫配藍色裙子。', '👚'),
    W('pajamas', N, '睡衣（褲）', '一定用複數；a pair of pajamas', 'I put on my pajamas and went to bed.', '我換上睡衣去睡覺。', '🛌'),
    W('raincoat', N, '雨衣', 'rain + coat', 'Wear a raincoat when you ride a scooter in the rain.', '下雨騎機車要穿雨衣。', '🧥'),
    W('suit', N, '套裝；西裝', 'swimsuit 泳衣', 'Dad wears a suit and tie to work.', '爸爸穿西裝打領帶去上班。', '🤵'),
    W('swimsuit', N, '泳衣', 'swim + suit', 'Don\'t forget your swimsuit for the beach trip.', '去海邊別忘了帶泳衣。', '🩱'),
    W('trousers', N, '長褲', '= pants；a pair of trousers', 'These trousers are too long for me.', '這條長褲對我來說太長了。', '👖'),
    W('underwear', N, '內衣褲', '不可數', 'Pack enough underwear for the five-day trip.', '五天的旅行要帶夠內衣褲。', '🩲'),
    W('vest', N, '背心', 'life vest 救生衣', 'Everyone on the boat must wear a life vest.', '船上每個人都要穿救生衣。', '🦺'),
    W('contact lens', N, '隱形眼鏡', '複數 contact lenses', 'I wear contact lenses when I play basketball.', '我打籃球時戴隱形眼鏡。', '👁️'),
    W('earrings', N, '耳環', '通常用複數（一對）', 'Mom got a pair of pearl earrings for her birthday.', '媽媽生日收到一對珍珠耳環。', '💎'),
    W('handkerchief', N, '手帕', 'd 不發音', 'Grandpa always carries a handkerchief in his pocket.', '爺爺口袋裡總是帶著手帕。', '🤧'),
    W('necklace', N, '項鍊', 'neck + lace', 'She wears a gold necklace.', '她戴著一條金項鍊。', '📿'),
    W('purse', N, '錢包；（女用）手提包', 'wallet 是男用皮夾', 'Mom took some money out of her purse.', '媽媽從錢包裡拿出一些錢。', '👛'),
    W('scarf', N, '圍巾；絲巾', '複數 scarves', 'Wear a scarf. It\'s cold outside.', '戴條圍巾，外面很冷。', '🧣'),
    W('slippers', N, '拖鞋', 'a pair of slippers', 'Please put on slippers when you come in.', '進來時請換拖鞋。', '🩴'),
    W('sneakers', N, '運動鞋', 'a pair of sneakers', 'I need new sneakers for P.E. class.', '我體育課需要新的運動鞋。', '👟'),
    W('hole', N, '洞', 'a hole in my sock 襪子破洞', 'There is a hole in my sock.', '我的襪子破了一個洞。', '🕳️'),
    W('spot', N, '斑點；汙漬；地點', 'a spot on my shirt 衣服上的汙點', 'There\'s a coffee spot on your shirt.', '你的襯衫上有一塊咖啡漬。', '🔴'),
    W('cotton', N, '棉；棉花', '不可數；cotton candy 棉花糖', 'This T-shirt is made of cotton.', '這件 T 恤是棉做的。', '☁️'),
    W('diamond', N, '鑽石', 'diamond ring 鑽戒', 'Diamonds are very hard and expensive.', '鑽石又硬又貴。', '💍'),
    W('gold', N, '金；黃金', '不可數；golden 金色的', 'The winner got a medal made of gold.', '冠軍拿到一面金做的獎牌。', '🥇'),
    W('silver', 'adj. / n.', '銀色的；銀', 'silver medal 銀牌', 'She won a silver medal in the race.', '她在比賽中得到銀牌。', '🥈'),
    W('iron', 'n. / v.', '鐵；熨斗；燙衣服', 'iron 不可數；熨斗可數', 'Mom irons Dad\'s shirts every Sunday.', '媽媽每個星期天幫爸爸燙襯衫。', '🧺'),
  ],
  'focus': [
    {'title': '一雙、一條：a pair of', 'head': ('東西', '說法', ''),
     'rows': [('長褲', 'a pair of trousers', ''), ('拖鞋', 'a pair of slippers', ''), ('運動鞋', 'a pair of sneakers', ''), ('睡衣', 'a pair of pajamas', ''), ('耳環', 'a pair of earrings', '')],
     'note': '兩件一組的東西用複數，數的時候說 a pair of、two pairs of。'},
    {'title': '金、銀、鐵', 'head': ('名詞', '形容詞', ''),
     'rows': [('gold 金', 'golden 金色的', ''), ('silver 銀', 'silver 銀色的', ''), ('iron 鐵', 'iron 鐵的', '')],
     'note': 'gold、silver、iron 當材料時不可數。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=12, n_ce=6, n_ec=5, n_sp=5, fill=[
  F('I bought a ______ of sneakers yesterday.', ['pair', 'piece', 'slice', 'hole'], 0, 'a pair of sneakers 一雙運動鞋。'),
  F('It\'s raining hard. Take your ______.', ['raincoat', 'swimsuit', 'pajamas', 'necklace'], 0, '下大雨 → raincoat 雨衣。'),
  F('It\'s time for bed. Put on your ______.', ['pajamas', 'suit', 'vest', 'raincoat'], 0, '睡覺穿 pajamas。'),
  F('My sock has a big ______ in it. I can see my toe.', ['hole', 'spot', 'cotton', 'scarf'], 0, '看得到腳趾 → hole 洞。'),
  F('She came in second and won a ______ medal.', ['silver', 'gold', 'iron', 'cotton'], 0, '第二名 → silver medal 銀牌。'),
  F('My shirt is wrinkled. I need to ______ it.', ['iron', 'spread', 'wear', 'spot'], 0, '衣服皺了要 iron 燙。'),
  F('Put on a life ______ before you get on the boat.', ['vest', 'suit', 'scarf', 'blouse'], 0, 'life vest 救生衣。'),
])
