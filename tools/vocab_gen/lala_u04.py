# LaLa Word Unit 4（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 42–50 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 4, 'en': 'The Talking Shower', 'zh': '一字多義（四）',
  'intro': 'shower 是淋浴，也是「陣雨」；face 是臉，也可以當動詞「面對」。這個單元有 6 個主題單字、11 個更多單字。',
  'words': [
    W('shower', '🚿', [
        S('n.', '淋浴', 'I take a shower every night.', '我每天晚上淋浴。', 'take a shower 洗澡；shower cap 浴帽'),
        S('n.', '陣雨', 'There will be showers this afternoon.', '今天下午會有陣雨。'),
        S('v.', '大量地給予', 'Grandma showered us with gifts.', '奶奶送我們好多禮物。', 'shower + 人 + with + 物 送給某人很多…'),
    ], 'shower - showered - showered - showering', key=True),
    W('work', '💼', [
        S('v.', '工作', 'My dad works at a hospital.', '我爸爸在醫院工作。'),
        S('v.', '（機器）運轉', 'The TV doesn\'t work. Can you fix it?', '電視壞了，你可以修嗎？'),
        S('v.', '運動健身（work out）', 'She works out at the gym every morning.', '她每天早上去健身房運動。', 'work out 健身'),
        S('v.', '起作用；有效', 'This medicine really works.', '這個藥真的有效。'),
        S('n.', '作品；著作', 'This painting is a famous work of art.', '這幅畫是有名的藝術作品。'),
    ], 'work - worked - worked - working', key=True),
    W('answer', '🙋', [
        S('v.', '回答', 'Please answer my question.', '請回答我的問題。'),
        S('v.', '接（電話）；應（門）', 'Can you answer the phone? I\'m busy.', '你可以接電話嗎？我在忙。', 'answer the phone 接電話；answer the door 應門'),
        S('n.', '答案', 'Do you know the answer to question 5?', '你知道第五題的答案嗎？', 'the answer to …的答案'),
        S('n.', '回覆', 'I sent her a message, but I got no answer.', '我傳訊息給她，但沒有回覆。'),
    ], 'answer - answered - answered - answering', key=True),
    W('strong', '💪', [
        S('adj.', '強壯的；有力的', 'My brother is strong. He can carry the big box.', '我哥哥很強壯，他搬得動這個大箱子。'),
        S('adj.', '強勁的（風、水流）', 'The strong wind blew my hat away.', '強風把我的帽子吹走了。'),
        S('adj.', '濃的（氣味、味道）', 'This coffee is too strong for me.', '這杯咖啡對我來說太濃了。'),
        S('adj.', '堅固的', 'We need a strong box for the books.', '我們需要一個堅固的箱子裝書。'),
    ], 'strong - stronger - strongest', key=True),
    W('question', '❓', [
        S('n.', '問題；試題', 'May I ask you a question?', '我可以問你一個問題嗎？'),
        S('n.', '懷疑', 'There is no question that he is the best player.', '毫無疑問，他是最好的球員。'),
        S('v.', '詢問；質問', 'The police questioned the man for an hour.', '警察盤問那個男人一個小時。'),
    ], 'question - questioned - questioned - questioning', key=True),
    W('face', '🙂', [
        S('n.', '臉', 'Wash your face before breakfast.', '吃早餐前先洗臉。'),
        S('n.', '表情', 'Why the long face? What happened?', '幹嘛板著臉？發生什麼事？', 'pull a long face 板著臉'),
        S('n.', '面子', 'He didn\'t want to lose face in front of his friends.', '他不想在朋友面前丟臉。', 'lose face 丟臉；save face 保住面子'),
        S('n.', '表面；正面', 'They climbed the north face of the mountain.', '他們攀爬山的北面。'),
        S('v.', '面對', 'You have to face the problem.', '你必須面對這個問題。', 'face the music 承擔後果；Let\'s face it. 面對現實吧。'),
        S('v.', '面向；朝向', 'My bedroom faces the sea.', '我的房間面向大海。'),
    ], 'face - faced - faced - facing', key=True),
    W('brush', '🪥', [
        S('n.', '刷子；畫筆', 'I need a brush to paint the door.', '我需要一支刷子來漆門。', 'toothbrush 牙刷；hairbrush 梳子'),
        S('n.', '灌木叢', 'A rabbit ran into the brush.', '一隻兔子跑進灌木叢裡。', 'brush fire 灌木叢火災'),
        S('v.', '刷', 'Brush your teeth before bed.', '睡前要刷牙。'),
        S('v.', '輕輕擦過', 'A cat brushed against my leg.', '一隻貓輕輕擦過我的腳。', 'brush against 輕碰；brush past 擦身而過'),
        S('v.', '塗（醬汁）', 'Brush some oil on the bread.', '在麵包上刷一點油。'),
    ], 'brush - brushed - brushed - brushing'),
    W('court', '🎾', [
        S('n.', '球場', 'The students are playing on the basketball court.', '學生們在籃球場上打球。'),
        S('n.', '法院；法庭', 'The man had to go to court.', '那個男人必須上法院。'),
    ], '複數 courts'),
    W('even', '⚖️', [
        S('adv.', '甚至', 'Even my grandma can use a smartphone.', '連我奶奶都會用智慧型手機。'),
        S('adv.', '更加（比較）', 'Today is even hotter than yesterday.', '今天比昨天更熱。'),
        S('adv.', '即使（even if）', 'Even if it rains, we will go.', '即使下雨，我們也會去。', 'even if 即使'),
        S('adv.', '儘管（even though）', 'Even though he was sick, he went to school.', '儘管他生病了，他還是去上學。', 'even though 儘管'),
        S('adj.', '平坦的；均等的', 'The road is not even. Be careful.', '路面不平，小心。'),
        S('adj.', '偶數的', 'Two, four and six are even numbers.', '二、四、六是偶數。'),
    ]),
    W('exercise', '🏋️', [
        S('v.', '運動', 'I exercise for thirty minutes every day.', '我每天運動三十分鐘。'),
        S('n.', '運動', 'Swimming is good exercise.', '游泳是很好的運動。', 'do / take exercise 運動'),
        S('v.', '行使（權利）', 'Adults can exercise their right to vote.', '成年人可以行使投票權。'),
        S('n.', '練習；習題', 'Do the exercises on page 20.', '做第二十頁的習題。'),
    ], 'exercise - exercised - exercised - exercising'),
    W('eye', '👁️', [
        S('n.', '眼睛', 'She has big brown eyes.', '她有一雙棕色的大眼睛。'),
        S('n.', '注目', 'All eyes were on the new student.', '所有人都在注意那位新同學。', 'all eyes are on 大家都注意著…'),
        S('v.', '注視；打量', 'The boy eyed the last piece of cake.', '那個男孩盯著最後一塊蛋糕看。'),
    ], 'eye - eyed - eyed - eyeing'),
    W('like', '👍', [
        S('v.', '喜歡', 'I like ice cream very much.', '我非常喜歡冰淇淋。'),
        S('v.', '想要（would like）', 'I would like a glass of water, please.', '我想要一杯水。', 'would like to + V 想要'),
        S('prep.', '像', 'You look like your mother.', '你長得像你媽媽。', 'look / sound like 看起來／聽起來像'),
        S('prep.', '例如', 'I like fruits like apples and grapes.', '我喜歡蘋果、葡萄之類的水果。'),
    ], 'like - liked - liked - liking'),
    W('once', '1️⃣', [
        S('adv.', '一次', 'I go swimming once a week.', '我一星期游泳一次。', 'once in a while 偶爾'),
        S('adv.', '曾經', 'There was once a big tree here.', '這裡曾經有一棵大樹。'),
        S('conj.', '一旦…就…', 'Once you start, you can\'t stop.', '你一開始就停不下來。'),
    ]),
    W('paint', '🎨', [
        S('n.', '油漆；顏料', 'Wet paint! Don\'t touch.', '油漆未乾，請勿觸摸。'),
        S('v.', '油漆', 'We painted the fence white.', '我們把籬笆漆成白色。'),
        S('v.', '（用顏料）畫', 'Amy likes to paint flowers.', 'Amy 喜歡畫花。'),
    ], 'paint - painted - painted - painting'),
    W('then', '➡️', [
        S('adj.', '當時', 'I met him in 2020, and we have been friends since then.', '我 2020 年認識他，從那時起我們就是朋友。', 'since then 從那時起；just then 就在那時'),
        S('adv.', '然後；接著', 'Wash the rice, then cook it.', '先洗米，然後煮。'),
        S('adv.', '那麼；既然如此', 'You\'re tired? Then go to bed.', '你累了？那就去睡覺吧。'),
    ]),
    W('thick', '📚', [
        S('adj.', '厚的；粗的', 'This dictionary is very thick.', '這本字典很厚。'),
        S('adj.', '濃的（湯、霧）', 'The fog was so thick that we couldn\'t see the road.', '霧濃到我們看不見路。'),
        S('adj.', '茂密的', 'The girl has thick black hair.', '那個女孩有濃密的黑髮。', 'be thick with 布滿'),
    ], 'thick - thicker - thickest'),
    W('top', '🔝', [
        S('n.', '頂部', 'We climbed to the top of the hill.', '我們爬到山丘頂上。', 'on the top of 在…最上面'),
        S('n.', '上衣', 'I like your yellow top.', '我喜歡你的黃色上衣。'),
        S('adj.', '頂尖的；最好的', 'She is one of the top students in our school.', '她是我們學校最頂尖的學生之一。'),
    ], '複數 tops'),
  ],
  'focus': [
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('shower', '淋浴', '陣雨；大量地給'),
      ('work', '工作', '（機器）運轉；有效；作品'),
      ('face', '臉', '面子；面對；朝向'),
      ('brush', '刷子；刷', '灌木叢；輕輕擦過'),
      ('court', '球場', '法院'),
      ('even', '甚至', '平坦的；偶數的'),
      ('eye', '眼睛', '注視；打量'),
      ('top', '頂部', '上衣；頂尖的'),
    ], 'note': ''},
    {'title': '常用片語', 'head': ('片語', '意思', '例句'), 'rows': [
      ('take a shower', '洗澡', 'I take a shower after dinner.'),
      ('work out', '健身', 'He works out three times a week.'),
      ('answer the phone / door', '接電話／應門', 'Can you answer the door?'),
      ('lose face / save face', '丟臉／保住面子', 'He didn\'t want to lose face.'),
      ('even if / even though', '即使／儘管', 'Even though it was late, he kept working.'),
      ('once in a while', '偶爾', 'Once in a while, we eat out.'),
      ('would like to', '想要', 'I would like to go to Japan.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'Take an umbrella. There may be <b>showers</b> later.', 'opts': ['淋浴', '陣雨', '颱風', '雪'], 'answer': 1, 'exp': 'showers 陣雨。'},
    {'type': 'mc', 'q': 'My phone doesn\'t <b>work</b>. I need a new one.', 'opts': ['工作', '運轉；能用', '健身', '作品'], 'answer': 1, 'exp': '手機不能用 → 運轉。'},
    {'type': 'mc', 'q': 'This tea is too <b>strong</b>. Can I have some water?', 'opts': ['強壯的', '堅固的', '濃的', '強勁的'], 'answer': 2, 'exp': '茶太濃。'},
    {'type': 'mc', 'q': 'The living room <b>faces</b> the park.', 'opts': ['臉', '面子', '面向', '表情'], 'answer': 2, 'exp': 'face 動詞：面向。'},
    {'type': 'mc', 'q': 'The man had to go to <b>court</b> because he stole a car.', 'opts': ['球場', '法院', '學校', '醫院'], 'answer': 1, 'exp': '偷車 → 上法院。'},
    {'type': 'mc', 'q': 'Ten is an <b>even</b> number.', 'opts': ['甚至', '平坦的', '偶數的', '均等的'], 'answer': 2, 'exp': 'even number 偶數。'},
    {'type': 'mc', 'q': 'Turn to page 30 and do the <b>exercises</b>.', 'opts': ['運動', '習題', '權利', '故事'], 'answer': 1, 'exp': 'do the exercises 做習題。'},
    {'type': 'mc', 'q': 'There was <b>once</b> a king who loved gold.', 'opts': ['一次', '曾經', '一旦', '只有'], 'answer': 1, 'exp': 'There was once… 從前曾經有…'},
    {'type': 'mc', 'q': 'She bought a pink <b>top</b> and a white skirt.', 'opts': ['頂部', '上衣', '帽子', '頂尖的'], 'answer': 1, 'exp': '和裙子一起買 → 上衣。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'Can you ______ the phone, please?  ／  I don\'t know the ______ to this question.', 'opts': ['pick', 'answer', 'reply', 'call'], 'answer': 1, 'exp': 'answer 接電話／答案。'},
    {'type': 'mc', 'q': 'Wash your ______ and hands.  ／  You must ______ your problems.', 'opts': ['face', 'eye', 'body', 'hair'], 'answer': 0, 'exp': 'face 臉／面對。'},
    {'type': 'mc', 'q': 'Don\'t forget to ______ your teeth.  ／  The artist cleaned his ______.', 'opts': ['wash', 'brush', 'paint', 'clean'], 'answer': 1, 'exp': 'brush 刷／畫筆。'},
    {'type': 'mc', 'q': 'She looks ______ her sister.  ／  Do you ______ Korean food?', 'opts': ['as', 'like', 'enjoy', 'love'], 'answer': 1, 'exp': 'like 像／喜歡。'},
    {'type': 'mc', 'q': 'Wet ______! Don\'t sit on the bench.  ／  The kids ______ pictures in art class.', 'opts': ['paint', 'color', 'draw', 'ink'], 'answer': 0, 'exp': 'paint 油漆／（用顏料）畫。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'I go to the gym to work {0} on weekends. （健身）', 'blanks': [['out']], 'exp': 'work out 健身。'},
    {'q': 'The book is too {0} to finish in one day. （厚的）', 'blanks': [['thick']], 'exp': 'thick 厚的。'},
    {'q': 'We eat out once in a {0}. （偶爾）', 'blanks': [['while']], 'exp': 'once in a while 偶爾。'},
    {'q': 'I would {0} to try the beef noodles. （想要）', 'blanks': [['like']], 'exp': 'would like to 想要。'},
    {'q': 'First, open the box. {0}, take out the toy. （然後）', 'blanks': [['Then', 'then']], 'exp': 'then 然後。'},
    {'q': 'All {0} were on the singer when she walked in. （眼睛；注目）', 'blanks': [['eyes']], 'exp': 'All eyes were on… 大家都注意著…'},
  ]},
]
