# 主題 2000 字 Unit 27：Articles & determiners 冠詞與限定詞（字表依課本單元；詞性、中文、例句、題目為本站自編）
# 功能詞沒有適合的照片，全部用 emoji。
def W(w, pos, zh, note, ex, exzh, pic, exsay=None, say=None):
    d = {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}
    if exsay:
        d['exsay'] = exsay
    if say:
        d['say'] = say
    return d

UNIT = {
  'book': 'w2000', 'no': 27, 'en': 'Articles & determiners', 'zh': '冠詞與限定詞',
  'intro': '放在名詞前面的小字：a／an、the、this／that／these／those、every，還有 my、your、his… 這些「誰的」。字很短，但每天都會用到。',
  'words': [
    W('a', 'art.', '一（個、位、隻…）', '母音開頭的字前面用 an：an apple、an hour', 'I have a dog and an old cat.', '我有一隻狗和一隻老貓。', '1️⃣', say='a, an'),
    W('every', 'adj.', '每一（個、天…）', '後面接單數名詞', 'I walk to school every day.', '我每天走路上學。', '📅'),
    W('the', 'art.', '這；那（指特定的）', '說過的、大家都知道的、獨一無二的東西用 the', 'I bought a book. The book is very funny.', '我買了一本書。那本書很好笑。', '👉'),
    W('this', 'pron./adj.', '這；這個', '複數 these', 'This is my new bike.', '這是我的新腳踏車。', '👇'),
    W('that', 'pron./adj.', '那；那個', '複數 those', 'That boy over there is my brother.', '那邊那個男孩是我弟弟。', '👉'),
    W('these', 'pron./adj.', '這些', 'this 的複數', 'These shoes are too small for me.', '這些鞋子對我來說太小了。', '👟'),
    W('those', 'pron./adj.', '那些', 'that 的複數', 'Those birds are flying south.', '那些鳥正往南飛。', '🐦'),
    W('my', 'adj.', '我的', '所有格，後面接名詞', 'My mother is a nurse.', '我媽媽是護理師。', '🙋'),
    W('our', 'adj.', '我們的', '', 'Our classroom is on the second floor.', '我們的教室在二樓。', '🏫'),
    W('your', 'adj.', '你的；你們的', '', 'Is this your pencil?', '這是你的鉛筆嗎？', '✏️'),
    W('his', 'adj./pron.', '他的', '', 'Tom is cleaning his room.', '湯姆正在打掃他的房間。', '👦'),
    W('her', 'adj./pron.', '她的；她（受格）', '', 'Amy is talking to her friend.', 'Amy 正在和她的朋友說話。', '👧'),
    W('its', 'adj.', '它的；牠的', '不要和 it\'s（＝it is）搞混', 'The cat is washing its face.', '貓正在洗牠的臉。', '🐱'),
    W('their', 'adj.', '他們的', '不要和 there（那裡）搞混', 'The students are doing their homework.', '學生們正在寫他們的功課。', '📚'),
  ],
  'focus': [
    {'title': 'a 還是 an？看第一個「音」', 'head': ('a + 子音', 'an + 母音', '注意'), 'rows': [
      ('a book', 'an apple', ''),
      ('a dog', 'an egg', ''),
      ('a university', 'an hour', 'university 唸 [ju]，是子音；hour 的 h 不發音'),
      ('a uniform', 'an umbrella', ''),
    ], 'note': '看的是發音，不是字母：a useful book、an honest boy。'},
    {'title': '這、那、這些、那些', 'head': ('', '單數', '複數'), 'rows': [
      ('近的', 'this 這個', 'these 這些'),
      ('遠的', 'that 那個', 'those 那些'),
    ], 'note': 'This is a pen. → These are pens. 名詞和 be 動詞也要一起變複數。'},
    {'title': '所有格：誰的？', 'head': ('人稱', '所有格', '例'), 'rows': [
      ('I', 'my 我的', 'my bag'),
      ('you', 'your 你的', 'your bag'),
      ('he', 'his 他的', 'his bag'),
      ('she', 'her 她的', 'her bag'),
      ('it', 'its 它的', 'its tail'),
      ('we', 'our 我們的', 'our bags'),
      ('they', 'their 他們的', 'their bags'),
    ], 'note': '所有格後面一定要接名詞。its（它的）沒有一撇；it\'s = it is。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '這些', 'opts': ['this', 'these', 'those', 'that'], 'answer': 1, 'exp': 'these 這些（this 的複數）。'},
    {'type': 'mc', 'q': '那些', 'opts': ['those', 'these', 'there', 'their'], 'answer': 0, 'exp': 'those 那些（that 的複數）。'},
    {'type': 'mc', 'q': '他們的', 'opts': ['there', 'they', 'their', 'them'], 'answer': 2, 'exp': 'their 他們的；there 是那裡。'},
    {'type': 'mc', 'q': '每一（個）', 'opts': ['all', 'every', 'any', 'very'], 'answer': 1, 'exp': 'every 每一，後面接單數。'},
  ]},
  {'title': '② a、an 或 the：選出正確的答案', 'items': [
    {'type': 'mc', 'q': 'I eat ______ egg every morning.', 'opts': ['a', 'an', 'the', '不填'], 'answer': 1, 'exp': 'egg 母音開頭，用 an。'},
    {'type': 'mc', 'q': 'We waited for ______ hour.', 'opts': ['a', 'an', 'two', 'many'], 'answer': 1, 'exp': 'hour 的 h 不發音，用 an。'},
    {'type': 'mc', 'q': 'My sister goes to ______ university in Taipei.', 'opts': ['a', 'an', 'two', 'these'], 'answer': 0, 'exp': 'university 唸 [ju]，子音開頭，用 a。'},
    {'type': 'mc', 'q': '______ sun is very bright today.', 'opts': ['A', 'An', 'The', 'This'], 'answer': 2, 'exp': '獨一無二的東西用 the：the sun。'},
    {'type': 'mc', 'q': 'I have a cat. ______ cat is white.', 'opts': ['A', 'An', 'The', 'Those'], 'answer': 2, 'exp': '前面說過的東西用 the。'},
  ]},
  {'title': '③ 單數變複數', 'items': [
    {'q': 'this → {0}', 'blanks': [['these']], 'exp': 'this → these。'},
    {'q': 'that → {0}', 'blanks': [['those']], 'exp': 'that → those。'},
    {'q': 'my → {0}', 'blanks': [['our']], 'exp': '我的 → 我們的。'},
    {'q': 'his → {0}', 'blanks': [['their']], 'exp': '他的 → 他們的。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'I walk to school {0} day. （每一）', 'blanks': [['every']], 'exp': 'every day 每天。'},
    {'q': 'Is this {0} pencil, Ken? （你的）', 'blanks': [['your']], 'exp': 'your 你的。'},
    {'q': 'Amy is talking to {0} friend. （她的）', 'blanks': [['her']], 'exp': 'her 她的。'},
    {'q': 'Tom is cleaning {0} room. （他的）', 'blanks': [['his']], 'exp': 'his 他的。'},
    {'q': '{0} classroom is on the second floor. （我們的）', 'blanks': [['Our', 'our']], 'exp': 'our 我們的，句首大寫。'},
  ]},
  {'title': '⑤ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'The dog is wagging ______ tail.', 'opts': ["it's", 'its', 'it', 'his'], 'answer': 1, 'exp': '它的 → its；it\'s 是 it is。'},
    {'type': 'mc', 'q': '______ are my new shoes.', 'opts': ['This', 'That', 'These', 'It'], 'answer': 2, 'exp': 'shoes 複數、be 動詞 are → These。'},
    {'type': 'mc', 'q': 'Every student ______ a book.', 'opts': ['have', 'has', 'are', 'having'], 'answer': 1, 'exp': 'every 接單數，動詞用 has。'},
    {'type': 'mc', 'q': 'Look at ______ birds over there!', 'opts': ['this', 'that', 'these', 'those'], 'answer': 3, 'exp': '遠的、複數 → those。'},
    {'type': 'mc', 'q': 'The children are playing with ______ dog.', 'opts': ['there', 'their', 'they', 'them'], 'answer': 1, 'exp': '他們的 → their。'},
    {'type': 'mc', 'q': 'I have ______ umbrella in my bag.', 'opts': ['a', 'an', 'these', 'every'], 'answer': 1, 'exp': 'umbrella 唸 [ʌ]，母音開頭，用 an。'},
  ]},
]
