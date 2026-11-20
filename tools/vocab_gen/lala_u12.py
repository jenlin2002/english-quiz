# LaLa Word Unit 12（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 132–143 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 12, 'en': 'The Beating Heart', 'zh': '一字多義（十二）',
  'intro': 'bill 是帳單，也是「鈔票」和「鳥嘴」；nail 是指甲，也是「釘子」。這個單元有 6 個主題單字、17 個更多單字。',
  'words': [
    W('push', '🛒', [
        S('v.', '推；推擠', 'Push the door to open it.', '推門就能打開。'),
        S('n.', '推一下', 'Can you give the car a push?', '你可以幫忙推一下車嗎？'),
        S('v.', '按（按鈕）', 'Push the button to call the elevator.', '按按鈕叫電梯。'),
        S('v.', '逼迫', 'Don\'t push yourself too hard.', '別把自己逼得太緊。'),
    ], 'push - pushed - pushed - pushing', key=True),
    W('full', '🈵', [
        S('adj.', '完整的；全部的', 'Please write your full name here.', '請在這裡寫你的全名。', 'full name 全名；full marks 滿分'),
        S('adj.', '吃飽的', 'No more, thanks. I\'m full.', '不用了，謝謝，我吃飽了。'),
        S('adj.', '滿的', 'The bus is full. Let\'s wait for the next one.', '公車滿了，我們等下一班。'),
        S('adj.', '充滿的', 'The room is full of balloons.', '房間裡滿是氣球。', 'be full of 充滿'),
    ], 'full - fuller - fullest', key=True),
    W('circle', '⭕', [
        S('n.', '循環', 'Exercise and good sleep make a healthy circle.', '運動和好睡眠形成健康的循環。'),
        S('n.', '圓圈', 'The kids sat in a circle.', '孩子們圍成一圈坐著。'),
        S('n.', '圈子；界', 'She has a large circle of friends.', '她的朋友圈很廣。'),
        S('v.', '盤旋；繞圈', 'A bird circled over the lake.', '一隻鳥在湖上盤旋。'),
        S('v.', '圈起來', 'Circle the right answer.', '把正確答案圈起來。'),
    ], 'circle - circled - circled - circling', key=True),
    W('test', '🧪', [
        S('n.', '檢查', 'I had an eye test today.', '我今天做了視力檢查。', 'eye test 視力檢查；blood test 驗血'),
        S('v.', '檢測；測試', 'They tested the new phone for a month.', '他們測試新手機一個月。'),
        S('n.', '考試；測驗', 'We have an English test tomorrow.', '我們明天有英文考試。', 'take a test 考試；pass / fail a test 通過／沒通過'),
        S('v.', '考驗', 'The long hike tested our strength.', '長途健行考驗我們的體力。'),
    ], 'test - tested - tested - testing', key=True),
    W('record', '🎙️', [
        S('v.', '記錄', 'Record your weight every day.', '每天記錄你的體重。'),
        S('v.', '錄製', 'The band recorded a new song.', '樂團錄了一首新歌。'),
        S('n.', '紀錄；最佳成績', 'She broke the school record.', '她打破了學校紀錄。', 'set / break a record 創／破紀錄（名詞唸 [ˋrɛkɚd]）'),
    ], 'record - recorded - recorded - recording', key=True),
    W('stand', '🎤', [
        S('v.', '忍受', 'I can\'t stand the hot weather.', '我受不了這麼熱的天氣。'),
        S('v.', '站立', 'Please stand still for the photo.', '拍照請站好別動。', 'stand back 往後站；stand for 代表'),
        S('n.', '攤位；架子', 'We bought juice at a fruit stand.', '我們在水果攤買了果汁。', 'music stand 譜架'),
    ], 'stand - stood - stood - standing', key=True),
    W('angle', '📐', [
        S('n.', '角度', 'A square has four right angles.', '正方形有四個直角。'),
        S('n.', '（看的）角度', 'Take the photo from a different angle.', '從不同的角度拍照。'),
        S('n.', '觀點', 'Let\'s look at the problem from another angle.', '我們從另一個觀點看這個問題。'),
    ], '複數 angles'),
    W('bill', '🧾', [
        S('n.', '帳單', 'Can we have the bill, please?', '請給我們帳單。'),
        S('n.', '紙鈔', 'I only have a 1,000-dollar bill.', '我只有一張千元鈔。'),
        S('n.', '法案', 'The new bill will help the farmers.', '新法案會幫助農民。'),
        S('n.', '鳥嘴', 'The duck has a yellow bill.', '這隻鴨子有黃色的嘴。'),
    ], '複數 bills'),
    W('care', '❤️', [
        S('n.', '照顧', 'Take care of your little brother.', '照顧好你弟弟。', 'take care of 照顧；Take care! 保重'),
        S('n.', '小心', 'Handle the glass with care.', '小心拿玻璃杯。', 'with care 小心'),
        S('v.', '在乎', 'I don\'t care what others think.', '我不在乎別人怎麼想。', 'care about 在乎'),
    ], 'care - cared - cared - caring'),
    W('cold', '🤧', [
        S('adj.', '冷的', 'It\'s cold today. Wear a jacket.', '今天很冷，穿件外套。'),
        S('adj.', '冷淡的', 'Why are you so cold to me?', '你為什麼對我這麼冷淡？', 'give + 人 + the cold shoulder 冷落某人'),
        S('n.', '感冒', 'I have a bad cold.', '我得了重感冒。', 'catch / have a cold 感冒'),
    ], 'cold - colder - coldest'),
    W('count', '🔢', [
        S('v.', '數；計算', 'Can you count to one hundred?', '你會從一數到一百嗎？', 'count + 人 + in 算某人一份'),
        S('n.', '計數', 'I lost count of how many times I watched it.', '我已經數不清看了幾次。', 'lose count of 數不清'),
        S('v.', '有重要性；算數', 'Every vote counts.', '每一票都很重要。', 'count on 依靠'),
        S('n.', '總數', 'The teacher did a head count on the bus.', '老師在車上清點人數。'),
    ], 'count - counted - counted - counting'),
    W('dead', '🔋', [
        S('adj.', '死的', 'The fish in the tank is dead.', '魚缸裡的魚死了。'),
        S('adj.', '壞掉的；沒電的', 'My phone is dead. Can I use yours?', '我的手機沒電了，可以借你的嗎？', 'dead end 死巷'),
        S('adj.', '死氣沉沉的', 'The town is dead at night.', '這個小鎮晚上很冷清。'),
    ]),
    W('excuse', '🙇', [
        S('n.', '藉口', 'Stop making excuses.', '別再找藉口了。', 'make excuses 找藉口'),
        S('v.', '原諒', 'Please excuse me for being late.', '請原諒我遲到。', 'Excuse me. 不好意思；借過'),
    ], 'excuse - excused - excused - excusing（名詞唸 [ɪkˋskjus]）'),
    W('fair', '🎡', [
        S('adj.', '公平的', 'That\'s not fair!', '這不公平！'),
        S('adj.', '合理的', 'The price is fair.', '這個價格很合理。'),
        S('adj.', '（膚色）白皙的；（頭髮）金色的', 'The baby has fair hair.', '寶寶有一頭淡金色的頭髮。'),
        S('n.', '展覽；博覽會', 'We went to the book fair.', '我們去了書展。'),
    ], 'fair - fairer - fairest'),
    W('group', '👥', [
        S('n.', '群；團體', 'We work in groups of four.', '我們四人一組。'),
        S('n.', '（企業）集團', 'His dad works for a big business group.', '他爸爸在一家大企業集團上班。'),
        S('v.', '分類；分組', 'Group the animals by where they live.', '把動物依照住的地方分類。'),
    ], 'group - grouped - grouped - grouping'),
    W('head', '🧠', [
        S('n.', '頭', 'He shook his head.', '他搖搖頭。', 'shake one\'s head 搖頭'),
        S('n.', '頭腦', 'Use your head!', '動動腦！', 'lose one\'s head 失去理智'),
        S('n.', '負責人；主管', 'Ms. Wu is the head of our school.', '吳老師是我們的校長。'),
        S('v.', '前往', 'We\'re heading home.', '我們正要回家。'),
    ], 'head - headed - headed - heading'),
    W('hold', '🤝', [
        S('v.', '拿著；握住', 'Hold my hand when we cross the street.', '過馬路時牽著我的手。'),
        S('v.', '舉辦', 'The school will hold a sports day next week.', '學校下星期要辦運動會。'),
        S('v.', '容納', 'This bottle holds one liter of water.', '這個瓶子可以裝一公升的水。'),
        S('v.', '保持（紀錄）', 'He holds the school record for the 100 meters.', '他保持學校一百公尺的紀錄。'),
        S('v.', '等待；暫停', 'Hold on. I\'m coming.', '等一下，我來了。', 'hold on 等一下；hold one\'s breath 憋氣'),
    ], 'hold - held - held - holding'),
    W('matter', '❔', [
        S('n.', '事情', 'As a matter of fact, I don\'t like cake.', '事實上，我不喜歡蛋糕。', 'as a matter of fact 事實上'),
        S('n.', '麻煩；問題', 'What\'s the matter with you?', '你怎麼了？', 'What\'s the matter? 怎麼了'),
        S('v.', '要緊；有關係', 'It doesn\'t matter.', '沒關係。'),
    ], 'matter - mattered - mattered - mattering'),
    W('nail', '🔨', [
        S('n.', '指甲', 'Cut your nails every week.', '每週剪指甲。', 'fingernail 手指甲；toenail 腳趾甲'),
        S('n.', '釘子', 'Hand me a nail and the hammer.', '把釘子和槌子遞給我。'),
        S('v.', '釘牢', 'Dad nailed the sign to the door.', '爸爸把牌子釘在門上。'),
        S('v.', '做到；做得很好', 'You nailed it!', '你做得太棒了！'),
    ], 'nail - nailed - nailed - nailing'),
    W('pass', '🎫', [
        S('v.', '經過', 'We passed a park on the way.', '我們在路上經過一座公園。'),
        S('v.', '傳遞', 'Please pass me the salt.', '請把鹽遞給我。'),
        S('v.', '度過（時間）', 'We played games to pass the time.', '我們玩遊戲打發時間。'),
        S('v.', '通過（考試）', 'I passed the math test!', '我數學考試及格了！'),
        S('n.', '通行證；票卡', 'Show your bus pass to the driver.', '把公車定期票給司機看。'),
    ], 'pass - passed - passed - passing'),
    W('point', '👉', [
        S('n.', '小數點', 'Two point five is bigger than two.', '二點五比二大。'),
        S('n.', '得分；分數', 'Our team won by two points.', '我們隊贏了兩分。'),
        S('n.', '觀點；重點', 'I see your point.', '我懂你的意思。', 'from one\'s point of view 從某人的觀點'),
        S('n.', '目的；意義', 'What\'s the point of waiting?', '等下去有什麼用？'),
        S('v.', '指', 'It\'s rude to point at people.', '用手指著別人不禮貌。', 'point at 指著'),
    ], 'point - pointed - pointed - pointing'),
    W('shape', '🔷', [
        S('n.', '形狀', 'The cookie is in the shape of a heart.', '這塊餅乾是心形的。', 'in the shape of 以…的形狀'),
        S('n.', '健康狀況；身材', 'I run every day to stay in shape.', '我每天跑步保持身材。', 'in shape 健康；身材好；out of shape 身材走樣'),
        S('v.', '塑造成…形狀', 'Shape the clay into a bowl.', '把黏土捏成碗的形狀。'),
        S('v.', '決定；影響', 'What you do today will shape your future.', '你今天做的事會影響你的未來。'),
    ], 'shape - shaped - shaped - shaping'),
    W('throw', '🎲', [
        S('v.', '丟；擲', 'Throw the ball to me!', '把球丟給我！', 'throw away 丟掉；throw up 嘔吐'),
        S('v.', '舉辦（派對）', 'Let\'s throw a party for Mom.', '我們幫媽媽辦個派對吧。'),
    ], 'throw - threw - thrown - throwing'),
  ],
  'focus': [
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('bill', '帳單', '紙鈔；法案；鳥嘴'),
      ('nail', '指甲', '釘子；做得很好'),
      ('stand', '站', '忍受；攤位'),
      ('cold', '冷的', '感冒；冷淡的'),
      ('count', '數', '重要；count on 依靠'),
      ('fair', '公平的', '展覽；白皙的'),
      ('head', '頭', '負責人；前往'),
      ('shape', '形狀', '身材；健康狀況'),
      ('point', '指', '分數；重點；小數點'),
    ], 'note': ''},
    {'title': '常用片語', 'head': ('片語', '意思', '例句'), 'rows': [
      ('take care of', '照顧', 'I take care of my dog.'),
      ('be full of', '充滿', 'The box is full of toys.'),
      ('count on', '依靠', 'You can count on me.'),
      ('hold on', '等一下', 'Hold on, please.'),
      ('What\'s the matter?', '怎麼了？', 'What\'s the matter with you?'),
      ('stay in shape', '保持身材', 'She swims to stay in shape.'),
      ('throw away', '丟掉', 'Don\'t throw away the box.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'I can\'t <b>stand</b> the noise next door.', 'opts': ['站立', '忍受', '攤位', '代表'], 'answer': 1, 'exp': 'can\'t stand 受不了。'},
    {'type': 'mc', 'q': 'I don\'t have any coins, only a 100-dollar <b>bill</b>.', 'opts': ['帳單', '紙鈔', '法案', '鳥嘴'], 'answer': 1, 'exp': '沒有硬幣，只有一張百元 → 紙鈔。'},
    {'type': 'mc', 'q': 'My phone is <b>dead</b>. I forgot to charge it.', 'opts': ['死的', '沒電的', '冷清的', '舊的'], 'answer': 1, 'exp': '忘了充電 → 沒電。'},
    {'type': 'mc', 'q': 'We went to the Taipei Game Show and the book <b>fair</b>.', 'opts': ['公平的', '合理的', '白皙的', '展覽'], 'answer': 3, 'exp': 'book fair 書展。'},
    {'type': 'mc', 'q': 'The theater can <b>hold</b> 300 people.', 'opts': ['拿著', '舉辦', '容納', '等待'], 'answer': 2, 'exp': 'hold 人數 → 容納。'},
    {'type': 'mc', 'q': 'Wow, you <b>nailed</b> the speech!', 'opts': ['指甲', '釘子', '釘牢', '做得很好'], 'answer': 3, 'exp': 'nail it 做得很好。'},
    {'type': 'mc', 'q': 'What\'s the <b>point</b> of buying a car if you can\'t drive?', 'opts': ['分數', '小數點', '意義；目的', '指著'], 'answer': 2, 'exp': 'What\'s the point of…? …有什麼用？'},
    {'type': 'mc', 'q': 'Grandpa walks every day to stay in <b>shape</b>.', 'opts': ['形狀', '健康狀態', '塑形', '決定'], 'answer': 1, 'exp': 'stay in shape 保持健康。'},
    {'type': 'mc', 'q': 'The student <b>passed</b> the exam with high marks.', 'opts': ['經過', '傳遞', '度過', '通過'], 'answer': 3, 'exp': 'pass the exam 考試通過。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'I\'m ______. I can\'t eat any more.  ／  The box is ______ of books.', 'opts': ['busy', 'full', 'empty', 'tired'], 'answer': 1, 'exp': 'full 飽的／充滿。'},
    {'type': 'mc', 'q': 'Wear a coat, or you\'ll catch a ______.  ／  She was ______ to me and didn\'t say hi.', 'opts': ['cold', 'fever', 'hot', 'rude'], 'answer': 0, 'exp': 'cold 感冒／冷淡的。'},
    {'type': 'mc', 'q': 'She ______ed the world record.  ／  Let\'s ______ a video for Grandma.', 'opts': ['break', 'hold', 'record', 'make'], 'answer': 2, 'exp': 'record（名詞）紀錄／錄製。'},
    {'type': 'mc', 'q': '______ the right answer with a red pen.  ／  The students sat in a ______.', 'opts': ['Circle', 'Mark', 'Line', 'Point'], 'answer': 0, 'exp': 'circle 圈起來／圓圈。'},
    {'type': 'mc', 'q': 'Please ______ me for a moment.  ／  Don\'t make ______s. Just do it.', 'opts': ['forgive', 'excuse', 'reason', 'sorry'], 'answer': 1, 'exp': 'excuse 原諒／藉口。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Please take {0} of yourself. （照顧）', 'blanks': [['care']], 'exp': 'take care of 照顧。'},
    {'q': 'You can always count {0} me. （依靠）', 'blanks': [['on']], 'exp': 'count on 依靠。'},
    {'q': 'Hold {0}. I\'ll be right back. （等一下）', 'blanks': [['on']], 'exp': 'hold on 等一下。'},
    {'q': 'What\'s the {0} with your leg? （怎麼了）', 'blanks': [['matter']], 'exp': 'What\'s the matter with…? …怎麼了？'},
    {'q': 'Don\'t throw {0} the bottles. Recycle them. （丟掉）', 'blanks': [['away']], 'exp': 'throw away 丟掉。'},
    {'q': 'Please {0} the button for the 5th floor. （按）', 'blanks': [['push']], 'exp': 'push the button 按按鈕。'},
  ]},
]
