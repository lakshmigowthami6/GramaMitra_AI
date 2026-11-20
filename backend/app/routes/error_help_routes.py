from flask import Blueprint, request, jsonify
from app.tools.portal_error_tool import PortalErrorTool
from app.utils.validators import sanitize_string, validate_language

error_help_bp = Blueprint("error_help", __name__)

@error_help_bp.route("/portal-error/analyze", methods=["POST"])
def analyze_error():
    data = request.get_json() or {}
    error_text = sanitize_string(data.get("error_text", ""), max_length=1500)
    lang = validate_language(data.get("lang", "te"))

    if not error_text:
        return jsonify({
            "error": "Bad Request",
            "message": "ఎర్రర్ టెక్స్ట్ అవసరం (Error text is required)"
        }), 400

    result = PortalErrorTool.analyze_error(error_text, lang=lang)
    return jsonify(result), 200
