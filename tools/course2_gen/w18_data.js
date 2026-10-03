const GRAMMAR_QUESTIONS = [
  { text:"Everyone in my class <span class='blank'>______</span> ready for the trip.", options:["is","are","be","were"], answer:0, note:"everyone 是單數，動詞用 is。" },
  { text:"Each of the students <span class='blank'>______</span> a laptop.", options:["has","have","having","are having"], answer:0, note:"each of + 複數名詞，真正的主詞是 each，動詞用單數 has。" },
  { text:"A number of students <span class='blank'>______</span> absent today.", options:["are","is","was","has"], answer:0, note:"a number of = many（很多），後面接複數名詞，動詞用複數 are。" },
  { text:"The number of students in our school <span class='blank'>______</span> about five hundred.", options:["is","are","were","have"], answer:0, note:"the number of 指「…的數目」，主詞是 number，動詞用單數 is。" },
  { text:"Ten dollars <span class='blank'>______</span> too much for a pencil.", options:["is","are","were","have"], answer:0, note:"金額當成一個整體，動詞用單數 is。" },
  { text:"Mathematics <span class='blank'>______</span> my favorite subject.", options:["is","are","were","be"], answer:0, note:"mathematics 雖然 -s 結尾，但是學科名稱，用單數 is。" },
  { text:"The rich <span class='blank'>______</span> not always happy.", options:["are","is","was","has"], answer:0, note:"the + 形容詞 = 一群人（the rich = rich people），動詞用複數 are。" },
  { text:"The teacher, as well as the students, <span class='blank'>______</span> excited.", options:["is","are","were","have"], answer:0, note:"as well as 不影響動詞，真正的主詞是 the teacher，用單數 is。" },
  { text:"The police <span class='blank'>______</span> looking for the thief.", options:["are","is","was","has"], answer:0, note:"police 一定當複數用，動詞用 are。" },
  { text:"I have two brothers. One is a doctor, and <span class='blank'>______</span> is a teacher.", options:["the other","another","other","others"], answer:0, note:"兩個中的另一個用 the other。" },
  { text:"Some students like math; <span class='blank'>______</span> like English.", options:["others","the other","another","other"], answer:0, note:"some…others：一些…另一些（不是全部），用 others。" },
  { text:"This cookie is delicious. Can I have <span class='blank'>______</span>?", options:["another","the other","others","other"], answer:0, note:"不特定的「再一個」用 another。" },
  { text:"I lost my umbrella, so I bought a new <span class='blank'>______</span>.", options:["one","it","ones","them"], answer:0, note:"買的是同類的另一把傘，不是原來那一把，用 one。" },
  { text:"There is <span class='blank'>______</span> milk in the fridge, so we need to buy some.", options:["little","few","a few","many"], answer:0, note:"milk 不可數，「幾乎沒有」用 little，所以才需要買。" },
  { text:"<span class='blank'>______</span> of my two sisters can drive.", options:["Neither","None","No","Nobody"], answer:0, note:"兩個人中「都不」用 neither；三個以上才用 none。" },
  { text:"She taught <span class='blank'>______</span> to play the guitar.", options:["herself","her","she","hers"], answer:0, note:"主詞和受詞是同一個人，用反身代名詞 herself。" },
  { text:"Never <span class='blank'>______</span> such a beautiful beach.（回收）", options:["have I seen","I have seen","I saw","seen I have"], answer:0, note:"否定副詞 Never 放句首要倒裝：have I seen。" },
  { text:"A: I don't like horror movies. B: <span class='blank'>______</span> do I.（回收）", options:["Neither","So","Either","Too"], answer:0, note:"前一句是否定句，「我也不」用 Neither do I。" },
  { text:"It was my father <span class='blank'>______</span> fixed the bike.（回收）", options:["who","what","which","whom"], answer:0, note:"強調句 It was…who / that…，強調人用 who。" },
  { text:"Not until ten o'clock <span class='blank'>______</span> home.（回收）", options:["did he get","he got","he did get","got he"], answer:0, note:"Not until 放句首，主要子句要倒裝：did he get。" }
];

const READING_PASSAGE = {
  title:"Walking to School",
  html:`The number of students who walk to school is falling in many cities. Today, a number of parents drive their children to school every morning. Each of these short trips adds to the traffic, and the air near schools is getting worse.<br><br>
Some families have started "walking groups." A few parents take turns walking with a group of children. Others share cars with their neighbors. Neither idea is perfect, but both help. The school, as well as the city, is now building safer sidewalks. Everyone hopes that more children will walk to school again.`
};

