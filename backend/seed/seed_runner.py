import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app as create_flask_app
from app.config import Config
from app.extensions import db
from seed.seed_schemes import seed_official_sources_and_schemes
from seed.seed_faqs import seed_faqs
from seed.seed_lessons import seed_lessons

def run_seed():
    flask_app = create_flask_app(Config)
    with flask_app.app_context():
        print("Creating database tables if not existing...")
        db.create_all()

        print("Seeding verified official sources and government schemes...")
        seed_official_sources_and_schemes()

        print("Seeding community and e-governance FAQs...")
        seed_faqs()

        print("Seeding digital literacy modules and quizzes...")
        seed_lessons()

        print("All database records seeded successfully for GramaMitra AI!")

if __name__ == "__main__":
    run_seed()
