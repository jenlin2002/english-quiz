const GRAMMAR_QUESTIONS = [
  { text:"The box is too heavy for me <span class='blank'>______</span>.", options:["to carry","carrying","carried","carry"], answer:0, note:"【第 1 週】too + 形容詞 + (for 人) + to V：太…而不能…。" },
  { text:"I <span class='blank'>______</span> my homework before my mom came home.", options:["had finished","have finished","finish","am finishing"], answer:0, note:"【第 2 週】在過去某件事（mom came home）之前完成的動作，用過去完成式。" },
  { text:"By next June, I <span class='blank'>______</span> here for ten years.", options:["will have lived","will live","have lived","lived"], answer:0, note:"【第 3 週】By + 未來時間，到那時已經完成的事，用未來完成式。" },
  { text:"The road <span class='blank'>______</span> now, so we have to go another way.", options:["is being repaired","is repairing","repairs","has repaired"], answer:0, note:"【第 4 週】路「正在被」修理，進行式被動：is being + p.p.。" },
  { text:"She got her car <span class='blank'>______</span> yesterday.", options:["washed","wash","washing","to wash"], answer:0, note:"【第 4 週】get + 物 + p.p.：請人把某物處理好。" },
  { text:"You <span class='blank'>______</span> have told me earlier! I waited for an hour.", options:["should","must","will","shall"], answer:0, note:"【第 6 週】should have + p.p.：當初應該做卻沒做（責備、後悔）。" },
  { text:"I'd rather <span class='blank'>______</span> at home tonight.", options:["stay","to stay","staying","stayed"], answer:0, note:"【第 6 週】would rather + 原形動詞。" },
  { text:"If I had taken the medicine last night, I <span class='blank'>______</span> better now.", options:["would feel","would have felt","will feel","felt"], answer:0, note:"【第 7 週】混合條件句：過去沒吃藥（had p.p.），影響現在（now）→ would + 原形。" },
  { text:"I wish I <span class='blank'>______</span> harder last year.", options:["had studied","studied","have studied","would study"], answer:0, note:"【第 8 週】wish 表示和過去事實相反（last year），用 had + p.p.。" },
  { text:"It's high time we <span class='blank'>______</span> home.", options:["went","go","will go","going"], answer:0, note:"【第 8 週】It's (high) time + 主詞 + 過去式：早該…了。" },
  { text:"Remember <span class='blank'>______</span> the door when you leave.", options:["to lock","locking","lock","locked"], answer:0, note:"【第 9 週】remember to V：記得要去做（還沒做）。" },
  { text:"He stopped <span class='blank'>______</span> because it was bad for his health.", options:["smoking","to smoke","smoke","smoked"], answer:0, note:"【第 9 週】stop V-ing：停止做某事；stop to V 是「停下來去做」，意思不合。" },
  { text:"The boy <span class='blank'>______</span> father is a doctor is my classmate.", options:["whose","who","whom","which"], answer:0, note:"【第 11 週】後面接名詞 father，表示「誰的」，用 whose。" },
  { text:"You can invite <span class='blank'>______</span> you like to the party.", options:["whoever","whatever","which","what"], answer:0, note:"【第 12 週】whoever = anyone who，指「任何人」。" },
  { text:"She asked me <span class='blank'>______</span> I had seen her keys.", options:["if","that","what","which"], answer:0, note:"【第 13 週】轉述 yes/no 問句，用 if 或 whether。" },
  { text:"<span class='blank'>______</span> finished his homework, he went to bed.", options:["Having","Had","Have","To have"], answer:0, note:"【第 14 週】完成式分詞構句：Having + p.p.，表示比主句更早發生。" },
  { text:"I like summer, <span class='blank'>______</span> my brother likes winter.", options:["whereas","despite","so that","because"], answer:0, note:"【第 14 週】對比兩個人的喜好，用 whereas。" },
  { text:"No other city in Taiwan is <span class='blank'>______</span> than Taipei.", options:["more crowded","crowded","the most crowded","most crowded"], answer:0, note:"【第 16 週】No other + 單數名詞 + 比較級 + than：用比較級表示最高級。" },
  { text:"Not only <span class='blank'>______</span> English, but he also speaks Japanese.", options:["does he speak","he speaks","he does speak","speaks he"], answer:0, note:"【第 17 週】Not only 放句首，前半句要倒裝：does he speak。" },
  { text:"Five kilometers <span class='blank'>______</span> a long way to walk.", options:["is","are","were","have been"], answer:0, note:"【第 18 週】距離當成一個整體，用單數 is。" }
];

