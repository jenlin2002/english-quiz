# LaLa Word Unit 1：一字多義（字表與每個字的意思依課本單元；例句、中文、題目為本站自編，不照抄課本）
# 課本：115[翰林]國中英語 LaLa Word 小單字大視野，學用 PDF 印刷頁第 7–19 頁（PDF 頁序＝印刷頁碼－1）
# S(詞性, 中文, 例句, 例句中文, 片語)：片語可省略，例如 'out of the blue 出乎意料'

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 1, 'en': 'Colors Can Talk!', 'zh': '一字多義（一）',
  'intro': '同一個英文字，在不同句子裡可能有完全不同的意思：blue 是「藍色的」，也可以是「憂鬱的」；pen 是「筆」，也可以是「動物的圍欄」。'
           '先記住最常見的意思，再看例句學其他意思。前 7 個是主題單字，後 23 個是更多單字。',
  'words': [
    W('color', '🎨', [
        S('n.', '顏色', 'What color is your new bike?', '你的新腳踏車是什麼顏色？'),
        S('n.', '膚色', 'We should never judge people by their color.', '我們絕不該以膚色評斷別人。'),
        S('v.', '上色；染色', 'The kids colored the pictures with crayons.', '孩子們用蠟筆幫圖畫上色。'),
    ], 'color - colored - colored - coloring', key=True),
    W('blue', '💙', [
        S('n.', '藍色', 'The sea changes from light blue to dark blue.', '海從淺藍色變成深藍色。', 'dark / light blue 深藍／淺藍'),
        S('adj.', '藍色的', 'Tom is wearing a blue cap today.', 'Tom 今天戴一頂藍色的帽子。'),
        S('adj.', '憂鬱的；難過的', 'I feel a little blue on rainy Mondays.', '下雨的星期一我覺得有點憂鬱。'),
        S('片語', '出乎意料地', 'My old friend called me out of the blue.', '我的老朋友突然打電話給我。', 'out of the blue 出乎意料、突然'),
    ], 'blue - bluer - bluest', key=True),
    W('green', '🥦', [
        S('adj.', '綠色的', 'The leaves turn green in spring.', '春天葉子變綠了。'),
        S('n.', '草地；（複數）蔬菜', 'Eat your greens, and you will grow strong.', '把青菜吃完，你就會長得強壯。'),
        S('adj.', '沒經驗的；生手的', 'He is still green at his new job.', '他對新工作還很生疏。'),
        S('adj.', '環保的', 'Our school is trying to go green.', '我們學校正努力推動環保。', 'go green 做環保'),
    ], 'green - greener - greenest', key=True),
    W('room', '🛏️', [
        S('n.', '房間', 'My room is next to the kitchen.', '我的房間在廚房旁邊。'),
        S('n.', '空間（不可數）', 'Is there room for one more person in the car?', '車上還有空間再坐一個人嗎？', 'make room for 騰出空間給'),
    ], key=True),
    W('pen', '🖊️', [
        S('n.', '筆', 'May I borrow your pen?', '我可以借你的筆嗎？'),
        S('n.', '（動物的）圍欄；圈', 'The pigs are sleeping in the pen.', '豬在圍欄裡睡覺。'),
        S('v.', '寫（＝write）', 'The poet penned this poem at the age of ten.', '這位詩人十歲時寫了這首詩。'),
    ], 'pen - penned - penned - penning', key=True),
    W('notebook', '📓', [
        S('n.', '筆記本', 'Write the new words in your notebook.', '把新單字寫在你的筆記本裡。'),
        S('n.', '筆記型電腦（＝laptop）', 'My sister uses a notebook to do her homework.', '我姊姊用筆電寫作業。'),
    ], key=True),
    W('down', '⬇️', [
        S('adv.', '向下；降低', 'Please sit down and open your books.', '請坐下，把書打開。', 'sit / lie / write down 坐下／躺下／寫下'),
        S('prep.', '沿著…往下', 'The ball rolled down the hill.', '球沿著山坡滾下去。'),
        S('adj.', '情緒低落的', 'Ben looks down because he lost the game.', 'Ben 輸了比賽，看起來很沮喪。'),
        S('adv.', '（音量）調低', 'Could you turn the TV down?', '你可以把電視轉小聲嗎？', 'turn down 調低；拒絕'),
        S('n.', '羽絨', 'This down jacket keeps me warm.', '這件羽絨外套讓我很溫暖。'),
    ], key=True),
    W('ball', '⚽', [
        S('n.', '球', 'The dog ran after the ball.', '狗追著球跑。'),
        S('n.', '舞會', 'Cinderella went to the ball in a beautiful dress.', '灰姑娘穿著漂亮的禮服去參加舞會。'),
    ]),
    W('baby', '👶', [
        S('n.', '嬰兒', 'The baby is sleeping. Please be quiet.', '寶寶在睡覺，請安靜。'),
        S('adj.', '幼小的（＋動物）', 'Look at the baby ducks!', '看那些小鴨子！', 'baby + 動物 小…'),
    ], 'baby - babies'),
    W('cook', '🍳', [
        S('v.', '煮；做菜', 'Dad cooks dinner for us on weekends.', '爸爸週末煮晚餐給我們吃。', 'cook + 人 + 食物 ＝ cook + 食物 + for + 人'),
        S('n.', '廚師（cooker 是爐具）', 'My uncle is a cook at a hotel.', '我叔叔在飯店當廚師。'),
    ]),
    W('drink', '🥤', [
        S('v.', '喝；喝酒', 'Drink more water on hot days.', '天氣熱要多喝水。'),
        S('n.', '飲料', 'Would you like a cold drink?', '你要不要來杯冷飲？'),
    ], 'drink - drank - drunk - drinking'),
    W('family', '👨‍👩‍👧', [
        S('n.', '家庭', 'There are four families in this building.', '這棟大樓住了四戶人家。'),
        S('n.', '家人們（當複數）', 'My family are all early birds.', '我的家人都是早起的人。'),
    ], 'family - families'),
    W('fat', '🥓', [
        S('adj.', '胖的', 'Our cat got fat after eating too much.', '我們的貓吃太多變胖了。'),
        S('adj.', '厚的；豐厚的', 'He is reading a fat book about history.', '他在看一本很厚的歷史書。'),
        S('n.', '脂肪；油脂', 'Fried food has a lot of fat.', '油炸食物有很多脂肪。'),
        S('片語', '不可能', 'Me, win the lottery? Fat chance!', '我中樂透？不可能啦！', 'fat chance 不可能'),
    ], 'fat - fatter - fattest'),
    W('fine', '👌', [
        S('adj.', '好的；健康的', 'A: How are you? B: I\'m fine, thank you.', 'A：你好嗎？ B：我很好，謝謝。'),
        S('adj.', '細的；細微的', 'The beach is covered with fine white sand.', '海灘上滿是細細的白沙。'),
        S('n.', '罰款', 'He had to pay a fine for parking there.', '他在那裡停車被罰了錢。'),
        S('v.', '處以罰款', 'The driver was fined for speeding.', '那位駕駛因超速被罰款。'),
    ], 'fine - fined - fined - fining'),
    W('fish', '🐟', [
        S('n.', '魚', 'There are many fish in the pond.', '池塘裡有很多魚。', '數量多還是 fish；種類多才用 fishes'),
        S('n.', '魚肉（不可數）', 'We had fish and rice for lunch.', '我們午餐吃魚和飯。'),
        S('v.', '釣魚；捕魚', 'Grandpa likes to go fishing by the river.', '爺爺喜歡去河邊釣魚。', 'go fishing 去釣魚'),
        S('v.', '摸索翻找', 'Mom fished in her bag for her phone.', '媽媽在包包裡翻找手機。'),
    ], 'fish - fished - fished - fishing'),
    W('gift', '🎁', [
        S('n.', '禮物（＝present）', 'Thank you for the birthday gift!', '謝謝你的生日禮物！'),
        S('n.', '天分；才能', 'Amy has a gift for music.', 'Amy 有音樂天分。', 'have a gift for 有…的天分'),
    ]),
    W('hungry', '😋', [
        S('adj.', '飢餓的', 'I\'m so hungry. Let\'s eat now.', '我好餓，我們現在吃飯吧。'),
        S('adj.', '渴望的', 'The young player is hungry for a win.', '這位年輕選手渴望贏球。', 'be hungry for 渴望'),
    ], 'hungry - hungrier - hungriest'),
    W('look', '👀', [
        S('v.', '看', 'Look at the board, please.', '請看黑板。', 'look at 看著'),
        S('v.', '看起來', 'You look happy today.', '你今天看起來很開心。'),
        S('v.', '尋找；查閱', 'I\'m looking for my glasses.', '我在找我的眼鏡。', 'look for 尋找；look up 查（字典）'),
        S('v.', '照顧', 'Can you look after my dog this weekend?', '這週末你可以幫我照顧狗嗎？', 'look after 照顧'),
        S('n.', '看一眼；（複數）長相', 'Let me take a look at your homework.', '讓我看一下你的作業。', 'take a look 看一下'),
    ], 'look - looked - looked - looking'),
    W('marker', '🖍️', [
        S('n.', '麥克筆；白板筆', 'The teacher wrote the answer with a red marker.', '老師用紅色白板筆寫下答案。'),
        S('n.', '標記；記號', 'Follow the markers, and you won\'t get lost.', '跟著路標走，你就不會迷路。'),
    ]),
    W('meet', '🤝', [
        S('v.', '遇見；見面', 'Let\'s meet at the bus stop at nine.', '我們九點在公車站見面吧。'),
        S('v.', '認識', 'Nice to meet you.', '很高興認識你。'),
        S('v.', '開會', 'The class leaders meet every Friday.', '班長們每週五開會。'),
        S('v.', '達到；滿足（期限、要求）', 'We worked hard to meet the deadline.', '我們努力工作以趕上截止日期。'),
        S('n.', '比賽；運動會', 'Our school has a swim meet next week.', '我們學校下週有游泳比賽。', 'track / swim meet 田徑／游泳比賽'),
    ], 'meet - met - met - meeting'),
    W('name', '📛', [
        S('n.', '名字', 'What\'s your first name?', '你的名字（不含姓）是什麼？', 'first name 名；last name 姓'),
        S('v.', '命名；取名', 'They named their dog Lucky.', '他們把狗取名叫 Lucky。', 'be named after 以…命名'),
        S('v.', '說出；指定', 'Can you name three animals that live in the sea?', '你能說出三種住在海裡的動物嗎？'),
    ], 'name - named - named - naming'),
    W('open', '🔓', [
        S('v.', '打開', 'Please open the window. It\'s hot.', '請打開窗戶，好熱。'),
        S('v.', '開始；開幕', 'The new park will open next month.', '新公園下個月開幕。'),
        S('adj.', '開著的', 'Don\'t leave the door open.', '別讓門開著。'),
        S('adj.', '營業中的', 'Is the bookstore open on Sundays?', '書店星期天有開嗎？'),
    ], 'open - opened - opened - opening'),
    W('rain', '🌧️', [
        S('n.', '雨（不可數）', 'We had a lot of rain last week.', '上週下了很多雨。'),
        S('v.', '下雨', 'It\'s raining hard outside.', '外面雨下得很大。', 'rain hard / heavily 下大雨'),
        S('片語', '無論如何；風雨無阻', 'The game will go on, rain or shine.', '比賽風雨無阻照常舉行。', 'rain or shine 風雨無阻'),
    ], 'rain - rained - rained - raining'),
    W('ride', '🚲', [
        S('v.', '騎；搭乘', 'I ride my bike to school every day.', '我每天騎腳踏車上學。'),
        S('n.', '搭車；車程', 'Can you give me a ride to the station?', '你可以載我去車站嗎？', 'give + 人 + a ride 載某人'),
        S('n.', '（遊樂園的）遊樂設施', 'The roller coaster is the best ride in the park.', '雲霄飛車是樂園裡最好玩的設施。'),
    ], 'ride - rode - ridden - riding'),
    W('ruler', '📏', [
        S('n.', '尺', 'Use a ruler to draw a straight line.', '用尺畫一條直線。'),
        S('n.', '統治者', 'The king was a kind ruler.', '那位國王是一位仁慈的統治者。'),
    ]),
    W('run', '🏃', [
        S('v.', '跑', 'Don\'t run in the hallway.', '不要在走廊上奔跑。'),
        S('n.', '跑步', 'Let\'s go for a run after school.', '放學後我們去跑步吧。', 'go for a run 去跑步'),
        S('v.', '經營；運作', 'Her parents run a noodle shop.', '她爸媽開了一間麵店。'),
        S('片語', '用完', 'We have run out of milk.', '我們的牛奶喝完了。', 'run out of 用完'),
    ], 'run - ran - run - running'),
    W('school', '🏫', [
        S('n.', '學校', 'Our school has a big library.', '我們學校有一間很大的圖書館。'),
        S('n.', '上學；上課時間（不可數）', 'Let\'s play basketball after school.', '我們放學後去打籃球吧。', 'after school 放學後；go to school 上學'),
        S('n.', '（魚、海豚的）群', 'A school of fish swam past our boat.', '一群魚游過我們的船。', 'a school of fish 一群魚'),
    ]),
    W('short', '🩳', [
        S('adj.', '短的；矮的', 'My little brother is too short to reach the shelf.', '我弟弟太矮，搆不到架子。'),
        S('adj.', '（時間）短暫的', 'Let\'s take a short break.', '我們休息一下吧。', 'in short 簡單來說'),
        S('adj.', '不足的；缺少的', 'We are short of time. Hurry up!', '我們時間不夠了，快一點！', 'be short of 缺少'),
        S('n.', '短褲（用複數 shorts）', 'He wears shorts and a T-shirt in summer.', '他夏天穿短褲和 T 恤。'),
    ], 'short - shorter - shortest'),
    W('thin', '🥢', [
        S('adj.', '瘦的（↔ fat）', 'The model is tall and thin.', '那位模特兒又高又瘦。'),
        S('adj.', '薄的；細的（↔ thick）', 'I cut the bread into thin slices.', '我把麵包切成薄片。'),
        S('adj.', '稀薄的；稀疏的', 'The air is thin on high mountains.', '高山上的空氣很稀薄。'),
    ], 'thin - thinner - thinnest'),
    W('watch', '⌚', [
        S('n.', '手錶', 'My watch is five minutes fast.', '我的手錶快了五分鐘。'),
        S('v.', '觀看', 'We watched a movie last night.', '我們昨晚看了一部電影。'),
        S('v.', '照看；看守', 'Can you watch my bag for a minute?', '你可以幫我顧一下包包嗎？'),
        S('v.', '小心；注意', 'Watch your step! The floor is wet.', '小心腳步！地板是濕的。', 'watch out 小心'),
    ], 'watch - watched - watched - watching'),
  ],
  'focus': [
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('blue', '藍色的', '憂鬱的；out of the blue 突然'),
      ('green', '綠色的', '沒經驗的；環保的；greens 蔬菜'),
      ('pen', '筆', '動物的圍欄'),
      ('down', '向下', '情緒低落的；羽絨'),
      ('ball', '球', '舞會'),
      ('fine', '好的', '細的；罰款'),
      ('ruler', '尺', '統治者'),
      ('school', '學校', '（魚）群'),
      ('watch', '手錶；看', '照顧；小心'),
    ], 'note': '看到熟悉的字卻讀不通句子時，想想看這個字是不是還有別的意思。'},
    {'title': '常用片語', 'head': ('片語', '意思', '例句'), 'rows': [
      ('look for / look after', '尋找／照顧', 'I\'m looking for my keys.'),
      ('run out of', '用完', 'We have run out of milk.'),
      ('be short of', '缺少', 'We are short of time.'),
      ('have a gift for', '有…的天分', 'Amy has a gift for music.'),
      ('give + 人 + a ride', '載某人一程', 'Can you give me a ride?'),
      ('rain or shine', '風雨無阻', 'The game will go on, rain or shine.'),
      ('out of the blue', '突然；出乎意料', 'He called me out of the blue.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'I feel <b>blue</b> because my best friend moved away.', 'opts': ['藍色的', '憂鬱的', '突然的', '寒冷的'], 'answer': 1, 'exp': 'feel blue 心情憂鬱。'},
    {'type': 'mc', 'q': 'The farmer put the sheep back in the <b>pen</b>.', 'opts': ['筆', '圍欄', '帳篷', '草地'], 'answer': 1, 'exp': '羊被放回「圍欄」。'},
    {'type': 'mc', 'q': 'The princess danced with the prince at the <b>ball</b>.', 'opts': ['球', '舞會', '城堡', '比賽'], 'answer': 1, 'exp': '和王子跳舞 → 舞會。'},
    {'type': 'mc', 'q': 'He had to pay a $500 <b>fine</b> for riding a scooter without a helmet.', 'opts': ['好的', '細的', '罰款', '禮物'], 'answer': 2, 'exp': 'pay a fine 繳罰款。'},
    {'type': 'mc', 'q': 'We saw a <b>school</b> of dolphins near the island.', 'opts': ['學校', '一群', '一隻', '上課時間'], 'answer': 1, 'exp': 'a school of dolphins 一群海豚。'},
    {'type': 'mc', 'q': 'Can you <b>watch</b> my little sister while I cook dinner?', 'opts': ['手錶', '觀看電視', '照看', '小心'], 'answer': 2, 'exp': 'watch + 人 照看某人。'},
    {'type': 'mc', 'q': 'The new worker is still <b>green</b>, so he makes some mistakes.', 'opts': ['綠色的', '環保的', '沒經驗的', '生氣的'], 'answer': 2, 'exp': '新人常犯錯 → 沒經驗的。'},
    {'type': 'mc', 'q': 'Mr. Wang <b>runs</b> a small bookstore near our school.', 'opts': ['跑步', '經營', '用完', '跑過'], 'answer': 1, 'exp': 'run a shop 經營一家店。'},
    {'type': 'mc', 'q': 'Is there <b>room</b> for my bag in your car?', 'opts': ['房間', '空間', '時間', '座位號碼'], 'answer': 1, 'exp': 'room 不可數時是「空間」。'},
    {'type': 'mc', 'q': 'Kevin has a <b>gift</b> for drawing. His pictures look real.', 'opts': ['禮物', '天分', '工具', '習慣'], 'answer': 1, 'exp': 'have a gift for 有…的天分。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'I can\'t find my ______. What time is it?  ／  Let\'s ______ a movie tonight.', 'opts': ['look', 'watch', 'clock', 'see'], 'answer': 1, 'exp': 'watch 手錶／觀看。'},
    {'type': 'mc', 'q': 'Use a ______ to draw a line.  ／  The king was a cruel ______.', 'opts': ['pen', 'marker', 'ruler', 'leader'], 'answer': 2, 'exp': 'ruler 尺／統治者。'},
    {'type': 'mc', 'q': 'A: How are you?  B: I\'m ______.  ／  You have to pay a ______ if you park here.', 'opts': ['good', 'fine', 'well', 'ticket'], 'answer': 1, 'exp': 'fine 很好／罰款。'},
    {'type': 'mc', 'q': 'Turn the music ______. It\'s too loud.  ／  This ______ jacket is light and warm.', 'opts': ['off', 'up', 'down', 'thick'], 'answer': 2, 'exp': 'turn down 調小聲／down jacket 羽絨外套。'},
    {'type': 'mc', 'q': 'I\'m ______ for my keys.  ／  Can you ______ after my cat?', 'opts': ['looking / look', 'seeing / see', 'finding / find', 'watching / watch'], 'answer': 0, 'exp': 'look for 尋找；look after 照顧。'},
    {'type': 'mc', 'q': 'Can you give me a ______ home?  ／  The roller coaster is my favorite ______.', 'opts': ['drive', 'car', 'ride', 'trip'], 'answer': 2, 'exp': 'give + 人 + a ride 載某人／遊樂設施。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'We have run out {0} sugar. （用完）', 'blanks': [['of']], 'exp': 'run out of 用完。'},
    {'q': 'My cat is too {0}. He needs to eat less. （胖的）', 'blanks': [['fat']], 'exp': 'fat 胖的。'},
    {'q': 'Grandpa often goes {0} on weekends. （釣魚）', 'blanks': [['fishing']], 'exp': 'go fishing 去釣魚。'},
    {'q': 'The air is {0} at the top of the mountain. （稀薄的）', 'blanks': [['thin']], 'exp': 'thin 稀薄的。'},
    {'q': 'We are {0} of money this month. （缺少的）', 'blanks': [['short']], 'exp': 'be short of 缺少。'},
    {'q': 'They {0} the baby Emma. （取名）', 'blanks': [['named']], 'exp': 'name 取名，過去式 named。'},
  ]},
]
