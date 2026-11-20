import re

PORTAL_ERROR_PATTERNS = [
    {
        "keywords": ["aadhaar", "mismatch", "name mismatch", "dob mismatch", "ఆధార్", "పేరు తేడా"],
        "error_type": "Aadhaar Demographic Mismatch",
        "title_en": "Name or Date of Birth Mismatch with Aadhaar",
        "title_te": "ఆధార్ కార్డుతో పేరు లేదా పుట్టిన తేదీ తేడా",
        "explanation_en": "The name or birth date entered in the application does not exactly match your official Aadhaar card records, including spelling and initials.",
        "explanation_te": "మీరు దరఖాస్తులో రాసిన పేరు లేదా పుట్టిన తేదీ, మీ ఆధార్ కార్డులోని అధికారిక వివరాలతో (అక్షరాలు, ఇంటిపేరు) సరిపోలడం లేదు.",
        "steps_en": [
            "Check your physical Aadhaar card and type the name EXACTLY as printed.",
            "If your Aadhaar card has an outdated name or spelling mistake, visit the nearest MeeSeva / Aadhaar Seva Kendra to update Aadhaar first.",
            "Ensure marital status or surname updates are updated in both bank passbook and Aadhaar."
        ],
        "steps_te": [
            "మీ చేతిలోని ఆధార్ కార్డును చూసి, అందులో ఉన్న విధంగానే అక్షరం పొల్లు పోకుండా టైప్ చేయండి.",
            "ఆధార్ కార్డులోనే పేరు తప్పుగా ఉంటే, మొదట సమీపంలోని ఆధార్ సేవా కేంద్రం లేదా మీసేవ వద్ద ఆధార్ వివరాలు సరిచేయించండి.",
            "బ్యాంకు ఖాతా పుస్తకంలో మరియు ఆధార్ కార్డులో ఒకే విధమైన పేరు ఉండేలా చూసుకోండి."
        ],
        "warning_en": "Never share your Aadhaar OTP with any unknown phone callers claiming to 'fix' your Aadhaar.",
        "warning_te": "ఆధార్ సమస్య సరిచేస్తామని ఫోన్ చేసి ఓటీపీ (OTP) అడిగితే ఎట్టిపరిస్థితుల్లోనూ ఎవరికీ చెప్పవద్దు."
    },
    {
        "keywords": ["ekyc", "biometric", "fingerprint", "iris", "బయోమెట్రిక్", "ఈకేవైసీ"],
        "error_type": "eKYC Biometric Authentication Failure",
        "title_en": "eKYC / Biometric Verification Failed",
        "title_te": "ఈ-కేవైసీ / వేలిముద్ర ధృవీకరణ విఫలమైంది",
        "explanation_en": "The fingerprint or facial scanner could not verify your identity with UIDAI, or your eKYC has expired.",
        "explanation_te": "వేలిముద్ర లేదా కంటిపాప స్కానర్ ద్వారా మీ ఆధార్ వివరాలు సరిపోలలేదు లేదా మీ ఈ-కేవైసీ గడువు ముగిసింది.",
        "steps_en": [
            "Clean and dry your fingertips thoroughly before scanning.",
            "Ask the Village Volunteer or Sachivalayam operator to try Iris (eye) scan or Facial recognition via Aadhaar FaceRD app.",
            "If biometric authentication consistently fails due to elderly age or worn fingerprints, update your biometrics at an Aadhaar Kendra."
        ],
        "steps_te": [
            "వేలిముద్ర వేసే ముందు చేతులను శుభ్రంగా కడిగి ఆరబెట్టుకోండి.",
            "వృద్ధులకు వేలిముద్రలు పడకపోతే, ఐరిస్ (కంటిపాప స్కానర్) లేదా గ్రామ సచివాలయంలో ఫేస్ అథెంటికేషన్ ప్రయత్నించండి.",
            "తరచూ విఫలమైతే ఆధార్ కేంద్రానికి వెళ్లి బయోమెట్రిక్స్ అప్‌డేట్ చేయించుకోండి."
        ],
        "warning_en": "Government staff will never ask you to pay unofficial extra fees for biometric eKYC.",
        "warning_te": "ఈ-కేవైసీ కోసం ఎవరికీ అనధికారికంగా అదనపు లంచాలు లేదా రుసుములు ఇవ్వవలసిన అవసరం లేదు."
    },
    {
        "keywords": ["otp", "session", "expired", "timeout", "కాలం ముగిసింది", "ఓటీపీ"],
        "error_type": "Session Expired / OTP Timeout",
        "title_en": "Session Expired or OTP Expired",
        "title_te": "సెషన్ గడువు ముగిసింది లేదా ఓటీపీ నిలిచిపోయింది",
        "explanation_en": "Government portals have strict 5-10 minute security timers. Inactivity or network delay resets the form.",
        "explanation_te": "ప్రభుత్వ పోర్టల్స్ భద్రత కోసం 5 నుండి 10 నిమిషాల సమయం మాత్రమే ఇస్తాయి. ఆలస్యం కావడం వల్ల పేజీ ఆగిపోయింది.",
        "steps_en": [
            "Close the browser tab, reopen the portal, and login afresh.",
            "Keep all required numbers (Ration card, Survey number, Aadhaar) written on paper before starting the form.",
            "Wait up to 2 minutes for mobile OTP; if not received, click 'Resend OTP' once."
        ],
        "steps_te": [
            "బ్రౌజర్ పేజీని మూసివేసి, మళ్ళీ మొదటి నుండి వెబ్‌సైట్ ఓపెన్ చేయండి.",
            "దరఖాస్తు ప్రారంభించే ముందే అవసరమైన నంబర్లు (రేషన్ కార్డు, సర్వే నంబర్) కాగితంపై రాసి సిద్ధంగా ఉంచుకోండి.",
            "మొబైల్ సిగ్నల్ బాగున్న చోట ఉండి ఓటీపీ ఎంటర్ చేయండి."
        ],
        "warning_en": "Official government OTPs are only valid for 5 to 10 minutes. Do not share them with strangers.",
        "warning_te": "ఓటీపీ కేవలం 5-10 నిమిషాలు మాత్రమే పనిచేస్తుంది. మీ ఫోన్‌కు వచ్చిన ఓటీపీని ఇతరులకు ఎప్పుడూ చెప్పకండి."
    },
    {
        "keywords": ["payment", "cfms", "debit", "failed", "డబ్బులు కట్", "చెల్లింపు"],
        "error_type": "Payment Pending or Deduction Without Receipt",
        "title_en": "Payment Deducted but Receipt Not Generated",
        "title_te": "బ్యాంకులో డబ్బులు కట్ అయ్యాయి కానీ రసీదు రాలేదు",
        "explanation_en": "Bank servers and government payment gateways sometimes delay transaction reconciliation.",
        "explanation_te": "బ్యాంకు సర్వర్ మరియు ప్రభుత్వ గేట్‌వే మధ్య లింక్ సమస్య వల్ల డబ్బులు డెబిట్ అయినప్పటికీ రసీదు వెంటనే రాకపోవచ్చు.",
        "steps_en": [
            "DO NOT make an immediate second payment.",
            "Wait 24 to 48 hours for automatic bank reconciliation.",
            "Note down the Bank Reference Number (UTR number) from your SMS.",
            "Check the 'Payment Status' tab on the portal using your application reference."
        ],
        "steps_te": [
            "వెంటనే రెండోసారి డబ్బులు చెల్లించవద్దు.",
            "24 నుండి 48 గంటలు వేచి ఉండండి. చాలా సందర్భాల్లో డబ్బులు తిరిగి మీ ఖాతాకు వస్తాయి లేదా దరఖాస్తు పూర్తవుతుంది.",
            "బ్యాంకు మెసేజ్‌లోని UTR నంబర్ లేదా రిఫరెన్స్ నంబర్ రాసి పెట్టుకోండి.",
            "గ్రామ సచివాలయంలో మీ దరఖాస్తు సంఖ్య చెప్పి స్టేటస్ తనిఖీ చేయించండి."
        ],
        "warning_en": "Never click unknown refund links sent by SMS or WhatsApp.",
        "warning_te": "డబ్బులు వాపస్ ఇస్తామంటూ వాట్సాప్ లేదా ఎస్ఎంఎస్ లో వచ్చే అనుమానాస్పద లింకులను ఎట్టి పరిస్థితుల్లో నొక్కవద్దు."
    },
    {
        "keywords": ["server", "500", "502", "503", "504", "down", "error", "సర్వర్"],
        "error_type": "Government Server Busy or Under Maintenance",
        "title_en": "Government Server Busy or Under Maintenance",
        "title_te": "ప్రభుత్వ సర్వర్ రద్దీగా ఉంది లేదా మరమ్మతుల్లో ఉంది",
        "explanation_en": "Due to thousands of citizens applying near deadlines, the portal server is experiencing heavy traffic load.",
        "explanation_te": "ఒకేసారి వేలాది మంది ప్రజలు దరఖాస్తు చేసుకోవడం వల్ల సర్వర్ రద్దీగా మారింది.",
        "steps_en": [
            "Try accessing the portal during non-peak hours (early morning 6 AM - 8 AM or after 8 PM).",
            "Clear browser cache or try an Incognito / Private browsing window.",
            "If applying in person, visit your Konanki Grama Sachivalayam operator."
        ],
        "steps_te": [
            "ఉదయం 6 నుండి 8 గంటల మధ్య లేదా రాత్రి 8 గంటల తర్వాత ప్రయత్నించండి, ఆ సమయంలో రద్దీ తక్కువగా ఉంటుంది.",
            "బ్రౌజర్ హిస్టరీ క్లియర్ చేసి మళ్ళీ చూడండి.",
            "సమస్య కొనసాగితే మీ గ్రామంలోని గ్రామ సచివాలయ సిబ్బందిని సంప్రదించండి."
        ],
        "warning_en": "Official portals never require you to install unauthorized third-party APKs to access government schemes.",
        "warning_te": "ప్రభుత్వ సేవల కోసం ప్లే స్టోర్ లో లేని ఏ యాప్‌లను (APK) డౌన్‌లోడ్ చేయవద్దు."
    }
]

