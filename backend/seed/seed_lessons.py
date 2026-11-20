import json
from app.extensions import db
from app.models.lesson import DigitalLiteracyLesson, LessonQuiz

def seed_lessons():
    lessons_data = [
        {
            "id": "smartphone-basics-1",
            "module_category": "Smartphone Basics",
            "title_en": "Getting Started with Your Smartphone",
            "title_te": "స్మార్ట్‌ఫోన్ ప్రాథమిక అంశాలు & బటన్లు",
            "summary_en": "Learn about the power button, volume controls, touch gestures, and connecting to Wi-Fi safely.",
            "summary_te": "స్మార్ట్‌ఫోన్ బటన్లు, టచ్ స్క్రీన్ వాడకం, వాల్యూమ్ పెంచడం మరియు వై-ఫై లేదా మొబైల్ డేటా ఆన్ చేయడం నేర్చుకోండి.",
            "reading_time_minutes": 4,
            "order_index": 1,
            "icon_name": "Smartphone",
            "content_en": """### 📱 Understanding Smartphone Buttons & Gestures

Welcome to digital literacy! A smartphone is like a pocket computer that helps you talk, read news, and access government services.

#### 1. The Key Physical Buttons
* **Power Button (Side):** Press once briefly to wake up or lock the screen. Press and hold for 3 seconds to Turn Off or Restart your phone.
* **Volume Buttons (Side):** Press upper button to increase sound (for calls and ringers), press lower button to reduce volume.

#### 2. Essential Touch Screen Gestures
* **Tap (నొక్కడం):** Touch lightly once with your finger to open an app or click a button.
* **Scroll (పైకి లేదా కిందకు లాగడం):** Swipe your finger up or down gently to read a long page.
* **Zoom (దగ్గరకు జరపడం):** Place two fingers on a photo or map and spread them apart to make text larger and easier to read!

#### 3. Turning on Mobile Data or Wi-Fi
1. Swipe down from the very top of your screen to open the Quick Settings shade.
2. Tap the **Mobile Data** icon (two vertical arrows) to connect to your phone's internet.
3. If at home or Sachivalayam, tap the **Wi-Fi** icon (fan shape) to connect to wireless internet.""",
            "content_te": """### 📱 స్మార్ట్‌ఫోన్ బటన్లు & టచ్ స్క్రీన్ ఉపయోగించే విధానం

డిజిటల్ అక్షరాస్యత కేంద్రానికి స్వాగతం! స్మార్ట్‌ఫోన్ అనేది మీ చేతిలో ఉండే చిన్న కంప్యూటర్ వంటిది. ఇది ప్రభుత్వ పథకాలు, వార్తలు మరియు సమాచారం తెలుసుకోవడానికి ఎంతగానో ఉపయోగపడుతుంది.

#### 1. ముఖ్యమైన బటన్లు
* **పవర్ బటన్ (Power Button):** స్క్రీన్ వెలగడానికి లేదా ఆపడానికి పక్కన ఉండే ఈ బటన్‌ను ఒకసారి నొక్కండి. ఫోన్ స్విచ్ ఆఫ్ లేదా రీస్టార్ట్ చేయాలంటే 3 సెకన్లు నొక్కి పట్టి ఉంచాలి.
* **వాల్యూమ్ బటన్లు (Volume Buttons):** ఫోన్ మాట్లాడేటప్పుడు లేదా పాటలు వినేటప్పుడు శబ్దం పెంచడానికి పై బటన్, తగ్గించడానికి కింది బటన్ నొక్కండి.

#### 2. స్క్రీన్‌ను ఎలా తాకాలి (టచ్ గెస్చర్స్)
* **ట్యాప్ (స్పర్శించడం):** ఏదైనా యాప్ తెరవడానికి మీ వేలితో స్క్రీన్‌పై ఒకసారి సున్నితంగా నొక్కండి.
* **స్క్రోల్ (పైకి కిందకు జరపడం):** పొడవైన వార్తలు లేదా దరఖాస్తు చదివేటప్పుడు వేలితో స్క్రీన్‌ను పైకి లేదా కిందకు లాగండి.
* **జూమ్ (అక్షరాలు పెద్దవి చేయడం):** చిన్న అక్షరాలు కనిపించకపోతే రెండు వేళ్లను స్క్రీన్‌పై పెట్టి దూరం జరిపితే అక్షరాలు పెద్దవవుతాయి!

#### 3. ఇంటర్నెట్ (మొబైల్ డేటా) ఆన్ చేయడం
1. స్క్రీన్ పై భాగం నుండి కిందకు వేలితో లాగండి (నోటిఫికేషన్ బార్ తెరుచుకుంటుంది).
2. రెండు బాణం గుర్తులు ఉన్న **Mobile Data** బటన్‌ను తాకితే ఇంటర్నెట్ ఆన్ అవుతుంది.""",
            "quizzes": [
                {
                    "question_en": "What should you do if text on a webpage or photo is too small to read?",
                    "question_te": "స్క్రీన్‌పై ఉన్న అక్షరాలు చాలా చిన్నగా ఉండి చదవడానికి కష్టంగా ఉంటే ఏం చేయాలి?",
                    "options_en": ["Turn off the phone", "Pinch and spread two fingers apart to zoom in", "Press the power button 10 times", "Shake the phone"],
                    "options_te": ["ఫోన్ స్విచ్ ఆఫ్ చేయాలి", "రెండు వేళ్లతో స్క్రీన్‌పై జూమ్ చేసి అక్షరాలు పెద్దవి చేయాలి", "పవర్ బటన్ 10 సార్లు నొక్కాలి", "ఫోన్‌ను గట్టిగా ఊపాలి"],
                    "correct_index": 1,
                    "explanation_en": "Spreading two fingers apart on the touchscreen magnifies (zooms in) text and images.",
                    "explanation_te": "స్క్రీన్‌పై రెండు వేళ్లను పెట్టి దూరం జరపడం (Pinch to Zoom) ద్వారా అక్షరాలను స్పష్టంగా పెద్దవి చేసి చదువుకోవచ్చు."
                }
            ]
        },
        {
            "id": "internet-search-2",
            "module_category": "Internet Basics",
            "title_en": "Surfing the Internet & Identifying Official Websites",
            "title_te": "ఇంటర్నెట్ బ్రౌజింగ్ & అసలైన ప్రభుత్వ వెబ్‌సైట్ల గుర్తింపు",
            "summary_en": "Understand web browsers, how to search in Telugu, and how to verify legitimate government (.gov.in) web addresses.",
            "summary_te": "క్రోమ్ బ్రౌజర్ వాడటం, గూగుల్ లో వెతకడం మరియు నకిలీ వెబ్‌సైట్లను కాకుండా అధికారిక .gov.in సైట్లను గుర్తించడం.",
            "reading_time_minutes": 5,
            "order_index": 2,
            "icon_name": "Globe",
            "content_en": """### 🌐 The Internet, Browsers, and Web Addresses

The internet connects millions of computers worldwide. Here is how to browse safely and find what you need.

#### 1. What is a Web Browser?
A browser is an application that opens websites. On your Android phone, look for the **Google Chrome** app (the round red, yellow, green, and blue icon).

#### 2. How to Search in Telugu or English
1. Open Google Chrome.
2. In the white search box in the middle, type what you want to know (for example: *'PM Kisan Konanki Martur'* or *'ఆంధ్రప్రదేశ్ పెన్షన్ లిస్ట్'*).
3. You can also tap the **Microphone icon** inside the search box and speak in Telugu!

#### 3. Golden Rule: Identifying Official Government Websites
Scammers often create fake websites to steal your personal information. Always check the ending of the web address:
* ✅ **Official Indian Government sites ALWAYS end with `.gov.in` or `.nic.in`** (e.g., `pmkisan.gov.in`, `sspensions.ap.gov.in`, `ap.gov.in`).
* ❌ Commercial websites end with `.com`, `.in`, `.org`, or `.xyz` (e.g., `pmkisan-online.com` is FAKE).
* 🔒 Always check for the padlock icon in the browser address bar indicating an encrypted secure connection.""",
            "content_te": """### 🌐 ఇంటర్నెట్ వాడకం & అసలైన ప్రభుత్వ వెబ్‌సైట్ల గుర్తింపు

ఇంటర్నెట్ ద్వారా ప్రపంచంలోని ఏ సమాచారాన్నైనా క్షణాల్లో మన మొబైల్‌లో చూడవచ్చు.

#### 1. బ్రౌజర్ అంటే ఏమిటి?
వెబ్‌సైట్లను తెరవడానికి ఉపయోగించే యాప్‌ను బ్రౌజర్ అంటారు. మీ ఆండ్రాయిడ్ ఫోన్‌లో **Google Chrome** (ఎరుపు, పసుపు, ఆకుపచ్చ, నీలం రంగుల చక్రం గుర్తు) ప్రధాన బ్రౌజర్.

#### 2. గూగుల్‌లో సమాచారం వెతకడం
1. గూగుల్ క్రోమ్ యాప్ ఓపెన్ చేయండి.
2. మధ్యలో తెల్లటి సెర్చ్ బార్‌లో మీకు కావాల్సిన విషయాన్ని టైప్ చేయండి (ఉదాహరణకు: *పీఎం కిసాన్ అర్హతలు* లేదా *NTR భరోసా పెన్షన్*).
3. టైప్ చేయడం కష్టమైతే, పక్కనే ఉన్న **మైక్రోఫోన్ (మైక్) గుర్తు** నొక్కి తెలుగులోనే మాట్లాడి వెతకవచ్చు!

#### 3. అత్యంత ముఖ్యమైన సూత్రం: అసలైన ప్రభుత్వ వెబ్‌సైట్‌ను ఎలా గుర్తించాలి?
మోసగాళ్లు ప్రజలను బురిడీ కొట్టించడానికి ప్రభుత్వ సైట్లలాగే ఉండే నకిలీ వెబ్‌సైట్లను సృష్టిస్తారు. అసలైన వెబ్‌సైట్‌ను గుర్తించే విధానం:
* ✅ **భారత ప్రభుత్వ మరియు ఆంధ్రప్రదేశ్ అధికారిక వెబ్‌సైట్ల చివర తప్పనిసరిగా `.gov.in` లేదా `.nic.in` ఉంటుంది** (ఉదాహరణ: `pmkisan.gov.in`, `ap.gov.in`).
* ❌ ప్రైవేట్ లేదా నకిలీ సైట్ల చివర `.com`, `.xyz`, `.club` అని ఉంటుంది. వాటిని ఎట్టి పరిస్థితుల్లోనూ నమ్మవద్దు.
* 🔒 అడ్రస్ బార్ పక్కన తాళం గుర్తు (లాక్ సింబల్) ఉంటే ఆ సైట్ సురక్షితమైనదని అర్థం.""",
            "quizzes": [
                {
                    "question_en": "Which of the following is an authentic official government website address?",
                    "question_te": "కింది వాటిలో అసలైన అధికారిక ప్రభుత్వ వెబ్‌సైట్ అడ్రస్ ఏది?",
                    "options_en": ["www.pmkisan-yojana-free-money.com", "https://pmkisan.gov.in", "www.pmkisan2025.xyz", "www.ap-govt-schemes.org"],
                    "options_te": ["www.pmkisan-yojana-free-money.com", "https://pmkisan.gov.in", "www.pmkisan2025.xyz", "www.ap-govt-schemes.org"],
                    "correct_index": 1,
                    "explanation_en": "Only domains ending with .gov.in are officially registered and operated by the Government of India.",
                    "explanation_te": "కేవలం .gov.in లేదా .nic.in తో ముగిసే వెబ్‌సైట్లు మాత్రమే భారత ప్రభుత్వ అధికారిక వెబ్‌సైట్లు."
                }
            ]
        },
        {
            "id": "digital-safety-3",
            "module_category": "Digital Safety & Fraud",
            "title_en": "Protecting Yourself from Online Fraud & OTP Scams",
            "title_te": "ఆన్‌లైన్ భద్రత & ఓటీపీ (OTP) మోసాల నివారణ",
            "summary_en": "Crucial guidelines on never sharing OTPs, recognizing fake lottery SMS, avoiding suspicious WhatsApp links, and dialing 1930.",
            "summary_te": "ఓటీపీ ఎవరికీ చెప్పకపోవడం, నకిలీ లాటరీ కాల్స్ నమ్మకపోవడం మరియు మోసం జరిగితే 1930 టోల్‌ఫ్రీ నంబర్‌కు ఫిర్యాదు చేయడం.",
            "reading_time_minutes": 5,
            "order_index": 3,
            "icon_name": "ShieldAlert",
            "content_en": """### 🛡️ Digital Safety: Protecting Your Bank Account & Personal Data

Smartphones make life convenient, but rural citizens are increasingly targeted by cyber fraudsters. Follow these simple safety rules:

#### 1. What is an OTP (One-Time Password)?
An OTP is a 4 or 6-digit secret code sent via SMS to verify transactions or logins. **An OTP is like the key to your bank locker.**
* ⚠️ **RULE #1:** Never read out or forward an OTP to anyone over phone call or WhatsApp, even if they claim to be a Bank Manager, Village Volunteer, or Government Officer. Real officers NEVER ask for your OTP!

#### 2. Beware of Common Scams Targeting Rural Citizens
* **"Your Electricity Bill is Overdue" SMS:** Threatens power will be cut tonight at 9:30 PM with a phone number. This is 100% FAKE.
* **"PM Kisan / Housing Bonus Approved" WhatsApp Links:** Sends a link asking you to click and claim ₹25,000. Clicking installs harmful virus apps.
* **"Lottery / Lucky Draw" Phone Calls:** Asks you to deposit ₹2,000 processing fee to receive a car or ₹5 lakh. Never pay!

#### 3. Emergency Action if Defrauded
1. Call your bank immediately and ask them to **BLOCK** your ATM card and Net Banking.
2. Dial the National Cyber Crime Helpline **1930** (Toll-Free, 24/7).
3. Report the fraud at the nearest Martur Police Station or online at `cybercrime.gov.in`.""",
            "content_te": """### 🛡️ డిజిటల్ భద్రత: మీ బ్యాంక్ ఖాతాను మరియు సమాచారాన్ని కాపాడుకోండి

స్మార్ట్‌ఫోన్లు మనకు ఎంతో సౌకర్యాన్ని ఇస్తున్నాయి, కానీ గ్రామీణ ప్రజలను లక్ష్యంగా చేసుకుని సైబర్ మోసగాళ్లు రకరకాల దారుల్లో డబ్బులు కొట్టేస్తున్నారు.

#### 1. ఓటీపీ (OTP) అంటే ఏమిటి?
ఓటీపీ అనేది బ్యాంక్ లావాదేవీలు లేదా దరఖాస్తులను నిర్ధారించడానికి మీ ఫోన్‌కు ఎస్ఎంఎస్ ద్వారా వచ్చే 4 లేదా 6 అంకెల రహస్య కోడ్. **ఓటీపీ అనేది మీ బ్యాంక్ బీరువా తాళంచెవి లాంటిది.**
* ⚠️ **మొదటి సూత్రం:** మీ ఫోన్‌కు వచ్చిన ఓటీపీని ఎట్టి పరిస్థితుల్లోనూ ఎవరికీ ఫోన్‌లో చదివి చెప్పవద్దు. బ్యాంక్ మేనేజర్, ప్రభుత్వ అధికారి లేదా వాలంటీర్ అని చెప్పినా సరే సరే ఎవరికీ చెప్పకూడదు. అసలైన బ్యాంక్ అధికారులు ఎప్పుడూ ఓటీపీ అడగరు!

#### 2. గ్రామీణ ప్రజలను మోసం చేసే సాధారణ పద్ధతులు
* **"కరెంట్ బిల్లు కట్టకపోతే రాత్రికి విద్యుత్ సరఫరా నిలిపివేస్తాం" అనే మెసేజ్‌లు:** ఇది పూర్తి మోసం. దీనికి స్పందించి ఏ నంబర్లకూ ఫోన్ చేయవద్దు.
* **"పీఎం కిసాన్ డబ్బులు విడుదలయ్యాయి, ఈ లింక్ నొక్కండి" అని వచ్చే వాట్సాప్ మెసేజ్‌లు:** గుర్తు తెలియని లింకులను నొక్కితే మీ ఫోన్ హ్యాక్ అయి బ్యాంక్ ఖాతా ఖాళీ అవుతుంది.
* **లాటరీ లేదా కారు గెలుచుకున్నారు అంటూ వచ్చే కాల్స్:** ప్రాసెసింగ్ ఫీజు కింద ₹1000 లేదా ₹2000 కట్టమంటారు. ఒక్క రూపాయి కూడా కట్టవద్దు.

#### 3. ఒకవేళ పొరపాటున మోసపోతే వెంటనే ఏం చేయాలి?
1. వెంటనే మీ బ్యాంకును సంప్రదించి ఖాతాను లేదా ఏటీఎం కార్డును బ్లాక్ చేయించండి.
2. జాతీయ సైబర్ క్రైమ్ హెల్ప్‌లైన్ నంబర్ **1930** కి వెంటనే ఫోన్ చేయండి (ఉచితం, 24 గంటలు పనిచేస్తుంది).
3. మార్టూరు పోలీసు స్టేషన్ లేదా `cybercrime.gov.in` లో ఫిర్యాదు చేయండి.""",
            "quizzes": [
                {
                    "question_en": "If an unknown caller claiming to be a bank official asks for your OTP to credit your scheme money, what should you do?",
                    "question_te": "బ్యాంక్ మేనేజర్‌ను మాట్లాడుతున్నానని, మీ పథకం డబ్బులు జమ చేయడానికి ఓటీపీ చెప్పాలని అడిగితే మీరు ఏం చేయాలి?",
                    "options_en": ["Give the OTP immediately", "Ask for half the money first", "Refuse to give the OTP and hang up the call immediately", "Share your ATM card PIN instead"],
                    "options_te": ["వెంటనే ఓటీపీ చెప్పాలి", "సగం డబ్బులు పంపిన తర్వాత చెబుతాననాలి", "ఓటీపీ ఎట్టి పరిస్థితుల్లో చెప్పకుండా వెంటనే ఫోన్ కట్ చేయాలి", "ఓటీపీ కాకుండా ఏటీఎం పిన్ చెప్పాలి"],
                    "correct_index": 2,
                    "explanation_en": "Legitimate bank and government officials will NEVER ask for your confidential OTP over the phone.",
                    "explanation_te": "అసలైన బ్యాంక్ లేదా ప్రభుత్వ అధికారులు ఎప్పుడూ ఫోన్ చేసి మీ రహస్య ఓటీపీని అడగరు. అడిగితే వారు కచ్చితంగా మోసగాళ్లే."
                }
            ]
        },
        {
            "id": "govt-portals-4",
            "module_category": "Government Portals",
            "title_en": "How to Use MeeSeva & Sachivalayam Services Online",
            "title_te": "మీసేవ & గ్రామ సచివాలయ ఆన్‌లైన్ సేవల వినియోగం",
            "summary_en": "Learn how to check your application status, download official certificates, and track government welfare benefits safely.",
            "summary_te": "ఆన్‌లైన్ లో దరఖాస్తు స్టేటస్ తనిఖీ చేసుకోవడం, సర్టిఫికెట్లు డౌన్‌లోడ్ చేసుకోవడం మరియు రసీదు సంఖ్యను భద్రపరుచుకోవడం.",
            "reading_time_minutes": 5,
            "order_index": 4,
            "icon_name": "Landmark",
            "content_en": """### 🏛️ Navigating Government Portals & Citizen Services

Andhra Pradesh provides extensive digital services through Grama Ward Sachivalayam and MeeSeva. Here is how to use them with confidence:

#### 1. The Power of Your Application Reference Number
Whenever you submit an application (for a caste certificate, income certificate, or welfare scheme) at MeeSeva or Sachivalayam, you receive an **Acknowledgement Slip**.
* Keep this slip safe! The 12-to-15 digit number (e.g., `APP12345678`) allows you to check status anytime.

#### 2. How to Track Application Status Online
1. Open your browser and go to `gramawardsachivalayam.ap.gov.in` or `meeseva.ap.gov.in`.
2. Find the **Check Application Status** search bar on the homepage.
3. Enter your Application Reference Number or Aadhaar Number.
4. The system will clearly display whether the application is:
   * **Under Scrutiny (పరిశీలనలో ఉంది):** Official is currently checking your papers.
   * **Approved (ఆమోదించబడింది):** Your certificate is ready to download or collect.
   * **Rejected (తిరస్కరించబడింది):** Reason for rejection will be listed (e.g., missing proof).

#### 3. Overcoming Website Timeouts
If a portal displays "Session Expired" or blank screen:
* Do not panic or submit twice.
* Close the browser tab and wait 5 minutes before opening the page again.""",
            "content_te": """### 🏛️ మీసేవ & గ్రామ సచివాలయ ఆన్‌లైన్ సేవల వినియోగం

ఆంధ్రప్రదేశ్ ప్రభుత్వం గ్రామ/వార్డు సచివాలయాలు మరియు మీసేవ ద్వారా ప్రజలకు అవసరమైన సర్టిఫికెట్లు, సేవలను ఆన్‌లైన్‌లో అందిస్తోంది.

#### 1. దరఖాస్తు రసీదు సంఖ్య (Acknowledgement Number) ప్రాముఖ్యత
మీరు సచివాలయంలో లేదా మీసేవలో కుల ధృవీకరణ పత్రం, ఆదాయ సర్టిఫికెట్ లేదా ఏదైనా సంక్షేమ పథకానికి దరఖాస్తు చేసినప్పుడు మీకు ఒక **రసీదు కాగితం (Acknowledgment Slip)** ఇస్తారు.
* ఈ రసీదును ఎప్పుడూ పోగొట్టుకోకండి! అందులో ఉండే 12 నుండి 15 అంకెల నంబర్ ద్వారా మీ పని ఎంతవరకు వచ్చిందో ఇంట్లో కూర్చునే ఫోన్‌లో తెలుసుకోవచ్చు.

#### 2. ఆన్‌లైన్‌లో దరఖాస్తు స్టేటస్ ఎలా తనిఖీ చేయాలి?
1. మీ మొబైల్ బ్రౌజర్‌లో `gramawardsachivalayam.ap.gov.in` వెబ్‌సైట్ ఓపెన్ చేయండి.
2. హోమ్ పేజీలో **'Know Your Application Status'** అనే ఆప్షన్ ఎంచుకోండి.
3. మీ దరఖాస్తు సంఖ్య (Application Number) లేదా ఆధార్ నంబర్ నమోదు చేయండి.
4. మీ దరఖాస్తు ఏ దశలో ఉందో స్పష్టంగా కనిపిస్తుంది:
   * **పరిశీలనలో ఉంది (In Progress):** అధికారులు మీ కాగితాలను పరిశీలిస్తున్నారు.
   * **ఆమోదించబడింది (Approved):** మీ సర్టిఫికెట్ సిద్ధంగా ఉంది, సచివాలయంలో ప్రింట్ తీసుకోవచ్చు.
   * **తిరస్కరించబడింది (Rejected):** ఏ కారణం వల్ల తిరస్కరణ జరిగిందో వివరంగా ఉంటుంది.

#### 3. వెబ్‌సైట్ ఎర్రర్ వస్తే ఏం చేయాలి?
స్క్రీన్‌పై "Session Expired" లేదా "Error" అని వస్తే కంగారుపడకుండా, పేజీని మూసివేసి 5 నిమిషాల తర్వాత మళ్ళీ ఓపెన్ చేయండి.""",
            "quizzes": [
                {
                    "question_en": "What is the most important information needed to track the progress of your government service application online?",
                    "question_te": "ఆన్‌లైన్‌లో మీ దరఖాస్తు ఏ దశలో ఉందో తనిఖీ చేయడానికి అత్యంత ముఖ్యమైన వివరాలు ఏవి?",
                    "options_en": ["Bank account PIN", "Application Reference Number from the acknowledgment slip", "Email password", "Electricity meter serial number"],
                    "options_te": ["బ్యాంక్ ఖాతా ఏటీఎం పిన్", "రసీదుపై ఉన్న దరఖాస్తు రిఫరెన్స్ సంఖ్య (Application Reference Number)", "ఈమెయిల్ పాస్‌వర్డ్", "కరెంట్ మీటర్ సీరియల్ నంబర్"],
                    "correct_index": 1,
                    "explanation_en": "The application reference number printed on the MeeSeva or Sachivalayam acknowledgment receipt is the primary tracking key.",
                    "explanation_te": "మీసేవ లేదా సచివాలయంలో దరఖాస్తు చేసినప్పుడు ఇచ్చే రసీదుపై ఉండే రిఫరెన్స్ నంబర్ ద్వారా ఆన్‌లైన్‌లో స్టేటస్ తెలుసుకోవచ్చు."
                }
            ]
        }
    ]

    for l_data in lessons_data:
        existing = DigitalLiteracyLesson.query.get(l_data["id"])
        if not existing:
            lesson = DigitalLiteracyLesson(
                id=l_data["id"],
                module_category=l_data["module_category"],
                title_en=l_data["title_en"],
                title_te=l_data["title_te"],
                summary_en=l_data["summary_en"],
                summary_te=l_data["summary_te"],
                content_en=l_data["content_en"],
                content_te=l_data["content_te"],
                reading_time_minutes=l_data["reading_time_minutes"],
                order_index=l_data["order_index"],
                icon_name=l_data.get("icon_name", "BookOpen")
            )
            db.session.add(lesson)
            db.session.commit()

            # Seed quizzes
            for q_data in l_data.get("quizzes", []):
                quiz = LessonQuiz(
                    lesson_id=lesson.id,
                    question_en=q_data["question_en"],
                    question_te=q_data["question_te"],
                    options_json_en=json.dumps(q_data["options_en"], ensure_ascii=False),
                    options_json_te=json.dumps(q_data["options_te"], ensure_ascii=False),
                    correct_index=q_data["correct_index"],
                    explanation_en=q_data["explanation_en"],
                    explanation_te=q_data["explanation_te"]
                )
                db.session.add(quiz)
            db.session.commit()

    print("Verified digital literacy lessons and quizzes seeded successfully.")