const READING_PASSAGE = {
  title:"The Robot Teacher",
  html:`Last year, a school in Taipei started using a robot to help teach English. The robot, which can speak five languages, answers students' questions and corrects their pronunciation. Not only does it never get tired, but it also remembers every student's name.<br><br>
However, a number of parents are worried. They argue that students need real teachers who can understand their feelings. If the school had asked parents first, there might have been less trouble. Now the school says the robot will only be used as a helper, not as a teacher.`
};

const READING_QUESTIONS = [
  { type:"閱讀理解", text:"What is the passage mainly about?", options:["A school using a robot to help teach English","A robot that plays soccer","How to build a robot","A teacher who speaks five languages"], answer:0, note:"【主旨題】全文講一所學校用機器人協助英文教學，以及家長的反應。" },
  { type:"閱讀理解", text:"Why are some parents worried?", options:["They think students need teachers who understand their feelings.","The robot is too expensive.","The robot can't speak English.","The robot often gets tired."], answer:0, note:"【細節題】文章提到 students need real teachers who can understand their feelings。" },
  { type:"閱讀理解", text:"How will the robot be used from now on?", options:["As a helper","As the only teacher","As a security guard","It will not be used at all."], answer:0, note:"【細節題】文章最後提到 the robot will only be used as a helper, not as a teacher。" },
  { type:"文意選填", text:"The robot, ______ can speak five languages, answers students' questions.（選出最適合填入文中空格的字）", options:["which","that","who","what"], answer:0, note:"【第 11 週】有逗號的非限定用法，指物用 which，不能用 that。" },
  { type:"文意選填", text:"However, a number of parents ______ worried.（選出最適合填入文中空格的字）", options:["are","is","was","has"], answer:0, note:"【第 18 週】a number of = many，後面接複數動詞 are。" }
];

const CLOZE_PASSAGE = {
  title:"My English Journey",
  html:`When I started junior high, I (1)<span class='blank'>____</span> hardly say a word in English. My teacher encouraged me (2)<span class='blank'>____</span> English songs every day.<br><br>
(3)<span class='blank'>____</span> I practiced, the more I enjoyed it. Now I am preparing (4)<span class='blank'>____</span> the GEPT, and I feel more confident than ever.`
};

const CLOZE_QUESTIONS = [
  { type:"克漏字 (1)", text:"選出最適合填入空格 (1) 的字：", options:["could","can","will","have"], answer:0, note:"【時態】When I started junior high 是過去，用 could。" },
  { type:"克漏字 (2)", text:"選出最適合填入空格 (2) 的字：", options:["to sing","singing","sing","sang"], answer:0, note:"【第 9 週】encourage + 人 + to V：鼓勵某人做某事。" },
  { type:"克漏字 (3)", text:"選出最適合填入空格 (3) 的字：", options:["The more","More","The most","Most"], answer:0, note:"【第 16 週】the + 比較級, the + 比較級：越…就越…。" },
  { type:"克漏字 (4)", text:"選出最適合填入空格 (4) 的字：", options:["for","to","with","at"], answer:0, note:"【片語】prepare for + 考試或活動：為…做準備。" }
];