const READING_QUESTIONS = [
  { type:"閱讀理解", text:"What is the passage mainly about?", options:["Fewer students walking to school and ways to help","How to buy a new car","A new school sport","Why students like math"], answer:0, note:"全文講走路上學的學生變少，以及家庭和學校想出的辦法。" },
  { type:"閱讀理解", text:"What problem do the short car trips cause?", options:["More traffic and worse air","Cheaper gas","Fewer parents at school","Longer school days"], answer:0, note:"文章提到 Each of these short trips adds to the traffic, and the air near schools is getting worse。" },
  { type:"閱讀理解", text:"What is a \"walking group\"?", options:["Parents taking turns walking with children","Children walking alone at night","A sports club for parents","A group of teachers who drive"], answer:0, note:"文章提到 A few parents take turns walking with a group of children。" },
  { type:"閱讀理解", text:"What are the school and the city doing?", options:["Building safer sidewalks","Closing the roads","Buying school buses","Making students drive"], answer:0, note:"文章提到 The school, as well as the city, is now building safer sidewalks。" },
  { type:"閱讀理解", text:"What does the writer say about the two ideas?", options:["Neither is perfect, but both help.","Both are perfect.","Only walking groups help.","Neither idea helps at all."], answer:0, note:"文章提到 Neither idea is perfect, but both help。" },
  { type:"文意選填", text:"The number of students who walk to school ______ falling.（選出最適合填入文中空格的字）", options:["is","are","have","were"], answer:0, note:"the number of 的主詞是 number，動詞用單數 is。" },
  { type:"文意選填", text:"Each of these short trips ______ to the traffic.（選出最適合填入文中空格的字）", options:["adds","add","adding","are adding"], answer:0, note:"each of + 複數名詞，動詞用單數 adds。" },
  { type:"文意選填", text:"Some families have started walking groups. ______ share cars with their neighbors.（選出最適合填入文中空格的字）", options:["Others","The other","Another","Other"], answer:0, note:"some…others：一些…另一些，後面動詞 share 是複數，用 Others。" },
  { type:"文意選填", text:"The school, as well as the city, ______ now building safer sidewalks.（選出最適合填入文中空格的字）", options:["is","are","were","have"], answer:0, note:"as well as 不影響動詞，主詞是 the school，用 is。" },
  { type:"文意選填", text:"______ hopes that more children will walk to school again.（選出最適合填入文中空格的字）", options:["Everyone","All","Both","Many"], answer:0, note:"動詞 hopes 是單數，主詞用 Everyone。" }
];

const CLOZE_PASSAGE = {
  title:"Our Class Trip",
  html:`Last week our class went to the zoo. Everyone (1)<span class='blank'>____</span> excited. I brought two sandwiches. One was for me, and (2)<span class='blank'>____</span> was for my friend Ben.<br><br>
(3)<span class='blank'>____</span> of the animals were sleeping, but the monkeys were very active. Two hours (4)<span class='blank'>____</span> not enough to see everything!`
};

const CLOZE_QUESTIONS = [
  { type:"克漏字 (1)", text:"選出最適合填入空格 (1) 的字：", options:["was","were","are","be"], answer:0, note:"everyone 是單數，過去式用 was。" },
  { type:"克漏字 (2)", text:"選出最適合填入空格 (2) 的字：", options:["the other","another","others","the others"], answer:0, note:"兩個三明治中的另一個用 the other。" },
  { type:"克漏字 (3)", text:"選出最適合填入空格 (3) 的字：", options:["Some","Each","Every","Neither"], answer:0, note:"動詞 were 是複數，「有些動物」用 Some of the animals。" },
  { type:"克漏字 (4)", text:"選出最適合填入空格 (4) 的字：", options:["was","were","are","have"], answer:0, note:"一段時間（two hours）當成一個整體，用單數 was。" }
];

