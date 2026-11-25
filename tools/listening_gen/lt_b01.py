"""聽力訓練 初級 第 1 回（內容自編，題型照多益聽力四部分）"""
UNIT = {
    'id': 'b01', 'level': 'b', 'no': 1,
    'title': '初級 第 1 回', 'theme': '家裡、學校、買東西',
    # 第一部分：看照片，選出最符合的描述（選項不印出來，只用聽的）
    'p1': [
        {'img': 'b01p1', 'answer': 1, 'opts': [
            ('The boy is writing a letter.', '男孩正在寫信。'),
            ('The boy is reading a book.', '男孩正在看書。'),
            ('The boy is playing soccer.', '男孩正在踢足球。')],
         'tip': '男孩坐在草地上，手上拿著一本打開的書。read a book＝看書。'},
        {'img': 'b01p2', 'answer': 2, 'opts': [
            ('The woman is washing the dishes.', '女子正在洗碗。'),
            ('The woman is eating lunch.', '女子正在吃午餐。'),
            ('The woman is cooking at the stove.', '女子正在爐子前煮東西。')],
         'tip': '她站在瓦斯爐前，鍋子在爐子上。stove＝爐子。洗碗要在水槽（sink）。'},
        {'img': 'b01p3', 'answer': 0, 'opts': [
            ('The children are riding bikes.', '孩子們正在騎腳踏車。'),
            ('The children are walking to school.', '孩子們正走路去上學。'),
            ('The children are driving a car.', '孩子們正在開車。')],
         'tip': 'ride a bike＝騎腳踏車（bike 就是 bicycle）。'},
        {'img': 'b01p4', 'answer': 1, 'opts': [
            ('The dog is running in the park.', '狗正在公園裡跑。'),
            ('The dog is sleeping on the sofa.', '狗正在沙發上睡覺。'),
            ('The dog is eating its food.', '狗正在吃牠的食物。')],
         'tip': '狗趴在沙發上、閉著眼睛。sofa＝沙發，on the sofa＝在沙發上。'},
    ],
    # 第二部分：聽問句，選出最適當的回答（題目和選項都只用聽的）
    'p2': [
        {'q': ("What's your name?", '你叫什麼名字？'), 'answer': 1, 'opts': [
            ("I'm twelve.", '我十二歲。'), ('My name is Amy.', '我的名字是艾咪。'), ("It's on the desk.", '它在書桌上。')],
         'tip': '問 name（名字）就回答名字。I\'m twelve 是回答年紀（How old…?）。'},
        {'q': ('Where is my pencil?', '我的鉛筆在哪裡？'), 'answer': 0, 'opts': [
            ("It's under your chair.", '在你的椅子下面。'), ("It's yellow.", '它是黃色的。'), ('Yes, it is.', '是的，它是。')],
         'tip': 'Where 問地點，要回答「在哪裡」：under your chair。Wh- 問句不能用 Yes／No 回答。'},
        {'q': ('How old is your brother?', '你哥哥（弟弟）幾歲？'), 'answer': 2, 'opts': [
            ("He's tall.", '他很高。'), ("He's in the kitchen.", '他在廚房。'), ("He's ten years old.", '他十歲。')],
         'tip': 'How old 問年紀 → ten years old。He\'s tall 是回答外表（What does he look like?）。'},
        {'q': ('Do you like apples?', '你喜歡蘋果嗎？'), 'answer': 0, 'opts': [
            ('Yes, I do.', '是的，我喜歡。'), ("No, it isn't.", '不，它不是。'), ('I like red.', '我喜歡紅色。')],
         'tip': 'Do you…? 用 Yes, I do.／No, I don\'t. 回答。I like red 用「蘋果是紅色」來騙你，要小心。'},
        {'q': ('Who is that girl?', '那個女孩是誰？'), 'answer': 0, 'opts': [
            ("She's my sister, Mary.", '她是我妹妹瑪莉。'), ("She's at school.", '她在學校。'), ('She likes music.', '她喜歡音樂。')],
         'tip': 'Who 問「是誰」→ 回答身分或名字：my sister, Mary。'},
        {'q': ('When do you get up?', '你幾點起床？'), 'answer': 1, 'opts': [
            ('At school.', '在學校。'), ('At six thirty.', '六點半。'), ('By bus.', '搭公車。')],
         'tip': 'When 問時間 → At six thirty。At school 是地點、By bus 是交通方式。'},
        {'q': ('What color is your bag?', '你的包包是什麼顏色？'), 'answer': 0, 'opts': [
            ("It's blue.", '它是藍色的。'), ("It's big.", '它很大。'), ("It's my bag.", '它是我的包包。')],
         'tip': 'What color 問顏色 → blue。big 是大小，不是顏色。'},
        {'q': ('Can you help me, please?', '可以請你幫我嗎？'), 'answer': 0, 'opts': [
            ('Sure. What is it?', '當然。什麼事？'), ("I'm fine, thank you.", '我很好，謝謝。'), ("No, I don't.", '不，我沒有。')],
         'tip': '別人請你幫忙，可以說 Sure.（當然）。Can you…? 不能用 I don\'t 回答。'},
    ],
    # 第三部分：簡短對話（問題和選項印在畫面上，題目也會唸出來）
    'p3': [
        {'lines': [('W', "Tom, it's time for school. Where's your bag?", '湯姆，該上學了。你的書包在哪裡？'),
                   ('M', "It's in my room, Mom. I'll go and get it.", '在我房間，媽媽。我去拿。')],
         'q': ("Where is Tom's bag?", '湯姆的書包在哪裡？'), 'answer': 1,
         'opts': [('In the kitchen.', '在廚房。'), ('In his room.', '在他的房間。'), ('At school.', '在學校。')],
         'tip': '男生說 It\'s in my room（在我房間）。題目問 his room（他的房間）。'},
        {'lines': [('M', "Let's play basketball after school.", '放學後我們去打籃球吧。'),
                   ('W', "Sorry, I can't. I have a piano lesson today.", '抱歉，我不行。我今天有鋼琴課。')],
         'q': ('What will the girl do after school?', '女孩放學後要做什麼？'), 'answer': 2,
         'opts': [('Play basketball.', '打籃球。'), ('Do her homework.', '寫功課。'), ('Have a piano lesson.', '上鋼琴課。')],
         'tip': '打籃球是男生提議的，女孩說 Sorry, I can\'t（不行），因為她有 piano lesson（鋼琴課）。'},
        {'lines': [('W', 'Excuse me. How much is this T-shirt?', '不好意思，這件 T 恤多少錢？'),
                   ('M', "It's two hundred dollars.", '兩百元。'),
                   ('W', "OK. I'll take it.", '好，我要買。')],
         'q': ('How much is the T-shirt?', 'T 恤多少錢？'), 'answer': 1,
         'opts': [('100 dollars.', '100 元。'), ('200 dollars.', '200 元。'), ('300 dollars.', '300 元。')],
         'tip': 'two hundred＝200。I\'ll take it＝我要買這件。'},
        {'lines': [('M', 'Mom, is it going to rain today?', '媽，今天會下雨嗎？'),
                   ('W', 'Yes. Take your umbrella with you.', '會。把你的雨傘帶著。')],
         'q': ('What should the boy take?', '男孩應該帶什麼？'), 'answer': 0,
         'opts': [('His umbrella.', '他的雨傘。'), ('His jacket.', '他的外套。'), ('His lunch.', '他的午餐。')],
         'tip': '媽媽說 Take your umbrella（帶你的雨傘）。'},
    ],
    # 第四部分：簡短獨白（廣播、留言、公告）
    'p4': [
        {'kind': ('School announcement', '學校廣播'), 'voice': 'M',
         'lines': [('Good morning, students. Today is Sports Day.', '同學早安。今天是運動會。'),
                   ('Please go to the playground at nine o\'clock.', '請在九點到操場集合。'),
                   ("Don't forget to bring some water.", '別忘了帶水。')],
         'q': ('Where should the students go?', '學生們要去哪裡？'), 'answer': 1,
         'opts': [('To the library.', '去圖書館。'), ('To the playground.', '去操場。'), ('To the classroom.', '去教室。')],
         'tip': 'go to the playground＝去操場。Sports Day＝運動會。'},
        {'kind': ('Phone message', '電話留言'), 'voice': 'M',
         'lines': [("Hi, Jenny. This is Kevin.", '嗨，珍妮，我是凱文。'),
                   ("I'm sick today, so I can't go to the movies with you.", '我今天生病了，所以不能跟你去看電影。'),
                   ("Let's go next Saturday. Bye!", '我們下星期六再去吧。再見！')],
         'q': ("Why can't Kevin go to the movies?", '凱文為什麼不能去看電影？'), 'answer': 0,
         'opts': [('He is sick.', '他生病了。'), ('He is busy.', '他很忙。'), ('He has no money.', '他沒有錢。')],
         'tip': 'I\'m sick today, so I can\'t go… → so（所以）前面就是原因：生病了。'},
        {'kind': ('Store announcement', '商店廣播'), 'voice': 'W',
         'lines': [('Welcome to Happy Mart.', '歡迎光臨快樂超市。'),
                   ('Today, all fruit is half price.', '今天所有水果半價。'),
                   ('Apples, bananas, and oranges are all on sale.', '蘋果、香蕉和柳橙都在特價。'),
                   ('Thank you for shopping with us.', '謝謝您的光臨。')],
         'q': ('What is on sale today?', '今天什麼在特價？'), 'answer': 2,
         'opts': [('Milk.', '牛奶。'), ('Bread.', '麵包。'), ('Fruit.', '水果。')],
         'tip': 'all fruit is half price＝所有水果半價；on sale＝特價。蘋果、香蕉、柳橙都是水果。'},
        {'kind': ('Weather report', '氣象報告'), 'voice': 'W',
         'lines': [("Here is the weather for Taipei.", '以下是臺北的天氣。'),
                   ('It will be sunny and hot this morning.', '今天早上晴朗炎熱。'),
                   ('In the afternoon, it will rain.', '下午會下雨。'),
                   ('Take an umbrella when you go out.', '出門請帶傘。')],
         'q': ('What will the weather be like in the afternoon?', '下午天氣會怎樣？'), 'answer': 1,
         'opts': [('Sunny.', '晴天。'), ('Rainy.', '下雨。'), ('Windy.', '颳風。')],
         'tip': '早上 sunny（晴天），下午 it will rain（會下雨）。題目問的是 afternoon（下午），要聽清楚時間。'},
    ],
}
