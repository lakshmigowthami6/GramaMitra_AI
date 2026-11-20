from flask import Blueprint, request, jsonify
from app.models.scheme import GovernmentScheme
from app.services.retrieval_service import KnowledgeRetriever
from app.utils.validators import validate_language

scheme_bp = Blueprint("schemes", __name__)

@scheme_bp.route("/schemes", methods=["GET"])
def get_schemes():
    lang = validate_language(request.args.get("lang", "te"))
    category = request.args.get("category")
    beneficiary = request.args.get("beneficiary")
    query = request.args.get("q")
    state_or_central = request.args.get("state_or_central")

    query_obj = GovernmentScheme.query

    if category:
        query_obj = query_obj.filter(GovernmentScheme.category.ilike(f"%{category}%"))
    if state_or_central:
        query_obj = query_obj.filter(GovernmentScheme.state_or_central.ilike(f"%{state_or_central}%"))
    if beneficiary:
        query_obj = query_obj.filter(
            (GovernmentScheme.target_beneficiaries_en.ilike(f"%{beneficiary}%")) |
            (GovernmentScheme.target_beneficiaries_te.ilike(f"%{beneficiary}%"))
        )

    if query:
        schemes = KnowledgeRetriever.search_schemes(query, limit=20)
    else:
        schemes = query_obj.order_by(GovernmentScheme.created_at.desc()).all()

    return jsonify({
        "count": len(schemes),
        "schemes": [s.to_dict(lang=lang, include_relations=False) for s in schemes]
    }), 200

@scheme_bp.route("/schemes/categories", methods=["GET"])
def get_categories():
    categories = [
        {"id": "all", "name_en": "All Schemes", "name_te": "అన్ని పథకాలు"},
        {"id": "Agriculture", "name_en": "Agriculture & Farming", "name_te": "వ్యవసాయం & రైతు సంక్షేమం"},
        {"id": "Social Security", "name_en": "Social Security & Pensions", "name_te": "సామాజిక భద్రత & పెన్షన్లు"},
        {"id": "Education", "name_en": "Education & Scholarships", "name_te": "విద్య & ఉపకార వేతనాలు"},
        {"id": "Healthcare", "name_en": "Healthcare & Medical", "name_te": "ఆరోగ్యం & ఉచిత వైద్యం"},
        {"id": "Housing", "name_en": "Housing & Shelter", "name_te": "గృహనిర్మాణం & ఇళ్ల స్థలాలు"},
        {"id": "Women Welfare", "name_en": "Women & Child Welfare", "name_te": "మహిళా & శిశు సంక్షేమం"}
    ]
    return jsonify(categories), 200

@scheme_bp.route("/schemes/<scheme_id>", methods=["GET"])
def get_scheme_detail(scheme_id):
    lang = validate_language(request.args.get("lang", "te"))
    scheme = KnowledgeRetriever.get_scheme_by_id_or_name(scheme_id)
    if not scheme:
        return jsonify({
            "error": "Not Found",
            "message": "పథకం కనుగొనబడలేదు (Scheme not found)"
        }), 404

    return jsonify(scheme.to_dict(lang=lang, include_relations=True)), 200
