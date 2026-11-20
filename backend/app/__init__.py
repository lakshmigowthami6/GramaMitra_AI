import os
from flask import Flask
from app.config import Config
from app.extensions import db, cors
from app.routes import register_routes
from app.utils.error_handlers import register_error_handlers


def create_app(config_class=Config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)

    # Ensure instance directory exists
    instance_dir = os.path.join(flask_app.root_path, "..", "instance")
    os.makedirs(instance_dir, exist_ok=True)

    # Initialize extensions
    db.init_app(flask_app)
    cors.init_app(flask_app, origins=flask_app.config.get("CORS_ORIGINS", "*"), supports_credentials=True)

    # Register routes & error handlers
    register_routes(flask_app)
    register_error_handlers(flask_app)

    # Create tables & auto-seed if empty
    with flask_app.app_context():
        from app import models  # noqa: F401 — Ensure models are imported
        db.create_all()
        try:
            from app.models.scheme import GovernmentScheme
            if GovernmentScheme.query.count() == 0:
                from seed.seed_schemes import seed_official_sources_and_schemes
                from seed.seed_faqs import seed_faqs
                from seed.seed_lessons import seed_lessons
                seed_official_sources_and_schemes()
                seed_faqs()
                seed_lessons()
        except Exception:
            pass

    return flask_app
