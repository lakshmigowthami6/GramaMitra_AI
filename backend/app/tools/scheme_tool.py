from app.models.scheme import GovernmentScheme
from app.services.retrieval_service import KnowledgeRetriever

class SchemeTool:
    @staticmethod
    def execute(query=None, scheme_id=None, category=None, lang="te"):
        is_te = lang == "te"
        if scheme_id:
            scheme = GovernmentScheme.query.get(scheme_id)
            if scheme:
                return {
                    "found": True,
                    "scheme": scheme.to_dict(lang=lang, include_relations=True)
                }
            return {
                "found": False,
                "message": "పథకం కనుగొనబడలేదు" if is_te else "Scheme not found"
            }

        if category:
            schemes = GovernmentScheme.query.filter(GovernmentScheme.category.ilike(f"%{category}%")).all()
        elif query:
            schemes = KnowledgeRetriever.search_schemes(query, limit=5)
        else:
            schemes = GovernmentScheme.query.limit(10).all()

        return {
            "found": len(schemes) > 0,
            "count": len(schemes),
            "schemes": [s.to_dict(lang=lang, include_relations=False) for s in schemes]
        }
