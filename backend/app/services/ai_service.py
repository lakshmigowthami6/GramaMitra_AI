import logging
from app.agent.intent_classifier import IntentClassifier
from app.agent.query_processor import QueryProcessor
from app.agent.planner import Planner
from app.agent.tool_router import ToolRouter
from app.agent.response_builder import ResponseBuilder
from app.agent.memory_manager import MemoryManager
from app.services.retrieval_service import KnowledgeRetriever
from app.services.gemini_service import GeminiService

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        self.gemini_service = GeminiService()

    def process_message(self, user_query, session_id=None, preferred_language=None):
        # 1. Determine Language
        detected_lang = QueryProcessor.detect_language(user_query)
        lang = preferred_language if preferred_language in ["te", "en"] else detected_lang

        # 2. Extract Entities & Classify Intent
        scheme_id = QueryProcessor.extract_scheme_id(user_query)
        category = QueryProcessor.extract_category(user_query)
        intent = IntentClassifier.classify(user_query)

        # 3. Create Execution Plan & Run Tools
        plan = Planner.create_plan(intent, scheme_id, category, user_query)
        tool_results = ToolRouter.execute_plan(plan, lang=lang)

        # 4. Grounded Context Retrieval
        grounded_context, sources, matched_schemes = KnowledgeRetriever.get_grounded_context_for_query(user_query, lang=lang)

        # 5. Generate Response (Gemini or Fallback)
        response_text = None
        is_fallback = False

        if self.gemini_service.is_available():
            try:
                response_text = self.gemini_service.generate_response(
                    prompt=user_query,
                    grounded_context=grounded_context,
                    language=lang
                )
            except Exception as e:
                logger.error(f"Error calling Gemini service: {e}")
                response_text = None

        if not response_text:
            is_fallback = True
            response_text = ResponseBuilder.build_fallback_response(intent, tool_results, user_query, lang=lang)

        # 6. Save Turn to Session Memory
        if session_id:
            MemoryManager.save_turn(
                session_id=session_id,
                user_text=user_query,
                bot_text=response_text,
                lang=lang,
                intent=intent,
                sources=sources
            )

        # 7. Generate contextual suggestions
        is_te = lang == "te"
        suggestions = []
        if intent in ["scheme_discovery", "greeting"]:
            suggestions = [
                "పీఎం కిసాన్ పథకానికి అర్హతలు ఏమిటి?" if is_te else "What are the eligibility criteria for PM-KISAN?",
                "ఎన్టీఆర్ భరోసా పెన్షన్‌కు ఏ పత్రాలు కావాలి?" if is_te else "What documents are required for NTR Bharosa Pension?",
                "వెబ్‌సైట్ ఎర్రర్ వస్తే ఏం చేయాలి?" if is_te else "What should I do if a portal shows an error?",
                "ఆన్‌లైన్ భద్రత ఎలా పాటించాలి?" if is_te else "How to practice online safety?"
            ]
        elif intent == "eligibility":
            suggestions = [
                "ఈ పథకానికి ఏ పత్రాలు కావాలి?" if is_te else "What documents are needed for this scheme?",
                "దరఖాస్తు ఎలా చేయాలి?" if is_te else "How to apply for this scheme?",
                "మరొక పథకం చూడండి" if is_te else "Check another scheme"
            ]
        elif intent == "portal_error":
            suggestions = [
                "ఈకేవైసీ (eKYC) విఫలమైతే పరిష్కారం ఏమిటి?" if is_te else "What to do if eKYC biometric fails?",
                "ఓటీపీ రాకపోతే ఏం చేయాలి?" if is_te else "What to do if OTP does not arrive?",
                "గ్రామ సచివాలయంలో ఎవరిని కలవాలి?" if is_te else "Who to contact at Grama Sachivalayam?"
            ]
        else:
            suggestions = [
                "రైతు పథకాల వివరాలు" if is_te else "Farmer welfare schemes",
                "వృద్ధాప్య పెన్షన్ వివరాలు" if is_te else "Old age pension details",
                "ఆరోగ్యశ్రీ ఆసుపత్రి కార్డు" if is_te else "Aarogyasri health card"
            ]

        return {
            "response": response_text,
            "language": lang,
            "intent": intent,
            "is_fallback": is_fallback,
            "sources": sources,
            "suggestions": suggestions,
            "session_id": session_id
        }
