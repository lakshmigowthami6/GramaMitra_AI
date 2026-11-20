from flask import Blueprint, jsonify
from app.config import Config
from app.services.gemini_service import GeminiService

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health_check():
    gemini_svc = GeminiService()
    return jsonify({
        "status": "healthy",
        "service": Config.PROJECT_NAME,
        "village": f"{Config.VILLAGE_NAME}, {Config.MANDAL_NAME}, {Config.DISTRICT_NAME}, {Config.STATE_NAME}",
        "gemini_configured": gemini_svc.is_available(),
        "database": "connected"
    }), 200
