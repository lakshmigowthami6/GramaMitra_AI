import re

class IntentClassifier:
    INTENTS = {
        "greeting": [
            r"\b(hello|hi|hey|namaste|vanakkam|నమస్కారం|హలో|బాగున్నారా)\b"
        ],
        "portal_error": [
            r"(error|failed|rejected|mismatch|timeout|expired|ekyc|biometric|payment failed|ఎర్రర్|విఫలమైంది|సమస్య|ఓటీపీ రావడం లేదు|డబ్బులు కట్|వేలిముద్ర)"
        ],
        "eligibility": [
            r"(eligible|eligibility|qualify|age limit|conditions|rules|అర్హత|అర్హుడినా|వయస్సు|నిబంధనలు|ఎవరు అర్హులు|ఎవరికి వస్తుంది)"
        ],
        "documents": [
            r"(document|documents|certificate|proof|passbook|aadhaar|కావాల్సిన పత్రాలు|సర్టిఫికెట్|ఆధార్|కాగితాలు|ఏమేం కావాలి)"
        ],
        "application_steps": [
            r"(how to apply|apply|procedure|steps|process|portal|meeseva|ఎలా దరఖాస్తు|దరఖాస్తు విధానం|ఎక్కడ దరఖాస్తు చేయాలి|స్టెప్స్|మీసేవ)"
        ],
        "digital_literacy": [
            r"(smartphone|phone|internet|wifi|browser|password|learn|digital|safety|స్మార్ట్‌ఫోన్|ఫోన్ వాడటం|ఇంటర్నెట్|నేర్చుకోవాలి|పాస్‌వర్డ్|డిజిటల్)"
        ],
        "scheme_details": [
            r"(tell me about|details of|about scheme|గురించి చెప్పు|వివరాలు|సమాచారం)"
        ],
        "scheme_discovery": [
            r"(schemes|welfare|farmer|agriculture|pension|housing|women|student|scholarship|పథకాలు|రైతు పథకాలు|పెన్షన్|ఇళ్ల పథకం|మహిళా పథకాలు|విద్యార్థులు)"
        ],
        "faq": [
            r"(faq|help|question|doubt|సహాయం|సందేహం|తరచుగా అడిగే ప్రశ్నలు)"
        ]
    }

    @classmethod
    def classify(cls, query_text):
        if not query_text or not query_text.strip():
            return "unknown"

        text = query_text.strip().lower()

        for intent, patterns in cls.INTENTS.items():
            for pat in patterns:
                if re.search(pat, text, re.IGNORECASE):
                    return intent

        return "scheme_discovery"  # Default fallback to discovery
