# LaLa Word Unit 16（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 179–188 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 16, 'en': 'Moo Deng the Pygmy Hippo', 'zh': '一字多義（十六）',
  'intro': 'wave 是海浪，也是「揮手」；letter 是信，也是「字母」。這個單元有 4 個主題單字、14 個更多單字，'
           '再整理 quiet／quite、along／alone／lonely，和字尾 -ful、字首 re-。',
  'words': [
    W('cheer', '📣', [
        S('v.', '歡呼；喝采', 'The fans cheered when the team scored.', '球隊得分時球迷歡呼。', 'cheer up 打起精神；使開心'),
        S('n.', '歡呼；鼓勵', 'We gave a big cheer for the winners.', '我們為優勝者大聲歡呼。'),
    ], 'cheer - cheered - cheered - cheering', key=True),
    W('wave', '🌊', [
        S('n.', '浪', 'The waves are big today.', '今天浪很大。'),
        S('n.', '揮手', 'She gave me a wave from the bus.', '她從公車上對我揮手。'),
        S('v.', '揮手', 'The kids waved goodbye to their grandparents.', '孩子們向祖父母揮手道別。', 'wave goodbye 揮手道別'),
    ], 'wave - waved - waved - waving', key=True),
    W('letter', '✉️', [
        S('n.', '信', 'I wrote a letter to my pen pal.', '我寫了一封信給我的筆友。'),
        S('n.', '字母', 'The word "dog" has three letters.', 'dog 這個字有三個字母。'),
    ], '複數 letters', key=True),
    W('set', '⏰', [
        S('v.', '設定（鬧鐘、規則）', 'I set my alarm for six.', '我把鬧鐘設在六點。', 'set up 架設；成立；set off 出發'),
        S('v.', '樹立（榜樣）', 'Older kids should set a good example.', '年紀大的孩子應該樹立好榜樣。'),
        S('v.', '擺放', 'Please set the table for dinner.', '請擺好餐具準備吃晚飯。', 'set the table 擺餐具'),
        S('n.', '一組；一套', 'I bought a new set of colored pencils.', '我買了一套新色鉛筆。'),
    ], 'set - set - set - setting', key=True),
    W('as', '🟰', [
        S('conj.', '當…時', 'As I was leaving, it started to rain.', '我正要離開時開始下雨了。'),
        S('conj.', '像…一樣', 'Do as I say.', '照我說的做。'),
        S('adv.', '和…一樣', 'He is as tall as his father.', '他和他爸爸一樣高。', 'as + 形容詞 + as 和…一樣；as usual 和平常一樣'),
        S('prep.', '作為；身為', 'She works as a nurse.', '她的工作是護理師。'),
    ]),
    W('by', '🚄', [
        S('prep.', '在…旁邊', 'There is a café by the lake.', '湖邊有一家咖啡店。'),
        S('prep.', '藉由（方式）', 'We went to Kaohsiung by train.', '我們搭火車去高雄。', 'by oneself 獨自'),
        S('prep.', '被（被動語態）', 'This book was written by a teenager.', '這本書是一個青少年寫的。'),
        S('prep.', '在…之前', 'Please finish the report by Friday.', '請在星期五前完成報告。'),
    ]),
    W('correct', '✔️', [
        S('v.', '改正；訂正', 'Correct the mistakes in your homework.', '訂正你作業裡的錯誤。'),
        S('adj.', '正確的', 'That\'s the correct answer.', '那是正確答案。'),
    ], 'correct - corrected - corrected - correcting'),
    W('course', '🍽️', [
        S('n.', '課程', 'She is taking a cooking course.', '她在上烹飪課。'),
        S('n.', '（餐點的）一道菜', 'The main course is steak.', '主菜是牛排。'),
        S('n.', '路線；方向', 'The plane changed its course.', '飛機改變了航道。', 'of course 當然'),
    ], '複數 courses'),
    W('cross', '❎', [
        S('v.', '穿越', 'Look both ways before you cross the street.', '過馬路前要看兩邊。'),
        S('v.', '使交叉', 'Let\'s cross our fingers for good luck.', '我們祈求好運吧。', 'cross one\'s fingers 祈求好運'),
        S('n.', '十字形；叉號', 'Put a cross next to the wrong answers.', '在錯誤答案旁邊打叉。'),
    ], 'cross - crossed - crossed - crossing'),
    W('mind', '🧠', [
        S('n.', '頭腦', 'A good idea came to mind.', '我想到一個好主意。', 'come to mind 浮現腦海'),
        S('n.', '想法；心意', 'I changed my mind.', '我改變主意了。', 'make up one\'s mind 下定決心'),
        S('v.', '介意', 'Do you mind if I sit here?', '你介意我坐這裡嗎？'),
        S('v.', '小心；注意', 'Mind the gap.', '小心月台間隙。'),
    ], 'mind - minded - minded - minding'),
    W('park', '🏞️', [
        S('n.', '公園', 'Let\'s have a picnic in the park.', '我們去公園野餐吧。'),
        S('v.', '停車', 'You can\'t park here.', '這裡不能停車。'),
    ], 'park - parked - parked - parking'),
    W('power', '⚡', [
        S('n.', '力量；能力', 'Music has the power to make people happy.', '音樂有讓人快樂的力量。'),
        S('n.', '電力；能源', 'The typhoon cut the power.', '颱風造成停電。'),
        S('n.', '影響力；權力', 'The king had a lot of power.', '國王有很大的權力。'),
    ]),
    W('row', '🚣', [
        S('n.', '一排', 'We sat in the front row.', '我們坐在第一排。', 'in a row 連續'),
        S('v.', '划（船）', 'They rowed the boat across the lake.', '他們划船橫渡湖面。'),
    ], 'row - rowed - rowed - rowing'),
    W('sight', '🗿', [
        S('n.', '視力；視覺', 'My grandpa has poor sight.', '我爺爺視力不好。'),
        S('n.', '景象；看見', 'It was love at first sight.', '那是一見鍾情。', 'at first sight 第一眼；out of sight 看不見'),
        S('n.', '名勝；景點（sights）', 'We saw all the sights of Tainan.', '我們看遍了臺南的景點。'),
    ], '複數 sights'),
    W('sign', '🪧', [
        S('n.', '標誌；招牌', 'The sign says "No Parking."', '牌子上寫著「禁止停車」。'),
        S('n.', '符號；記號', '"+" is the plus sign.', '「+」是加號。'),
        S('n.', '手勢', 'She can use sign language.', '她會用手語。', 'sign language 手語'),
        S('v.', '簽名', 'Please sign your name here.', '請在這裡簽名。', 'sign up 報名'),
    ], 'sign - signed - signed - signing'),
    W('store', '🏬', [
        S('n.', '商店', 'There is a convenience store on the corner.', '轉角有一家便利商店。'),
        S('v.', '儲存', 'Store the rice in a cool place.', '把米存放在陰涼的地方。'),
    ], 'store - stored - stored - storing'),
    W('tidy', '🧺', [
        S('adj.', '整潔的', 'Her room is always tidy.', '她的房間總是很整齊。'),
        S('v.', '收拾；整理', 'Tidy up your desk, please.', '請整理你的桌子。', 'tidy up 收拾'),
    ], 'tidy - tidier - tidiest；tidy - tidied - tidied - tidying'),
    W('yard', '🏡', [
        S('n.', '院子', 'The kids are playing in the yard.', '孩子們在院子裡玩。'),
        S('n.', '碼（約 0.91 公尺）', 'He kicked the ball forty yards.', '他把球踢了四十碼遠。'),
    ], '複數 yards'),
    W('beautiful', '🌺', [S('adj.', '美麗的', 'What a beautiful sunset!', '好美的夕陽！')], 'beauty + -ful'),
    W('careful', '⚠️', [S('adj.', '小心的', 'Be careful with the hot soup.', '小心熱湯。')], 'care + -ful'),
    W('thankful', '🙏', [S('adj.', '感謝的', 'I\'m thankful for my family.', '我很感謝我的家人。')], 'thank + -ful'),
    W('wonderful', '🤩', [S('adj.', '極好的；精彩的', 'We had a wonderful time at the beach.', '我們在海邊玩得很開心。')], 'wonder + -ful'),
    W('useful', '🧰', [S('adj.', '有用的', 'This app is very useful.', '這個 app 很有用。')], 'use + -ful'),
    W('review', '📚', [S('v.', '複習；溫習', 'Review your notes before the test.', '考試前複習你的筆記。')], 're- + view'),
    W('return', '↩️', [S('v.', '返回；歸還', 'Please return the book by Monday.', '請在星期一前還書。')], 're- + turn'),
  ],
  'focus': [
    {'title': '易混淆字：quiet 和 quite', 'head': ('單字', '意思', '例句'), 'rows': [
      ('quiet', '（形容詞）安靜的', 'Please be quiet in the library.'),
      ('quite', '（副詞）相當；頗', 'The test was quite easy.'),
    ], 'note': '兩個字只差 e 和 t 的位置，唸法也不同：quiet 兩個音節，quite 一個音節。'},
    {'title': '易混淆字：along／alone／lonely', 'head': ('單字', '意思', '例句'), 'rows': [
      ('along', '沿著；一起', 'We walked along the river.'),
      ('alone', '單獨的；獨自（客觀描述，沒有別人在）', 'She lives alone.'),
      ('lonely', '孤單的；寂寞的（主觀感受）', 'He feels lonely without his friends.'),
    ], 'note': '一個人（alone）不一定寂寞（lonely）。'},
    {'title': '字尾 -ful、字首 re-', 'head': ('原來的字', '加字首／字尾', '意思'), 'rows': [
      ('beauty 美', 'beautiful', '美麗的'),
      ('care 小心', 'careful', '小心的'),
      ('thank 感謝', 'thankful', '感謝的'),
      ('wonder 驚奇', 'wonderful', '極好的'),
      ('use 用途', 'useful', '有用的'),
      ('view 看', 'review', '複習'),
      ('turn 轉', 'return', '返回；歸還'),
    ], 'note': '-ful＝充滿…的；re-＝再次、回來。'},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('wave', '浪', '揮手'),
      ('letter', '信', '字母'),
      ('set', '設定', '一組；擺放'),
      ('course', '課程', '一道菜；of course'),
      ('mind', '頭腦', '介意；小心'),
      ('park', '公園', '停車'),
      ('row', '一排', '划船'),
      ('yard', '院子', '碼'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'The word "apple" has five <b>letters</b>.', 'opts': ['信', '字母', '字', '音節'], 'answer': 1, 'exp': 'a-p-p-l-e 五個字母。'},
    {'type': 'mc', 'q': 'Grandma <b>waved</b> to us from the window.', 'opts': ['浪', '揮手', '跳舞', '叫'], 'answer': 1, 'exp': 'wave 動詞：揮手。'},
    {'type': 'mc', 'q': 'Can you help me <b>set</b> the table?', 'opts': ['設定', '樹立', '擺放', '一套'], 'answer': 2, 'exp': 'set the table 擺餐具。'},
    {'type': 'mc', 'q': 'The main <b>course</b> was fried fish.', 'opts': ['課程', '一道菜', '路線', '當然'], 'answer': 1, 'exp': 'main course 主菜。'},
    {'type': 'mc', 'q': 'Do you <b>mind</b> if I open the window?', 'opts': ['頭腦', '想法', '介意', '小心'], 'answer': 2, 'exp': 'Do you mind…? 你介意…嗎？'},
    {'type': 'mc', 'q': 'Dad <b>parked</b> the car in front of the store.', 'opts': ['公園', '停車', '洗車', '開車'], 'answer': 1, 'exp': 'park 動詞：停車。'},
    {'type': 'mc', 'q': 'We lost <b>power</b> during the storm.', 'opts': ['力量', '電力', '權力', '比賽'], 'answer': 1, 'exp': '暴風雨時停電 → 電力。'},
    {'type': 'mc', 'q': 'Our team has won five games in a <b>row</b>.', 'opts': ['一排', '連續', '划船', '吵架'], 'answer': 1, 'exp': 'in a row 連續。'},
    {'type': 'mc', 'q': 'The football flew fifty <b>yards</b>.', 'opts': ['院子', '碼', '公尺', '圈'], 'answer': 1, 'exp': '距離單位 → 碼。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'Please ______ your name here.  ／  The ______ says "Keep Out."', 'opts': ['write', 'sign', 'mark', 'note'], 'answer': 1, 'exp': 'sign 簽名／標誌。'},
    {'type': 'mc', 'q': 'The ______ sells snacks and drinks.  ／  ______ the milk in the fridge.', 'opts': ['shop', 'store', 'Keep', 'market'], 'answer': 1, 'exp': 'store 商店／儲存。'},
    {'type': 'mc', 'q': 'Be careful when you ______ the street.  ／  Let\'s ______ our fingers and hope for the best.', 'opts': ['pass', 'cross', 'walk', 'hold'], 'answer': 1, 'exp': 'cross 穿越／交叉手指。'},
    {'type': 'mc', 'q': 'The Eiffel Tower is one of the famous ______s of Paris.  ／  My grandpa\'s ______ is getting worse.', 'opts': ['view', 'sight', 'eye', 'place'], 'answer': 1, 'exp': 'sight 景點／視力。'},
    {'type': 'mc', 'q': 'Please ______ your mistakes.  ／  Is this the ______ answer?', 'opts': ['right', 'correct', 'fix', 'true'], 'answer': 1, 'exp': 'correct 訂正／正確的。'},
  ]},
  {'title': '③ 易混淆字與字首字尾', 'items': [
    {'type': 'mc', 'q': 'The baby is sleeping. Please be ______.', 'opts': ['quite', 'quiet', 'quit', 'quick'], 'answer': 1, 'exp': '安靜的 quiet。'},
    {'type': 'mc', 'q': 'This book is ______ interesting.', 'opts': ['quiet', 'quite', 'quietly', 'quit'], 'answer': 1, 'exp': '相當 quite。'},
    {'type': 'mc', 'q': 'My grandma lives ______, but she has many friends.', 'opts': ['along', 'alone', 'lonely', 'long'], 'answer': 1, 'exp': '獨自（客觀）alone。'},
    {'type': 'mc', 'q': 'The new student felt ______ on her first day.', 'opts': ['alone', 'along', 'lonely', 'only'], 'answer': 2, 'exp': '寂寞的（感受）lonely。'},
    {'type': 'mc', 'q': 'Please ______ the umbrella after you use it.', 'opts': ['review', 'return', 'remove', 'repeat'], 'answer': 1, 'exp': '歸還 return。'},
    {'type': 'mc', 'q': 'Thanks for the map. It\'s really ______.', 'opts': ['careful', 'useful', 'thankful', 'beautiful'], 'answer': 1, 'exp': '有用的 useful。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Let\'s cheer {0} Amy. She looks sad. （使開心）', 'blanks': [['up']], 'exp': 'cheer up 使開心。'},
    {'q': 'We set {0} early for the trip. （出發）', 'blanks': [['off']], 'exp': 'set off 出發。'},
    {'q': 'She is as tall {0} her mother. （和…一樣）', 'blanks': [['as']], 'exp': 'as + 形容詞 + as。'},
    {'q': 'I finished the puzzle all by {0}. （我自己）', 'blanks': [['myself']], 'exp': 'by oneself 獨自。'},
    {'q': 'I can\'t make up my {0}. Red or blue? （決心）', 'blanks': [['mind']], 'exp': 'make up one\'s mind 下定決心。'},
    {'q': 'Please tidy {0} your room before dinner. （收拾）', 'blanks': [['up']], 'exp': 'tidy up 收拾。'},
  ]},
]
