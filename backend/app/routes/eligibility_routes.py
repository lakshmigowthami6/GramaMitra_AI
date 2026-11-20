from flask import Blueprint, request, jsonify
from app.services.eligibility_service import EligibilityEvaluator
from app.models.scheme import GovernmentScheme
from app.models.eligibility import EligibilityCriterion
from app.utils.validators import validate_language

eligibility_bp = Blueprint("eligibility", __name__)

@eligibility_bp.route("/eligibility/<scheme_id>", methods=["GET"])
def get_eligibility_criteria(scheme_id):
    lang = validate_language(request.args.get("lang", "te"))
    scheme = GovernmentScheme.query.get(scheme_id)
    if not scheme:
        return jsonify({
            "error": "Not Found",
            "message": "పథకం కనుగొనబడలేదు" if lang == "te" else "Scheme not found"
        }), 404

    criteria = EligibilityCriterion.query.filter_by(scheme_id=scheme_id).all()
    return jsonify({
        "scheme_id": scheme.id,
        "scheme_name": scheme.name_te if lang == "te" else scheme.name_en,
        "criteria": [c.to_dict(lang) for c in criteria]
    }), 200

@eligibility_bp.route("/eligibility/check", methods=["POST"])
def check_eligibility():
    data = request.get_json() or {}
    scheme_id = data.get("scheme_id")
    user_answers = data.get("answers", {})
    lang = validate_language(data.get("lang", "te"))

    if not scheme_id:
        return jsonify({
            "error": "Bad Request",
            "message": "పథకం ID అవసరం (Scheme ID is required)"
        }), 400

    evaluation = EligibilityEvaluator.evaluate(scheme_id, user_answers, lang=lang)
    return jsonify(evaluation), 200
