import json
from datetime import datetime
from app.extensions import db

class DigitalLiteracyLesson(db.Model):
    __tablename__ = "digital_literacy_lessons"

    id = db.Column(db.String(64), primary_key=True)
    module_category = db.Column(db.String(100), nullable=False, index=True)
    title_en = db.Column(db.String(255), nullable=False)
    title_te = db.Column(db.String(255), nullable=False)
    summary_en = db.Column(db.Text, nullable=False)
    summary_te = db.Column(db.Text, nullable=False)
    content_en = db.Column(db.Text, nullable=False)  # Markdown or structured text
    content_te = db.Column(db.Text, nullable=False)
    reading_time_minutes = db.Column(db.Integer, default=5)
    order_index = db.Column(db.Integer, default=1)
    icon_name = db.Column(db.String(64), default="BookOpen")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    quizzes = db.relationship("LessonQuiz", back_populates="lesson", cascade="all, delete-orphan", lazy="joined")

    def to_dict(self, lang="te", include_quiz=True):
        is_te = lang == "te"
        data = {
            "id": self.id,
            "module_category": self.module_category,
            "title": self.title_te if is_te else self.title_en,
            "title_en": self.title_en,
            "title_te": self.title_te,
            "summary": self.summary_te if is_te else self.summary_en,
            "summary_en": self.summary_en,
            "summary_te": self.summary_te,
            "content": self.content_te if is_te else self.content_en,
            "content_en": self.content_en,
            "content_te": self.content_te,
            "reading_time_minutes": self.reading_time_minutes,
            "order_index": self.order_index,
            "icon_name": self.icon_name,
            "quiz_count": len(self.quizzes) if self.quizzes else 0
        }
        if include_quiz:
            data["quizzes"] = [q.to_dict(lang) for q in self.quizzes]
        return data

class LessonQuiz(db.Model):
    __tablename__ = "lesson_quizzes"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.String(64), db.ForeignKey("digital_literacy_lessons.id"), nullable=False, index=True)
    question_en = db.Column(db.Text, nullable=False)
    question_te = db.Column(db.Text, nullable=False)
    options_json_en = db.Column(db.Text, nullable=False)  # JSON string of options
    options_json_te = db.Column(db.Text, nullable=False)
    correct_index = db.Column(db.Integer, nullable=False)
    explanation_en = db.Column(db.Text, nullable=False)
    explanation_te = db.Column(db.Text, nullable=False)

    lesson = db.relationship("DigitalLiteracyLesson", back_populates="quizzes")

    def to_dict(self, lang="te"):
        is_te = lang == "te"
        try:
            options = json.loads(self.options_json_te if is_te else self.options_json_en)
        except Exception:
            options = []

        return {
            "id": self.id,
            "lesson_id": self.lesson_id,
            "question": self.question_te if is_te else self.question_en,
            "question_en": self.question_en,
            "question_te": self.question_te,
            "options": options,
            "correct_index": self.correct_index,
            "explanation": self.explanation_te if is_te else self.explanation_en,
            "explanation_en": self.explanation_en,
            "explanation_te": self.explanation_te
        }
