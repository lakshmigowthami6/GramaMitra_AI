from app.models.scheme import GovernmentScheme
from app.models.application_step import ApplicationStep

class ApplicationTool:
    @staticmethod
    def get_application_guide(scheme_id, lang="te"):
        is_te = lang == "te"
        scheme = GovernmentScheme.query.get(scheme_id)
        if not scheme:
            return {"found": False, "message": "పథకం కనుగొనబడలేదు" if is_te else "Scheme not found"}

        steps = ApplicationStep.query.filter_by(scheme_id=scheme_id).order_by(ApplicationStep.step_number).all()
        return {
            "found": True,
            "scheme_id": scheme.id,
            "scheme_name": scheme.name_te if is_te else scheme.name_en,
            "official_url": scheme.official_url,
            "steps": [s.to_dict(lang) for s in steps]
        }
