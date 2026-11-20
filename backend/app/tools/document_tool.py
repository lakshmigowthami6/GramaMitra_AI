from app.models.scheme import GovernmentScheme
from app.models.document import RequiredDocument

class DocumentTool:
    @staticmethod
    def get_documents_for_scheme(scheme_id, lang="te"):
        is_te = lang == "te"
        scheme = GovernmentScheme.query.get(scheme_id)
        if not scheme:
            return {"found": False, "message": "పథకం కనుగొనబడలేదు" if is_te else "Scheme not found"}

        documents = RequiredDocument.query.filter_by(scheme_id=scheme_id).all()
        return {
            "found": True,
            "scheme_id": scheme.id,
            "scheme_name": scheme.name_te if is_te else scheme.name_en,
            "documents": [d.to_dict(lang) for d in documents]
        }
