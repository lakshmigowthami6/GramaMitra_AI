from flask import Blueprint, request, jsonify
from app.models.faq import FAQ
from app.services.retrieval_service import KnowledgeRetriever
from app.utils.validators import validate_language

faq_bp = Blueprint("faqs", __name__)

@faq_bp.route("/faqs", methods=["GET"])
def get_faqs():
    lang = validate_language(request.args.get("lang", "te"))
    category = request.args.get("category")
    query = request.args.get("q")

    if query:
        faqs = KnowledgeRetriever.search_faqs(query, limit=20)
    elif category:
        faqs = FAQ.query.filter(FAQ.category.ilike(f"%{category}%")).all()
    else:
        faqs = FAQ.query.all()

    return jsonify({
        "count": len(faqs),
        "faqs": [f.to_dict(lang) for f in faqs]
    }), 200

@faq_bp.route("/faqs/categories", methods=["GET"])
def get_faq_categories():
    categories = [
        {"id": "all", "name_en": "All FAQs", "name_te": "అన్ని ప్రశ్నలు"},
        {"id": "General", "name_en": "About GramaMitra AI", "name_te": "గ్రామమిత్ర AI గురించి"},
        {"id": "Schemes", "name_en": "Welfare Schemes", "name_te": "సంక్షేమ పథకాలు"},
        {"id": "Eligibility", "name_en": "Eligibility & Rules", "name_te": "అర్హతలు & నిబంధనలు"},
        {"id": "Documents", "name_en": "Required Documents", "name_te": "కావాల్సిన పత్రాలు"},
        {"id": "Portal Errors", "name_en": "Portal Errors & Fixes", "name_te": "వెబ్‌సైట్ ఎర్రర్లు & పరిష్కారాలు"},
        {"id": "Digital Safety", "name_en": "Digital Safety & Fraud", "name_te": "డిజిటల్ భద్రత & మోసాలు"}
    ]
    return jsonify(categories), 200
