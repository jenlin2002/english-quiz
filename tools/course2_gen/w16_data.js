const GRAMMAR_QUESTIONS = [
  { text:"Tom is as <span class='blank'>______</span> as his father.", options:["tall","taller","tallest","more tall"], answer:0, note:"as…as 中間要用原級：as tall as。" },
  { text:"This test is not <span class='blank'>______</span> difficult as the last one.", options:["so","too","very","more"], answer:0, note:"否定的同級比較可以用 not as…as 或 not so…as。" },
  { text:"My room is <span class='blank'>______</span> as big as yours.", options:["twice","two","double times","second"], answer:0, note:"兩倍用 twice，放在 as…as 前面：twice as big as。" },
  { text:"This phone is <span class='blank'>______</span> cheaper than that one.", options:["very","much","more","so"], answer:1, note:"比較級要用 much、far、even、a lot 加強，不能用 very。" },
  { text:"The more you practice, <span class='blank'>______</span> you get.", options:["the better","better","the best","best"], answer:0, note:"「越…就越…」用 the + 比較級, the + 比較級，兩邊都要有 the。" },
  { text:"It is getting <span class='blank'>______</span>.", options:["colder and colder","cold and cold","more cold and cold","coldest and coldest"], answer:0, note:"「越來越…」用 比較級 and 比較級：colder and colder。" },
  { text:"Mount Jade is higher than any other <span class='blank'>______</span> in Taiwan.", options:["mountain","mountains","the mountains","mountain's"], answer:0, note:"than any other 後面接單數名詞：any other mountain。" },
  { text:"No other student in our class is <span class='blank'>______</span> than Amy.", options:["taller","tall","tallest","the tallest"], answer:0, note:"No other + 單數名詞 + 比較級 + than，用比較級表示最高級的意思。" },
  { text:"She is one of the best <span class='blank'>______</span> in our school.", options:["singers","singer","singing","sing"], answer:0, note:"one of the + 最高級 + 複數名詞：one of the best singers。" },
  { text:"This is the most interesting book I <span class='blank'>______</span> read.", options:["have ever","ever have","had never","am ever"], answer:0, note:"最高級 + (that) + 主詞 + have ever + p.p.，表示「我…過最…的」。" },
  { text:"The weather in Taipei is hotter than <span class='blank'>______</span> in Tokyo.", options:["that","those","it","one"], answer:0, note:"比較的對象要一致：weather 和 weather 比，用 that 代替單數的 the weather。" },
  { text:"I prefer tea <span class='blank'>______</span> coffee.", options:["to","than","from","with"], answer:0, note:"prefer A to B：比起 B 更喜歡 A，用 to 不用 than。" },
  { text:"I would rather stay home <span class='blank'>______</span> go out.", options:["than","to","or","from"], answer:0, note:"would rather A than B：寧願 A 也不要 B，A 和 B 都是原形動詞。" },
  { text:"Both Tom and Amy <span class='blank'>______</span> students.", options:["are","is","be","was"], answer:0, note:"both A and B 是兩個人，動詞用複數：are。" },
  { text:"Neither Tom nor his sisters <span class='blank'>______</span> at home.", options:["are","is","was","has"], answer:0, note:"neither…nor 用就近原則，動詞看最靠近的 his sisters（複數）：are。" },
  { text:"She likes reading, swimming, and <span class='blank'>______</span>.", options:["dancing","to dance","dance","danced"], answer:0, note:"平行結構：reading、swimming 都是 V-ing，第三個也要用 dancing。" },
  { text:"<span class='blank'>______</span> in 1990, the building is very old.（回收）", options:["Built","Building","Having building","To build"], answer:0, note:"建築物是「被建造」，被動的分詞構句用過去分詞：Built。" },
  { text:"<span class='blank'>______</span> the heavy traffic, we arrived on time.（回收）", options:["Despite","Although","Because","However"], answer:0, note:"後面是名詞 the heavy traffic，表示「儘管」用 despite。" },
  { text:"She studied hard <span class='blank'>______</span> she could pass the exam.（回收）", options:["so that","in order to","despite","however"], answer:0, note:"後面是子句 she could pass，表目的用 so that。" },
  { text:"It was late; <span class='blank'>______</span>, we kept working.（回收）", options:["however","although","despite","because"], answer:0, note:"前後意思相反，前面是分號，用副詞 however。" }
];

