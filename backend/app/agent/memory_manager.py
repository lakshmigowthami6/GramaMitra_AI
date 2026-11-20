from app.services.session_service import get_conversation_history, add_message, clear_conversation_history

class MemoryManager:
    @staticmethod
    def get_history(session_id, limit=6):
        return get_conversation_history(session_id, limit=limit)

    @staticmethod
    def save_turn(session_id, user_text, bot_text, lang="te", intent=None, sources=None):
        add_message(session_id, "user", user_text, language=lang, intent=intent)
        add_message(session_id, "assistant", bot_text, language=lang, intent=intent, sources=sources)

    @staticmethod
    def clear(session_id):
        return clear_conversation_history(session_id)
