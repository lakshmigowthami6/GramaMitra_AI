from app.models.scheme import GovernmentScheme
from app.models.eligibility import EligibilityCriterion
from app.services.eligibility_service import EligibilityEvaluator

class EligibilityTool:
    @staticmethod
    def get_scheme_criteria(scheme_id, lang="te"):
        is_te = lang == "te"
        scheme = GovernmentScheme.query.get(scheme_id)
        if not scheme:
            return {"found": False, "message": "పథకం కనుగొనబడలేదు" if is_te else "Scheme not found"}

        criteria = EligibilityCriterion.query.filter_by(scheme_id=scheme_id).all()
        return {
            "found": True,
            "scheme_id": scheme.id,
            "scheme_name": scheme.name_te if is_te else scheme.name_en,
            "criteria": [c.to_dict(lang) for c in criteria]
        }

    @staticmethod
    def evaluate(scheme_id, user_answers, lang="te"):
        return EligibilityEvaluator.evaluate(scheme_id, user_answers, lang=lang)
