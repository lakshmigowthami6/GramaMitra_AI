import re
from sqlalchemy import or_
from app.models.scheme import GovernmentScheme
from app.models.faq import FAQ
from app.models.lesson import DigitalLiteracyLesson

class KnowledgeRetriever:
    @staticmethod
    def search_schemes(query, limit=5):
        if not query or not query.strip():
            return GovernmentScheme.query.limit(limit).all()

        tokens = [t.lower().strip() for t in query.split() if len(t.strip()) > 1]
        if not tokens:
            return GovernmentScheme.query.limit(limit).all()

        filters = []
        for t in tokens:
            pattern = f"%{t}%"
            filters.append(GovernmentScheme.name_en.ilike(pattern))
            filters.append(GovernmentScheme.name_te.ilike(pattern))
            filters.append(GovernmentScheme.category.ilike(pattern))
            filters.append(GovernmentScheme.description_en.ilike(pattern))
            filters.append(GovernmentScheme.description_te.ilike(pattern))
            filters.append(GovernmentScheme.target_beneficiaries_en.ilike(pattern))
            filters.append(GovernmentScheme.target_beneficiaries_te.ilike(pattern))

        results = GovernmentScheme.query.filter(or_(*filters)).limit(limit).all()
        return results

    @staticmethod
    def get_scheme_by_id_or_name(scheme_identifier):
        if not scheme_identifier:
            return None
        # Try direct ID
        scheme = GovernmentScheme.query.get(scheme_identifier)
        if scheme:
            return scheme

        # Try partial match on ID or name
        pattern = f"%{scheme_identifier.lower().strip()}%"
        scheme = GovernmentScheme.query.filter(
            or_(
                GovernmentScheme.id.ilike(pattern),
                GovernmentScheme.name_en.ilike(pattern),
                GovernmentScheme.name_te.ilike(pattern)
            )
        ).first()
        return scheme

    @staticmethod
    def search_faqs(query, limit=4):
        if not query or not query.strip():
            return FAQ.query.limit(limit).all()

        tokens = [t.lower().strip() for t in query.split() if len(t.strip()) > 1]
        filters = []
        for t in tokens:
            pattern = f"%{t}%"
            filters.append(FAQ.question_en.ilike(pattern))
            filters.append(FAQ.question_te.ilike(pattern))
            filters.append(FAQ.answer_en.ilike(pattern))
            filters.append(FAQ.answer_te.ilike(pattern))
            filters.append(FAQ.keywords.ilike(pattern))
            filters.append(FAQ.category.ilike(pattern))

        return FAQ.query.filter(or_(*filters)).limit(limit).all()

    @staticmethod
    def search_lessons(query, limit=3):
        if not query or not query.strip():
            return DigitalLiteracyLesson.query.order_by(DigitalLiteracyLesson.order_index).limit(limit).all()

        tokens = [t.lower().strip() for t in query.split() if len(t.strip()) > 1]
        filters = []
        for t in tokens:
            pattern = f"%{t}%"
            filters.append(DigitalLiteracyLesson.title_en.ilike(pattern))
            filters.append(DigitalLiteracyLesson.title_te.ilike(pattern))
            filters.append(DigitalLiteracyLesson.summary_en.ilike(pattern))
            filters.append(DigitalLiteracyLesson.summary_te.ilike(pattern))
            filters.append(DigitalLiteracyLesson.module_category.ilike(pattern))

        return DigitalLiteracyLesson.query.filter(or_(*filters)).limit(limit).all()

    @classmethod
    def get_grounded_context_for_query(cls, query, lang="te"):
        """
        Retrieves factual database records relevant to the user query and formats them
        into a structured text context block for Gemini grounding.
        """
        schemes = cls.search_schemes(query, limit=3)
        faqs = cls.search_faqs(query, limit=3)
        lessons = cls.search_lessons(query, limit=2)

        context_lines = []
        referenced_sources = []

        if schemes:
            context_lines.append("=== VERIFIED GOVERNMENT SCHEMES DATA ===")
            for s in schemes:
                is_te = lang == "te"
                name = s.name_te if is_te else s.name_en
                desc = s.description_te if is_te else s.description_en
                beneficiaries = s.target_beneficiaries_te if is_te else s.target_beneficiaries_en
                benefits = s.benefits_summary_te if is_te else s.benefits_summary_en
                
                context_lines.append(f"\nScheme ID: {s.id}")
                context_lines.append(f"Name: {name} (English: {s.name_en})")
                context_lines.append(f"Government: {s.state_or_central}")
                context_lines.append(f"Category: {s.category}")
                context_lines.append(f"Target Beneficiaries: {beneficiaries}")
                context_lines.append(f"Benefits: {benefits}")
                context_lines.append(f"Official Portal: {s.official_url}")
                context_lines.append(f"Last Verified: {s.last_verified_at}")

                # Criteria
                if s.criteria:
                    context_lines.append("Eligibility Criteria:")
                    for c in s.criteria:
                        q = c.question_te if is_te else c.question_en
                        exp = c.explanation_te if is_te else c.explanation_en
                        context_lines.append(f" - [{c.rule_code}] {q} (Expected: {c.expected_value}) -> {exp}")

                # Documents
                if s.documents:
                    context_lines.append("Required Documents:")
                    for d in s.documents:
                        doc_name = d.document_name_te if is_te else d.document_name_en
                        authority = d.issuing_authority_te if is_te else d.issuing_authority_en
                        context_lines.append(f" - {doc_name}: Issued by {authority}")

                # Steps
                if s.steps:
                    context_lines.append("Application Steps:")
                    for st in s.steps:
                        st_title = st.title_te if is_te else st.title_en
                        st_desc = st.description_te if is_te else st.description_en
                        channel = st.portal_or_offline_te if is_te else st.portal_or_offline_en
                        context_lines.append(f" Step {st.step_number}. {st_title} ({channel}): {st_desc}")

                referenced_sources.append({
                    "id": s.id,
                    "name": name,
                    "url": s.official_url,
                    "verified": s.last_verified_at
                })

        if faqs:
            context_lines.append("\n=== RELEVANT OFFICIAL FAQS ===")
            for f in faqs:
                is_te = lang == "te"
                q = f.question_te if is_te else f.question_en
                a = f.answer_te if is_te else f.answer_en
                context_lines.append(f"Q: {q}\nA: {a}")

        if lessons:
            context_lines.append("\n=== DIGITAL LITERACY GUIDES ===")
            for l in lessons:
                is_te = lang == "te"
                t = l.title_te if is_te else l.title_en
                sm = l.summary_te if is_te else l.summary_en
                context_lines.append(f"Lesson [{l.id}]: {t} - {sm}")

        grounded_text = "\n".join(context_lines)
        return grounded_text, referenced_sources, schemes
