from app.extensions import db
from app.models.faq import FAQ

def seed_faqs():
    faqs_data = [
        {
            "category": "General",
            "question_en": "What is GramaMitra AI and how does it help me?",
            "question_te": "గ్రామమిత్ర AI అంటే ఏమిటి? ఇది నాకు ఎలా సహాయం చేస్తుంది?",
            "answer_en": "GramaMitra AI is an AI-powered digital literacy and e-governance assistant created for rural citizens (specifically piloted for Konanki Village, Martur Mandal, Bapatla District). It helps you understand government welfare schemes, check eligibility rules, view required document checklists, learn how to use government portals, and troubleshoot online website errors in simple Telugu and English.",
            "answer_te": "గ్రామమిత్ర AI అనేది గ్రామీణ ప్రజల కోసం రూపొందించబడిన డిజిటల్ సహాయక వేదిక (ప్రత్యేకంగా బాపట్ల జిల్లా మార్టూరు మండలం కొనంకి గ్రామాన్ని దృష్టిలో ఉంచుకుని రూపొందించబడింది). ఇది ప్రభుత్వ సంక్షేమ పథకాలు, అర్హతలు, కావాల్సిన పత్రాలు, ఆన్‌లైన్ దరఖాస్తు విధానం మరియు కంప్యూటర్/మొబైల్ వాడకాన్ని సులభమైన తెలుగులో అర్థమయ్యేలా వివరిస్తుంది.",
            "keywords": "gramamitra, what is, konanki, martur, bapatla, purpose, గ్రామమిత్ర, పరిచయం",
            "official_reference": "Community Service Project (CSP) - Digital Literacy"
        },
        {
            "category": "Schemes",
            "question_en": "Where should I go to apply for Andhra Pradesh welfare schemes in my village?",
            "question_te": "మా గ్రామంలో సంక్షేమ పథకాలకు దరఖాస్తు చేసుకోవడానికి ఎక్కడికి వెళ్లాలి?",
            "answer_en": "You can visit your local Grama Sachivalayam (Village Secretariat) in Konanki. Meet the Welfare and Education Assistant (WEA) for pensions and educational schemes, or the Village Agriculture Assistant (VAA) at Rythu Bharosa Kendra (RBK) for farmer schemes. Alternatively, you can visit the nearest authorized MeeSeva centre.",
            "answer_te": "మీరు మీ కొనంకి గ్రామ సచివాలయాన్ని సందర్శించవచ్చు. పెన్షన్లు మరియు విద్యా పథకాల కోసం సంక్షేమ సహాయకుడిని (WEA), రైతు పథకాల కోసం రైతు భరోసా కేంద్రం (RBK) లోని గ్రామ వ్యవసాయ సహాయకుడిని (VAA) లేదా సమీప మీసేవ కేంద్రాన్ని సంప్రదించవచ్చు.",
            "keywords": "where to apply, sachivalayam, meeseva, rbk, konanki, సచివాలయం, ఎక్కడ దరఖాస్తు చేయాలి",
            "official_reference": "Grama Ward Sachivalayam Department, AP"
        },
        {
            "category": "Eligibility",
            "question_en": "Does the eligibility checker provide an official government approval?",
            "question_te": "ఈ వెబ్‌సైట్‌లోని అర్హత తనిఖీ అధికారిక ప్రభుత్వ ఆమోదం ఇస్తుందా?",
            "answer_en": "No. The GramaMitra AI Eligibility Checker provides preliminary guidance based strictly on verified rules stored in our database. It does not replace the official scrutiny conducted by Village Revenue Officers (VRO), MPDO, or government departments.",
            "answer_te": "లేదు. ఈ వెబ్‌సైట్‌లోని అర్హత తనిఖీ కేవలం ప్రాథమిక మార్గదర్శకత్వం మాత్రమే. ఇది అధికారిక ప్రభుత్వ నిర్ణయం కాదు. మీ గ్రామ సచివాలయం లేదా సంబంధిత అధికారులు క్షేత్రస్థాయిలో పరిశీలించి తుది నిర్ణయం తీసుకుంటారు.",
            "keywords": "official decision, guarantee, eligibility checker, అధికారిక ఆమోదం, గ్యారంటీ",
            "official_reference": "GramaMitra AI Policy Notice"
        },
        {
            "category": "Documents",
            "question_en": "What basic documents should every rural citizen always keep ready for government schemes?",
            "question_te": "ప్రభుత్వ పథకాల కోసం ప్రతి గ్రామీణ పౌరుడు ఎల్లప్పుడూ సిద్ధంగా ఉంచుకోవాల్సిన ప్రాథమిక పత్రాలు ఏమిటి?",
            "answer_en": "Every citizen should keep: 1) Aadhaar Card with updated mobile number, 2) Rice Card (BPL Ration Card), 3) Bank Passbook with active Aadhaar DBT seeding, 4) Caste and Income certificates (from MeeSeva), and 5) Land Pattadar Passbook / 1-B Adangal (for farmers).",
            "answer_te": "ప్రతి పౌరుడు: 1) మొబైల్ నంబర్ లింక్ అయిన ఆధార్ కార్డు, 2) రైస్ కార్డు (తెల్ల రేషన్ కార్డు), 3) డీబీటీ లింక్ అయిన బ్యాంక్ పాస్‌బుక్, 4) కుల, ఆదాయ ధృవీకరణ పత్రాలు (మీసేవ ద్వారా), మరియు 5) రైతులకు పట్టాదారు పాస్‌బుక్/1-B కాపీలను ఎల్లప్పుడూ భద్రంగా ఉంచుకోవాలి.",
            "keywords": "documents required, basic proofs, passbook, aadhaar, rice card, పత్రాలు, ఆధార్, రేషన్ కార్డు",
            "official_reference": "Civil Supplies & Revenue Department"
        },
        {
            "category": "Portal Errors",
            "question_en": "What should I do if my Aadhaar biometric fingerprint fails during eKYC?",
            "question_te": "ఈకేవైసీ సమయంలో వేలిముద్ర (బయోమెట్రిక్) పడకపోతే ఏం చేయాలి?",
            "answer_en": "If fingerprints do not scan properly (especially common in elderly citizens or farm workers), request the operator to perform: 1) Iris (Eye scanner) authentication, or 2) Face authentication via Aadhaar FaceRD app, or 3) Mobile OTP authentication if your mobile number is linked to Aadhaar.",
            "answer_te": "వృద్ధులకు లేదా వ్యవసాయ పనుల వల్ల వేలిముద్రలు సరిగ్గా పడకపోతే: 1) ఐరిస్ (కంటిపాప స్కానర్) ద్వారా, లేదా 2) ఆధార్ ఫేస్ రికగ్నిషన్ (ముఖాన్ని స్కాన్ చేయడం) ద్వారా, లేదా 3) మొబైల్‌కు వచ్చే ఓటీపీ ద్వారా ఈకేవైసీ పూర్తి చేయవచ్చు.",
            "keywords": "fingerprint failed, biometric, ekyc, iris, face auth, వేలిముద్ర పడలేదు, బయోమెట్రిక్ సమస్య",
            "official_reference": "UIDAI Guidelines"
        },
        {
            "category": "Digital Safety",
            "question_en": "Someone calls claiming my government scheme money is ready and asks for an OTP. What should I do?",
            "question_te": "ప్రభుత్వ పథకం డబ్బులు పడతాయని చెప్పి ఎవరైనా ఫోన్ చేసి ఓటీపీ (OTP) అడిగితే ఏం చేయాలి?",
            "answer_en": "NEVER share any OTP, PIN, or password with anyone over the phone. Government officers and banks will NEVER call you to ask for your OTP. If you share the OTP, cyber criminals can empty your bank account immediately. Hang up and report to cyber crime helpline 1930.",
            "answer_te": "ఎట్టి పరిస్థితుల్లోనూ మీ మొబైల్‌కు వచ్చిన ఓటీపీ (OTP) లేదా బ్యాంక్ వివరాలను ఫోన్‌లో ఎవరికీ చెప్పవద్దు! ప్రభుత్వ అధికారులు ఎప్పుడూ ఫోన్ చేసి ఓటీపీ అడగరు. ఎవరైనా అడిగితే వెంటనే ఫోన్ కట్ చేసి, సైబర్ క్రైమ్ టోల్ ఫ్రీ నంబర్ 1930 కు ఫిర్యాదు చేయండి.",
            "keywords": "otp fraud, phone scam, safety, bank fraud, ఓటీపీ మోసం, సైబర్ నేరం, 1930",
            "official_reference": "National Cyber Crime Reporting Portal (cybercrime.gov.in)"
        }
    ]

    for f_data in faqs_data:
        existing = FAQ.query.filter_by(question_en=f_data["question_en"]).first()
        if not existing:
            faq = FAQ(
                category=f_data["category"],
                question_en=f_data["question_en"],
                question_te=f_data["question_te"],
                answer_en=f_data["answer_en"],
                answer_te=f_data["answer_te"],
                keywords=f_data["keywords"],
                official_reference=f_data["official_reference"]
            )
            db.session.add(faq)

    db.session.commit()
    print("Verified FAQs seeded successfully.")
