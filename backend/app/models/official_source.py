from datetime import datetime
from app.extensions import db

class OfficialSource(db.Model):
    __tablename__ = "official_sources"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    official_url = db.Column(db.String(500), nullable=False)
    department = db.Column(db.String(255), nullable=False)
    verification_date = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to schemes
    schemes = db.relationship("GovernmentScheme", back_populates="source", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "official_url": self.official_url,
            "department": self.department,
            "verification_date": self.verification_date,
            "category": self.category,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
