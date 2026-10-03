const GRAMMAR_QUESTIONS = [
  { text:"The movie was so <span class='blank'>______</span> that I fell asleep.", options:["boring","bored","bore","to bore"], answer:0, note:"【第 1 週．形容詞】電影「令人」無聊，用 -ing：boring。" },
  { text:"She <span class='blank'>______</span> for two hours, so she is very tired now.", options:["has been running","runs","will run","is run"], answer:0, note:"【第 2 週．動詞形式】從過去持續到現在的動作，用現在完成進行式：has been running。" },
  { text:"By the time we arrived, the movie <span class='blank'>______</span>.", options:["had started","has started","starts","will start"], answer:0, note:"【第 2 週．動詞形式】by the time + 過去式，更早發生的事用過去完成式：had started。" },
  { text:"This time tomorrow, I <span class='blank'>______</span> on the beach.", options:["will be lying","lie","have lain","was lying"], answer:0, note:"【第 3 週．動詞形式】未來某個時間點正在進行的動作，用未來進行式：will be lying。" },
  { text:"He said that he <span class='blank'>______</span> tired.", options:["was","be","being","been"], answer:0, note:"【第 3 週．時態一致】主要子句是過去式 said，that 子句跟著用過去式：was。" },
  { text:"My bike <span class='blank'>______</span> by my father yesterday.", options:["was repaired","repaired","is repairing","has repaired"], answer:0, note:"【第 4 週．被動】腳踏車是「被修理」，過去式被動：was repaired。" },
  { text:"I had my hair <span class='blank'>______</span> last week.", options:["cut","cutting","to cut","cuts"], answer:0, note:"【第 4 週．使役】have + 物 + 過去分詞，表示請別人做：had my hair cut。" },
  { text:"The ground is wet. It <span class='blank'>______</span> last night.", options:["must have rained","must rain","should rain","can't rain"], answer:0, note:"【第 6 週．推測過去】對過去很有把握的推測：must have + p.p.。" },
  { text:"If I <span class='blank'>______</span> you, I would say sorry to her.", options:["were","am","be","will be"], answer:0, note:"【第 7 週．條件句】與現在事實相反，be 動詞一律用 were。" },
  { text:"If she had studied harder, she <span class='blank'>______</span> the test.", options:["would have passed","would pass","will pass","passes"], answer:0, note:"【第 7 週．條件句】與過去事實相反：If + had p.p., would have p.p.。" },
  { text:"I wish I <span class='blank'>______</span> fly like a bird.", options:["could","can","will","am able"], answer:0, note:"【第 8 週．假設語氣】wish 表示和現在事實相反的願望，用過去式：could。" },
  { text:"I look forward to <span class='blank'>______</span> you soon.", options:["seeing","see","saw","be seen"], answer:0, note:"【第 9 週．動名詞】look forward to 的 to 是介系詞，後面接 V-ing：seeing。" },
  { text:"This is the town <span class='blank'>______</span> I grew up.", options:["where","which","who","what"], answer:0, note:"【第 11 週．關係副詞】先行詞是地點，後面句子完整（I grew up），用 where。" },
  { text:"The girl <span class='blank'>______</span> next to me is my cousin.", options:["sitting","sits","sat","is sitting"], answer:0, note:"【第 12 週．縮減子句】句子已經有動詞 is，用分詞 sitting 修飾 the girl（= who is sitting）。" },
  { text:"Do you know <span class='blank'>______</span>?", options:["what time it is","what time is it","what is time","it is what time"], answer:0, note:"【第 13 週．間接問句】疑問詞 + 主詞 + 動詞，不倒裝：what time it is。" },
  { text:"<span class='blank'>______</span> from the hill, the city looks beautiful.", options:["Seen","Seeing","To see","Saw"], answer:0, note:"【第 14 週．分詞構句】城市是「被看」，被動用過去分詞：Seen。" },
  { text:"This road is <span class='blank'>______</span> wider than that one.", options:["much","very","more","so"], answer:0, note:"【第 16 週．比較】比較級要用 much、far、even 加強，不能用 very。" },
  { text:"Rarely <span class='blank'>______</span> late for class.", options:["is she","she is","does she","she does"], answer:0, note:"【第 17 週．倒裝】Rarely 放句首要倒裝；有 be 動詞就直接把 is 放前面：is she。" },
  { text:"The number of tourists <span class='blank'>______</span> increasing every year.", options:["is","are","were","have"], answer:0, note:"【第 18 週．主詞動詞一致】the number of 的主詞是 number，用單數 is。" },
  { text:"Each of the rooms <span class='blank'>______</span> a window.", options:["has","have","are having","having"], answer:0, note:"【第 18 週．主詞動詞一致】each of + 複數名詞，動詞用單數 has。" }
];