const LISTENING_QUESTIONS = [
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/lunch.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The children, who are sitting at a table, are eating lunch.", "The children, which are sitting at a table, are eating lunch.", "The children, who is sitting at a table, are eating lunch."], answer: 0,
    note: "【第 11 週】指人用 who，children 是複數用 are，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/grocery.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The woman is reaching for something that is on the top shelf.", "The woman is reaching for something who is on the top shelf.", "The woman is reaching for something what is on the top shelf."], answer: 0,
    note: "【第 11 週】先行詞 something 是物，用 that，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/library.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["Having found an interesting book, the young man is reading it carefully.", "Having find an interesting book, the young man is reading it carefully.", "Have found an interesting book, the young man is reading it carefully."], answer: 0,
    note: "【第 14 週】完成式分詞構句：Having + p.p.（found），所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/laptop.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The woman seems to be busy working on her laptop.", "The woman seems to be busy to work on her laptop.", "The woman seems to be busy work on her laptop."], answer: 0,
    note: "【第 9 週】be busy + V-ing：忙著做某事，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/soccer.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The other children are watching the boy kick the ball.", "The other children are watching the boy to kick the ball.", "The other children are watching the boy kicked the ball."], answer: 0,
    note: "【感官動詞】watch + 受詞 + 原形或 V-ing，不能接 to V，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Have you ever been to Japan?", options: ["Yes, I went there last summer.", "Yes, I have gone there last summer.", "Yes, I go there last summer."], answer: 0,
    note: "【第 2 週】有明確的過去時間 last summer，用過去式 went，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Would you mind opening the window?", options: ["Not at all.", "Yes, I'd be happy to.", "I'm minding it."], answer: 0,
    note: "【第 9 週】Would you mind…? 是問「你介意嗎」，同意幫忙要說 Not at all（不介意），所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "What were you doing at nine last night?", options: ["I was watching TV.", "I will watch TV.", "I have watched TV."], answer: 0,
    note: "【時態】問過去某個時間點正在做什麼，用過去進行式，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Do you know why Tom was absent today?", options: ["I heard that he was sick.", "I heard that was he sick.", "I heard why was he sick."], answer: 0,
    note: "【第 13 週】that 子句用直述語序：he was sick，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A girl says, I can't believe I failed the test. A boy says, You should have studied harder. The girl says, I know. I spent too much time playing games. Why did the girl fail the test?",
    options: ["She didn't study enough.", "The test was too easy.", "She was sick."], answer: 0,
    note: "【第 6 週】You should have studied harder 和 I spent too much time playing games 表示她讀書不夠，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A man says, If I had left earlier, I wouldn't have missed the train. A woman says, Don't worry. The next one comes in twenty minutes. What happened to the man?",
    options: ["He missed the train.", "He arrived early.", "He took a taxi."], answer: 0,
    note: "【第 7 週】與過去事實相反：他其實沒有早出門，所以錯過了火車，答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A woman says, Which do you like better, the blue shirt or the white one? A man says, I'd rather have the white one. It's cheaper than the blue one. Which shirt will the man probably choose?",
    options: ["The white one", "The blue one", "Neither of them"], answer: 0,
    note: "【第 6、16 週】I'd rather have the white one，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A boy says, Neither my brother nor I have been to Kenting. A girl says, Really? It's one of the most beautiful places in Taiwan. Has the boy been to Kenting?",
    options: ["No, he hasn't.", "Yes, with his brother.", "Yes, many times."], answer: 0,
    note: "【第 16 週】Neither my brother nor I 表示兩個人都沒去過，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽廣播，選出最合理的答案。",
    audioQuestion: "Welcome to the National Science Museum. The museum, which opened in 1990, has more than one hundred rooms. Photos may be taken in most rooms, but not in the dinosaur hall. Not until five o'clock will the museum close today. Where are visitors not allowed to take photos?",
    options: ["In the dinosaur hall", "In the gift shop", "In every room"], answer: 0,
    note: "【英檢廣播題】Photos may be taken in most rooms, but not in the dinosaur hall，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽老師的話，選出最合理的答案。",
    audioQuestion: "Good morning, class. Today is our last lesson of the semester. I'm proud of all of you. The more you practiced, the better your English became. Remember that learning doesn't stop here. I hope that each of you will keep reading English every day. What does the teacher hope the students will do?",
    options: ["Keep reading English every day", "Take a long vacation", "Stop studying for a while"], answer: 0,
    note: "【英檢談話題】I hope that each of you will keep reading English every day，所以答案是 (A)。"
  }
];

