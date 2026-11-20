import json
from datetime import datetime
from app.extensions import db

class ConversationHistory(db.Model):
    __tablename__ = "conversation_history"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), db.ForeignKey("user_sessions.session_id"), nullable=False, index=True)
    role = db.Column(db.String(20), nullable=False)  # "user" or "assistant"
    message_text = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(10), default="te")
    intent = db.Column(db.String(100), nullable=True)
    sources_json = db.Column(db.Text, nullable=True)  # JSON array of referenced schemes or sources
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    session = db.relationship("UserSession", back_populates="messages")

    def to_dict(self):
        try:
            sources = json.loads(self.sources_json) if self.sources_json else []
        except Exception:
            sources = []

        return {
            "id": self.id,
            "session_id": self.session_id,
            "role": self.role,
            "message": self.message_text,
            "language": self.language,
            "intent": self.intent,
            "sources": sources,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