const READING_PASSAGE = {
  title:"Summer English Camp",
  html:`Are you looking for a fun way to improve your English? Our Summer English Camp, which has been held every July since 2015, is open to students aged 12 to 16. Not only will you take classes with teachers from different countries, but you will also go on trips to museums and night markets. Each of the students receives a free T-shirt.<br><br>
Students who sign up before June 1 will pay only NT$8,000, which is much cheaper than the regular price of NT$10,000. Had we known the camp would be so popular, we would have prepared more seats last year! This year, seats are limited, so don't wait. If you have any questions, please call 02-2345-6789.`
};

const READING_QUESTIONS = [
  { type:"閱讀理解", text:"What is this notice mainly about?", options:["An English camp for teenagers","A trip to a night market","A new museum in the city","A job for English teachers"], answer:0, note:"【主旨題】全文介紹給 12 到 16 歲學生參加的暑期英文營。" },
  { type:"閱讀理解", text:"Who can join the camp?", options:["Students aged 12 to 16","Students of any age","Only teachers","Students over 16"], answer:0, note:"【細節題】文章提到 is open to students aged 12 to 16。" },
  { type:"閱讀理解", text:"Since when has the camp been held?", options:["2015","2012","2016","Last year"], answer:0, note:"【細節題】文章提到 which has been held every July since 2015。" },
  { type:"閱讀理解", text:"How much will a student pay if he signs up on May 20?", options:["NT$8,000","NT$10,000","NT$12,000","Nothing"], answer:0, note:"【細節題】六月一日前報名只要 NT$8,000，五月二十日在六月一日之前。" },
  { type:"閱讀理解", text:"What can we infer about last year's camp?", options:["There were not enough seats.","Nobody joined it.","It was free.","It was held in December."], answer:0, note:"【推論題】Had we known it would be so popular, we would have prepared more seats = 去年位子不夠。" },
  { type:"文意選填", text:"Our Summer English Camp, ______ has been held every July since 2015, is open to students.（選出最適合填入文中空格的字）", options:["which","that","who","what"], answer:0, note:"【第 11 週】有逗號的非限定用法，指物用 which，不能用 that。" },
  { type:"文意選填", text:"Not only ______ you take classes with teachers from different countries…（選出最適合填入文中空格的字）", options:["will","you will","are","do you"], answer:0, note:"【第 17 週】Not only 放句首要倒裝：will you take。" },
  { type:"文意選填", text:"Each of the students ______ a free T-shirt.（選出最適合填入文中空格的字）", options:["receives","receive","receiving","are receiving"], answer:0, note:"【第 18 週】each of + 複數名詞，動詞用單數 receives。" },
  { type:"文意選填", text:"NT$8,000, which is ______ cheaper than the regular price…（選出最適合填入文中空格的字）", options:["much","very","more","most"], answer:0, note:"【第 16 週】比較級用 much 加強。" },
  { type:"文意選填", text:"______ we known the camp would be so popular, we would have prepared more seats.（選出最適合填入文中空格的字）", options:["Had","If","Have","Did"], answer:0, note:"【第 7、17 週】條件句省略 if 的倒裝：If we had known → Had we known。" }
];

const CLOZE_PASSAGE = {
  title:"A Letter from Canada",
  html:`Dear Grandma,<br>I (1)<span class='blank'>____</span> in Canada for two months now. The weather here is much colder (2)<span class='blank'>____</span> it is in Taiwan.<br><br>
Yesterday I visited a museum (3)<span class='blank'>____</span> was built 100 years ago. It was amazing! I wish you (4)<span class='blank'>____</span> here with me.<br>Love, Amy`
};

const CLOZE_QUESTIONS = [
  { type:"克漏字 (1)", text:"選出最適合填入空格 (1) 的字：", options:["have been","am","was","will be"], answer:0, note:"【第 2 週】for two months now 表示從過去到現在，用現在完成式：have been。" },
  { type:"克漏字 (2)", text:"選出最適合填入空格 (2) 的字：", options:["than","as","that","then"], answer:0, note:"【第 16 週】比較級 colder 後面接 than。" },
  { type:"克漏字 (3)", text:"選出最適合填入空格 (3) 的字：", options:["that","who","where","what"], answer:0, note:"【第 11 週】先行詞 a museum 是物，後面缺主詞，用 that（或 which）。" },
  { type:"克漏字 (4)", text:"選出最適合填入空格 (4) 的字：", options:["were","are","will be","be"], answer:0, note:"【第 8 週】wish 表示和現在事實相反，be 動詞用 were。" }
];

