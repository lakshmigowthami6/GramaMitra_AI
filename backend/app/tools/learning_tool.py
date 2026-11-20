from app.models.lesson import DigitalLiteracyLesson
from app.services.retrieval_service import KnowledgeRetriever

class LearningTool:
    @staticmethod
    def get_lessons(category=None, lesson_id=None, query=None, lang="te"):
        is_te = lang == "te"
        if lesson_id:
            lesson = DigitalLiteracyLesson.query.get(lesson_id)
            if lesson:
                return {
                    "found": True,
                    "lesson": lesson.to_dict(lang, include_quiz=True)
                }
            return {
                "found": False,
                "message": "పాఠం కనుగొనబడలేదు" if is_te else "Lesson not found"
            }

        if category:
            lessons = DigitalLiteracyLesson.query.filter(DigitalLiteracyLesson.module_category.ilike(f"%{category}%")).order_by(DigitalLiteracyLesson.order_index).all()
        elif query:
            lessons = KnowledgeRetriever.search_lessons(query, limit=5)
        else:
            lessons = DigitalLiteracyLesson.query.order_by(DigitalLiteracyLesson.order_index).all()

        return {
            "count": len(lessons),
            "lessons": [l.to_dict(lang, include_quiz=False) for l in lessons]
        }