const READING_PASSAGE = {
  title:"City Life or Country Life?",
  html:`Is city life better than country life? Many young people think so. In the city, buses come much more often, and shops stay open later. Hospitals and schools are also closer. However, rent in the city can be twice as high as it is in the country, and the air is not as clean as it is in the countryside.<br><br>
The bigger a city grows, the busier its streets become. That is why more and more families are moving to small towns. Country life is not only quiet but also healthy. Neither the noise nor the traffic bothers people there. In my opinion, the best place to live is the one that fits your lifestyle.`
};

const READING_QUESTIONS = [
  { type:"閱讀理解", text:"What is the passage mainly about?", options:["Comparing life in the city and in the country","How to find a cheap hospital","The history of a small town","Why buses are always late"], answer:0, note:"全文比較城市生活和鄉村生活的優缺點。" },
  { type:"閱讀理解", text:"According to the passage, what is one advantage of city life?", options:["Buses come more often.","The air is cleaner.","Rent is cheaper.","The streets are quieter."], answer:0, note:"文章提到 In the city, buses come much more often。" },
  { type:"閱讀理解", text:"How high can rent in the city be?", options:["Twice as high as in the country","Half as high as in the country","As high as in the country","Three times as high as in the country"], answer:0, note:"文章提到 rent in the city can be twice as high as it is in the country。" },
  { type:"閱讀理解", text:"Why are more and more families moving to small towns?", options:["Cities are getting busier.","Small towns have more shops.","Rent in small towns is higher.","Buses in small towns come more often."], answer:0, note:"文章提到 The bigger a city grows, the busier its streets become. That is why…" },
  { type:"閱讀理解", text:"What is the writer's opinion?", options:["The best place depends on your lifestyle.","Everyone should live in the city.","Everyone should live in the country.","Small towns are too noisy."], answer:0, note:"文章最後提到 the best place to live is the one that fits your lifestyle。" },
  { type:"文意選填", text:"Rent in the city can be ______ as high as it is in the country.（選出最適合填入文中空格的字）", options:["twice","two","double","second"], answer:0, note:"倍數 + as…as，兩倍用 twice。" },
  { type:"文意選填", text:"The air is not as ______ as it is in the countryside.（選出最適合填入文中空格的字）", options:["clean","cleaner","cleanest","more clean"], answer:0, note:"not as…as 中間用原級：clean。" },
  { type:"文意選填", text:"The bigger a city grows, ______ its streets become.（選出最適合填入文中空格的字）", options:["the busier","busier","the busiest","more busy"], answer:0, note:"the + 比較級, the + 比較級：the busier。" },
  { type:"文意選填", text:"Country life is not only quiet but also ______.（選出最適合填入文中空格的字）", options:["healthy","health","healthily","to be healthy"], answer:0, note:"平行結構：quiet 是形容詞，but also 後面也要用形容詞 healthy。" },
  { type:"文意選填", text:"Neither the noise nor the traffic ______ people there.（選出最適合填入文中空格的字）", options:["bothers","bother","bothering","are bothering"], answer:0, note:"neither…nor 用就近原則，the traffic 是單數，動詞用 bothers。" }
];

const CLOZE_PASSAGE = {
  title:"My Two Best Friends",
  html:`Amy and Lily are my best friends. Amy is (1)<span class='blank'>____</span> tall as Lily, but Lily runs much (2)<span class='blank'>____</span> than Amy. Both Amy and Lily (3)<span class='blank'>____</span> music.<br><br>
Lily is not only a good singer but also a (4)<span class='blank'>____</span> dancer. The more time I spend with them, the happier I feel.`
};

const CLOZE_QUESTIONS = [
  { type:"克漏字 (1)", text:"選出最適合填入空格 (1) 的字：", options:["as","more","than","so much"], answer:0, note:"同級比較 as + 原級 + as：as tall as。" },
  { type:"克漏字 (2)", text:"選出最適合填入空格 (2) 的字：", options:["faster","fast","fastest","more fast"], answer:0, note:"後面有 than，much 加強比較級：much faster。" },
  { type:"克漏字 (3)", text:"選出最適合填入空格 (3) 的字：", options:["love","loves","loving","is loving"], answer:0, note:"Both A and B 是複數主詞，動詞用原形的 love。" },
  { type:"克漏字 (4)", text:"選出最適合填入空格 (4) 的字：", options:["great","greatly","greatness","to be great"], answer:0, note:"平行結構：a good singer 對 a great dancer，形容詞修飾名詞。" }
];