const LISTENING_QUESTIONS = [
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/bus.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The girl, who is wearing a backpack, is standing next to a school bus.", "The girl, which is wearing a backpack, is standing next to a school bus.", "The girl, who are wearing a backpack, is standing next to a school bus."], answer: 0,
    note: "【第 11 週】指人用 who，主詞 the girl 是單數用 is，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/laptop.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The woman has been working on her laptop for a while.", "The woman has been worked on her laptop for a while.", "The woman have been working on her laptop for a while."], answer: 0,
    note: "【第 2 週】現在完成進行式 has been + V-ing，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/kitchen.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["Dinner is being cooked by the woman.", "Dinner is cooking by the woman.", "Dinner is being cook by the woman."], answer: 0,
    note: "【第 4 週】進行式的被動是 is being + p.p.，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/girls-reading.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The girls look interested in their books.", "The girls look interesting in their books.", "The girls look interest in their books."], answer: 0,
    note: "【第 1 週】人「感到」有興趣用 interested，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/soccer.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The boy is getting ready to kick the ball.", "The boy is getting ready kicking the ball.", "The boy is getting ready kick the ball."], answer: 0,
    note: "【第 9 週】be ready + to V，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "How long have you been waiting here?", options: ["For about twenty minutes.", "Since twenty minutes.", "In twenty minutes."], answer: 0,
    note: "【第 2 週】How long 問一段時間，用 for，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "What would you do if you won the lottery?", options: ["I would travel around the world.", "I will travel around the world.", "I traveled around the world."], answer: 0,
    note: "【第 7 週】與現在事實相反的假設，回答用 would + 原形，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Why didn't you come to the party last night?", options: ["I had to finish my report.", "I'm going to the party tonight.", "Yes, I came to the party."], answer: 0,
    note: "【問答策略】Why 問原因，回答要說明理由，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Do you know where the post office is?", options: ["Yes, it's next to the bank.", "Yes, where is it?", "No, I don't know where is it."], answer: 0,
    note: "【第 13 週】直接告訴對方地點最合適；(C) 的 where is it 語序錯誤，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A woman says, Excuse me, is this seat taken? A man says, No, please sit down. Actually, I was just leaving. What will the man probably do next?",
    options: ["Leave", "Sit down next to her", "Buy a ticket"], answer: 0,
    note: "【轉折策略】Actually 後面是重點：I was just leaving，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A boy says, I should have brought my umbrella. A girl says, Don't worry. We can share mine. What is true about the boy?",
    options: ["He didn't bring an umbrella.", "He brought two umbrellas.", "He lost the girl's umbrella."], answer: 0,
    note: "【第 6 週】should have + p.p. 表示「當初應該做卻沒做」，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A man says, The concert was supposed to start at seven, but not until eight did it begin. A woman says, That's terrible! How late did the concert start?",
    options: ["One hour late", "Half an hour late", "On time"], answer: 0,
    note: "【第 17 週】not until eight did it begin 表示八點才開始，比原訂七點晚一小時，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A girl says, My mom made me clean my room before I could go out. A boy says, So did mine! Who had to clean their room?",
    options: ["Both of them", "Only the girl", "Only the boy"], answer: 0,
    note: "【第 4、17 週】So did mine 表示他媽媽也叫他打掃，所以兩個人都要，答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽廣播，選出最合理的答案。",
    audioQuestion: "Attention, students. Because of the typhoon, all classes tomorrow have been cancelled. The school library, which is usually open on weekends, will also be closed. Students who have questions should check the school website. What will happen tomorrow?",
    options: ["There will be no classes.", "Classes will start late.", "The library will open early."], answer: 0,
    note: "【英檢廣播題】all classes tomorrow have been cancelled，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽分享，選出最合理的答案。",
    audioQuestion: "Hello, everyone. I'd like to share how I improved my English. At first, I could hardly understand English movies. Then I started watching one English movie every week. The more I watched, the more I understood. If I hadn't kept practicing, I wouldn't have passed the test. What helped the speaker improve?",
    options: ["Watching English movies every week", "Taking a trip abroad", "Reading English newspapers"], answer: 0,
    note: "【第 16 週】The more I watched, the more I understood，所以答案是 (A)。"
  }
];

