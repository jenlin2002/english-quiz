# LaLa Word Unit 9（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 96–107 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 9, 'en': 'A New Way to Get Food Fast', 'zh': '一字多義（九）',
  'intro': 'fly 是飛，也是「蒼蠅」；bank 是銀行，也是「河岸」。這個單元有 8 個主題單字、15 個更多單字，'
           '再整理 sell／sale，和都跟「花費」有關的 cost／spend／take／pay。',
  'words': [
    W('fly', '🪁', [
        S('v.', '飛；放（風箏）', 'Let\'s fly a kite in the park.', '我們去公園放風箏吧。', 'fly a kite 放風箏'),
        S('v.', '搭飛機；開飛機', 'We flew to Japan last summer.', '我們去年夏天搭飛機去日本。'),
        S('v.', '（時間）飛逝', 'Time flies!', '時間過得真快！'),
        S('n.', '蒼蠅', 'There is a fly on my cake!', '我的蛋糕上有一隻蒼蠅！'),
    ], 'fly - flew - flown - flying；複數 flies', key=True),
    W('straight', '📏', [
        S('adv.', '直接地；立刻', 'Go straight home after school.', '放學後直接回家。'),
        S('adv.', '連續地', 'It rained for five days straight.', '雨連續下了五天。'),
        S('adv.', '清楚地', 'I\'m so sleepy that I can\'t think straight.', '我睏到沒辦法好好思考。'),
        S('adv.', '挺直地', 'Sit up straight, please.', '請坐直。'),
        S('adj.', '直的', 'She has long straight hair.', '她有一頭長直髮。'),
        S('adj.', '誠實的；坦白的', 'Please give me a straight answer.', '請坦白回答我。'),
    ], 'straight - straighter - straightest', key=True),
    W('cut', '✂️', [
        S('v.', '減少', 'You should cut down on sweets.', '你應該少吃甜食。', 'cut down on 減少'),
        S('v.', '切；剪', 'Cut the apple into four pieces.', '把蘋果切成四塊。'),
        S('v.', '插嘴；插隊', 'Don\'t cut in line!', '不要插隊！', 'cut in line 插隊'),
        S('n.', '傷口', 'I got a cut on my finger.', '我的手指割傷了。'),
        S('n.', '剪髮；剪裁', 'I like your new cut!', '我喜歡你的新髮型！'),
    ], 'cut - cut - cut - cutting', key=True),
    W('ship', '🚢', [
        S('v.', '運送', 'The shop ships books all over Taiwan.', '這家店把書寄送到全臺灣。'),
        S('n.', '大船', 'The ship sailed across the ocean.', '那艘船橫渡大海。', 'by ship 搭船'),
    ], 'ship - shipped - shipped - shipping', key=True),
    W('cost', '💰', [
        S('n.', '成本；費用', 'The cost of food is going up.', '食物的成本在上漲。'),
        S('n.', '代價', 'He wanted to win at all costs.', '他不惜一切代價想要贏。', 'at all costs 不惜任何代價'),
        S('v.', '花費（金錢）', 'This shirt cost me 500 dollars.', '這件襯衫花了我五百元。', 'cost an arm and a leg 非常貴'),
        S('v.', '使喪失', 'One mistake cost us the game.', '一個失誤讓我們輸了比賽。'),
    ], 'cost - cost - cost - costing', key=True),
    W('price', '🏷️', [
        S('n.', '價格', 'The price of this bag is too high.', '這個包包的價格太高了。'),
        S('n.', '代價', 'He paid a high price for his mistake.', '他為自己的錯付出很大的代價。', 'pay a high price 付出很大代價'),
        S('v.', '給…定價', 'The new phone is priced at 30,000 dollars.', '新手機定價三萬元。'),
    ], 'price - priced - priced - pricing', key=True),
    W('block', '🧊', [
        S('v.', '擋住；堵塞', 'A big truck is blocking the road.', '一輛大卡車擋住了路。', 'block one\'s view 擋住視線'),
        S('n.', '阻擋', 'He made a great block in the game.', '他在比賽中做了一個漂亮的阻擋。'),
        S('n.', '街區', 'The bookstore is two blocks away.', '書店離這裡兩個街區。'),
        S('n.', '塊；積木', 'The kids built a tower with blocks.', '孩子們用積木蓋了一座塔。', 'a block of ice 一塊冰'),
    ], 'block - blocked - blocked - blocking', key=True),
    W('will', '📜', [
        S('aux.', '將要（未來式）', 'It will rain tomorrow.', '明天會下雨。'),
        S('aux.', '願意', 'Will you help me?', '你願意幫我嗎？'),
        S('n.', '意志', 'She has a strong will.', '她的意志很堅強。'),
        S('n.', '遺囑', 'The old man left his house to his son in his will.', '那位老人在遺囑中把房子留給兒子。'),
    ], key=True),
    W('along', '🏖️', [
        S('prep.', '沿著', 'We walked along the river.', '我們沿著河邊散步。'),
        S('adv.', '一起', 'Can I bring my sister along?', '我可以帶我妹妹一起去嗎？', 'bring… along 帶…一起；come along 一起來；get along 相處融洽'),
    ]),
    W('ask', '🙋', [
        S('v.', '問', 'Can I ask you a question?', '我可以問你一個問題嗎？'),
        S('v.', '要求；請求', 'Mom asked me to clean my room.', '媽媽要我整理房間。', 'ask + 人 + to V 要求某人做；ask for 要求；ask for help 求助'),
    ], 'ask - asked - asked - asking'),
    W('bank', '🏦', [
        S('n.', '銀行', 'Dad went to the bank to get some money.', '爸爸去銀行領錢。'),
        S('n.', '河岸', 'We had a picnic on the river bank.', '我們在河岸邊野餐。'),
    ], '複數 banks'),
    W('bike', '🚲', [
        S('n.', '腳踏車', 'I ride my bike to school.', '我騎腳踏車上學。'),
        S('v.', '騎腳踏車', 'We biked along the beach.', '我們沿著海邊騎腳踏車。'),
    ], 'bike - biked - biked - biking'),
    W('coat', '🧥', [
        S('n.', '大衣；外套', 'Put on your coat. It\'s cold outside.', '穿上外套，外面很冷。', 'raincoat 雨衣'),
        S('n.', '（動物的）毛', 'The dog has a soft white coat.', '這隻狗有一身柔軟的白毛。'),
        S('v.', '覆蓋；裹上', 'The cake is coated with chocolate.', '這個蛋糕外面裹了一層巧克力。'),
    ], 'coat - coated - coated - coating'),
    W('dress', '👗', [
        S('n.', '洋裝', 'She wore a pink dress to the party.', '她穿粉紅色洋裝去參加派對。'),
        S('n.', '服裝', 'Is there a dress code for the party?', '這個派對有服裝規定嗎？', 'dress code 服裝規定'),
        S('v.', '穿衣服', 'Get dressed quickly. We\'re late!', '快穿好衣服，我們遲到了！', 'get dressed 穿好衣服'),
        S('v.', '打扮', 'He dressed up as a pirate for Halloween.', '他萬聖節打扮成海盜。', 'dress up as 打扮成'),
        S('v.', '（給沙拉）調味', 'Dress the salad with some olive oil.', '用一點橄欖油拌沙拉。'),
    ], 'dress - dressed - dressed - dressing'),
    W('fast', '⚡', [
        S('adj.', '快的', 'A cheetah is a very fast animal.', '獵豹是跑得非常快的動物。'),
        S('adv.', '快速地', 'Don\'t eat so fast.', '別吃那麼快。'),
        S('adv.', '牢牢地', 'The baby is fast asleep.', '寶寶睡得很熟。', 'fast asleep 熟睡'),
        S('v.', '禁食', 'You need to fast before the blood test.', '抽血檢查前你需要禁食。'),
    ], 'fast - faster - fastest；fast - fasted - fasted - fasting'),
    W('foot', '🦶', [
        S('n.', '腳', 'I hurt my foot when I played soccer.', '我踢足球時傷了腳。', 'on foot 走路；get cold feet 臨陣退縮'),
        S('n.', '英尺', 'The tree is twenty feet tall.', '這棵樹有二十英尺高。'),
    ], '複數 feet'),
    W('ground', '⚽', [
        S('n.', '地面', 'The apple fell to the ground.', '蘋果掉到地上。'),
        S('n.', '土地；土壤', 'The ground is too dry for plants.', '土地太乾，植物長不了。'),
        S('n.', '（特殊用途的）場地', 'The kids are on the playground.', '孩子們在遊樂場。', 'playground 操場；遊樂場'),
        S('v.', '禁止外出；停飛', 'My parents grounded me for a week.', '我爸媽罰我一個星期不准出門。'),
    ], 'ground - grounded - grounded - grounding'),
    W('hit', '🎵', [
        S('v.', '打；撞', 'He hit the ball very hard.', '他用力打球。'),
        S('v.', '襲擊（災害）', 'A typhoon hit Taiwan last week.', '上週颱風侵襲臺灣。'),
        S('n.', '暢銷作品；熱門歌曲', 'This song is a big hit.', '這首歌非常紅。'),
        S('n.', '點擊數', 'The video got a million hits.', '這支影片有一百萬次點擊。'),
    ], 'hit - hit - hit - hitting'),
    W('hurt', '🩹', [
        S('v.', '傷害', 'I hurt my arm when I fell.', '我跌倒時傷了手臂。'),
        S('v.', '痛', 'My head hurts.', '我頭痛。'),
        S('adj.', '受傷的', 'Two people got hurt in the accident.', '這起意外有兩人受傷。', 'get hurt 受傷'),
    ], 'hurt - hurt - hurt - hurting'),
    W('pair', '🧤', [
        S('n.', '一對；一雙', 'I need a new pair of shoes.', '我需要一雙新鞋。', 'a pair of 一雙；一副'),
        S('n.', '一組；兩人一組', 'Work in pairs, please.', '請兩人一組。', 'in pairs 兩人一組'),
        S('v.', '搭配', 'Pair the cheese with some fruit.', '起司配一點水果。'),
    ], 'pair - paired - paired - pairing'),
    W('pay', '💳', [
        S('v.', '付錢', 'Can I pay by credit card?', '我可以刷卡嗎？', 'pay for 付…的錢；pay in cash 付現'),
        S('v.', '注意（pay attention）', 'Pay attention to the teacher.', '注意聽老師說話。', 'pay attention to 注意'),
        S('v.', '償還（pay back）', 'I\'ll pay you back tomorrow.', '我明天還你錢。', 'pay back 還錢'),
        S('n.', '薪水', 'The job is hard, but the pay is good.', '這份工作很辛苦，但薪水不錯。'),
    ], 'pay - paid - paid - paying'),
    W('surf', '🏄', [
        S('v.', '衝浪', 'We went surfing in Yilan.', '我們去宜蘭衝浪。'),
        S('v.', '（在網路上）瀏覽', 'He surfs the internet for hours.', '他上網好幾個小時。', 'surf the internet 上網'),
        S('n.', '海浪；浪花', 'The surf is big today.', '今天浪很大。'),
    ], 'surf - surfed - surfed - surfing'),
    W('tie', '👔', [
        S('v.', '綁；打結', 'Can you tie your shoes?', '你會綁鞋帶嗎？'),
        S('n.', '領帶', 'Dad wears a tie to work.', '爸爸打領帶去上班。'),
        S('n.', '關聯', 'There is a close tie between sleep and health.', '睡眠和健康有密切的關係。'),
        S('n.', '平手', 'The game ended in a tie.', '比賽以平手結束。'),
    ], 'tie - tied - tied - tying'),
  ],
  'focus': [
    {'title': '易混淆字：sell 和 sale', 'head': ('單字', '用法', '例句'), 'rows': [
      ('sell', '（動詞）賣：sell - sold - sold', 'They sell fresh fruit here.'),
      ('sale', '（名詞）出售；拍賣：on sale 特價；for sale 出售中', 'These shoes are on sale.'),
    ], 'note': ''},
    {'title': '易混淆字：cost／spend／take／pay', 'head': ('單字', '句型', '例句'), 'rows': [
      ('cost', '「東西」當主詞：物 + cost + 人 + 錢', 'The book cost me 300 dollars.'),
      ('spend', '「人」當主詞：人 + spend + 錢／時間 + on 物／V-ing', 'I spent two hours doing homework.'),
      ('take', '「事情」花時間：It takes + 人 + 時間 + to V', 'It takes me 20 minutes to walk to school.'),
      ('pay', '「人」付錢：人 + pay + 錢 + for 物', 'She paid 50 dollars for the cake.'),
    ], 'note': '問價錢：How much does it cost?；問時間：How long does it take?'},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('fly', '飛', '蒼蠅'),
      ('bank', '銀行', '河岸'),
      ('will', '將要', '意志；遺囑'),
      ('block', '擋住', '街區；積木'),
      ('coat', '外套', '動物的毛；裹上'),
      ('fast', '快的', '禁食；fast asleep 熟睡'),
      ('foot', '腳', '英尺'),
      ('ground', '地面', '禁足；停飛'),
      ('hit', '打', '熱門歌曲'),
      ('tie', '領帶', '平手'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'Close the door, or the <b>flies</b> will come in.', 'opts': ['飛', '蒼蠅', '飛機', '風箏'], 'answer': 1, 'exp': 'flies 蒼蠅（複數）。'},
    {'type': 'mc', 'q': 'The library is three <b>blocks</b> from here.', 'opts': ['積木', '阻擋', '街區', '冰塊'], 'answer': 2, 'exp': 'three blocks 三個街區。'},
    {'type': 'mc', 'q': 'The ducks are resting on the river <b>bank</b>.', 'opts': ['銀行', '河岸', '橋', '小島'], 'answer': 1, 'exp': 'river bank 河岸。'},
    {'type': 'mc', 'q': 'The game ended in a <b>tie</b>, 2 to 2.', 'opts': ['領帶', '綁', '關聯', '平手'], 'answer': 3, 'exp': '二比二 → 平手。'},
    {'type': 'mc', 'q': 'Her new song is a big <b>hit</b>.', 'opts': ['打擊', '撞', '熱門作品', '侵襲'], 'answer': 2, 'exp': 'a big hit 很紅的作品。'},
    {'type': 'mc', 'q': 'Tom was <b>grounded</b> for coming home late.', 'opts': ['坐在地上', '被禁足', '停飛', '種田'], 'answer': 1, 'exp': '晚回家被禁足。'},
    {'type': 'mc', 'q': 'My cat has a beautiful black <b>coat</b>.', 'opts': ['外套', '毛', '雨衣', '尾巴'], 'answer': 1, 'exp': '動物的 coat 是毛。'},
    {'type': 'mc', 'q': 'The baby is <b>fast</b> asleep.', 'opts': ['快速地', '熟熟地', '禁食', '早早地'], 'answer': 1, 'exp': 'fast asleep 熟睡。'},
    {'type': 'mc', 'q': 'The old man has a strong <b>will</b> to live.', 'opts': ['將要', '願意', '意志', '遺囑'], 'answer': 2, 'exp': 'strong will 堅強的意志。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'I ______ my finger with a knife.  ／  Please don\'t ______ in line.', 'opts': ['hurt', 'cut', 'hit', 'cross'], 'answer': 1, 'exp': 'cut 割傷／插隊。'},
    {'type': 'mc', 'q': 'Go ______ and turn left.  ／  She has long ______ hair.', 'opts': ['right', 'straight', 'curly', 'ahead'], 'answer': 1, 'exp': 'straight 直走／直的。'},
    {'type': 'mc', 'q': 'The ______ of the bike is 3,000 dollars.  ／  He paid a high ______ for being lazy.', 'opts': ['cost', 'price', 'money', 'pay'], 'answer': 1, 'exp': 'price 價格／代價。'},
    {'type': 'mc', 'q': 'He wore a black suit and a red ______.  ／  Can you help me ______ my shoes?', 'opts': ['tie', 'hat', 'band', 'belt'], 'answer': 0, 'exp': 'tie 領帶／綁。'},
    {'type': 'mc', 'q': 'I like to ______ the internet after dinner.  ／  Let\'s go ______ing at the beach.', 'opts': ['swim', 'surf', 'run', 'search'], 'answer': 1, 'exp': 'surf 上網／衝浪。'},
  ]},
  {'title': '③ 易混淆字：選出正確的字', 'items': [
    {'type': 'mc', 'q': 'These jackets are on ______. They\'re 50% off.', 'opts': ['sell', 'sale', 'sold', 'sells'], 'answer': 1, 'exp': 'on sale 特價。'},
    {'type': 'mc', 'q': 'The old man ______ his car last month.', 'opts': ['sale', 'sold', 'sell', 'sales'], 'answer': 1, 'exp': 'sell 的過去式 sold。'},
    {'type': 'mc', 'q': 'How much did the shoes ______ you?', 'opts': ['spend', 'pay', 'cost', 'take'], 'answer': 2, 'exp': '物 + cost + 人。'},
    {'type': 'mc', 'q': 'I ______ two hours playing games yesterday.', 'opts': ['spent', 'cost', 'took', 'paid'], 'answer': 0, 'exp': '人 + spend + 時間 + V-ing。'},
    {'type': 'mc', 'q': 'It ______ me ten minutes to walk to the station.', 'opts': ['spends', 'costs', 'takes', 'pays'], 'answer': 2, 'exp': 'It takes + 人 + 時間 + to V。'},
    {'type': 'mc', 'q': 'Mom ______ 200 dollars for the cake.', 'opts': ['spent on', 'cost', 'took', 'paid'], 'answer': 3, 'exp': '人 + pay + 錢 + for 物。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Doctors say I should cut {0} on sugar. （減少）', 'blanks': [['down']], 'exp': 'cut down on 減少。'},
    {'q': 'Do you get {0} with your classmates? （相處融洽）', 'blanks': [['along']], 'exp': 'get along with 和…相處融洽。'},
    {'q': 'If you need help, just ask {0} it. （要求）', 'blanks': [['for']], 'exp': 'ask for 要求。'},
    {'q': 'Please pay {0} to the safety rules. （注意）', 'blanks': [['attention']], 'exp': 'pay attention to 注意。'},
    {'q': 'I usually go to school on {0}. （步行）', 'blanks': [['foot']], 'exp': 'on foot 走路。'},
    {'q': 'Ben fell off his bike and got {0}. （受傷的）', 'blanks': [['hurt']], 'exp': 'get hurt 受傷。'},
  ]},
]
