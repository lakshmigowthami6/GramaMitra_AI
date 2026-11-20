import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "gramamitra-default-dev-secret-2025")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'instance' / 'gramamitra.db'}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # CORS
    cors_raw = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173")
    CORS_ORIGINS = [origin.strip() for origin in cors_raw.split(",") if origin.strip()]

    # Gemini AI
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

    # App Info
    VILLAGE_NAME = "Konanki"
    MANDAL_NAME = "Martur"
    DISTRICT_NAME = "Bapatla"
    STATE_NAME = "Andhra Pradesh"
    PROJECT_NAME = "GramaMitra AI"

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