const LISTENING_QUESTIONS = [
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/library.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The library is as quiet as it can be.", "The library is as quieter as it can be.", "The library is as quietest as it can be."], answer: 0,
    note: "as…as 中間要用原級 quiet，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/grocery.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The woman is reaching for something on the highest shelf.", "The woman is reaching for something on the most high shelf.", "The woman is reaching for something on the higher shelf than."], answer: 0,
    note: "high 的最高級是 highest，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/kitchen.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["One pot is bigger than the other.", "One pot is big than the other.", "One pot is biggest than the other."], answer: 0,
    note: "兩個鍋子比大小，用比較級 bigger + than，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/girls-reading.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["Both girls are reading books.", "Both girls is reading books.", "Both girls are read books."], answer: 0,
    note: "both 表示兩個都，動詞用複數 are，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/lunch.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["The children are eating, talking, and laughing.", "The children are eating, talk, and to laugh.", "The children are eating, talked, and laugh."], answer: 0,
    note: "平行結構：三個動作都要用 V-ing，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Is your brother taller than you?", options: ["No, he is not as tall as I am.", "No, he is not as taller as I am.", "No, he is not so tall than I am."], answer: 0,
    note: "not as…as 中間用原級，後面用 as 不用 than，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Which do you like better, tea or coffee?", options: ["I prefer tea to coffee.", "I prefer tea than coffee.", "I prefer tea from coffee."], answer: 0,
    note: "prefer A to B，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Who is going to clean the classroom?", options: ["Either Tom or I am going to do it.", "Either Tom or I is going to do it.", "Either Tom nor I am going to do it."], answer: 0,
    note: "either…or 用就近原則，動詞看 I，用 am，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "How was the new movie?", options: ["It was much better than I expected.", "It was very better than I expected.", "It was more better than I expected."], answer: 0,
    note: "比較級用 much 加強，better 前面不能再加 more，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A girl says, My new phone cost twice as much as my old one. A boy says, How much was your old one? The girl says, Five thousand dollars. How much did the new phone cost?",
    options: ["Ten thousand dollars", "Five thousand dollars", "Two thousand five hundred dollars"], answer: 0,
    note: "新手機是舊手機的兩倍（twice as much as），五千的兩倍是一萬，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A man says, Would you like to go out for dinner tonight? A woman says, I'd rather stay home than go out. I'm really tired. What will the woman probably do?",
    options: ["Stay home", "Go to a restaurant", "Go shopping"], answer: 0,
    note: "I'd rather stay home than go out 表示她寧願待在家，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A boy says, Neither my sister nor my brother likes vegetables. A girl says, What about you? The boy says, I love them! Who likes vegetables?",
    options: ["The boy", "The boy's sister", "The boy's brother"], answer: 0,
    note: "neither…nor 表示姊姊和哥哥都不喜歡，只有男孩喜歡，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A woman says, This is the most delicious cake I have ever eaten. A man says, Thanks! I made it myself. What does the woman think of the cake?",
    options: ["It is the best cake she has ever eaten.", "It is too sweet for her.", "It is not as good as the last one."], answer: 0,
    note: "the most delicious cake I have ever eaten 表示她吃過最好吃的蛋糕，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽氣象報告，選出最合理的答案。",
    audioQuestion: "Good morning. Here is today's weather. It is getting colder and colder this week. Today will be even colder than yesterday, and tomorrow will be the coldest day of the week. Please wear a warm coat. Which day will be the coldest?",
    options: ["Tomorrow", "Today", "Yesterday"], answer: 0,
    note: "報告說 tomorrow will be the coldest day of the week，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽演講，選出最合理的答案。",
    audioQuestion: "Welcome to our school's reading club. Reading is not only fun but also useful. The more you read, the more words you learn. Students who read every day often do better than those who don't. So join us every Friday afternoon. According to the speaker, what happens when you read more?",
    options: ["You learn more words.", "You get more homework.", "You sleep less."], answer: 0,
    note: "The more you read, the more words you learn，所以答案是 (A)。"
  }
];

