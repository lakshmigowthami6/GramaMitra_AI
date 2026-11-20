import uuid
from datetime import datetime
from app.extensions import db
from app.models.user_session import UserSession
from app.models.conversation import ConversationHistory

def get_or_create_session(session_id=None, preferred_language="te"):
    if not session_id:
        session_id = f"gm-{uuid.uuid4().hex[:12]}"
    
    session = UserSession.query.get(session_id)
    if not session:
        session = UserSession(session_id=session_id, preferred_language=preferred_language)
        db.session.add(session)
        db.session.commit()
    else:
        if preferred_language and session.preferred_language != preferred_language:
            session.preferred_language = preferred_language
        session.last_active_at = datetime.utcnow()
        db.session.commit()
    return session

def add_message(session_id, role, text, language="te", intent=None, sources=None):
    session = get_or_create_session(session_id, language)
    sources_json = None
    if sources:
        import json
        sources_json = json.dumps(sources, ensure_ascii=False)

    msg = ConversationHistory(
        session_id=session.session_id,
        role=role,
        message_text=text,
        language=language,
        intent=intent,
        sources_json=sources_json
    )
    db.session.add(msg)
    session.last_active_at = datetime.utcnow()
    db.session.commit()
    return msg

def get_conversation_history(session_id, limit=20):
    session = UserSession.query.get(session_id)
    if not session:
        return []
    messages = ConversationHistory.query.filter_by(session_id=session_id).order_by(ConversationHistory.created_at.asc()).limit(limit).all()
    return [m.to_dict() for m in messages]

def clear_conversation_history(session_id):
    messages = ConversationHistory.query.filter_by(session_id=session_id).all()
    for m in messages:
        db.session.delete(m)
    db.session.commit()
    return True