const LISTENING_QUESTIONS = [
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/girls-reading.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["One girl is holding a red book, and the other is holding a green one.", "One girl is holding a red book, and another are holding a green one.", "One girl is holding a red book, and the others is holding a green one."], answer: 0,
    note: "兩個女孩中的另一個用 the other，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/lunch.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["Each of the children has some food.", "Each of the children have some food.", "Each of the child has some food."], answer: 0,
    note: "each of + 複數名詞，動詞用單數 has，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/soccer.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["One boy is kicking the ball, and the others are standing in a line.", "One boy is kicking the ball, and the other are standing in a line.", "One boy is kicking the ball, and another are standing in a line."], answer: 0,
    note: "其餘的孩子（三個以上）用 the others，動詞用 are，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/library.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["There are a lot of books on the shelves.", "There is a lot of books on the shelves.", "There are a little books on the shelves."], answer: 0,
    note: "books 是複數，用 There are；a little 只能接不可數名詞，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/grocery.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The woman, along with her cart, is in the store.", "The woman, along with her cart, are in the store.", "The woman, along with her cart, were in the store."], answer: 0,
    note: "along with 不影響動詞，主詞是 the woman，用 is，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "How many students are in your class?", options: ["The number of students is thirty.", "The number of students are thirty.", "A number of students is thirty."], answer: 0,
    note: "the number of 指「數目」，動詞用單數 is，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Do you have any questions?", options: ["Yes, I have a few.", "Yes, I have a little.", "Yes, I have little."], answer: 0,
    note: "questions 可數，「有一些」用 a few，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Which shoes do you want, the red ones or the black ones?", options: ["I'll take the black ones.", "I'll take the black one shoes.", "I'll take the black it."], answer: 0,
    note: "ones 代替複數的 shoes，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Can either of your parents speak Japanese?", options: ["No, neither of them can.", "No, none of them can.", "No, both of them can't."], answer: 0,
    note: "父母是兩個人，「兩個都不」用 neither，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A boy says, I have two cats. One is white, and the other is black. A girl says, What are their names? The boy says, Snow and Coal. What color is the second cat?",
    options: ["Black", "White", "Gray"], answer: 0,
    note: "the other is black 表示另一隻是黑色的，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A woman says, How was the party? A man says, Not great. Few people came, and there was little food. How was the party?",
    options: ["Almost nobody came.", "It was very crowded.", "There was too much food."], answer: 0,
    note: "Few people came 表示幾乎沒有人來，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A girl says, I broke my phone yesterday. A boy says, Are you going to fix it? The girl says, No, it's too old. I'll buy a new one. What will the girl do?",
    options: ["Buy a new phone", "Fix her old phone", "Borrow a phone"], answer: 0,
    note: "I'll buy a new one 的 one 指另一支手機，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A man says, Some of my students like science, and others like history. A woman says, What about the rest? The man says, The others like art. What do the rest of the students like?",
    options: ["Art", "Science", "History"], answer: 0,
    note: "The others like art 表示剩下的學生喜歡美術，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽報告，選出最合理的答案。",
    audioQuestion: "Here are the results of our class survey. The number of students who exercise every day is twelve. A number of students exercise only on weekends. A few students never exercise at all. Everyone agrees that exercise is important. How many students exercise every day?",
    options: ["Twelve", "A few", "None"], answer: 0,
    note: "The number of students who exercise every day is twelve，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽廣播，選出最合理的答案。",
    audioQuestion: "Good afternoon, shoppers. Each of our customers today will get a free bag. The manager, as well as our staff, is happy to help you. Ten dollars is all you need to join our member club. What does each customer get today?",
    options: ["A free bag", "Ten dollars", "A member card"], answer: 0,
    note: "Each of our customers today will get a free bag，所以答案是 (A)。"
  }
];

