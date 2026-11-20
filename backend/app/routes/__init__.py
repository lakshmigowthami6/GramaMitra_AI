from app.routes.health_routes import health_bp
from app.routes.scheme_routes import scheme_bp
from app.routes.eligibility_routes import eligibility_bp
from app.routes.document_routes import document_bp
from app.routes.application_routes import application_bp
from app.routes.lesson_routes import lesson_bp
from app.routes.faq_routes import faq_bp
from app.routes.chat_routes import chat_bp
from app.routes.error_help_routes import error_help_bp

from flask import jsonify

def register_routes(app):
    @app.route("/", methods=["GET"])
    def root():
        return jsonify({
            "service": "GramaMitra AI API",
            "frontend_url": "http://localhost:3000",
            "health_check": "/api/health",
            "schemes": "/api/schemes",
            "lessons": "/api/lessons",
            "faqs": "/api/faqs",
            "chat": "/api/chat",
            "status": "online"
        }), 200

    @app.route("/api", methods=["GET"])
    def api_root():
        return jsonify({
            "service": "GramaMitra AI API Endpoints",
            "endpoints": [
                "/api/health",
                "/api/schemes",
                "/api/schemes/categories",
                "/api/schemes/<scheme_id>",
                "/api/lessons",
                "/api/lessons/categories",
                "/api/lessons/<lesson_id>",
                "/api/faqs",
                "/api/faqs/categories",
                "/api/chat",
                "/api/chat/history",
                "/api/eligibility/<scheme_id>",
                "/api/eligibility/<scheme_id>/check",
                "/api/documents/<scheme_id>",
                "/api/application/<scheme_id>/steps"
            ]
        }), 200

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(scheme_bp, url_prefix="/api")
    app.register_blueprint(eligibility_bp, url_prefix="/api")
    app.register_blueprint(document_bp, url_prefix="/api")
    app.register_blueprint(application_bp, url_prefix="/api")
    app.register_blueprint(lesson_bp, url_prefix="/api")
    app.register_blueprint(faq_bp, url_prefix="/api")
    app.register_blueprint(chat_bp, url_prefix="/api")
    app.register_blueprint(error_help_bp, url_prefix="/api")
