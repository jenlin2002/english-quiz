# 主題 2000 字 Unit 30：Be & auxiliaries be 動詞與助動詞（字表依課本單元；詞性、中文、例句、題目為本站自編）
# 功能詞沒有適合的照片，全部用 emoji。
def W(w, pos, zh, note, ex, exzh, pic, exsay=None):
    d = {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}
    if exsay:
        d['exsay'] = exsay
    return d

UNIT = {
  'book': 'w2000', 'no': 30, 'en': 'Be & auxiliaries', 'zh': 'be 動詞與助動詞',
  'intro': 'be 動詞（am、is、are…）、do／have 的各種變化，還有 can、will、may、must、should 這些助動詞，共 22 個字。助動詞後面一定接原形動詞。',
  'words': [
    W('be', 'v.', '是；在（原形）', '三態 be／was, were／been', 'Be quiet, please.', '請安靜。', '🟰'),
    W('am', 'v.', '是（主詞 I）', '過去式 was', 'I am a junior high school student.', '我是國中生。', '🙋'),
    W('are', 'v.', '是（主詞 you、複數）', '過去式 were', 'You are my best friend.', '你是我最好的朋友。', '👭'),
    W('is', 'v.', '是（第三人稱單數）', '過去式 was', 'She is my sister.', '她是我姊姊。', '👧'),
    W('was', 'v.', '是（am、is 的過去式）', '', 'I was sick yesterday.', '我昨天生病了。', '🤒'),
    W('were', 'v.', '是（are 的過去式）', '', 'They were at the park last Sunday.', '他們上星期天在公園。', '🌳'),
    W('been', 'v.', '是（be 的過去分詞）', 'have been to 去過', 'I have been to Japan twice.', '我去過日本兩次。', '✈️'),
    W('do', 'aux./v.', '（助動詞）；做', '三態 do／did／done', 'Do you like music?', '你喜歡音樂嗎？', '🎵'),
    W('does', 'aux./v.', '（第三人稱單數的 do）；做', '', "He doesn't eat meat.", '他不吃肉。', '🥦'),
    W('did', 'aux./v.', '（do 的過去式）；做了', '', 'Did you finish your homework?', '你作業寫完了嗎？', '📝'),
    W('done', 'v.', '做（do 的過去分詞）', 'Well done! 做得好！', 'Have you done your homework?', '你寫完功課了嗎？', '✅'),
    W('have', 'aux./v.', '有；吃、喝；（完成式助動詞）', '三態 have／had／had', 'We have lunch at noon.', '我們中午吃午餐。', '🍱'),
    W('has', 'aux./v.', '有（第三人稱單數）', '', 'My brother has a new bike.', '我哥哥有一台新腳踏車。', '🚲'),
    W('had', 'aux./v.', '有（have 的過去式、過去分詞）', '', 'We had a good time at the beach.', '我們在海灘玩得很開心。', '🏖️'),
    W('can', 'aux.', '能；可以', '過去式 could；否定 can\'t', 'Can you swim?', '你會游泳嗎？', '🏊'),
    W('could', 'aux.', '（can 的過去式）；可以（客氣）', '', 'Could you open the window, please?', '可以請你開窗嗎？', '🪟'),
    W('will', 'aux.', '將會', '否定 won\'t', 'It will rain tomorrow.', '明天會下雨。', '🌧️'),
    W('would', 'aux.', '（will 的過去式）；願意（客氣）', 'Would you like…? 你要不要…？', 'Would you like some tea?', '你要不要來點茶？', '🍵'),
    W('may', 'aux.', '可以；可能', '', 'May I come in?', '我可以進來嗎？', '🚪'),
    W('might', 'aux.', '可能（比 may 不確定）；（may 的過去式）', '', 'He might be late today.', '他今天可能會遲到。', '🤷'),
    W('must', 'aux.', '必須；一定', '否定 mustn\'t 不可以', 'You must wash your hands before eating.', '吃東西前你必須洗手。', '🧼'),
    W('should', 'aux.', '應該', '', 'You should go to bed early.', '你應該早點睡。', '🛏️'),
  ],
  'focus': [
    {'title': 'be 動詞怎麼配', 'head': ('主詞', '現在式／過去式', '完成式'), 'rows': [
      ('I', 'am／was', 'have been'),
      ('you、we、they、複數', 'are／were', 'have been'),
      ('he、she、it、單數', 'is／was', 'has been'),
    ], 'note': 'I am → I was；they are → they were。'},
    {'title': 'do 和 have 的變化', 'head': ('原形', '第三人稱單數', '過去式／過去分詞'), 'rows': [
      ('do', 'does', 'did／done'),
      ('have', 'has', 'had／had'),
    ], 'note': '問句、否定句用 do／does／did，後面的動詞回到原形：Does he like it? He didn\'t go.'},
    {'title': '助動詞＋原形動詞', 'head': ('助動詞', '意思', '例句'), 'rows': [
      ('can／could', '能、可以', 'I can swim.'),
      ('will／would', '將會；願意', 'I will call you.'),
      ('may／might', '可以；可能', 'It may rain.'),
      ('must', '必須', 'You must stop.'),
      ('should', '應該', 'You should rest.'),
    ], 'note': '助動詞後面一律接原形，也不加 s：He can swim.（不是 can swims）'},
  ],
}

