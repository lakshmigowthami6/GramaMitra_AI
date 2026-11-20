from flask import Blueprint, request, jsonify
from app.models.scheme import GovernmentScheme
from app.models.document import RequiredDocument
from app.utils.validators import validate_language

document_bp = Blueprint("documents", __name__)

@document_bp.route("/documents/<scheme_id>", methods=["GET"])
def get_documents(scheme_id):
    lang = validate_language(request.args.get("lang", "te"))
    scheme = GovernmentScheme.query.get(scheme_id)
    if not scheme:
        return jsonify({
            "error": "Not Found",
            "message": "పథకం కనుగొనబడలేదు" if lang == "te" else "Scheme not found"
        }), 404

    docs = RequiredDocument.query.filter_by(scheme_id=scheme_id).all()
    return jsonify({
        "scheme_id": scheme.id,
        "scheme_name": scheme.name_te if lang == "te" else scheme.name_en,
        "documents": [d.to_dict(lang) for d in docs]
    }), 200
