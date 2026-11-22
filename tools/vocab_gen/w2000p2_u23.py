# 主題 2000 字 PART 2 Unit 23：Occupations 職業（字表依課本 PART 2 印刷頁 162–164，27 字；書上 baby sitter、hair dresser 用常見寫法 babysitter、hairdresser；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

N = 'n.'
UNIT = {
  'book': 'w2000p2', 'no': 23, 'en': 'Occupations', 'zh': '職業',
  'card': 'assistant、barber、journalist、magician、mechanic、scientist、vendor、hire… 共 27 字；-er／-ist／-ian',
  'intro': '各種職業和雇用相關的字，共 27 個。很多職業是在字尾加 -er（hunter）、-ist（artist、scientist）、-ian（magician、musician）。',
  'words': [
    W('artist', N, '藝術家；畫家', 'art + -ist', 'The artist painted a picture of the sea.', '那位藝術家畫了一幅海的畫。', '🎨'),
    W('assistant', N, '助理；助手', 'assist 協助 + -ant', 'The teacher\'s assistant handed out the papers.', '老師的助理發考卷。', '🗂️'),
    W('babysitter', N, '臨時保母', 'babysit 當保母', 'The babysitter played games with my little sister.', '保母陪我妹妹玩遊戲。', '🍼'),
    W('barber', N, '（男士）理髮師', 'barbershop 理髮店', 'The barber cut my hair very short.', '理髮師把我的頭髮剪得很短。', '💈'),
    W('cowboy', N, '牛仔', 'cow + boy', 'The cowboy rode his horse across the field.', '那位牛仔騎馬穿過田野。', '🤠'),
    W('diplomat', N, '外交官', 'diplomacy 外交', 'A diplomat works for his country in other countries.', '外交官在其他國家為自己的國家工作。', '🤝'),
    W('guide', 'n. / v.', '導遊；嚮導；引導', 'tour guide 導遊', 'Our tour guide told us the history of the temple.', '導遊告訴我們這座廟的歷史。', '🚩'),
    W('hairdresser', N, '美髮師', 'hair + dresser', 'My aunt is a hairdresser at a hair salon.', '我阿姨是美髮店的美髮師。', '💇'),
    W('hunter', N, '獵人', 'hunt 打獵 + -er', 'The hunter followed the deer into the forest.', '獵人跟著鹿走進森林。', '🏹'),
    W('journalist', N, '記者；新聞工作者', 'journal 期刊 + -ist', 'The journalist asked the mayor many questions.', '那位記者問了市長很多問題。', '📰'),
    W('judge', 'n. / v.', '法官；裁判；判斷', 'Don\'t judge a book by its cover. 不要以貌取人', 'The judge listened to both sides.', '法官聽了雙方的說法。', '👨‍⚖️'),
    W('magician', N, '魔術師', 'magic + -ian', 'The magician pulled a rabbit out of his hat.', '魔術師從帽子裡變出一隻兔子。', '🎩'),
    W('manager', N, '經理；管理人', 'manage 管理 + -er', 'I want to talk to the manager of the store.', '我想找這家店的經理談談。', '💼'),
    W('mechanic', N, '技工；修車師傅', 'ch 讀 [k]', 'The mechanic fixed our car in one hour.', '修車師傅一個小時就修好了我們的車。', '🔧'),
    W('model', N, '模特兒；模型', 'model plane 模型飛機', 'The model walked down the runway in a red dress.', '模特兒穿著紅洋裝走伸展台。', '🕴️'),
    W('musician', N, '音樂家；樂手', 'music + -ian', 'The street musician played the guitar.', '街頭音樂家在彈吉他。', '🎸'),
    W('owner', N, '主人；擁有者', 'own 擁有 + -er', 'The owner of the dog thanked us for finding it.', '狗的主人謝謝我們找到牠。', '🔑'),
    W('painter', N, '畫家；油漆工', 'paint + -er', 'The painter painted our house blue.', '油漆工把我們的房子漆成藍色。', '🖌️'),
    W('president', N, '總統；總裁；會長', 'the President 總統', 'The president gave a speech on TV.', '總統在電視上發表演說。', '🎙️'),
    W('priest', N, '神父；牧師；祭司', '', 'The priest talked to the people in the church.', '神父在教堂對大家說話。', '⛪'),
    W('sailor', N, '水手；船員', 'sail 航行 + -or', 'The sailors worked on the ship for months.', '水手們在船上工作了好幾個月。', '⚓'),
    W('scientist', N, '科學家', 'science + -ist', 'Scientists are studying the new virus.', '科學家正在研究這種新病毒。', '🔬'),
    W('servant', N, '僕人；傭人', 'serve 服務 + -ant', 'In the story, the king had a hundred servants.', '故事裡，國王有一百個僕人。', '🛎️'),
    W('vendor', N, '小販', 'street vendor 街頭小販', 'The vendor sells hot sweet potatoes in winter.', '那個小販冬天賣烤地瓜。', '🍠'),
    W('company', N, '公司；陪伴', '複數 companies；keep sb. company 陪伴某人', 'My dad works for a computer company.', '我爸爸在一家電腦公司上班。', '🏢'),
    W('employ', 'v.', '雇用', 'employer 雇主；employee 員工', 'The factory employs 200 workers.', '這家工廠雇用了兩百名工人。', '🧑‍🏭'),
    W('hire', 'v.', '雇用；租用', '= employ（比較口語）', 'We hired a guide to show us around.', '我們雇了一位導遊帶我們參觀。', '📋'),
  ],
  'focus': [
    {'title': '職業的字尾', 'head': ('字尾', '例子', ''),
     'rows': [('-er／-or', 'hunter、owner、manager、sailor', ''), ('-ist', 'artist、journalist、scientist', ''), ('-ian', 'magician、musician', ''), ('-ant', 'assistant、servant', '')],
     'note': 'employ → employer（雇主）／employee（員工）：-er 是做這件事的人，-ee 是被這樣對待的人。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=23, n_ce=7, n_ec=6, n_sp=6, fill=[
  F('A ______ fixes cars.', ['mechanic', 'magician', 'diplomat', 'priest'], 0, '修車 → mechanic。'),
  F('A ______ writes news stories for newspapers.', ['journalist', 'barber', 'cowboy', 'vendor'], 0, '寫新聞 → journalist 記者。'),
  F('The ______ made a coin disappear. Everyone was surprised.', ['magician', 'mechanic', 'judge', 'sailor'], 0, '讓硬幣消失 → magician 魔術師。'),
  F('My parents are going out tonight, so a ______ will take care of us.', ['babysitter', 'servant', 'hunter', 'model'], 0, '照顧小孩 → babysitter 保母。'),
  F('The ______ of the restaurant is very friendly to all the customers.', ['owner', 'hunter', 'cowboy', 'priest'], 0, '餐廳的 owner 老闆。'),
  F('The company plans to ______ ten new workers.', ['hire', 'judge', 'guide', 'serve'], 0, '雇用新員工 → hire。'),
  F('Einstein was a great ______.', ['scientist', 'barber', 'vendor', 'sailor'], 0, '愛因斯坦是 scientist 科學家。'),
  F('The tour ______ showed us around the old town.', ['guide', 'owner', 'judge', 'model'], 0, 'tour guide 導遊。'),
])