class PortalErrorTool:
    @staticmethod
    def analyze_error(error_text, lang="te"):
        is_te = lang == "te"
        if not error_text or not error_text.strip():
            return {
                "matched": False,
                "message": "దయచేసి పోర్టల్ లో కనిపించిన ఎర్రర్ మెసేజ్ ను నమోదు చేయండి." if is_te else "Please provide the error message from the portal."
            }

        text_lower = error_text.lower()

        # Match against patterns
        best_match = None
        highest_score = 0

        for pattern in PORTAL_ERROR_PATTERNS:
            score = 0
            for kw in pattern["keywords"]:
                if kw in text_lower:
                    score += 1
            if score > highest_score:
                highest_score = score
                best_match = pattern

        if best_match and highest_score > 0:
            return {
                "matched": True,
                "error_type": best_match["error_type"],
                "title": best_match["title_te"] if is_te else best_match["title_en"],
                "explanation": best_match["explanation_te"] if is_te else best_match["explanation_en"],
                "steps": best_match["steps_te"] if is_te else best_match["steps_en"],
                "warning": best_match["warning_te"] if is_te else best_match["warning_en"]
            }

        # General helpful fallback
        return {
            "matched": False,
            "error_type": "General Portal Technical Issue",
            "title": "సాధారణ వెబ్‌సైట్ సాంకేతిక సమస్య" if is_te else "General Portal Technical Issue",
            "explanation": "మీరు పేర్కొన్న ఎర్రర్ సర్వర్ రద్దీ లేదా నెట్‌వర్క్ అంతరాయం వల్ల ఏర్పడి ఉండవచ్చు." if is_te else "The error described could be due to temporary server traffic or a network connection glitch.",
            "steps": [
                "బ్రౌజర్‌ను రిఫ్రెష్ చేయండి లేదా క్లోజ్ చేసి మళ్ళీ ఓపెన్ చేయండి.",
                "మీ మొబైల్ లేదా కంప్యూటర్ ఇంటర్నెట్ కనెక్షన్ సరిగ్గా ఉందో లేదో చూడండి.",
                "మీ కొనంకి గ్రామ సచివాలయంలోని డిజిటల్ అసిస్టెంట్ లేదా సంబంధిత అధికారిని సంప్రదించండి."
            ] if is_te else [
                "Refresh the browser page or restart the browser.",
                "Verify your internet and Wi-Fi connection.",
                "Visit your local Grama Sachivalayam Digital Assistant for on-ground verification."
            ],
            "warning": "ఎట్టి పరిస్థితుల్లోనూ మీ ఆధార్ ఓటీపీ, పాస్‌వర్డ్‌లను ఎవరితోనూ పంచుకోవద్దు." if is_te else "Never share your Aadhaar OTP or bank password with anyone under any circumstances."
        }
