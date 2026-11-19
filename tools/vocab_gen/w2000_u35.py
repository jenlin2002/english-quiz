# 主題 2000 字 Unit 35：Other verbs (1) 其他動詞 (1)（字表依課本單元；詞性、中文、例句、題目為本站自編）
def W(w, zh, note, ex, exzh, pic, pos='v.'):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000', 'no': 35, 'en': 'Other verbs (1)', 'zh': '其他動詞 (1)',
  'intro': '感官動詞（看、聽、聞、嚐）和表示想法、感覺的動詞，共 33 個。重點：感官動詞＋形容詞、後面接 to V 還是 V-ing。',
  'words': [
    W('feel', '感覺；摸起來', '三態 feel／felt／felt', 'I feel much better after a rest.', '休息之後我覺得好多了。', '🤗'),
    W('hear', '聽到', '三態 hear／heard／heard', 'I heard someone knocking at the door.', '我聽見有人在敲門。', '👂'),
    W('listen', '聽', 'listen to 聽…（主動去聽）', 'I like to listen to music.', '我喜歡聽音樂。', '🎧'),
    W('look', '看；看起來', 'look at 看…', 'Look at the beautiful flowers!', '看那些漂亮的花！', '👀'),
    W('see', '看見', '三態 see／saw／seen', 'I saw many birds at the zoo.', '我在動物園看到很多鳥。', '👁️'),
    W('smell', '聞；聞起來', '', 'The soup smells good.', '這湯聞起來很香。', '👃'),
    W('sound', '聽起來', '', 'Your idea sounds great.', '你的主意聽起來很棒。', '🔉'),
    W('taste', '嚐；嚐起來', '', 'This cake tastes sweet.', '這蛋糕嚐起來很甜。', '👅'),
    W('watch', '看；觀看', 'watch TV 看電視', 'We watched a baseball game last night.', '我們昨晚看了一場棒球賽。', '📺'),
    W('check', '檢查', '', 'Check your bag before you leave.', '離開前檢查一下你的包包。', '✅'),
    W('end', '結束', '也可當名詞', 'What time does the party end?', '派對幾點結束？', '🔚'),
    W('finish', '完成', '後接 V-ing', 'I finished doing my homework.', '我寫完功課了。', '🏁'),
    W('believe', '相信', '', 'I can\'t believe it!', '我不敢相信！', '🙌'),
    W('forget', '忘記', '三態 forget／forgot／forgotten', 'Don\'t forget to bring your umbrella.', '別忘了帶雨傘。', '🤦'),
    W('guess', '猜', '', 'Guess what I have in my hand.', '猜猜看我手上有什麼。', '🤔'),
    W('hate', '討厭', '', 'I hate getting up early in winter.', '我討厭冬天早起。', '😖'),
    W('hope', '希望', 'hope to V', 'I hope to see you again.', '我希望能再見到你。', '🌈'),
    W('know', '知道；認識', '三態 know／knew／known', 'I have known Amy for five years.', '我認識 Amy 五年了。', '💡'),
    W('like', '喜歡', 'like to V／V-ing', 'I like playing basketball.', '我喜歡打籃球。', '👍'),
    W('love', '愛；喜愛', '', 'My sister loves traveling.', '我姊姊很愛旅行。', '❤️'),
    W('mind', '介意', '後接 V-ing', 'Would you mind opening the window?', '你介意打開窗戶嗎？', '🙇'),
    W('need', '需要', '', 'Do you need any help?', '你需要幫忙嗎？', '🆘'),
    W('notice', '注意到', '', 'Did you notice the new sign?', '你有注意到新的告示牌嗎？', '👀'),
    W('remember', '記得', '', 'Remember to turn off the lights.', '記得關燈。', '🧠'),
    W('surprise', '使驚訝', '也可當名詞：驚喜', 'The news surprised everyone.', '這則消息讓大家很驚訝。', '😲'),
    W('think', '想；認為', '三態 think／thought／thought', 'I think it will rain today.', '我想今天會下雨。', '💭'),
    W('want', '想要', 'want to V', 'What do you want to be in the future?', '你將來想做什麼？', '🙋'),
    W('wish', '希望；祝福', 'I wish… 但願…（不太可能的事）', 'I wish you a happy birthday.', '祝你生日快樂。', '🌠'),
    W('worry', '擔心', 'worry about 擔心…', 'Don\'t worry about me.', '不要擔心我。', '😟'),
    W('act', '行動；演戲', '', 'We must act quickly.', '我們必須快點行動。', '🎭'),
    W('blow', '吹', '三態 blow／blew／blown', 'Blow out the candles!', '吹熄蠟燭！', '🌬️'),
    W('bow', '鞠躬', '', 'The singer bowed to the audience.', '歌手向觀眾鞠躬。', '🙇'),
    W('break', '打破；弄壞', '三態 break／broke／broken', 'Who broke the window?', '誰打破了窗戶？', '💔'),
  ],
  'focus': [
    {'title': '感官動詞＋形容詞', 'head': ('動詞', '意思', '例句'), 'rows': [
      ('look', '看起來', 'You look tired.'),
      ('sound', '聽起來', 'That sounds great.'),
      ('smell', '聞起來', 'The soup smells good.'),
      ('taste', '嚐起來', 'The cake tastes sweet.'),
      ('feel', '感覺；摸起來', 'I feel happy.'),
    ], 'note': '後面接形容詞，不接副詞：It tastes good.（不是 well）；接名詞要加 like：She looks like her mother.'},
    {'title': '看和聽', 'head': ('動詞', '意思', ''), 'rows': [
      ('look at', '注意看（靜態）', ''),
      ('watch', '觀看（動態：電視、比賽）', ''),
      ('see', '看見（自然看到）', ''),
      ('listen to', '注意聽', ''),
      ('hear', '聽見（自然聽到）', ''),
    ], 'note': ''},
    {'title': '後面接 to V 還是 V-ing', 'head': ('接法', '動詞', '例句'), 'rows': [
      ('V-ing', 'finish、mind', 'I finished reading the book.'),
      ('to V', 'want、hope、need', 'I want to go home.'),
      ('兩種都可以', 'like、love、hate', 'I like swimming. ＝ I like to swim.'),
      ('意思不同', 'forget／remember', 'forget to V 忘了要做；forget V-ing 忘了做過'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '注意到', 'opts': ['notice', 'nature', 'note', 'need'], 'answer': 0, 'exp': 'notice 注意到。'},
    {'type': 'mc', 'q': '擔心', 'opts': ['wish', 'worry', 'want', 'watch'], 'answer': 1, 'exp': 'worry 擔心。'},
    {'type': 'mc', 'q': '相信', 'opts': ['belong', 'believe', 'begin', 'become'], 'answer': 1, 'exp': 'believe 相信。'},
  ]},
  {'title': '② 感官動詞：選出正確的答案', 'items': [
    {'type': 'mc', 'q': 'This cake tastes ______.', 'opts': ['well', 'good', 'nicely', 'badly'], 'answer': 1, 'exp': '感官動詞＋形容詞 → good。'},
    {'type': 'mc', 'q': 'Your idea ______ great.', 'opts': ['sounds', 'hears', 'listens', 'sees'], 'answer': 0, 'exp': '聽起來 → sounds。'},
    {'type': 'mc', 'q': 'She ______ like her mother.', 'opts': ['looks', 'sees', 'watches', 'looks at'], 'answer': 0, 'exp': 'look like 看起來像。'},
    {'type': 'mc', 'q': 'I like to ______ music.', 'opts': ['hear', 'listen', 'listen to', 'sound'], 'answer': 2, 'exp': 'listen to music 聽音樂。'},
    {'type': 'mc', 'q': 'We ______ a baseball game on TV last night.', 'opts': ['saw at', 'watched', 'looked', 'heard'], 'answer': 1, 'exp': '看比賽 → watch。'},
  ]},
  {'title': '③ 寫出過去式', 'items': [
    {'q': 'think → {0}', 'blanks': [['thought']], 'exp': 'think → thought。'},
    {'q': 'break → {0}', 'blanks': [['broke']], 'exp': 'break → broke。'},
    {'q': 'know → {0}', 'blanks': [['knew']], 'exp': 'know → knew。'},
    {'q': 'feel → {0}', 'blanks': [['felt']], 'exp': 'feel → felt。'},
    {'q': 'forget → {0}', 'blanks': [['forgot']], 'exp': 'forget → forgot。'},
  ]},
  {'title': '④ to V 還是 V-ing', 'items': [
    {'type': 'mc', 'q': 'I finished ______ my homework.', 'opts': ['do', 'to do', 'doing', 'did'], 'answer': 2, 'exp': 'finish + V-ing。'},
    {'type': 'mc', 'q': 'Would you mind ______ the door?', 'opts': ['close', 'closing', 'to close', 'closed'], 'answer': 1, 'exp': 'mind + V-ing。'},
    {'type': 'mc', 'q': 'I hope ______ you again.', 'opts': ['see', 'seeing', 'to see', 'saw'], 'answer': 2, 'exp': 'hope + to V。'},
    {'type': 'mc', 'q': 'Don\'t forget ______ your umbrella. It will rain.', 'opts': ['bring', 'to bring', 'bringing', 'brought'], 'answer': 1, 'exp': '忘了要去做 → forget to V。'},
  ]},
  {'title': '⑤ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': '{0} out the candles! （吹）', 'blanks': [['Blow', 'blow']], 'exp': 'blow 吹。'},
    {'q': 'Don\'t {0} about me. （擔心）', 'blanks': [['worry']], 'exp': 'worry about 擔心。'},
    {'q': '{0} what I have in my hand. （猜）', 'blanks': [['Guess', 'guess']], 'exp': 'guess 猜。'},
  ]},
]