const VOCAB_QUESTIONS = [
  { word:"compare", text:"compare 這個字的中文意思最接近：", options:["比較","準備","宣布","借用"], answer:0, note:"compare (v.) 比較；compare A with B = 拿 A 和 B 比較。",
    example:"Don't compare yourself with others.", exampleZh:"不要拿自己和別人比較。",
    scrambleSentence:"We compared the two phones carefully.", zh:"我們仔細比較了這兩支手機。" },
  { word:"similar", text:"similar 這個字的中文意思最接近：", options:["相似的","危險的","昂貴的","安靜的"], answer:0, note:"similar (adj.) 相似的；be similar to = 和…相似。",
    example:"My bag is similar to yours.", exampleZh:"我的包包和你的很像。",
    scrambleSentence:"The two sisters look very similar.", zh:"這兩姊妹看起來很像。" },
  { word:"prefer", text:"prefer 這個字的中文意思最接近：", options:["比較喜歡","拒絕","忘記","修理"], answer:0, note:"prefer (v.) 比較喜歡；prefer A to B = 比起 B 更喜歡 A。",
    example:"I prefer walking to taking the bus.", exampleZh:"比起搭公車，我比較喜歡走路。",
    scrambleSentence:"Most students prefer summer to winter.", zh:"大部分學生喜歡夏天勝過冬天。" },
  { word:"convenient", text:"convenient 這個字的中文意思最接近：", options:["方便的","擁擠的","昂貴的","無聊的"], answer:0, note:"convenient (adj.) 方便的；名詞是 convenience。",
    example:"Living near the station is very convenient.", exampleZh:"住在車站附近很方便。",
    scrambleSentence:"The new store is more convenient for us.", zh:"新的商店對我們來說更方便。" },
  { word:"crowded", text:"crowded 這個字的中文意思最接近：", options:["擁擠的","乾淨的","安靜的","空曠的"], answer:0, note:"crowded (adj.) 擁擠的；crowd (n.) 人群。",
    example:"The train is crowded in the morning.", exampleZh:"早上的火車很擁擠。",
    scrambleSentence:"The night market was more crowded than usual.", zh:"夜市比平常更擁擠。" },
  { word:"rent", text:"rent 這個字的中文意思最接近：", options:["租金；租用","禮物","旅行","薪水"], answer:0, note:"rent (n.) 租金；(v.) 租用。",
    example:"The rent in this area is very high.", exampleZh:"這一區的房租很高。",
    scrambleSentence:"They rented a small house near the beach.", zh:"他們在海邊附近租了一間小房子。" },
  { word:"average", text:"average 這個字的中文意思最接近：", options:["平均的；一般的","特別的","最高的","免費的"], answer:0, note:"average (adj./n.) 平均（的）、一般的；on average = 平均來說。",
    example:"The average age of the players is sixteen.", exampleZh:"這些球員的平均年齡是十六歲。",
    scrambleSentence:"He is taller than the average student.", zh:"他比一般學生高。" },
  { word:"quality", text:"quality 這個字的中文意思最接近：", options:["品質","數量","價格","顏色"], answer:0, note:"quality (n.) 品質；quantity 是「數量」，不要搞混。",
    example:"This shop sells clothes of high quality.", exampleZh:"這家店賣高品質的衣服。",
    scrambleSentence:"Quality is more important than price.", zh:"品質比價格更重要。" },
  { word:"lifestyle", text:"lifestyle 這個字的中文意思最接近：", options:["生活方式","生日派對","圖書館","交通工具"], answer:0, note:"lifestyle (n.) 生活方式。",
    example:"A healthy lifestyle is important.", exampleZh:"健康的生活方式很重要。",
    scrambleSentence:"Country life fits my lifestyle better.", zh:"鄉村生活比較適合我的生活方式。" },
  { word:"traffic", text:"traffic 這個字的中文意思最接近：", options:["交通、車流","天氣","噪音","垃圾"], answer:0, note:"traffic (n.) 交通、車流；traffic jam = 塞車。",
    example:"The traffic is heavy in the city.", exampleZh:"城市裡的交通很繁忙。",
    scrambleSentence:"We were late because of the heavy traffic.", zh:"因為交通繁忙，我們遲到了。" }
];

const SPEAKING_QUESTIONS = [
  { en:"Compare yourself with someone in your family. Use as…as or not as…as.", hint:"用 as…as 或 not as…as", sample:"My sister is not as tall as I am.", sampleZh:"我妹妹沒有我高。", checkType:"asas" },
  { en:"Tell me about something that gets better the more you do it.", hint:"用 The + 比較級…, the + 比較級…", sample:"The more I read, the more I learn.", sampleZh:"我讀得越多，就學得越多。", checkType:"themore" },
  { en:"What is the best place in your city? Use than any other or one of the best.", hint:"用 than any other 或 one of the + 最高級", sample:"The night market is more interesting than any other place in my city.", sampleZh:"夜市比我城市裡其他任何地方都有趣。", checkType:"superlative" },
  { en:"What two sports or hobbies do you like?", hint:"用 both…and 或 either…or", sample:"I like both basketball and swimming.", sampleZh:"我籃球和游泳都喜歡。", checkType:"correl" },
  { en:"Describe your best friend. Use not only…but also.", hint:"用 not only…but also，前後形式要一樣", sample:"My best friend is not only funny but also helpful.", sampleZh:"我最好的朋友不但有趣，而且樂於助人。", checkType:"notonly" }
];
