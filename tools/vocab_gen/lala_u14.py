# LaLa Word Unit 14（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 155–164 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 14, 'en': 'Getting Lazy with Technology', 'zh': '一字多義（十四）',
  'intro': 'button 是按鈕，也是「鈕扣」；key 是鑰匙，也是「關鍵」。這個單元有 5 個主題單字、14 個更多單字，'
           '再整理 cross／across，和都是「帶」的 take／bring／carry。',
  'words': [
    W('button', '🔘', [
        S('n.', '按鈕', 'Press the red button to start.', '按紅色按鈕開始。', 'press / push the button 按按鈕'),
        S('n.', '鈕扣', 'A button fell off my shirt.', '我襯衫掉了一顆扣子。', 'do up / undo the buttons 扣上／解開扣子'),
        S('v.', '扣上（鈕扣）', 'Button up your coat. It\'s windy.', '把外套扣好，風很大。', 'button up 扣好'),
    ], 'button - buttoned - buttoned - buttoning', key=True),
    W('note', '🗒️', [
        S('n.', '筆記', 'Take notes during the class.', '上課時要做筆記。', 'take notes 做筆記'),
        S('n.', '便條', 'Mom left a note on the fridge.', '媽媽在冰箱上留了一張便條。', 'leave a note 留便條'),
        S('n.', '音符；語氣', 'She can sing very high notes.', '她能唱很高的音。'),
        S('v.', '記下；注意', 'Please note down my phone number.', '請把我的電話記下來。', 'note down 記下'),
    ], 'note - noted - noted - noting', key=True),
    W('type', '⌨️', [
        S('v.', '打字', 'My sister can type very fast.', '我姊姊打字很快。'),
        S('n.', '類型', 'What type of movies do you like?', '你喜歡哪一類的電影？', 'blood type 血型'),
        S('n.', '字型；字體', 'The type on this sign is too small.', '這個牌子上的字太小了。'),
    ], 'type - typed - typed - typing', key=True),
    W('screen', '📱', [
        S('n.', '螢幕', 'Don\'t look at the screen too long.', '不要盯著螢幕太久。', 'screen time 使用螢幕的時間；touch screen 觸控螢幕'),
        S('v.', '放映；播出', 'The movie will be screened next week.', '這部電影下星期上映。'),
        S('v.', '篩選；檢查', 'All bags are screened at the airport.', '機場會檢查所有行李。'),
    ], 'screen - screened - screened - screening', key=True),
    W('seed', '🌻', [
        S('n.', '種子', 'Plant the seeds in the spring.', '春天把種子種下去。', 'plant a seed 播種'),
        S('v.', '播種', 'The farmer seeded the field with corn.', '農夫在田裡播了玉米種子。'),
        S('v.', '去籽', 'Seed the peppers before you cook them.', '煮之前先把辣椒去籽。'),
    ], 'seed - seeded - seeded - seeding', key=True),
    W('area', '🗺️', [
        S('n.', '地區；區域', 'There are many parks in this area.', '這個地區有很多公園。', 'area code 區碼'),
        S('n.', '領域；方面', 'Math is her best area.', '數學是她最強的領域。'),
        S('n.', '面積', 'What is the area of this room?', '這個房間的面積是多少？'),
    ], '複數 areas'),
    W('drop', '💧', [
        S('v.', '掉落', 'I dropped my phone on the floor.', '我的手機掉到地上。'),
        S('v.', '下降', 'The temperature dropped to 12°C.', '氣溫降到十二度。'),
        S('v.', '放棄；停止', 'Let\'s drop the subject.', '我們別再談這件事了。', 'drop out 中途退出'),
        S('n.', '一滴；少量', 'Just a drop of milk, please.', '請加一點點牛奶就好。', 'eye drops 眼藥水'),
    ], 'drop - dropped - dropped - dropping'),
    W('gate', '🚪', [
        S('n.', '大門', 'Let\'s meet at the school gate.', '我們在校門口碰面吧。'),
        S('n.', '登機門', 'Our flight leaves from Gate 12.', '我們的班機從十二號登機門出發。'),
    ], '複數 gates'),
    W('glue', '🧴', [
        S('n.', '膠水', 'I need some glue for my art project.', '我的美勞作業需要膠水。'),
        S('v.', '用膠黏', 'Glue the picture onto the card.', '把圖片黏到卡片上。'),
        S('v.', '盯著（be glued to）', 'He was glued to the TV all night.', '他整晚盯著電視看。', 'be glued to 全神貫注盯著'),
    ], 'glue - glued - glued - gluing'),
    W('honey', '🍯', [
        S('n.', '蜂蜜', 'I put some honey in my tea.', '我在茶裡加了一些蜂蜜。'),
        S('n.', '親愛的', 'Honey, dinner is ready.', '親愛的，晚餐好了。'),
    ]),
    W('key', '🔑', [
        S('n.', '鑰匙', 'I can\'t find my keys.', '我找不到我的鑰匙。', 'key chain 鑰匙圈'),
        S('n.', '關鍵', 'Practice is the key to success.', '練習是成功的關鍵。', 'the key to …的關鍵；key word 關鍵字'),
        S('n.', '音調', 'This song is in a high key.', '這首歌的調很高。'),
        S('v.', '用鍵盤輸入', 'Key in your password.', '輸入你的密碼。', 'key in 輸入'),
    ], 'key - keyed - keyed - keying'),
    W('land', '🛬', [
        S('n.', '陸地；土地', 'The sailors were happy to see land.', '水手們很高興看到陸地。'),
        S('n.', '國家；國度', 'Taiwan is a land of beautiful mountains.', '臺灣是一片山景美麗的土地。'),
        S('v.', '著陸；降落', 'The plane will land in ten minutes.', '飛機十分鐘後降落。'),
        S('v.', '得到；贏得', 'She landed a part in the school play.', '她在學校話劇中拿到了一個角色。'),
    ], 'land - landed - landed - landing'),
    W('list', '📝', [
        S('v.', '列出', 'List three things you are thankful for.', '列出三件你感謝的事。'),
        S('n.', '名單；清單', 'I made a shopping list.', '我寫了一張購物清單。', 'to-do list 待辦清單'),
    ], 'list - listed - listed - listing'),
    W('pack', '🎒', [
        S('v.', '打包；收拾行李', 'Pack your bag tonight.', '今晚把包包整理好。', 'pack up 收拾好'),
        S('v.', '擠滿', 'The MRT was packed with people.', '捷運擠滿了人。', 'be packed with 擠滿'),
        S('n.', '一包；一副', 'I bought a pack of gum.', '我買了一包口香糖。', 'a pack of cards 一副撲克牌'),
        S('n.', '一群（動物）', 'A pack of dogs ran down the street.', '一群狗沿著街跑過去。'),
    ], 'pack - packed - packed - packing'),
    W('paste', '📋', [
        S('v.', '貼上', 'Paste the picture in your notebook.', '把圖片貼在你的筆記本上。'),
        S('v.', '（電腦）貼上', 'Copy the link and paste it here.', '把連結複製貼到這裡。', 'copy and paste 複製貼上'),
        S('n.', '漿糊；糊狀物', 'Squeeze some toothpaste onto your brush.', '在牙刷上擠一點牙膏。', 'toothpaste 牙膏'),
    ], 'paste - pasted - pasted - pasting'),
    W('pipe', '🪈', [
        S('n.', '管子', 'Water is coming out of the broken pipe.', '水從破掉的管子流出來。'),
        S('n.', '菸斗', 'The old sailor smoked a pipe.', '那位老水手抽菸斗。'),
    ], '複數 pipes'),
    W('pot', '🪴', [
        S('n.', '鍋；壺；罐', 'Mom is cooking soup in a big pot.', '媽媽用大鍋煮湯。', 'hot pot 火鍋；teapot 茶壺'),
        S('v.', '把…種在盆裡', 'Let\'s pot these little plants.', '我們把這些小植物種進盆裡吧。'),
    ], 'pot - potted - potted - potting'),
    W('program', '💻', [
        S('n.', '電腦程式', 'Download this program to edit photos.', '下載這個程式來修圖。'),
        S('n.', '節目', 'My favorite TV program is on at eight.', '我最喜歡的電視節目八點播出。'),
        S('n.', '計畫；課程', 'Our school has an exchange program.', '我們學校有交換學生計畫。'),
        S('v.', '寫程式；設定', 'He programmed the robot to dance.', '他寫程式讓機器人跳舞。'),
    ], 'program - programmed - programmed - programming'),
    W('swing', '🛝', [
        S('v.', '擺動；盪', 'The kids are swinging in the park.', '孩子們在公園盪鞦韆。', 'swing by 順道去'),
        S('v.', '揮動', 'Swing the bat hard!', '用力揮棒！'),
        S('v.', '（心情）轉變', 'Her mood swings from happy to sad quickly.', '她的心情很快就從開心變難過。'),
        S('n.', '變化', 'There was a big swing in temperature today.', '今天溫差很大。'),
        S('n.', '鞦韆', 'Let\'s take turns on the swing.', '我們輪流盪鞦韆吧。'),
    ], 'swing - swung - swung - swinging'),
  ],
  'focus': [
    {'title': '易混淆字：cross 和 across', 'head': ('單字', '用法', '例句'), 'rows': [
      ('cross', '（動詞）穿越；橫越；交叉', 'Look both ways before you cross the street.'),
      ('across', '（介系詞、副詞）在…的對面；橫越', 'The bank is across from the school.／We walked across the bridge.'),
    ], 'note': 'cross 是動作本身；across 要配動詞（walk across、swim across）。'},
    {'title': '易混淆字：take／bring／carry', 'head': ('單字', '用法', '例句'), 'rows': [
      ('take', '帶去：從說話者這裡帶到別的地方', 'Take an umbrella with you.'),
      ('bring', '帶來：帶到說話者這裡', 'Bring your homework tomorrow.'),
      ('carry', '搬、提、背：強調「拿著移動」的動作', 'He carried the heavy box upstairs.'),
    ], 'note': ''},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('button', '按鈕', '鈕扣'),
      ('note', '筆記', '便條；音符'),
      ('screen', '螢幕', '放映；檢查'),
      ('key', '鑰匙', '關鍵；音調'),
      ('land', '陸地', '降落；得到'),
      ('pack', '打包', '一包；一群'),
      ('honey', '蜂蜜', '親愛的'),
      ('swing', '擺動', '鞦韆'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'Can you help me sew this <b>button</b> back on?', 'opts': ['按鈕', '鈕扣', '口袋', '拉鍊'], 'answer': 1, 'exp': '縫回去的 → 鈕扣。'},
    {'type': 'mc', 'q': 'The piano player hit a wrong <b>note</b>.', 'opts': ['筆記', '便條', '音符', '鈔票'], 'answer': 2, 'exp': '彈錯音 → 音符。'},
    {'type': 'mc', 'q': 'My blood <b>type</b> is O.', 'opts': ['打字', '類型', '字體', '號碼'], 'answer': 1, 'exp': 'blood type 血型。'},
    {'type': 'mc', 'q': 'All passengers must be <b>screened</b> before boarding.', 'opts': ['螢幕', '放映', '檢查', '拍照'], 'answer': 2, 'exp': '登機前要接受安全檢查。'},
    {'type': 'mc', 'q': 'Hard work is the <b>key</b> to winning.', 'opts': ['鑰匙', '關鍵', '音調', '輸入'], 'answer': 1, 'exp': 'the key to …的關鍵。'},
    {'type': 'mc', 'q': 'Our plane <b>landed</b> at Taoyuan Airport at 9 p.m.', 'opts': ['陸地', '國家', '降落', '得到'], 'answer': 2, 'exp': '飛機 land → 降落。'},
    {'type': 'mc', 'q': 'The night market is <b>packed</b> with people on weekends.', 'opts': ['打包', '擠滿', '一包', '一群'], 'answer': 1, 'exp': 'be packed with 擠滿。'},
    {'type': 'mc', 'q': '<b>Honey</b>, can you pass me the salt?', 'opts': ['蜂蜜', '親愛的', '蜜蜂', '甜點'], 'answer': 1, 'exp': '叫人 → 親愛的。'},
    {'type': 'mc', 'q': 'The kids were <b>glued</b> to the cartoon.', 'opts': ['黏在…上', '盯著看', '睡著', '討厭'], 'answer': 1, 'exp': 'be glued to 全神貫注盯著。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'I need two ______s of eye medicine.  ／  Don\'t ______ the glass!', 'opts': ['drop', 'bottle', 'break', 'cup'], 'answer': 0, 'exp': 'drop 一滴／掉落。'},
    {'type': 'mc', 'q': 'Our flight leaves from ______ 7.  ／  Let\'s meet at the school ______.', 'opts': ['door', 'gate', 'station', 'stop'], 'answer': 1, 'exp': 'gate 登機門／大門。'},
    {'type': 'mc', 'q': 'Grandpa cooked hot ______ for us.  ／  Put the flower in a ______.', 'opts': ['pan', 'pot', 'bowl', 'vase'], 'answer': 1, 'exp': 'pot 火鍋／盆。'},
    {'type': 'mc', 'q': 'I watched a funny TV ______.  ／  She wrote a computer ______.', 'opts': ['show', 'program', 'game', 'file'], 'answer': 1, 'exp': 'program 節目／程式。'},
    {'type': 'mc', 'q': 'Let\'s play on the ______ in the park.  ／  ______ the bat as hard as you can.', 'opts': ['slide', 'swing', 'Hit', 'Throw'], 'answer': 1, 'exp': 'swing 鞦韆／揮動。'},
  ]},
  {'title': '③ 易混淆字：選出正確的字', 'items': [
    {'type': 'mc', 'q': 'Be careful when you ______ the road.', 'opts': ['across', 'cross', 'crossing', 'through'], 'answer': 1, 'exp': '動詞 → cross。'},
    {'type': 'mc', 'q': 'The post office is ______ from the park.', 'opts': ['cross', 'across', 'crossed', 'over'], 'answer': 1, 'exp': 'across from 在…對面。'},
    {'type': 'mc', 'q': 'Please ______ your lunch box when you come to school tomorrow.', 'opts': ['take', 'bring', 'carry', 'took'], 'answer': 1, 'exp': '帶來（說話者這裡）→ bring。'},
    {'type': 'mc', 'q': '______ this letter to the office, please.', 'opts': ['Bring', 'Take', 'Come', 'Go'], 'answer': 1, 'exp': '帶去別的地方 → take。'},
    {'type': 'mc', 'q': 'He ______ his little sister on his back.', 'opts': ['brought', 'took', 'carried', 'crossed'], 'answer': 2, 'exp': '背著 → carry。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Take {0} when the teacher talks. （筆記）', 'blanks': [['notes']], 'exp': 'take notes 做筆記。'},
    {'q': 'Kids should have less {0} time. （螢幕）', 'blanks': [['screen']], 'exp': 'screen time 使用螢幕的時間。'},
    {'q': 'Water the {0}s every day, and they will grow. （種子）', 'blanks': [['seed']], 'exp': 'seed 種子。'},
    {'q': 'Write down everything on your to-do {0}. （清單）', 'blanks': [['list']], 'exp': 'to-do list 待辦清單。'},
    {'q': 'Copy the sentence and {0} it into the box. （貼上）', 'blanks': [['paste']], 'exp': 'copy and paste 複製貼上。'},
    {'q': 'What is the {0} of this square? （面積）', 'blanks': [['area']], 'exp': 'area 面積。'},
  ]},
]
