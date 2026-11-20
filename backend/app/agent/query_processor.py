import re

KNOWN_SCHEME_ALIASES = {
    "pm-kisan": ["pm kisan", "pm-kisan", "పీఎం కిసాన్", "రైతు సమ్మాన్"],
    "annadata-sukhibhava": ["annadata", "sukhibhava", "rythu bharosa", "అన్నదాత సుఖీభవ", "రైతు భరోసా"],
    "ntr-bharosa-pension": ["pension", "ntr bharosa", "ysr pension", "వృద్ధాప్య పెన్షన్", "పెన్షన్ కానుక", "విధవరాలు పెన్షన్"],
    "thalliki-vandanam": ["thalliki vandanam", "amma vodi", "తల్లికి వందనం", "అమ్మ ఒడి", "స్కూలు పథకం"],
    "aarogyasri": ["aarogyasri", "ayushman bharat", "ఆరోగ్యశ్రీ", "ఆయుష్మాన్ భారత్", "ఆసుపత్రి కార్డు", "హెల్త్ కార్డు"],
    "pmay-gramin": ["pmay", "housing", "pedalandariki illu", "ఇళ్ల స్థలాలు", "ప్రధానమంత్రి ఆవాస్", "ఇల్లు"],
    "jagananna-vidya-deevena": ["vidya deevena", "fee reimbursement", "విద్యా దీవెన", "ఫీజు రీయింబర్స్‌మెంట్"],
}

class QueryProcessor:
    @staticmethod
    def detect_language(text):
        if not text:
            return "te"
        # Telugu Unicode range is \u0C00 - \u0C7F
        telugu_chars = len(re.findall(r"[\u0C00-\u0C7F]", text))
        total_letters = len(re.findall(r"\w", text))
        if total_letters > 0 and (telugu_chars / total_letters) > 0.15:
            return "te"
        return "en"

    @staticmethod
    def extract_scheme_id(text):
        if not text:
            return None
        text_lower = text.lower()
        for scheme_id, aliases in KNOWN_SCHEME_ALIASES.items():
            for alias in aliases:
                if alias in text_lower:
                    return scheme_id
        return None

    @staticmethod
    def extract_category(text):
        if not text:
            return None
        text_lower = text.lower()
        categories = {
            "Agriculture": ["farmer", "farming", "crop", "land", "రైతు", "వ్యవసాయం", "పంట", "భూమి"],
            "Social Security": ["pension", "widow", "elderly", "disabled", "పెన్షన్", "వృద్ధులు", "వికలాంగులు"],
            "Education": ["student", "school", "college", "scholarship", "fee", "విద్యార్థి", "చదువు", "ఫీజు"],
            "Healthcare": ["health", "hospital", "treatment", "card", "వైద్యం", "ఆసుపత్రి", "చికిత్స"],
            "Housing": ["house", "housing", "pmay", "ఇల్లు", "గృహనిర్మాణం", "ఇళ్ల స్థలం"],
            "Women Welfare": ["women", "dwcra", "mother", "మహిళ", "డ్వాక్రా", "తల్లి"],
        }
        for cat, kws in categories.items():
            for kw in kws:
                if kw in text_lower:
                    return cat
        return None
