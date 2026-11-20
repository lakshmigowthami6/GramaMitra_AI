from datetime import datetime
from app.extensions import db

class GovernmentScheme(db.Model):
    __tablename__ = "government_schemes"

    id = db.Column(db.String(64), primary_key=True)  # e.g., 'pm-kisan', 'ntr-bharosa-pension'
    name_en = db.Column(db.String(255), nullable=False)
    name_te = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False, index=True)
    description_en = db.Column(db.Text, nullable=False)
    description_te = db.Column(db.Text, nullable=False)
    target_beneficiaries_en = db.Column(db.String(255), nullable=False)
    target_beneficiaries_te = db.Column(db.String(255), nullable=False)
    state_or_central = db.Column(db.String(50), nullable=False, default="Andhra Pradesh")
    benefits_summary_en = db.Column(db.Text, nullable=False)
    benefits_summary_te = db.Column(db.Text, nullable=False)
    official_url = db.Column(db.String(500), nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey("official_sources.id"), nullable=True)
    last_verified_at = db.Column(db.String(50), nullable=False)
    important_notes_en = db.Column(db.Text, nullable=True)
    important_notes_te = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    source = db.relationship("OfficialSource", back_populates="schemes")
    criteria = db.relationship("EligibilityCriterion", back_populates="scheme", cascade="all, delete-orphan", lazy="joined")
    documents = db.relationship("RequiredDocument", back_populates="scheme", cascade="all, delete-orphan", lazy="joined")
    steps = db.relationship("ApplicationStep", back_populates="scheme", cascade="all, delete-orphan", order_by="ApplicationStep.step_number", lazy="joined")

    def to_dict(self, lang="te", include_relations=False):
        is_te = lang == "te"
        data = {
            "id": self.id,
            "name": self.name_te if is_te else self.name_en,
            "name_en": self.name_en,
            "name_te": self.name_te,
            "category": self.category,
            "description": self.description_te if is_te else self.description_en,
            "description_en": self.description_en,
            "description_te": self.description_te,
            "target_beneficiaries": self.target_beneficiaries_te if is_te else self.target_beneficiaries_en,
            "target_beneficiaries_en": self.target_beneficiaries_en,
            "target_beneficiaries_te": self.target_beneficiaries_te,
            "state_or_central": self.state_or_central,
            "benefits_summary": self.benefits_summary_te if is_te else self.benefits_summary_en,
            "benefits_summary_en": self.benefits_summary_en,
            "benefits_summary_te": self.benefits_summary_te,
            "official_url": self.official_url,
            "last_verified_at": self.last_verified_at,
            "important_notes": self.important_notes_te if is_te else self.important_notes_en,
            "important_notes_en": self.important_notes_en,
            "important_notes_te": self.important_notes_te,
            "source": self.source.to_dict() if self.source else None,
            "criteria_count": len(self.criteria) if self.criteria else 0,
            "documents_count": len(self.documents) if self.documents else 0,
            "steps_count": len(self.steps) if self.steps else 0,
        }

        if include_relations:
            data["criteria"] = [c.to_dict(lang) for c in self.criteria]
            data["documents"] = [d.to_dict(lang) for d in self.documents]
            data["steps"] = [s.to_dict(lang) for s in self.steps]

        return data
