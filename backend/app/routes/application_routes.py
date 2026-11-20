from flask import Blueprint, request, jsonify
from app.models.scheme import GovernmentScheme
from app.models.application_step import ApplicationStep
from app.utils.validators import validate_language

application_bp = Blueprint("application", __name__)

@application_bp.route("/application-guide/<scheme_id>", methods=["GET"])
def get_application_guide(scheme_id):
    lang = validate_language(request.args.get("lang", "te"))
    scheme = GovernmentScheme.query.get(scheme_id)
    if not scheme:
        return jsonify({
            "error": "Not Found",
            "message": "పథకం కనుగొనబడలేదు" if lang == "te" else "Scheme not found"
        }), 404

    steps = ApplicationStep.query.filter_by(scheme_id=scheme_id).order_by(ApplicationStep.step_number).all()
    return jsonify({
        "scheme_id": scheme.id,
        "scheme_name": scheme.name_te if lang == "te" else scheme.name_en,
        "official_url": scheme.official_url,
        "steps": [s.to_dict(lang) for s in steps]
    }), 200
