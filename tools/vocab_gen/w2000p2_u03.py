# 主題 2000 字 PART 2 Unit 3：Parts of body 身體部位（字表依課本 PART 2 印刷頁 146–147，10 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 3, 'en': 'Parts of body', 'zh': '身體部位',
  'intro': '進階的身體部位，共 10 個：鬍子、下巴、舌頭、腳踝、骨頭、臀部、皮膚、拇指、腰、手腕。',
  'words': [
    W('beard', 'n.', '鬍鬚；山羊鬍', '下巴的鬍子；嘴上的叫 mustache', 'Santa Claus has a long white beard.', '聖誕老公公有長長的白鬍子。', '🧔'),
    W('chin', 'n.', '下巴', 'Keep your chin up! 別灰心！', 'He rested his chin on his hand and thought.', '他用手托著下巴思考。', '🤔'),
    W('tongue', 'n.', '舌頭；語言', 'mother tongue 母語', 'The dog stuck out its tongue on the hot day.', '大熱天那隻狗吐著舌頭。', '👅'),
    W('ankle', 'n.', '腳踝', 'twist my ankle 扭到腳踝', 'I twisted my ankle in P.E. class.', '我在體育課扭到腳踝。', '🦶'),
    W('bone', 'n.', '骨頭', 'lazybones 懶骨頭（懶人）', 'The dog is hiding a bone in the yard.', '那隻狗把骨頭藏在院子裡。', '🦴'),
    W('hip', 'n.', '臀部；屁股（髖部）', 'with hands on hips 雙手叉腰', 'She stood with her hands on her hips.', '她雙手叉腰站著。', '🧍'),
    W('skin', 'n.', '皮膚；（水果的）皮', 'banana skin 香蕉皮', 'Use sunscreen to protect your skin.', '擦防曬乳保護你的皮膚。', '🧴'),
    W('thumb', 'n.', '拇指', 'thumbs up 比讚（b 不發音）', 'He gave me a thumbs up after my speech.', '我演講完，他對我比讚。', '👍'),
    W('waist', 'n.', '腰；腰部', '和 waste（浪費）同音', 'These pants are too big for my waist.', '這條褲子的腰圍對我來說太大了。', '👖'),
    W('wrist', 'n.', '手腕', 'w 不發音；wristwatch 手錶', 'She wears a watch on her left wrist.', '她左手腕戴著一支錶。', '⌚'),
  ],
  'focus': [
    {'title': '不發音的字母', 'head': ('單字', '不發音', ''),
     'rows': [('thumb', 'b', ''), ('wrist', 'w', ''), ('tongue', 'ue', '')], 'note': '拼字時要記得這些不發音的字母。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=3, n_ce=5, n_ec=4, n_sp=5, fill=[
  F('He hasn\'t shaved for weeks. Now he has a long ______.', ['beard', 'ankle', 'bone', 'waist'], 0, '很久沒刮鬍子 → beard 鬍子。'),
  F('I fell down the stairs and hurt my ______. I can\'t walk well.', ['chin', 'ankle', 'thumb', 'tongue'], 1, '走不好路 → 傷到 ankle 腳踝。'),
  F('Chinese is my mother ______.', ['tongue', 'skin', 'hip', 'wrist'], 0, 'mother tongue 母語。'),
  F('Put on a hat. The sun can hurt your ______.', ['beard', 'skin', 'bone', 'waist'], 1, '太陽會傷害 skin 皮膚。'),
  F('Good job! Two ______ up!', ['wrists', 'thumbs', 'ankles', 'hips'], 1, 'thumbs up 比讚。'),
  F('Milk is good for your teeth and ______.', ['bones', 'beards', 'tongues', 'chins'], 0, '牛奶對牙齒和 bones 骨頭好。'),
])
