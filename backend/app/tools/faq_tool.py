from app.models.faq import FAQ
from app.services.retrieval_service import KnowledgeRetriever

class FaqTool:
    @staticmethod
    def search(query=None, category=None, lang="te"):
        if category:
            faqs = FAQ.query.filter(FAQ.category.ilike(f"%{category}%")).all()
        elif query:
            faqs = KnowledgeRetriever.search_faqs(query, limit=5)
        else:
            faqs = FAQ.query.limit(10).all()

        return {
            "count": len(faqs),
            "faqs": [f.to_dict(lang) for f in faqs]
        }
