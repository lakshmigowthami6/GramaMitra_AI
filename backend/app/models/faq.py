from datetime import datetime
from app.extensions import db

class FAQ(db.Model):
    __tablename__ = "faqs"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False, index=True)
    question_en = db.Column(db.Text, nullable=False)
    question_te = db.Column(db.Text, nullable=False)
    answer_en = db.Column(db.Text, nullable=False)
    answer_te = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.String(500), nullable=True)
    official_reference = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self, lang="te"):
        is_te = lang == "te"
        return {
            "id": self.id,
            "category": self.category,
            "question": self.question_te if is_te else self.question_en,
            "question_en": self.question_en,
            "question_te": self.question_te,
            "answer": self.answer_te if is_te else self.answer_en,
            "answer_en": self.answer_en,
            "answer_te": self.answer_te,
            "official_reference": self.official_reference
        }
