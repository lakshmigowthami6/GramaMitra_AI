from datetime import datetime
from app.extensions import db

class UserSession(db.Model):
    __tablename__ = "user_sessions"

    session_id = db.Column(db.String(100), primary_key=True)
    preferred_language = db.Column(db.String(10), default="te", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_active_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    messages = db.relationship("ConversationHistory", back_populates="session", cascade="all, delete-orphan", order_by="ConversationHistory.created_at", lazy="select")

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "preferred_language": self.preferred_language,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "last_active_at": self.last_active_at.isoformat() if self.last_active_at else None,
            "message_count": len(self.messages) if self.messages else 0
        }
