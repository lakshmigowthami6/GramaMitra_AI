from flask import Blueprint, request, jsonify
from app.services.ai_service import AIService
from app.services.session_service import get_conversation_history, clear_conversation_history
from app.utils.validators import sanitize_string, validate_language, validate_session_id

chat_bp = Blueprint("chat", __name__)
ai_service = AIService()

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = sanitize_string(data.get("message", ""), max_length=1500)
    session_id = validate_session_id(data.get("session_id"))
    preferred_language = validate_language(data.get("language", "te"))

    if not message:
        return jsonify({
            "error": "Bad Request",
            "message": "సందేశం ఖాళీగా ఉండకూడదు (Message cannot be empty)"
        }), 400

    result = ai_service.process_message(
        user_query=message,
        session_id=session_id,
        preferred_language=preferred_language
    )
    return jsonify(result), 200

@chat_bp.route("/chat/history", methods=["GET"])
def get_history():
    session_id = validate_session_id(request.args.get("session_id"))
    if not session_id:
        return jsonify({"history": []}), 200

    history = get_conversation_history(session_id, limit=30)
    return jsonify({"session_id": session_id, "history": history}), 200

@chat_bp.route("/chat/history", methods=["DELETE"])
def clear_history():
    session_id = validate_session_id(request.args.get("session_id"))
    if not session_id:
        return jsonify({"success": False, "message": "Session ID required"}), 400

    clear_conversation_history(session_id)
    return jsonify({"success": True, "message": "చాట్ చరిత్ర విజయవంతంగా తొలగించబడింది"}), 200