const VOCAB_QUESTIONS = [
  { word:"improve", text:"improve 這個字的中文意思最接近：", options:["改善、進步","放棄","忘記","借用"], answer:0, note:"improve (v.) 改善、使進步；名詞是 improvement。",
    example:"Reading every day can improve your English.", exampleZh:"每天閱讀可以讓你的英文進步。",
    scrambleSentence:"She has improved a lot this year.", zh:"她今年進步很多。" },
  { word:"regular", text:"regular 這個字的中文意思最接近：", options:["一般的、規律的","特別的","奇怪的","免費的"], answer:0, note:"regular (adj.) 規律的、一般的；regular price = 原價。",
    example:"The regular price is ten thousand dollars.", exampleZh:"原價是一萬元。",
    scrambleSentence:"Regular exercise is good for your health.", zh:"規律運動對健康有益。" },
  { word:"limited", text:"limited 這個字的中文意思最接近：", options:["有限的","無限的","便宜的","吵雜的"], answer:0, note:"limited (adj.) 有限的；limit (n./v.) 限制。",
    example:"Seats are limited, so sign up early.", exampleZh:"座位有限，所以要早點報名。",
    scrambleSentence:"We have limited time for the test.", zh:"我們考試的時間有限。" },
  { word:"cancel", text:"cancel 這個字的中文意思最接近：", options:["取消","舉辦","延長","參加"], answer:0, note:"cancel (v.) 取消；be cancelled = 被取消。",
    example:"The game was cancelled because of the rain.", exampleZh:"比賽因為下雨被取消了。",
    scrambleSentence:"All classes have been cancelled today.", zh:"今天所有的課都取消了。" },
  { word:"confident", text:"confident 這個字的中文意思最接近：", options:["有自信的","緊張的","害羞的","生氣的"], answer:0, note:"confident (adj.) 有自信的；名詞是 confidence。",
    example:"She feels confident about the test.", exampleZh:"她對考試很有信心。",
    scrambleSentence:"The more I practice, the more confident I feel.", zh:"我練習得越多，就越有自信。" },
  { word:"abroad", text:"abroad 這個字的中文意思最接近：", options:["在國外","在家裡","在樓上","在學校"], answer:0, note:"abroad (adv.) 在國外、到國外；study abroad = 出國留學。前面不加 to。",
    example:"He wants to study abroad.", exampleZh:"他想出國念書。",
    scrambleSentence:"My cousin has lived abroad for five years.", zh:"我表哥已經住在國外五年了。" },
  { word:"communicate", text:"communicate 這個字的中文意思最接近：", options:["溝通","比賽","計算","搬運"], answer:0, note:"communicate (v.) 溝通；名詞是 communication。",
    example:"English helps us communicate with people from other countries.", exampleZh:"英文幫助我們和其他國家的人溝通。",
    scrambleSentence:"We communicate by email every week.", zh:"我們每週用電子郵件聯絡。" },
  { word:"available", text:"available 這個字的中文意思最接近：", options:["可用的、有空的","昂貴的","危險的","破舊的"], answer:0, note:"available (adj.) 可取得的、有空的。",
    example:"Are you available this Friday?", exampleZh:"你這個星期五有空嗎？",
    scrambleSentence:"No seats are available now.", zh:"現在沒有空位了。" },
  { word:"register", text:"register 這個字的中文意思最接近：", options:["登記、報名","退出","延期","付錢"], answer:0, note:"register (v.) 登記、報名（= sign up）；名詞是 registration。",
    example:"You must register before June 1.", exampleZh:"你必須在六月一日前報名。",
    scrambleSentence:"I registered for the English test online.", zh:"我在網路上報名了英文考試。" },
  { word:"progress", text:"progress 這個字的中文意思最接近：", options:["進步、進展","錯誤","休息","比賽"], answer:0, note:"progress (n.) 進步、進展，不可數；make progress = 進步。",
    example:"You have made great progress.", exampleZh:"你進步很多。",
    scrambleSentence:"The teacher was happy with our progress.", zh:"老師對我們的進步很滿意。" }
];

const SPEAKING_QUESTIONS = [
  { en:"How long have you been learning English?", hint:"用 have been + V-ing，加上 for 或 since", sample:"I have been learning English for six years.", sampleZh:"我已經學英文六年了。", checkType:"perfprog_forsince" },
  { en:"If you had more free time, what would you do?", hint:"用 If + 過去式，would + 原形", sample:"If I had more free time, I would learn to play the piano.", sampleZh:"如果我有更多空閒時間，我會學彈鋼琴。", checkType:"cond2" },
  { en:"Who helps you the most? Tell me about this person.", hint:"用 who 引導的關係子句", sample:"The person who helps me the most is my mother.", sampleZh:"最常幫助我的人是我媽媽。", checkType:"relwho" },
  { en:"What do you like to do on weekends? Give a reason and an example.", hint:"用「回答 + because 理由 + For example 例子」", sample:"I like to go to the library on weekends because it is quiet. For example, last Saturday I read two books there.", sampleZh:"我週末喜歡去圖書館，因為那裡很安靜。例如上週六我在那裡讀了兩本書。", checkType:"reasonex" },
  { en:"Imagine a picture of students eating lunch in a school cafeteria. Describe the picture.", hint:"用 In this picture…、There are…、They are + V-ing", sample:"In this picture, there are some students in a cafeteria. They are eating lunch and talking. They seem to be very happy.", sampleZh:"這張圖裡，有幾個學生在餐廳。他們正在吃午餐和聊天，看起來很開心。", checkType:"describe" }
];