QUIZ = [
  {'title': '① be 動詞：選出正確的答案', 'items': [
    {'type': 'mc', 'q': 'I ______ a student.', 'opts': ['am', 'is', 'are', 'be'], 'answer': 0, 'exp': 'I am。'},
    {'type': 'mc', 'q': 'They ______ at the park last Sunday.', 'opts': ['are', 'was', 'were', 'is'], 'answer': 2, 'exp': '過去、複數 → were。'},
    {'type': 'mc', 'q': 'I ______ sick yesterday.', 'opts': ['am', 'was', 'were', 'been'], 'answer': 1, 'exp': 'I 的過去式 → was。'},
    {'type': 'mc', 'q': 'She has ______ to Japan twice.', 'opts': ['be', 'was', 'been', 'is'], 'answer': 2, 'exp': '完成式 has been。'},
    {'type': 'mc', 'q': '______ quiet, please.', 'opts': ['Am', 'Be', 'Is', 'Are'], 'answer': 1, 'exp': '祈使句用原形 Be。'},
  ]},
  {'title': '② do、have：選出正確的答案', 'items': [
    {'type': 'mc', 'q': '______ your brother like soccer?', 'opts': ['Do', 'Does', 'Is', 'Are'], 'answer': 1, 'exp': '第三人稱單數 → Does。'},
    {'type': 'mc', 'q': '______ you finish your homework last night?', 'opts': ['Do', 'Does', 'Did', 'Done'], 'answer': 2, 'exp': 'last night 過去 → Did。'},
    {'type': 'mc', 'q': 'Have you ______ your homework?', 'opts': ['do', 'did', 'does', 'done'], 'answer': 3, 'exp': '完成式 have + done。'},
    {'type': 'mc', 'q': 'My sister ______ a new bike.', 'opts': ['have', 'has', 'having', 'is'], 'answer': 1, 'exp': '第三人稱單數 → has。'},
    {'type': 'mc', 'q': 'We ______ a good time at the beach yesterday.', 'opts': ['have', 'has', 'had', 'having'], 'answer': 2, 'exp': '過去式 → had。'},
  ]},
  {'title': '③ 寫出過去式', 'items': [
    {'q': 'do → {0}', 'blanks': [['did']], 'exp': 'do → did。'},
    {'q': 'have → {0}', 'blanks': [['had']], 'exp': 'have → had。'},
    {'q': 'can → {0}', 'blanks': [['could']], 'exp': 'can → could。'},
    {'q': 'will → {0}', 'blanks': [['would']], 'exp': 'will → would。'},
    {'q': 'may → {0}', 'blanks': [['might']], 'exp': 'may → might。'},
  ]},
  {'title': '④ 例句填空：寫出正確的助動詞', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'You {0} wash your hands before eating. （必須）', 'blanks': [['must']], 'exp': 'must 必須。'},
    {'q': 'You {0} go to bed early. （應該）', 'blanks': [['should']], 'exp': 'should 應該。'},
    {'q': 'It {0} rain tomorrow. （將會）', 'blanks': [['will']], 'exp': 'will 將會。'},
    {'q': '{0} I come in? （可以，客氣地問）', 'blanks': [['May', 'may']], 'exp': 'May I…? 我可以…嗎？'},
  ]},
  {'title': '⑤ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'He can ______ very fast.', 'opts': ['run', 'runs', 'running', 'ran'], 'answer': 0, 'exp': '助動詞後面接原形。'},
    {'type': 'mc', 'q': '______ you like some tea?', 'opts': ['Will', 'Would', 'Do', 'Are'], 'answer': 1, 'exp': 'Would you like…? 要不要…？'},
    {'type': 'mc', 'q': '______ you open the window, please?', 'opts': ['Could', 'Must', 'Should', 'Did'], 'answer': 0, 'exp': '客氣地請求 → Could you…?'},
    {'type': 'mc', 'q': 'Take an umbrella. It ______ rain this afternoon.', 'opts': ['might', 'must', 'did', 'was'], 'answer': 0, 'exp': '可能 → might。'},
    {'type': 'mc', 'q': 'John ______ do his homework yesterday.', 'opts': ["doesn't", "didn't", "wasn't", "isn't"], 'answer': 1, 'exp': '過去否定、後接原形 do → didn\'t。'},
  ]},
]
