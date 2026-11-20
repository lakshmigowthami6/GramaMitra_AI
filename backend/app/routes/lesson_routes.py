from flask import Blueprint, request, jsonify
from app.models.lesson import DigitalLiteracyLesson
from app.utils.validators import validate_language

lesson_bp = Blueprint("lessons", __name__)

@lesson_bp.route("/lessons", methods=["GET"])
def get_lessons():
    lang = validate_language(request.args.get("lang", "te"))
    category = request.args.get("category")

    query = DigitalLiteracyLesson.query
    if category:
        query = query.filter(DigitalLiteracyLesson.module_category.ilike(f"%{category}%"))

    lessons = query.order_by(DigitalLiteracyLesson.order_index.asc()).all()
    return jsonify({
        "count": len(lessons),
        "lessons": [l.to_dict(lang=lang, include_quiz=False) for l in lessons]
    }), 200

@lesson_bp.route("/lessons/categories", methods=["GET"])
def get_lesson_categories():
    categories = [
        {"id": "all", "name_en": "All Lessons", "name_te": "అన్ని పాఠాలు"},
        {"id": "Smartphone Basics", "name_en": "Smartphone Basics", "name_te": "స్మార్ట్‌ఫోన్ ప్రాథమిక అంశాలు"},
        {"id": "Internet Basics", "name_en": "Internet & Web Basics", "name_te": "ఇంటర్నెట్ & బ్రౌజింగ్"},
        {"id": "Digital Safety & Fraud", "name_en": "Digital Safety & Fraud Prevention", "name_te": "డిజిటల్ భద్రత & మోసాల నివారణ"},
        {"id": "Government Portals", "name_en": "Using Government Portals", "name_te": "ప్రభుత్వ పోర్టల్స్ వినియోగం"}
    ]
    return jsonify(categories), 200

@lesson_bp.route("/lessons/<lesson_id>", methods=["GET"])
def get_lesson_detail(lesson_id):
    lang = validate_language(request.args.get("lang", "te"))
    lesson = DigitalLiteracyLesson.query.get(lesson_id)
    if not lesson:
        return jsonify({
            "error": "Not Found",
            "message": "పాఠం కనుగొనబడలేదు" if lang == "te" else "Lesson not found"
        }), 404

    return jsonify(lesson.to_dict(lang=lang, include_quiz=True)), 200