const VOCAB_QUESTIONS = [
  { word:"opportunity", text:"opportunity 這個字的中文意思最接近：", options:["機會","責任","危險","理由"], answer:0, note:"opportunity (n.) 機會。（第 7 週）",
    example:"Studying abroad is a great opportunity.", exampleZh:"出國念書是很棒的機會。",
    scrambleSentence:"Don't miss this opportunity to learn.", zh:"不要錯過這個學習的機會。" },
  { word:"decision", text:"decision 這個字的中文意思最接近：", options:["決定","問題","比賽","意外"], answer:0, note:"decision (n.) 決定；make a decision = 做決定。（第 7 週）",
    example:"It was a difficult decision.", exampleZh:"那是個困難的決定。",
    scrambleSentence:"She made a decision to study harder.", zh:"她決定要更用功。" },
  { word:"evidence", text:"evidence 這個字的中文意思最接近：", options:["證據","秘密","意見","習慣"], answer:0, note:"evidence (n.) 證據，不可數。（第 6 週）",
    example:"The police found new evidence.", exampleZh:"警方找到了新的證據。",
    scrambleSentence:"There is no evidence that he did it.", zh:"沒有證據顯示是他做的。" },
  { word:"habit", text:"habit 這個字的中文意思最接近：", options:["習慣","愛好","節日","規則"], answer:0, note:"habit (n.) 習慣；a good habit = 好習慣。（第 9 週）",
    example:"Reading before bed is a good habit.", exampleZh:"睡前閱讀是好習慣。",
    scrambleSentence:"It is hard to change a bad habit.", zh:"改掉壞習慣很難。" },
  { word:"tradition", text:"tradition 這個字的中文意思最接近：", options:["傳統","科技","紀念品","比賽"], answer:0, note:"tradition (n.) 傳統；形容詞是 traditional。（第 12 週）",
    example:"Eating mooncakes is a Mid-Autumn tradition.", exampleZh:"吃月餅是中秋節的傳統。",
    scrambleSentence:"Every family has its own traditions.", zh:"每個家庭都有自己的傳統。" },
  { word:"opinion", text:"opinion 這個字的中文意思最接近：", options:["意見、看法","問題","工作","假期"], answer:0, note:"opinion (n.) 意見、看法；in my opinion = 依我看。（第 14 週）",
    example:"In my opinion, the robot is very useful.", exampleZh:"依我看，這個機器人很有用。",
    scrambleSentence:"Everyone has a right to give an opinion.", zh:"每個人都有權利表達意見。" },
  { word:"convenient", text:"convenient 這個字的中文意思最接近：", options:["方便的","擁擠的","昂貴的","危險的"], answer:0, note:"convenient (adj.) 方便的。（第 16 週）",
    example:"The MRT is fast and convenient.", exampleZh:"捷運又快又方便。",
    scrambleSentence:"Online shopping is more convenient than going to a store.", zh:"網路購物比去商店更方便。" },
  { word:"kindness", text:"kindness 這個字的中文意思最接近：", options:["仁慈、好意","力量","速度","財富"], answer:0, note:"kindness (n.) 仁慈、好意。（第 17 週）",
    example:"Never will I forget your kindness.", exampleZh:"我永遠不會忘記你的好意。",
    scrambleSentence:"Small acts of kindness make a big difference.", zh:"小小的善行能帶來很大的改變。" },
  { word:"survey", text:"survey 這個字的中文意思最接近：", options:["調查","考試","報告","旅行"], answer:0, note:"survey (n./v.) 調查。（第 18 週）",
    example:"The survey shows that most students sleep too little.", exampleZh:"調查顯示大部分學生睡得太少。",
    scrambleSentence:"We did a survey about school lunches.", zh:"我們做了一份關於學校午餐的調查。" },
  { word:"pronunciation", text:"pronunciation 這個字的中文意思最接近：", options:["發音","文法","拼字","翻譯"], answer:0, note:"pronunciation (n.) 發音；動詞是 pronounce。",
    example:"Your pronunciation is very clear.", exampleZh:"你的發音很清楚。",
    scrambleSentence:"The robot can correct our pronunciation.", zh:"這個機器人可以糾正我們的發音。" }
];

const SPEAKING_QUESTIONS = [
  { en:"Compare two seasons. Which do you like better? Use as…as or not as…as.", hint:"用 as…as 或 not as…as", sample:"Winter is not as hot as summer, so I like it better.", sampleZh:"冬天沒有夏天那麼熱，所以我比較喜歡冬天。", checkType:"asas" },
  { en:"Tell me about something you have never done. Start with Never have I…", hint:"用 Never have I + p.p. 的倒裝句", sample:"Never have I traveled to another country.", sampleZh:"我從來沒有出國旅行過。", checkType:"neverinv" },
  { en:"Tell me about a mistake you made. What should you have done?", hint:"用 should have + p.p.", sample:"I should have gone to bed earlier before the test.", sampleZh:"考試前我應該早點睡的。", checkType:"shouldhave" },
  { en:"If you could live anywhere in the world, where would you live?", hint:"用 If + 過去式，would + 原形", sample:"If I could live anywhere, I would live in Japan.", sampleZh:"如果我可以住在任何地方，我會住在日本。", checkType:"cond2" },
  { en:"Tell me about your class. Use Everyone or Each of.", hint:"用 Everyone / Each of… + 單數動詞", sample:"Everyone in my class works hard, and each of us has a dream.", sampleZh:"我們班每個人都很努力，每個人都有夢想。", checkType:"everyone" }
];
