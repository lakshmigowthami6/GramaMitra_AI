from app.extensions import db
from app.models.official_source import OfficialSource
from app.models.scheme import GovernmentScheme
from app.models.eligibility import EligibilityCriterion
from app.models.document import RequiredDocument
from app.models.application_step import ApplicationStep

def seed_official_sources_and_schemes():
    # 1. Sources
    source_pmk = OfficialSource.query.filter_by(title="PM-KISAN Official Portal").first()
    if not source_pmk:
        source_pmk = OfficialSource(
            title="PM-KISAN Official Portal",
            official_url="https://pmkisan.gov.in",
            department="Ministry of Agriculture & Farmers Welfare, GoI",
            verification_date="2025-01-15",
            category="Agriculture"
        )
        db.session.add(source_pmk)

    source_ap_agri = OfficialSource.query.filter_by(title="AP Agriculture & Annadata Sukhibhava Portal").first()
    if not source_ap_agri:
        source_ap_agri = OfficialSource(
            title="AP Agriculture & Annadata Sukhibhava Portal",
            official_url="https://annadathasukhibhava.ap.gov.in",
            department="Department of Agriculture, Government of Andhra Pradesh",
            verification_date="2025-01-20",
            category="Agriculture"
        )
        db.session.add(source_ap_agri)

    source_pension = OfficialSource.query.filter_by(title="NTR Bharosa / SSPensions Portal").first()
    if not source_pension:
        source_pension = OfficialSource(
            title="NTR Bharosa / SSPensions Portal",
            official_url="https://sspensions.ap.gov.in",
            department="Panchayat Raj & Rural Development Department, GoAP",
            verification_date="2025-02-01",
            category="Social Security"
        )
        db.session.add(source_pension)

    source_edu = OfficialSource.query.filter_by(title="Department of School Education AP").first()
    if not source_edu:
        source_edu = OfficialSource(
            title="Department of School Education AP",
            official_url="https://jaganannaammavodi.ap.gov.in",
            department="School Education Department, Government of Andhra Pradesh",
            verification_date="2025-01-10",
            category="Education"
        )
        db.session.add(source_edu)

    source_health = OfficialSource.query.filter_by(title="Dr. YSR Aarogyasri Trust").first()
    if not source_health:
        source_health = OfficialSource(
            title="Dr. YSR Aarogyasri Trust",
            official_url="https://ysraarogyasri.ap.gov.in",
            department="Health, Medical & Family Welfare Department, GoAP",
            verification_date="2025-02-05",
            category="Healthcare"
        )
        db.session.add(source_health)

    source_housing = OfficialSource.query.filter_by(title="Pradhan Mantri Awas Yojana - Gramin").first()
    if not source_housing:
        source_housing = OfficialSource(
            title="Pradhan Mantri Awas Yojana - Gramin",
            official_url="https://pmayg.nic.in",
            department="Ministry of Rural Development, GoI",
            verification_date="2025-01-18",
            category="Housing"
        )
        db.session.add(source_housing)

    db.session.commit()

    # 2. Schemes Data
    schemes_data = [
        {
            "id": "pm-kisan",
            "name_en": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
            "name_te": "పీఎం కిసాన్ సమ్మాన్ నిధి",
            "category": "Agriculture",
            "description_en": "A Central Sector scheme to provide income support of ₹6,000 per year in three equal installments to all landholding farmer families across the country.",
            "description_te": "రైతు కుటుంబాలకు వ్యవసాయ పెట్టుబడి ఖర్చుల కోసం కేంద్ర ప్రభుత్వం ఏడాదికి మూడు విడతల్లో ₹6,000 ఆర్థిక సహాయం నేరుగా బ్యాంక్ ఖాతాలో జమ చేసే సంక్షేమ పథకం.",
            "target_beneficiaries_en": "Small and marginal landholder farmer families owning cultivable land.",
            "target_beneficiaries_te": "సాగుభూమి కలిగి ఉన్న సన్నకారు, చిన్నకారు రైతు కుటుంబాలు.",
            "state_or_central": "Central Government",
            "benefits_summary_en": "₹6,000 per year transferred directly to the beneficiary's Aadhaar-linked bank account in 3 installments of ₹2,000 each.",
            "benefits_summary_te": "సంవత్సరానికి ₹6,000 మొత్తం 3 విడతల్లో (విడతకు ₹2,000 చొప్పున) ఆధార్ అనుసంధాన బ్యాంక్ ఖాతాలో జమ చేయబడుతుంది.",
            "official_url": "https://pmkisan.gov.in",
            "source_id": source_pmk.id,
            "last_verified_at": "2025-01-15",
            "important_notes_en": "Mandatory requirements: eKYC on PM-KISAN portal, Aadhaar-seeded active bank account, and land seeding verified by village revenue officer.",
            "important_notes_te": "ముఖ్య గమనిక: పీఎం కిసాన్ పోర్టల్‌లో ఈకేవైసీ (eKYC) పూర్తి కావాలి, బ్యాంకు ఖాతాకు ఆధార్ లింక్ అయి ఉండాలి, పట్టాదారు పాస్‌బుక్ వివరాలు రెవెన్యూ రికార్డుల్లో ధృవీకరించబడి ఉండాలి.",
            "criteria": [
                {
                    "rule_code": "land_ownership",
                    "question_en": "Do you or your family own cultivable agricultural land with your name on the land record (Pattadar Passbook / 1-B)?",
                    "question_te": "మీ పేరిట లేదా మీ కుటుంబ సభ్యుల పేరిట వ్యవసాయ సాగుభూమి పట్టాదారు పాస్‌బుక్ / 1-B రికార్డులో నమోదై ఉందా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Land ownership in official revenue records is mandatory for PM-KISAN.",
                    "explanation_te": "పీఎం కిసాన్ పథకానికి అధికారిక రెవెన్యూ రికార్డుల్లో భూమి యాజమాన్య హక్కులు తప్పనిసరి.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "not_constitutional_post",
                    "question_en": "Are you or any family member NOT holding constitutional or government posts (like Minister, MLA, MP, Mayor)?",
                    "question_te": "మీరు లేదా మీ కుటుంబంలో ఎవరైనా రాజ్యాంగబద్ధ పదవులు, ప్రజాప్రతినిధి లేదా ప్రభుత్వ ఉద్యోగిగా లేరా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Constitutional post holders and regular government employees are excluded from PM-KISAN.",
                    "explanation_te": "రాజ్యాంగ పదవులు కలిగినవారు మరియు ప్రభుత్వ ఉద్యోగులు ఈ పథకానికి అనర్హులు.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "not_income_tax_payer",
                    "question_en": "Did you NOT pay Income Tax in the last assessment year?",
                    "question_te": "గత ఆర్థిక సంవత్సరంలో మీరు లేదా మీ కుటుంబ సభ్యులు ఆదాయపు పన్ను (Income Tax) చెల్లించలేదా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Income tax payers are excluded under PM-KISAN guidelines.",
                    "explanation_te": "ఆదాయపు పన్ను చెల్లించేవారు పీఎం కిసాన్ ప్రయోజనాలకు అర్హులు కారు.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "bank_aadhaar_seeded",
                    "question_en": "Is your bank account linked to your Aadhaar and enabled for NPCI Direct Benefit Transfer (DBT)?",
                    "question_te": "మీ బ్యాంక్ ఖాతాకు ఆధార్ లింక్ చేయబడి, డీబీటీ (DBT) సౌకర్యం యాక్టివ్‌గా ఉందా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Funds are transferred exclusively via Aadhaar Payment Bridge (APB).",
                    "explanation_te": "డబ్బులు ఆధార్ ద్వారానే పంపబడతాయి కాబట్టి బ్యాంకులో ఆధార్ సీడింగ్ తప్పనిసరి.",
                    "is_mandatory": True
                }
            ],
            "documents": [
                {
                    "document_name_en": "Aadhaar Card",
                    "document_name_te": "ఆధార్ కార్డు",
                    "purpose_en": "Identity and biometric authentication for Direct Benefit Transfer.",
                    "purpose_te": "గుర్తింపు మరియు ప్రత్యక్ష నగదు బదిలీ కోసం బయోమెట్రిక్ ధృవీకరణ.",
                    "issuing_authority_en": "UIDAI / Aadhaar Seva Kendra",
                    "issuing_authority_te": "యూఐడీఏఐ / మీసేవ / ఆధార్ కేంద్రం",
                    "preparation_tips_en": "Ensure mobile number linked with Aadhaar is active for receiving eKYC OTP.",
                    "preparation_tips_te": "ఈకేవైసీ ఓటీపీ అందుకోవడానికి ఆధార్‌తో లింక్ అయిన మొబైల్ నంబర్ యాక్టివ్‌గా ఉండేలా చూసుకోండి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "Pattadar Passbook / Land 1-B RoR",
                    "document_name_te": "పట్టాదారు పాస్‌బుక్ / 1-B రికార్డు",
                    "purpose_en": "Proof of agricultural land ownership and survey number.",
                    "purpose_te": "వ్యవసాయ భూమి హక్కులు మరియు సర్వే నంబర్ రుజువు.",
                    "issuing_authority_en": "Tahsildar / Revenue Department / MeeSeva",
                    "issuing_authority_te": "తహశీల్దార్ కార్యాలయం / మీసేవ / గ్రామ సచివాలయం",
                    "preparation_tips_en": "Check that the name in Pattadar Passbook matches your Aadhaar card name.",
                    "preparation_tips_te": "పాస్‌బుక్‌లోని పేరు మరియు ఆధార్‌లోని పేరు ఒకేలా ఉండాలి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "Bank Passbook (DBT Enabled)",
                    "document_name_te": "బ్యాంక్ పాస్‌బుక్ (డీబీటీ లింక్ చేయబడినది)",
                    "purpose_en": "Direct deposit of installment money via NPCI gateway.",
                    "purpose_te": "విడతల వారీ డబ్బులు నేరుగా ఖాతాలో జమ కావడం కోసం.",
                    "issuing_authority_en": "Commercial / Grameena / Cooperative Bank",
                    "issuing_authority_te": "మీ బ్యాంకు శాఖ (ఉదా: ఆంధ్రా ప్రగతి గ్రామీణ బ్యాంక్ / ఎస్‌బీఐ)",
                    "preparation_tips_en": "Visit bank branch to ensure NPCI Aadhaar seeding mapping is active.",
                    "preparation_tips_te": "బ్యాంకుకు వెళ్లి మీ ఖాతాకు ఎన్‌పీసీఐ (NPCI) మ్యాపింగ్ పూర్తయిందో లేదో సరిచూసుకోండి.",
                    "is_mandatory": True
                }
            ],
            "steps": [
                {
                    "step_number": 1,
                    "title_en": "Verify Land Records & Aadhaar Details",
                    "title_te": "భూమి రికార్డులు & ఆధార్ వివరాల సరిచూపు",
                    "description_en": "Check your 1-B Adangal record and ensure land survey numbers and owner name are correct.",
                    "description_te": "మీ 1-B అడంగల్ రికార్డును మీసేవ లేదా మీభూమి పోర్టల్‌లో సరిచూసి, సర్వే నంబర్లు సరిగ్గా ఉన్నాయో లేదో నిర్ధారించుకోండి.",
                    "portal_or_offline_en": "MeeBhoomi Portal / Grama Sachivalayam",
                    "portal_or_offline_te": "మీభూమి పోర్టల్ / కొనంకి గ్రామ సచివాలయం",
                    "caution_warning_en": "Ensure no spelling errors exist between land records and Aadhaar.",
                    "caution_warning_te": "భూమి రికార్డుల్లోని పేరు మరియు ఆధార్ కార్డులోని పేరు అక్షరం తేడా లేకుండా ఉండాలి."
                },
                {
                    "step_number": 2,
                    "title_en": "Submit Application at Sachivalayam or PM-KISAN Portal",
                    "title_te": "గ్రామ సచివాలయంలో లేదా పోర్టల్‌లో దరఖాస్తు సమర్పణ",
                    "description_en": "Register via 'New Farmer Registration' on pmkisan.gov.in or submit hard copies at Konanki Village Secretariat (VRO desk).",
                    "description_te": "పీఎం కిసాన్ పోర్టల్‌లో ఆన్‌లైన్‌లో నమోదు చేయండి లేదా కొనంకి గ్రామ సచివాలయంలోని వీఆర్వో (VRO) గారి వద్ద దరఖాస్తు ఇవ్వండి.",
                    "portal_or_offline_en": "Grama Sachivalayam / pmkisan.gov.in",
                    "portal_or_offline_te": "గ్రామ సచివాలయం / pmkisan.gov.in",
                    "caution_warning_en": "Always collect the acknowledgment slip with application reference number.",
                    "caution_warning_te": "దరఖాస్తు రిఫరెన్స్ నంబర్ ఉన్న రసీదును తప్పనిసరిగా భద్రపరుచుకోండి."
                },
                {
                    "step_number": 3,
                    "title_en": "Complete Biometric / OTP eKYC",
                    "title_te": "బయోమెట్రిక్ లేదా ఓటీపీ ఈకేవైసీ (eKYC) పూర్తి చేయండి",
                    "description_en": "Perform OTP eKYC on the PM-KISAN portal or biometric fingerprint eKYC at the Sachivalayam CSC center.",
                    "description_te": "పీఎం కిసాన్ వెబ్‌సైట్‌లో మొబైల్ ఓటీపీ ద్వారా లేదా సచివాలయంలో వేలిముద్ర ద్వారా ఈకేవైసీ పూర్తి చేయండి.",
                    "portal_or_offline_en": "pmkisan.gov.in / CSC Centre",
                    "portal_or_offline_te": "ఆన్‌లైన్ పోర్టల్ / సి.ఎస్.సి కేంద్రం",
                    "caution_warning_en": "Without completed eKYC, installments will be halted automatically.",
                    "caution_warning_te": "ఈకేవైసీ పూర్తి చేయకపోతే వాయిదాల డబ్బులు ఆగిపోతాయి."
                },
                {
                    "step_number": 4,
                    "title_en": "Track Beneficiary Status",
                    "title_te": "లబ్ధిదారుడి స్టేటస్ తనిఖీ చేసుకోండి",
                    "description_en": "Check 'Know Your Status' on pmkisan.gov.in using Registration Number or Aadhaar to confirm land seeding and DBT readiness.",
                    "description_te": "పీఎం కిసాన్ పోర్టల్‌లోని 'Know Your Status' ఆప్షన్‌లో మీ ఆధార్ లేదా రిజిస్ట్రేషన్ నంబర్ ఇచ్చి డబ్బులు జమ అవుతున్నాయో లేదో తనిఖీ చేయండి.",
                    "portal_or_offline_en": "Online Portal",
                    "portal_or_offline_te": "ఆన్‌లైన్ పోర్టల్",
                    "caution_warning_en": "Beware of fake SMS links promising instant PM-KISAN refunds or cash rewards.",
                    "caution_warning_te": "పీఎం కిసాన్ డబ్బుల పేరిట వాట్సాప్‌లో వచ్చే నకిలీ లింకులను క్లిక్ చేయకండి."
                }
            ]
        },
        {
            "id": "annadata-sukhibhava",
            "name_en": "Annadata Sukhibhava / Rythu Bharosa",
            "name_te": "అన్నదాత సుఖీభవ / రైతు భరోసా",
            "category": "Agriculture",
            "description_en": "Andhra Pradesh Government flagship farmer welfare scheme providing ₹20,000 financial support per year per eligible farmer family (including tenant farmers / CCRC holders).",
            "description_te": "ఆంధ్రప్రదేశ్ ప్రభుత్వం రైతు కుటుంబాలకు మరియు కౌలు రైతులకు వ్యవసాయ ఖర్చుల నిమిత్తం ఏడాదికి ₹20,000 ఆర్థిక భరోసా అందించే ప్రతిష్టాత్మక సంక్షేమ పథకం.",
            "target_beneficiaries_en": "Cultivating farmer families, ROFR forest land cultivators, and registered CCRC tenant farmers in Andhra Pradesh.",
            "target_beneficiaries_te": "ఆంధ్రప్రదేశ్‌లోని సాగుదారులైన రైతులు, అటవీ హక్కుల సాగుదారులు (ROFR) మరియు రిజిస్టర్డ్ కౌలు రైతులు (CCRC).",
            "state_or_central": "Andhra Pradesh Government",
            "benefits_summary_en": "Total ₹20,000 per year per farmer family provided before Kharif, Rabi, and harvest seasons.",
            "benefits_summary_te": "రైతు కుటుంబానికి ఏడాదికి మొత్తం ₹20,000 ఆర్థిక సహాయం ఖరీఫ్, రబీ సీజన్ల సమయంలో నేరుగా బ్యాంక్ ఖాతాలో జమ.",
            "official_url": "https://annadathasukhibhava.ap.gov.in",
            "source_id": source_ap_agri.id,
            "last_verified_at": "2025-01-20",
            "important_notes_en": "Tenant farmers require Crop Cultivator Rights Card (CCRC) agreement signed with the landowner for that crop year.",
            "important_notes_te": "కౌలు రైతులు భూ యజమానితో కుదుర్చుకున్న పంట సాగుదారు హక్కు పత్రం (CCRC కార్డ్) కలిగి ఉండాలి.",
            "criteria": [
                {
                    "rule_code": "ap_resident",
                    "question_en": "Are you a permanent resident of Andhra Pradesh?",
                    "question_te": "మీరు ఆంధ్రప్రదేశ్ రాష్ట్రంలో శాశ్వత నివాసిగా ఉన్నారా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Scheme is exclusively for cultivating farmers in Andhra Pradesh.",
                    "explanation_te": "ఈ పథకం కేవలం ఆంధ్రప్రదేశ్ రైతులకు మాత్రమే వర్తిస్తుంది.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "cultivator_or_tenant",
                    "question_en": "Are you an active cultivating farmer or registered tenant farmer holding land/CCRC card?",
                    "question_te": "మీరు స్వయంగా వ్యవసాయం చేస్తున్న రైతు లేదా రిజిస్టర్డ్ కౌలు కార్డు (CCRC) ఉన్న సాగుదారులా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Actual cultivation is verified by Village Agriculture Assistant (VAA).",
                    "explanation_te": "గ్రామ వ్యవసాయ సహాయకుడు (VAA) పంట సాగును ఈ-క్రాప్ (e-Crop) ద్వారా ధృవీకరిస్తారు.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "ecrop_booking",
                    "question_en": "Is your crop booked under the government e-Crop booking system for the current season?",
                    "question_te": "ప్రస్తుత సీజన్‌లో మీ పంట ఈ-క్రాప్ (e-Crop) లో గ్రామ సచివాలయ సిబ్బంది ద్వారా నమోదై ఉందా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "e-Crop booking is compulsory for receiving input subsidy and assistance.",
                    "explanation_te": "రైతు భరోసా సహాయం అందడానికి ఈ-క్రాప్ నమోదు తప్పనిసరి.",
                    "is_mandatory": True
                }
            ],
            "documents": [
                {
                    "document_name_en": "Aadhaar Card",
                    "document_name_te": "ఆధార్ కార్డు",
                    "purpose_en": "Citizen authentication and DBT linkage.",
                    "purpose_te": "గుర్తింపు మరియు ప్రభుత్వ నగదు బదిలీ కొరకు.",
                    "issuing_authority_en": "UIDAI",
                    "issuing_authority_te": "యూఐడీఏఐ",
                    "preparation_tips_en": "Make sure name matches bank passbook.",
                    "preparation_tips_te": "ఆధార్ కార్డులోని వివరాలు సరిచూసుకోండి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "Pattadar Passbook or CCRC Card (for Tenants)",
                    "document_name_te": "పట్టాదారు పాస్‌బుక్ లేదా కౌలు రైతు కార్డ్ (CCRC)",
                    "purpose_en": "Proof of agricultural land or tenancy agreement.",
                    "purpose_te": "సాగుభూమి హక్కులు లేదా కౌలు ఒప్పందం రుజువు.",
                    "issuing_authority_en": "Tahsildar / Village Revenue Officer",
                    "issuing_authority_te": "తహశీల్దార్ కార్యాలయం / గ్రామ వీఆర్వో",
                    "preparation_tips_en": "Tenants must ensure CCRC agreement is renewed for current agricultural year.",
                    "preparation_tips_te": "కౌలు రైతులు ప్రస్తుత సంవత్సరానికి సీసీఆర్‌సీ కార్డు పునరుద్ధరించుకోవాలి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "Bank Account Details (Aadhaar Seeded)",
                    "document_name_te": "బ్యాంక్ ఖాతా వివరాలు (ఆధార్ లింక్ అయినది)",
                    "purpose_en": "Direct Benefit Transfer.",
                    "purpose_te": "సహాయం నేరుగా జమ కావడం కోసం.",
                    "issuing_authority_en": "Bank",
                    "issuing_authority_te": "బ్యాంకు",
                    "preparation_tips_en": "Verify that your account has not turned dormant/inactive.",
                    "preparation_tips_te": "బ్యాంక్ ఖాతా చలామణిలో (Active) ఉండేలా చూసుకోండి.",
                    "is_mandatory": True
                }
            ],
            "steps": [
                {
                    "step_number": 1,
                    "title_en": "Complete e-Crop Registration at Rythu Bharosa Kendra (RBK)",
                    "title_te": "రైతు భరోసా కేంద్రం (ఆర్బీకే) వద్ద ఈ-క్రాప్ నమోదు",
                    "description_en": "Contact your Village Agriculture Assistant (VAA) in Konanki to register your crop details in e-Crop system with GPS survey.",
                    "description_te": "కొనంకిలోని రైతు భరోసా కేంద్రం (RBK) వద్ద గ్రామ వ్యవసాయ అసిస్టెంట్ (VAA) ద్వారా పంటను ఈ-క్రాప్‌లో నమోదు చేయించండి.",
                    "portal_or_offline_en": "Rythu Bharosa Kendra (RBK)",
                    "portal_or_offline_te": "రైతు భరోసా కేంద్రం (ఆర్బీకే)",
                    "caution_warning_en": "Ensure physical digital photograph of crop is taken by the assistant.",
                    "caution_warning_te": "పొలంలో పంట ఫొటో తీసి జియోట్యాగ్ చేశారో లేదో నిర్ధారించుకోండి."
                },
                {
                    "step_number": 2,
                    "title_en": "Verify Social Audit List at Grama Sachivalayam",
                    "title_te": "గ్రామ సచివాలయంలో అర్హుల సోషల్ ఆడిట్ జాబితా పరిశీలన",
                    "description_en": "Check the provisional eligible/ineligible beneficiary list displayed on the Sachivalayam notice board.",
                    "description_te": "సచివాలయం నోటీస్ బోర్డుపై ప్రదర్శించే తాత్కాలిక అర్హుల జాబితాలో మీ పేరు ఉందో లేదో చూడండి.",
                    "portal_or_offline_en": "Grama Sachivalayam Notice Board",
                    "portal_or_offline_te": "గ్రామ సచివాలయ నోటీసు బోర్డు",
                    "caution_warning_en": "If your name appears in the ineligible list, you have 15 days to file a grievance at Sachivalayam.",
                    "caution_warning_te": "అనర్హుల జాబితాలో పేరు ఉంటే 15 రోజుల్లోగా గ్రామ సచివాలయంలో గ్రీవెన్స్ (అభ్యంతరం) నమోదు చేయాలి."
                },
                {
                    "step_number": 3,
                    "title_en": "Receive Direct Benefit Transfer",
                    "title_te": "నేరుగా బ్యాంక్ ఖాతాలో నిధుల జమ పొందండి",
                    "description_en": "Upon final approval, installment amounts will be credited directly to your bank account with SMS notification.",
                    "description_te": "తుది ఆమోదం పొందిన తర్వాత ఆర్థిక సహాయం నేరుగా బ్యాంక్ ఖాతాలో జమవుతుంది.",
                    "portal_or_offline_en": "Bank DBT / SMS Notification",
                    "portal_or_offline_te": "బ్యాంక్ డీబీటీ / మొబైల్ మెసేజ్",
                    "caution_warning_en": "Check your bank passbook statement to confirm credit.",
                    "caution_warning_te": "డబ్బులు జమ అయినట్లు మీ బ్యాంకు పాస్‌బుక్‌లో లేదా మొబైల్ ఎస్ఎంఎస్ లో సరిచూసుకోండి."
                }
            ]
        },
        {
            "id": "ntr-bharosa-pension",
            "name_en": "NTR Bharosa / YSR Pension Kanuka",
            "name_te": "ఎన్టీఆర్ భరోసా / పెన్షన్ కానుక",
            "category": "Social Security",
            "description_en": "Monthly social security pension for vulnerable sections including Old Age Pension (OAP), Widows, Weavers, Toddy Tappers, Fishermen, Single Women, and Disabled Persons in Andhra Pradesh.",
            "description_te": "ఆంధ్రప్రదేశ్‌లోని పేద వృద్ధులు, వితంతువులు, దివ్యాంగులు, చేనేత, కల్లుగీత కార్మికులు మరియు ఒంటరి మహిళలకు ప్రతి నెలా 1వ తేదీనే ఇంటి వద్దే పింఛను అందించే సాంఘిక సంక్షేమ పథకం.",
            "target_beneficiaries_en": "Senior citizens (60+ years), Widows (18+), Disabled persons (40%+ disability), Weavers (50+), Toddy tappers (50+).",
            "target_beneficiaries_te": "వృద్ధులు (60 ఏళ్లు నిండినవారు), వితంతువులు (18 ఏళ్లు పైబడినవారు), దివ్యాంగులు (40% పైబడి వైకల్యం ఉన్నవారు), ఒంటరి మహిళలు.",
            "state_or_central": "Andhra Pradesh Government",
            "benefits_summary_en": "Monthly financial assistance of ₹4,000 for Old Age, Widow, Weavers, Fishermen, Single Women pensions; ₹6,000 per month for fully disabled persons; ₹15,000 for severe chronic kidney/dialysis patients.",
            "benefits_summary_te": "వృద్ధాప్య, వితంతు, ఒంటరి మహిళల పెన్షన్ నెలకు ₹4,000; దివ్యాంగుల పింఛను నెలకు ₹6,000; తీవ్రమైన కిడ్నీ/డయాలసిస్ రోగులకు నెలకు ₹15,000.",
            "official_url": "https://sspensions.ap.gov.in",
            "source_id": source_pension.id,
            "last_verified_at": "2025-02-01",
            "important_notes_en": "Delivered directly at the doorstep on the 1st of every month through Village Secretariat Welfare Assistants.",
            "important_notes_te": "ప్రతి నెలా 1వ తారీఖున సచివాలయ సిబ్బంది ద్వారా లబ్ధిదారుడి ఇంటి వద్దకే పెన్షన్ నగదు అందజేయబడుతుంది.",
            "criteria": [
                {
                    "rule_code": "oap_age_60",
                    "question_en": "For Old Age Pension, is the applicant 60 years of age or older?",
                    "question_te": "వృద్ధాప్య పెన్షన్ కోసం దరఖాస్తుదారుడి వయస్సు 60 సంవత్సరాలు లేదా అంతకంటే ఎక్కువ ఉందా?",
                    "condition_type": "numeric_min",
                    "expected_value": "60",
                    "explanation_en": "Applicant must have completed 60 years on the date of verification.",
                    "explanation_te": "వృద్ధాప్య పెన్షన్‌కు 60 సంవత్సరాలు పూర్తి కావాలి (వితంతు పెన్షన్‌కు 18 ఏళ్లు నిండి ఉండాలి).",
                    "is_mandatory": True
                },
                {
                    "rule_code": "rural_monthly_income",
                    "question_en": "Is the total family monthly income in rural areas less than or equal to ₹10,000 (or annual income <= ₹1,20,000)?",
                    "question_te": "గ్రామీణ ప్రాంతంలో మీ కుటుంబ మొత్తం నెలసరి ఆదాయం ₹10,000 కంటే తక్కువగా ఉందా?",
                    "condition_type": "numeric_max",
                    "expected_value": "10000",
                    "explanation_en": "Rural income ceiling for pension eligibility is ₹10,000/month.",
                    "explanation_te": "గ్రామీణ ప్రాంతాల్లో కుటుంబ నెలసరి ఆదాయం ₹10,000 లోపు ఉండాలి.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "land_holding_ceiling",
                    "question_en": "Does your family own less than 3 acres of wet land OR less than 10 acres of dry land?",
                    "question_te": "మీ కుటుంబానికి 3 ఎకరాలలోపు మాగాణి (తరి) లేదా 10 ఎకరాలలోపు మెట్ట భూమి మాత్రమే ఉందా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Total landholding must not exceed 3 acres wet or 10 acres dry.",
                    "explanation_te": "భూమి పరిమితి 3 ఎకరాల మాగాణి లేదా 10 ఎకరాల మెట్ట దాటకూడదు.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "no_four_wheeler",
                    "question_en": "Does your family NOT own a four-wheeler (excluding tractors/autos for livelihood)?",
                    "question_te": "మీ కుటుంబంలో ఎవరికీ స్వంత కార్లు లేదా నాలుగు చక్రాల వాహనాలు లేవా (ఆటోలు, ట్రాక్టర్లు మినహా)?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Families owning 4-wheelers (cars/taxis) are ineligible.",
                    "explanation_te": "నాలుగు చక్రాల ప్రైవేట్ కార్లు ఉన్నవారు అర్హులు కారు.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "no_govt_employee_in_family",
                    "question_en": "Are there NO regular government employees or pensioners in your family?",
                    "question_te": "మీ కుటుంబంలో ఎవరూ ప్రభుత్వ ఉద్యోగి లేదా సర్వీస్ పెన్షనర్ కాదా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Families with government employees or service pensioners are not eligible.",
                    "explanation_te": "ప్రభుత్వ ఉద్యోగులు లేదా రిటైర్డ్ పెన్షనర్లు ఉన్న కుటుంబాలు అనర్హులు.",
                    "is_mandatory": True
                }
            ],
            "documents": [
                {
                    "document_name_en": "Aadhaar Card",
                    "document_name_te": "ఆధార్ కార్డు",
                    "purpose_en": "Proof of identity and age.",
                    "purpose_te": "వయస్సు మరియు గుర్తింపు రుజువు.",
                    "issuing_authority_en": "UIDAI",
                    "issuing_authority_te": "యూఐడీఏఐ",
                    "preparation_tips_en": "Verify date of birth matches other official documents.",
                    "preparation_tips_te": "పుట్టిన తేదీ స్పష్టంగా ఉండేలా చూసుకోండి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "Rice Card / BPL Ration Card",
                    "document_name_te": "రైస్ కార్డు / తెల్ల రేషన్ కార్డు",
                    "purpose_en": "Proof of economic backwardness and family composition.",
                    "purpose_te": "కుటుంబ ఆర్థిక స్థితి మరియు సభ్యుల వివరాల రుజువు.",
                    "issuing_authority_en": "Civil Supplies Department / Sachivalayam",
                    "issuing_authority_te": "పౌర సరఫరాల శాఖ / గ్రామ సచివాలయం",
                    "preparation_tips_en": "Ensure applicant is listed in the rice card.",
                    "preparation_tips_te": "దరఖాస్తుదారుడి పేరు రైస్ కార్డులో నమోదై ఉండాలి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "Death Certificate of Husband (For Widow Pension)",
                    "document_name_te": "భర్త మరణ ధృవీకరణ పత్రం (వితంతు పెన్షన్ కొరకు)",
                    "purpose_en": "Mandatory proof of widowhood for widow pension category.",
                    "purpose_te": "వితంతు పెన్షన్ దరఖాస్తుకు భర్త మరణ ధృవీకరణ తప్పనిసరి.",
                    "issuing_authority_en": "Grama Sachivalayam / Registrar of Births & Deaths",
                    "issuing_authority_te": "గ్రామ సచివాలయం / జనన మరణాల రిజిస్ట్రార్",
                    "preparation_tips_en": "Collect official death certificate from local Sachivalayam/Panchayat office.",
                    "preparation_tips_te": "అధికారిక డెత్ సర్టిఫికెట్ ఒరిజినల్ కాపీ ఉంచుకోండి.",
                    "is_mandatory": False
                },
                {
                    "document_name_en": "SADAREM Disability Certificate (For Disabled Pension)",
                    "document_name_te": "సదరమ్ (SADAREM) దివ్యాంగుల సర్టిఫికెట్",
                    "purpose_en": "Medical proof of 40% or more disability.",
                    "purpose_te": "కనీసం 40% వైకల్యం ఉన్నట్లు వైద్య బోర్డు ధృవీకరణ.",
                    "issuing_authority_en": "District Medical Board / SADAREM",
                    "issuing_authority_te": "జిల్లా వైద్య బోర్డు / సదరమ్ క్యాంపు",
                    "preparation_tips_en": "Certificate must carry valid registration number.",
                    "preparation_tips_te": "సదరమ్ సర్టిఫికెట్ నంబర్ ఆన్‌లైన్‌లో నమోదై ఉండాలి.",
                    "is_mandatory": False
                }
            ],
            "steps": [
                {
                    "step_number": 1,
                    "title_en": "Approach Welfare and Education Assistant (WEA) at Sachivalayam",
                    "title_te": "గ్రామ సచివాలయంలోని సంక్షేమ సహాయకుడిని (WEA) కలవండి",
                    "description_en": "Visit Konanki Grama Sachivalayam with your Aadhaar and Rice Card. The WEA will enter details in the Navasakam beneficiary portal.",
                    "description_te": "కొనంకి గ్రామ సచివాలయంలో సంక్షేమ సహాయకుడిని (WEA) కలిసి మీ ఆధార్, రైస్ కార్డు అందించి నవశకం పోర్టల్‌లో దరఖాస్తు చేయించండి.",
                    "portal_or_offline_en": "Grama Sachivalayam (Konanki)",
                    "portal_or_offline_te": "గ్రామ సచివాలయం (కొనంకి)",
                    "caution_warning_en": "No application fee is charged by the government for pension applications.",
                    "caution_warning_te": "పెన్షన్ దరఖాస్తుకు ప్రభుత్వం ఎలాంటి రుసుము తీసుకోదు, ఇది ఉచిత సేవ."
                },
                {
                    "step_number": 2,
                    "title_en": "Doorstep Verification by Village Functionary",
                    "title_te": "క్షేత్రస్థాయి ఇంటి పరిశీలన",
                    "description_en": "The village assistant conducts on-ground verification of family assets, electricity consumption, and residence.",
                    "description_te": "సచివాలయ సిబ్బంది మీ ఇంటి వద్దకు వచ్చి ఆర్థిక వివరాలు, నివాసం పరిశీలిస్తారు.",
                    "portal_or_offline_en": "Doorstep Verification",
                    "portal_or_offline_te": "ఇంటి వద్దే పరిశీలన",
                    "caution_warning_en": "Be present in person with original Aadhaar during verification.",
                    "caution_warning_te": "పరిశీలన సమయంలో ఒరిజినల్ కార్డులతో స్వయంగా అందుబాటులో ఉండండి."
                },
                {
                    "step_number": 3,
                    "title_en": "Social Audit & Mandal Parishad Development Officer (MPDO) Approval",
                    "title_te": "సామాజిక తనిఖీ & ఎంపీడీవో (MPDO) గారి ఆమోదం",
                    "description_en": "Applications are published for public scrutiny at Grama Sabha and approved digitally by the MPDO.",
                    "description_te": "గ్రామసభ ఆమోదం తర్వాత మార్టూరు మండల పరిషత్ అభివృద్ధి అధికారి (MPDO) గారు ఆమోదిస్తారు.",
                    "portal_or_offline_en": "Martur Mandal Office (MPDO)",
                    "portal_or_offline_te": "మార్టూరు మండల కార్యాలయం (ఎంపీడీవో)",
                    "caution_warning_en": "Track progress using the application tracking number on sspensions.ap.gov.in.",
                    "caution_warning_te": "దరఖాస్తు స్టేటస్‌ను సచివాలయంలో లేదా పోర్టల్‌లో ఎప్పటికప్పుడు తెలుసుకోవచ్చు."
                },
                {
                    "step_number": 4,
                    "title_en": "Pension Sanction and Doorstep Monthly Delivery",
                    "title_te": "పెన్షన్ మంజూరు మరియు ప్రతి నెలా 1వ తేదీన నగదు పంపిణీ",
                    "description_en": "Once sanctioned, pension ID card is issued and cash is delivered at home via biometric authentication on the 1st of every month.",
                    "description_te": "మంజూరైన వెంటనే పెన్షన్ కార్డు జారీ అవుతుంది. ప్రతి నెలా 1వ తారీఖున వేలిముద్ర లేదా ఫేస్ అథెంటికేషన్ ద్వారా ఇంటివద్దే నగదు అందుతుంది.",
                    "portal_or_offline_en": "Doorstep Delivery",
                    "portal_or_offline_te": "ఇంటి వద్దే పంపిణీ",
                    "caution_warning_en": "If biometric fails for elderly citizens, Iris or Face authorization is provided.",
                    "caution_warning_te": "వేలిముద్రలు పడని వృద్ధులకు కంటిపాప (Iris) లేదా ఫేస్ రికగ్నిషన్ ద్వారా నగదు ఇస్తారు."
                }
            ]
        },
        {
            "id": "thalliki-vandanam",
            "name_en": "Thalliki Vandanam / Amma Vodi",
            "name_te": "తల్లికి వందనం / అమ్మ ఒడి",
            "category": "Education",
            "description_en": "Annual financial incentive of ₹15,000 provided to every eligible mother or recognized guardian sending her children to recognized schools or junior colleges (Classes 1 to 12) in Andhra Pradesh.",
            "description_te": "పిల్లలను బడికి పంపే ప్రతి నిరుపేద తల్లి లేదా సంరక్షకురాలికి విద్యా ప్రోత్సాహకంగా ప్రభుత్వం ఏటా అందించే ₹15,000 ఆర్థిక సహాయం.",
            "target_beneficiaries_en": "Mothers / guardians with children studying in Class 1 to 12 in recognized Government, Aided, or Private schools/colleges in AP.",
            "target_beneficiaries_te": "ఆంధ్రప్రదేశ్‌లోని గుర్తింపు పొందిన పాఠశాలలు, జూనియర్ కళాశాలల్లో (1 నుండి 12వ తరగతి) చదువుతున్న విద్యార్థుల తల్లులు.",
            "state_or_central": "Andhra Pradesh Government",
            "benefits_summary_en": "₹15,000 per academic year directly credited to the mother's bank account (with ₹1,000 designated for school sanitation maintenance).",
            "benefits_summary_te": "విద్యా సంవత్సరానికి ₹15,000 నేరుగా తల్లి బ్యాంక్ ఖాతాలో జమ (పాఠశాల నిర్వహణ నిధి కింద ₹1,000 మినహాయింపు).",
            "official_url": "https://jaganannaammavodi.ap.gov.in",
            "source_id": source_edu.id,
            "last_verified_at": "2025-01-10",
            "important_notes_en": "Child must maintain at least 75% attendance in school throughout the academic year. Mother's Aadhaar must be active and DBT enabled.",
            "important_notes_te": "పాఠశాలలో విద్యార్థికి కనీసం 75% హాజరు తప్పనిసరి. తల్లి బ్యాంకు ఖాతాకు ఆధార్ డీబీటీ అనుసంధానమై ఉండాలి.",
            "criteria": [
                {
                    "rule_code": "school_enrolled_1_to_12",
                    "question_en": "Is your child enrolled and studying in Classes 1 to 12 in a recognized school or junior college?",
                    "question_te": "మీ పిల్లలు గుర్తింపు పొందిన పాఠశాల లేదా జూనియర్ కళాశాలలో 1 నుండి 12వ తరగతి చదువుతున్నారా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Child must be enrolled in recognized institutions.",
                    "explanation_te": "గుర్తింపు పొందిన ప్రభుత్వ లేదా ప్రైవేట్ బడిలో చదువుతూ ఉండాలి.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "child_attendance_75",
                    "question_en": "Does the student maintain minimum 75% classroom attendance?",
                    "question_te": "విద్యార్థికి పాఠశాలలో కనీసం 75% హాజరు నమోదవుతోందా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "75% school attendance is mandatory as per government orders.",
                    "explanation_te": "ప్రభుత్వ నిబంధనల ప్రకారం 75% హాజరు శాతం తప్పనిసరి.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "bpl_ration_card",
                    "question_en": "Does your family possess a valid Rice Card (BPL white card)?",
                    "question_te": "మీ కుటుంబానికి చెల్లుబాటయ్యే రైస్ కార్డు (తెల్ల రేషన్ కార్డు) ఉందా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "BPL rice card determines economic eligibility.",
                    "explanation_te": "పేదరిక నిర్ధారణకు రైస్ కార్డు అవసరం.",
                    "is_mandatory": True
                }
            ],
            "documents": [
                {
                    "document_name_en": "Mother's & Child's Aadhaar Cards",
                    "document_name_te": "తల్లి మరియు విద్యార్థి ఆధార్ కార్డులు",
                    "purpose_en": "Verification of parentage and child identity.",
                    "purpose_te": "తల్లి-పిల్లల సంబంధం మరియు గుర్తింపు ధృవీకరణ.",
                    "issuing_authority_en": "UIDAI",
                    "issuing_authority_te": "యూఐడీఏఐ",
                    "preparation_tips_en": "Verify that mother's name is accurately spelled in school register.",
                    "preparation_tips_te": "స్కూల్ రికార్డుల్లో తల్లి పేరు ఆధార్ ప్రకారమే ఉండేలా చూసుకోండి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "White Ration Card / Rice Card",
                    "document_name_te": "రైస్ కార్డు / బియ్యం కార్డు",
                    "purpose_en": "Economic criterion verification.",
                    "purpose_te": "ఆర్థిక అర్హత పరిశీలన కొరకు.",
                    "issuing_authority_en": "Civil Supplies Department",
                    "issuing_authority_te": "పౌర సరఫరాల శాఖ",
                    "preparation_tips_en": "Both mother and child must be listed under the same card.",
                    "preparation_tips_te": "తల్లీబిడ్డలు ఇద్దరి పేర్లూ ఒకే రైస్ కార్డులో ఉండాలి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "Mother's Bank Account Passbook",
                    "document_name_te": "తల్లి బ్యాంక్ పాస్‌బుక్",
                    "purpose_en": "Direct Benefit Transfer credit.",
                    "purpose_te": "సహాయం తల్లి వ్యక్తిగత ఖాతాలో జమ కావడం కోసం.",
                    "issuing_authority_en": "Bank",
                    "issuing_authority_te": "బ్యాంకు",
                    "preparation_tips_en": "Joint accounts are not allowed; must be single account in mother's name.",
                    "preparation_tips_te": "జాయింట్ అకౌంట్ చెల్లదు; తల్లి పేరిట మాత్రమే సింగిల్ ఖాతా ఉండాలి.",
                    "is_mandatory": True
                }
            ],
            "steps": [
                {
                    "step_number": 1,
                    "title_en": "Submit Child Details at School Headmaster Desk",
                    "title_te": "పాఠశాల ప్రధానోపాధ్యాయుడి (హెచ్.ఎం) వద్ద వివరాల సమర్పణ",
                    "description_en": "Provide mother's bank details and Aadhaar to school headmaster for entry into the Child Info Education Portal.",
                    "description_te": "పాఠశాల హెచ్.ఎం గారికి తల్లి ఆధార్, బ్యాంక్ ఖాతా వివరాలు ఇవ్వండి. వారు చైల్డ్ ఇన్ఫో పోర్టల్‌లో నమోదు చేస్తారు.",
                    "portal_or_offline_en": "School / College Headmaster",
                    "portal_or_offline_te": "పాఠశాల / కళాశాల ప్రధానోపాధ్యాయుడు",
                    "caution_warning_en": "Verify IFSC code and account number entered on the school computer screen.",
                    "caution_warning_te": "బ్యాంక్ ఖాతా సంఖ్య, ఐఎఫ్ఎస్సీ కోడ్ కంప్యూటర్‌లో సరిగ్గా కొట్టారో లేదో సరిచూసుకోండి."
                },
                {
                    "step_number": 2,
                    "title_en": "Field Verification by Grama Sachivalayam Education Assistant",
                    "title_te": "సచివాలయ విద్యా సహాయకుడి క్షేత్ర పరిశీలన",
                    "description_en": "The Education Assistant verifies student attendance, six-step validation, and bank mapping.",
                    "description_te": "సచివాలయ సంక్షేమ/విద్యా సహాయకుడు ఆరు దశల ధృవీకరణ మరియు విద్యార్థి హాజరును పరిశీలిస్తారు.",
                    "portal_or_offline_en": "Grama Sachivalayam",
                    "portal_or_offline_te": "గ్రామ సచివాలయం",
                    "caution_warning_en": "Check provisional beneficiary list published at the Sachivalayam in June/July.",
                    "caution_warning_te": "సచివాలయంలో ప్రదర్శించే జాబితాలో మీ వివరాలు ఉన్నాయో లేదో జూన్/జూలై నెలల్లో చూసుకోండి."
                },
                {
                    "step_number": 3,
                    "title_en": "Fund Disbursal into Mother's Account",
                    "title_te": "తల్లి ఖాతాలో నిధుల విడుదల",
                    "description_en": "Annual ₹15,000 benefit is transferred to mother's DBT account directly at the start of the academic year.",
                    "description_te": "విద్యా సంవత్సరం ప్రారంభంలో నిధులు నేరుగా తల్లి బ్యాంక్ ఖాతాకు జమ చేయబడతాయి.",
                    "portal_or_offline_en": "Bank Transfer",
                    "portal_or_offline_te": "బ్యాంక్ ఖాతా",
                    "caution_warning_en": "Avoid closing or neglecting the bank account between academic sessions.",
                    "caution_warning_te": "బ్యాంక్ ఖాతాను నిలిపివేయకుండా ఎప్పటికప్పుడు వాడకంలో ఉంచండి."
                }
            ]
        },
        {
            "id": "aarogyasri",
            "name_en": "Dr. YSR Aarogyasri / Ayushman Bharat",
            "name_te": "డాక్టర్ వైఎస్సార్ ఆరోగ్యశ్రీ / ఆయుష్మాన్ భారత్",
            "category": "Healthcare",
            "description_en": "Universal health insurance coverage providing completely cashless hospitalization and surgeries up to ₹25,00,000 for critical and common medical treatments in empanelled network hospitals.",
            "description_te": "పేద ప్రజలకు కార్పొరేట్ మరియు నెట్‌వర్క్ ఆసుపత్రుల్లో ₹25 లక్షల వరకు ఉచిత నగదు రహిత శస్త్రచికిత్సలు, వైద్య సేవలు అందించే ఆరోగ్య రక్షణ పథకం.",
            "target_beneficiaries_en": "All BPL / Rice Card holders, low-income families, and government certified beneficiaries in Andhra Pradesh.",
            "target_beneficiaries_te": "ఆంధ్రప్రదేశ్‌లోని తెల్ల రేషన్ కార్డు/రైస్ కార్డు కలిగిన పేద మరియు మధ్యతరగతి కుటుంబాలు.",
            "state_or_central": "Joint (AP & Central Government)",
            "benefits_summary_en": "Cashless treatment up to ₹25 lakh per family per year covering over 3,250 medical and surgical procedures with free medicine and post-operative Aarogya Asara allowance.",
            "benefits_summary_te": "కుటుంబానికి ఏడాదికి ₹25 లక్షల వరకు ఉచిత వైద్యం. 3,250కి పైగా జబ్బులు, ఆపరేషన్లకు నగదు రహిత చికిత్స మరియు ఆపరేషన్ తర్వాత విశ్రాంతి సమయంలో ఆరోగ్య ఆసరా ఆర్థిక సాయం.",
            "official_url": "https://ysraarogyasri.ap.gov.in",
            "source_id": source_health.id,
            "last_verified_at": "2025-02-05",
            "important_notes_en": "Show your Aarogyasri card or Rice card or Aadhaar card at the hospital Aarogya Mithra assistance counter.",
            "important_notes_te": "నెట్‌వర్క్ ఆసుపత్రికి వెళ్లిన వెంటనే అక్కడ ఉండే ఆరోగ్యమిత్ర సహాయ కేంద్రం (హెల్ప్ డెస్క్) వద్ద మీ కార్డు చూపించాలి.",
            "criteria": [
                {
                    "rule_code": "ap_resident_health",
                    "question_en": "Are you a resident of Andhra Pradesh?",
                    "question_te": "మీరు ఆంధ్రప్రదేశ్ రాష్ట్ర నివాసిగా ఉన్నారా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Aarogyasri is provided to Andhra Pradesh families.",
                    "explanation_te": "ఈ కార్డు ఆంధ్రప్రదేశ్ ప్రజలకు వర్తిస్తుంది.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "rice_card_or_income_below_5lakh",
                    "question_en": "Does your family have a Rice Card OR annual income less than or equal to ₹5,00,000?",
                    "question_te": "మీ కుటుంబానికి రైస్ కార్డు ఉందా లేదా వార్షిక ఆదాయం ₹5,00,000 లోపు ఉందా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Eligible for all families with annual income up to ₹5 lakh or Rice card holders.",
                    "explanation_te": "వార్షిక ఆదాయం ₹5 లక్షల లోపు ఉన్నవారు లేదా రైస్ కార్డు ఉన్నవారు అర్హులు.",
                    "is_mandatory": True
                }
            ],
            "documents": [
                {
                    "document_name_en": "Aarogyasri Health Card / Rice Card",
                    "document_name_te": "ఆరోగ్యశ్రీ హెల్త్ కార్డు / రైస్ కార్డు",
                    "purpose_en": "Instant empanelment verification at hospital reception.",
                    "purpose_te": "ఆసుపత్రిలో ఉచిత చికిత్స అనుమతి కొరకు ప్రాథమిక కార్డు.",
                    "issuing_authority_en": "Aarogyasri Trust / Grama Sachivalayam",
                    "issuing_authority_te": "ఆరోగ్యశ్రీ ట్రస్ట్ / గ్రామ సచివాలయం",
                    "preparation_tips_en": "Digital card downloaded on mobile via Sachivalayam portal is equally valid.",
                    "preparation_tips_te": "మొబైల్‌లోని డిజిటల్ కార్డు లేదా ప్లాస్టిక్ కార్డు ఏదైనా చూపవచ్చు.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "Patient's Aadhaar Card",
                    "document_name_te": "రోగి యొక్క ఆధార్ కార్డు",
                    "purpose_en": "Biometric verification and admission registration.",
                    "purpose_te": "రోగి బయోమెట్రిక్ లేదా ఓటీపీ ధృవీకరణ కోసం.",
                    "issuing_authority_en": "UIDAI",
                    "issuing_authority_te": "యూఐడీఏఐ",
                    "preparation_tips_en": "Carry original card along with a photocopy.",
                    "preparation_tips_te": "ఒరిజినల్ కార్డు వెంట ఉంచుకోండి.",
                    "is_mandatory": True
                }
            ],
            "steps": [
                {
                    "step_number": 1,
                    "title_en": "Visit Empanelled Government or Private Network Hospital",
                    "title_te": "గుర్తింపు పొందిన నెట్‌వర్క్ ఆసుపత్రిని సందర్శించండి",
                    "description_en": "Go to any designated network hospital in Martur, Chilakaluripet, Guntur, or Bapatla with your Aarogyasri or Rice card.",
                    "description_te": "మార్టూరు, చిలకలూరిపేట, గుంటూరు లేదా బాపట్లలోని ఆరోగ్యశ్రీ గుర్తింపు ఉన్న నెట్‌వర్క్ ఆసుపత్రికి వెళ్లండి.",
                    "portal_or_offline_en": "Network Hospital Help Desk",
                    "portal_or_offline_te": "నెట్‌వర్క్ ఆసుపత్రి హెల్ప్ డెస్క్",
                    "caution_warning_en": "Always locate the 'Aarogya Mithra' desk at the hospital entrance first.",
                    "caution_warning_te": "ఆసుపత్రిలోకి వెళ్లగానే ముందుగా 'ఆరోగ్యమిత్ర' కౌంటర్ వద్ద రిపోర్ట్ చేయండి."
                },
                {
                    "step_number": 2,
                    "title_en": "Consult Aarogya Mithra & Pre-authorization",
                    "title_te": "ఆరోగ్యమిత్రను కలిసి ప్రీ-ఆథరైజేషన్ అనుమతి పొందండి",
                    "description_en": "The Aarogya Mithra checks the patient's card and doctor notes, and uploads the case for medical pre-authorization approval.",
                    "description_te": "ఆరోగ్యమిత్ర మీ కార్డును తనిఖీ చేసి, వైద్యుల పరీక్షల ఆధారంగా ఆన్‌లైన్‌లో అనుమతి (Pre-Auth) తీసుకుంటారు.",
                    "portal_or_offline_en": "Hospital Aarogya Mithra Counter",
                    "portal_or_offline_te": "ఆసుపత్రి ఆరోగ్యమిత్ర కౌంటర్",
                    "caution_warning_en": "Do not pay any cash deposit for Aarogyasri approved procedures.",
                    "caution_warning_te": "ఆరోగ్యశ్రీ పరిధిలోని చికిత్సలకు ఆసుపత్రి వారికి ఎలాంటి అడ్వాన్స్ లేదా డిపాజిట్ డబ్బులు ఇవ్వవద్దు."
                },
                {
                    "step_number": 3,
                    "title_en": "Receive Free Treatment, Medicines, and Food",
                    "title_te": "ఉచిత శస్త్రచికిత్స, మందులు మరియు ఆహారం పొందండి",
                    "description_en": "Patient receives free treatment, diagnostic investigations, surgery, diet, and 10 days post-discharge medicines.",
                    "description_te": "రోగికి ఆసుపత్రిలో చికిత్స, ఆపరేషన్, పరీక్షలు, భోజనం మరియు డిశ్చార్జి తర్వాత 10 రోజుల మందులు పూర్తిగా ఉచితంగా అందుతాయి.",
                    "portal_or_offline_en": "Hospital In-patient Ward",
                    "portal_or_offline_te": "ఆసుపత్రి వార్డు",
                    "caution_warning_en": "In case of any illegal bill demands, immediately dial toll-free helpline 104.",
                    "caution_warning_te": "ఆసుపత్రి వారు ఎవరైనా అదనపు బిల్లు అడిగితే వెంటనే 104 ఉచిత నంబర్‌కు ఫోన్ చేసి ఫిర్యాదు చేయండి."
                }
            ]
        },
        {
            "id": "pmay-gramin",
            "name_en": "Pradhan Mantri Awas Yojana - Gramin / YSR Pedalandariki Illu",
            "name_te": "పీఎం ఆవాస్ యోజన - గ్రామీణ్ / పేదలందరికీ ఇళ్లు",
            "category": "Housing",
            "description_en": "Comprehensive rural housing welfare scheme providing financial assistance and pucca house sanction for houseless rural families living in kutcha/dilapidated homes.",
            "description_te": "గ్రామీణ ప్రాంతాల్లో ఇళ్లు లేని పేదలకు, పూరిగుడిసెలలో నివసించే వారికి శాశ్వత పక్కా ఇల్లు నిర్మించుకోవడానికి ప్రభుత్వం అందించే గృహ నిర్మాణ సహాయ పథకం.",
            "target_beneficiaries_en": "Houseless rural families and households living in zero, one or two room kutcha houses according to SECC/Awas+ survey.",
            "target_beneficiaries_te": "గ్రామీణ ప్రాంతాల్లో సొంత ఇల్లు లేని పేదలు, మట్టి లేదా తాటాకు ఇళ్లలో నివసిస్తున్న నిరుపేద కుటుంబాలు.",
            "state_or_central": "Joint (Central & AP Government)",
            "benefits_summary_en": "Financial grant of ₹1,20,000 to ₹1,80,000 in plain rural areas for house construction released in 4 geo-tagged stages, plus 90 days MGNREGS wage employment assistance and toilet construction grant.",
            "benefits_summary_te": "నిర్మాణ దశల వారీగా ₹1,80,000 వరకు ఆర్థిక సహాయం, ఉపాధి హామీ (MGNREGS) పథకం ద్వారా కూలీ డబ్బులు మరియు ఉచిత మరుగుదొడ్డి నిర్మాణ నిధులు.",
            "official_url": "https://pmayg.nic.in",
            "source_id": source_housing.id,
            "last_verified_at": "2025-01-18",
            "important_notes_en": "House sanction requires geotagging of house construction progress at Basement, Lintel, Roof, and Completed levels.",
            "important_notes_te": "నిర్మాణం పూర్తయ్యే కొద్దీ బేస్‌మెంట్, గోడలు, శ్లాబ్, తుది దశల్లో జియోట్యాగింగ్ ఫొటోలు తీసిన తర్వాత మాత్రమే నిధులు విడుదలవుతాయి.",
            "criteria": [
                {
                    "rule_code": "houseless_or_kutcha",
                    "question_en": "Do you or your family NOT own a permanent pucca house anywhere in India?",
                    "question_te": "మీకు లేదా మీ కుటుంబ సభ్యులకు దేశంలో ఎక్కడా శాశ్వత పక్కా ఇల్లు లేదా అపార్ట్‌మెంట్ లేదా భవనం లేదా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "Only houseless or kutcha house dwellers are eligible.",
                    "explanation_te": "సొంతంగా పక్కా ఇల్లు లేని నిరుపేదలకు మాత్రమే ఈ పథకం వర్తిస్తుంది.",
                    "is_mandatory": True
                },
                {
                    "rule_code": "rural_resident_konanki",
                    "question_en": "Are you residing in a rural gram panchayat area (such as Konanki / Martur)?",
                    "question_te": "మీరు గ్రామీణ పంచాయతీ పరిధిలో (ఉదాహరణకు కొనంకి / మార్టూరు పరిసరాలు) నివసిస్తున్నారా?",
                    "condition_type": "boolean",
                    "expected_value": "true",
                    "explanation_en": "PMAY-Gramin strictly serves rural panchayat jurisdictions.",
                    "explanation_te": "పీఎంఏవై గ్రామీణ్ కేవలం గ్రామాల్లో నివసించే వారికి మాత్రమే అందుబాటులో ఉంటుంది.",
                    "is_mandatory": True
                }
            ],
            "documents": [
                {
                    "document_name_en": "Aadhaar Card (All Adult Family Members)",
                    "document_name_te": "కుటుంబ సభ్యులందరి ఆధార్ కార్డులు",
                    "purpose_en": "De-duplication and beneficiary verification.",
                    "purpose_te": "కుటుంబ సభ్యుల గుర్తింపు ధృవీకరణ.",
                    "issuing_authority_en": "UIDAI",
                    "issuing_authority_te": "యూఐడీఏఐ",
                    "preparation_tips_en": "Ensure mobile number linked for geo-tag notifications.",
                    "preparation_tips_te": "ఆధార్ కార్డుల నకళ్లు సిద్ధంగా ఉంచుకోండి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "House Site Pattadar Certificate / D-Form Patta",
                    "document_name_te": "ఇళ్ల స్థలం పట్టా (డి-ఫారమ్ పట్టా)",
                    "purpose_en": "Proof of allotted house plot or land for construction.",
                    "purpose_te": "ఇల్లు నిర్మించుకునే స్థల హక్కుల పత్రం.",
                    "issuing_authority_en": "Tahsildar / Village Revenue Officer",
                    "issuing_authority_te": "తహశీల్దార్ కార్యాలయం / రెవెన్యూ విభాగం",
                    "preparation_tips_en": "Check plot boundary numbers and village layout sheet.",
                    "preparation_tips_te": "స్థలం హద్దులు మరియు కొలతలు సరిగ్గా ఉన్నాయో లేదో నిర్ధారించుకోండి.",
                    "is_mandatory": True
                },
                {
                    "document_name_en": "Bank Account Passbook (MGNREGS Linked)",
                    "document_name_te": "బ్యాంక్ పాస్‌బుక్ (ఉపాధి హామీ లింక్ చేయబడినది)",
                    "purpose_en": "Stage-wise direct fund disbursement.",
                    "purpose_te": "దశలవారీగా బిల్లుల డబ్బులు జమ కావడం కోసం.",
                    "issuing_authority_en": "Bank",
                    "issuing_authority_te": "బ్యాంకు",
                    "preparation_tips_en": "Aadhaar DBT enabled account is mandatory.",
                    "preparation_tips_te": "డీబీటీ సౌకర్యం ఉన్న బ్యాంకు ఖాతా పాస్‌బుక్ కాపీ ఇవ్వండి.",
                    "is_mandatory": True
                }
            ],
            "steps": [
                {
                    "step_number": 1,
                    "title_en": "Verification in Awas+ Rural Housing Survey",
                    "title_te": "ఆవాస్+ గ్రామీణ గృహ నిర్మాణ సర్వేలో నమోదు",
                    "description_en": "Verify that your name is in the Grama Panchayat Awas+ waiting list prepared by the Engineering Assistant in Konanki.",
                    "description_te": "కొనంకి గ్రామ సచివాలయ ఇంజనీరింగ్ సహాయకుడు నిర్వహించే ఆవాస్+ సర్వేలో మీ పేరు నమోదై ఉందో లేదో చూడండి.",
                    "portal_or_offline_en": "Grama Sachivalayam / Engineering Assistant",
                    "portal_or_offline_te": "గ్రామ సచివాలయం / ఇంజనీరింగ్ అసిస్టెంట్",
                    "caution_warning_en": "Do not pay any middlemen for inclusion in the housing survey.",
                    "caution_warning_te": "గృహ సర్వేలో పేరు చేరుస్తామని చెప్పే దళారులను నమ్మి డబ్బులు ఇవ్వవద్దు."
                },
                {
                    "step_number": 2,
                    "title_en": "Receive Sanction Order and Construction Layout Peg-marking",
                    "title_te": "మంజూరు పత్రం (శాంక్షన్ ఆర్డర్) మరియు పునాది మార్కింగ్",
                    "description_en": "Upon sanction, obtain the official housing sanction letter and get plot boundaries demarcated on the ground.",
                    "description_te": "శాంక్షన్ ఆర్డర్ అందుకున్న తర్వాత స్థలంలో పునాది మార్కింగ్ వేయించండి.",
                    "portal_or_offline_en": "Housing Department / Sachivalayam",
                    "portal_or_offline_te": "హౌసింగ్ శాఖ / సచివాలయం",
                    "caution_warning_en": "Construct according to the approved standard minimum plinth area (25 sq meters).",
                    "caution_warning_te": "ప్రభుత్వ నిబంధనల ప్రకారం కనీసం 25 చదరపు మీటర్ల విస్తీర్ణంలో నిర్మాణం చేపట్టాలి."
                },
                {
                    "step_number": 3,
                    "title_en": "Stage-wise Geotagging and Payment Releases",
                    "title_te": "దశలవారీ జియోట్యాగింగ్ మరియు బిల్లుల విడుదల",
                    "description_en": "After completing Basement, Lintel, Roof slab, and Final plastering, the village assistant clicks geotagged photos to trigger automatic bank transfers.",
                    "description_te": "బేస్‌మెంట్, గోడలు, శ్లాబ్ పూర్తయిన వెంటనే సచివాలయ సహాయకుడితో ఫొటోలు తీయించి బిల్లులు రిలీజ్ చేయించుకోండి.",
                    "portal_or_offline_en": "AwaasApp Geotagging",
                    "portal_or_offline_te": "ఆవాస్ మొబైల్ యాప్ జియోట్యాగ్",
                    "caution_warning_en": "Ensure proper geotag coordinates match the allotted plot layout.",
                    "caution_warning_te": "ఫొటో తీసిన వెంటనే మీ బ్యాంకు ఖాతాలో డబ్బులు జమ అవుతాయి."
                }
            ]
        }
    ]

    for s_data in schemes_data:
        existing = GovernmentScheme.query.get(s_data["id"])
        if not existing:
            scheme = GovernmentScheme(
                id=s_data["id"],
                name_en=s_data["name_en"],
                name_te=s_data["name_te"],
                category=s_data["category"],
                description_en=s_data["description_en"],
                description_te=s_data["description_te"],
                target_beneficiaries_en=s_data["target_beneficiaries_en"],
                target_beneficiaries_te=s_data["target_beneficiaries_te"],
                state_or_central=s_data["state_or_central"],
                benefits_summary_en=s_data["benefits_summary_en"],
                benefits_summary_te=s_data["benefits_summary_te"],
                official_url=s_data["official_url"],
                source_id=s_data["source_id"],
                last_verified_at=s_data["last_verified_at"],
                important_notes_en=s_data["important_notes_en"],
                important_notes_te=s_data["important_notes_te"]
            )
            db.session.add(scheme)
            db.session.commit()

            # Seed Criteria
            for c in s_data.get("criteria", []):
                crit = EligibilityCriterion(
                    scheme_id=scheme.id,
                    rule_code=c["rule_code"],
                    question_en=c["question_en"],
                    question_te=c["question_te"],
                    condition_type=c["condition_type"],
                    expected_value=c["expected_value"],
                    explanation_en=c["explanation_en"],
                    explanation_te=c["explanation_te"],
                    is_mandatory=c.get("is_mandatory", True)
                )
                db.session.add(crit)

            # Seed Documents
            for d in s_data.get("documents", []):
                doc = RequiredDocument(
                    scheme_id=scheme.id,
                    document_name_en=d["document_name_en"],
                    document_name_te=d["document_name_te"],
                    purpose_en=d["purpose_en"],
                    purpose_te=d["purpose_te"],
                    issuing_authority_en=d["issuing_authority_en"],
                    issuing_authority_te=d["issuing_authority_te"],
                    preparation_tips_en=d["preparation_tips_en"],
                    preparation_tips_te=d["preparation_tips_te"],
                    is_mandatory=d.get("is_mandatory", True)
                )
                db.session.add(doc)

            # Seed Steps
            for st in s_data.get("steps", []):
                step = ApplicationStep(
                    scheme_id=scheme.id,
                    step_number=st["step_number"],
                    title_en=st["title_en"],
                    title_te=st["title_te"],
                    description_en=st["description_en"],
                    description_te=st["description_te"],
                    portal_or_offline_en=st["portal_or_offline_en"],
                    portal_or_offline_te=st["portal_or_offline_te"],
                    caution_warning_en=st.get("caution_warning_en"),
                    caution_warning_te=st.get("caution_warning_te")
                )
                db.session.add(step)

            db.session.commit()

    print("Verified government schemes seeded successfully.")