const VOCAB_QUESTIONS = [
  { word:"survey", text:"survey 這個字的中文意思最接近：", options:["調查","考試","比賽","旅行"], answer:0, note:"survey (n./v.) 調查。",
    example:"We did a survey about students' sleep.", exampleZh:"我們做了一個關於學生睡眠的調查。",
    scrambleSentence:"The survey shows that most students like music.", zh:"調查顯示大部分學生喜歡音樂。" },
  { word:"customer", text:"customer 這個字的中文意思最接近：", options:["顧客","經理","乘客","店員"], answer:0, note:"customer (n.) 顧客。",
    example:"Each customer gets a free gift.", exampleZh:"每位顧客都可以得到一份免費禮物。",
    scrambleSentence:"The shop has a lot of customers on weekends.", zh:"這家店週末有很多顧客。" },
  { word:"staff", text:"staff 這個字的中文意思最接近：", options:["全體員工","老闆","顧客","學生"], answer:0, note:"staff (n.) 全體員工、工作人員。",
    example:"The hotel staff are very friendly.", exampleZh:"飯店的員工都很友善。",
    scrambleSentence:"Please ask our staff for help.", zh:"請向我們的工作人員尋求協助。" },
  { word:"neighbor", text:"neighbor 這個字的中文意思最接近：", options:["鄰居","親戚","同學","客人"], answer:0, note:"neighbor (n.) 鄰居；neighborhood = 社區、鄰近地區。",
    example:"Our neighbors are very kind.", exampleZh:"我們的鄰居都很親切。",
    scrambleSentence:"My neighbor helped me carry the boxes.", zh:"我的鄰居幫我搬箱子。" },
  { word:"share", text:"share 這個字的中文意思最接近：", options:["分享、共用","藏起來","賣掉","丟掉"], answer:0, note:"share (v.) 分享、共用；share A with B = 和 B 分享 A。",
    example:"I share a room with my sister.", exampleZh:"我和妹妹共用一個房間。",
    scrambleSentence:"They share the car with their neighbors.", zh:"他們和鄰居共用一台車。" },
  { word:"absent", text:"absent 這個字的中文意思最接近：", options:["缺席的","出現的","忙碌的","生氣的"], answer:0, note:"absent (adj.) 缺席的；反義字是 present（出席的）。",
    example:"Three students were absent today.", exampleZh:"今天有三個學生缺席。",
    scrambleSentence:"He was absent because he was sick.", zh:"他因為生病缺席了。" },
  { word:"subject", text:"subject 這個字的中文意思最接近：", options:["科目；主題","禮物","工具","地圖"], answer:0, note:"subject (n.) 科目、主題；在文法裡也是「主詞」。",
    example:"Math is my favorite subject.", exampleZh:"數學是我最喜歡的科目。",
    scrambleSentence:"Which subject do you like best?", zh:"你最喜歡哪一個科目？" },
  { word:"result", text:"result 這個字的中文意思最接近：", options:["結果","原因","問題","計畫"], answer:0, note:"result (n.) 結果；as a result = 結果、因此。",
    example:"The test results will come out tomorrow.", exampleZh:"考試結果明天會出來。",
    scrambleSentence:"We were happy with the result.", zh:"我們對結果很滿意。" },
  { word:"sidewalk", text:"sidewalk 這個字的中文意思最接近：", options:["人行道","高速公路","停車場","地下室"], answer:0, note:"sidewalk (n.) 人行道（英式英文說 pavement）。",
    example:"Please walk on the sidewalk.", exampleZh:"請走在人行道上。",
    scrambleSentence:"The city is building wider sidewalks.", zh:"市政府正在蓋更寬的人行道。" },
  { word:"energy", text:"energy 這個字的中文意思最接近：", options:["精力、能量","時間","金錢","聲音"], answer:0, note:"energy (n.) 精力、能量；形容詞是 energetic。",
    example:"Children are full of energy.", exampleZh:"小孩子精力充沛。",
    scrambleSentence:"I have no energy after the long trip.", zh:"長途旅行後我一點力氣都沒有。" }
];

const SPEAKING_QUESTIONS = [
  { en:"Tell me something that everyone in your family likes.", hint:"用 Everyone… + 單數動詞", sample:"Everyone in my family loves music.", sampleZh:"我家每個人都喜歡音樂。", checkType:"everyone" },
  { en:"Tell me about your classmates. Use a number of.", hint:"用 A number of… + 複數動詞", sample:"A number of my classmates play basketball after school.", sampleZh:"我有很多同學放學後打籃球。", checkType:"anumber" },
  { en:"Tell me about two things you have, like two pets or two hobbies.", hint:"用 One…, and the other…", sample:"I have two hobbies. One is reading, and the other is swimming.", sampleZh:"我有兩個嗜好，一個是閱讀，另一個是游泳。", checkType:"theother" },
  { en:"What kinds of music do your friends like?", hint:"用 Some…, others…", sample:"Some of my friends like rock music; others like pop.", sampleZh:"我有些朋友喜歡搖滾樂，有些喜歡流行樂。", checkType:"someothers" },
  { en:"Tell me about your friends. Use a few or each other.", hint:"用 a few / few、each other", sample:"I have a few good friends, and we help each other.", sampleZh:"我有幾個好朋友，我們會互相幫忙。", checkType:"afew" }
];
