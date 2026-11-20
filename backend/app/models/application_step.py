from app.extensions import db

class ApplicationStep(db.Model):
    __tablename__ = "application_steps"

    id = db.Column(db.Integer, primary_key=True)
    scheme_id = db.Column(db.String(64), db.ForeignKey("government_schemes.id"), nullable=False, index=True)
    step_number = db.Column(db.Integer, nullable=False)
    title_en = db.Column(db.String(255), nullable=False)
    title_te = db.Column(db.String(255), nullable=False)
    description_en = db.Column(db.Text, nullable=False)
    description_te = db.Column(db.Text, nullable=False)
    portal_or_offline_en = db.Column(db.String(100), nullable=False, default="Grama Sachivalayam / MeeSeva")
    portal_or_offline_te = db.Column(db.String(100), nullable=False, default="గ్రామ సచివాలయం / మీసేవ")
    caution_warning_en = db.Column(db.Text, nullable=True)
    caution_warning_te = db.Column(db.Text, nullable=True)

    scheme = db.relationship("GovernmentScheme", back_populates="steps")

    def to_dict(self, lang="te"):
        is_te = lang == "te"
        return {
            "id": self.id,
            "scheme_id": self.scheme_id,
            "step_number": self.step_number,
            "title": self.title_te if is_te else self.title_en,
            "title_en": self.title_en,
            "title_te": self.title_te,
            "description": self.description_te if is_te else self.description_en,
            "description_en": self.description_en,
            "description_te": self.description_te,
            "channel": self.portal_or_offline_te if is_te else self.portal_or_offline_en,
            "channel_en": self.portal_or_offline_en,
            "channel_te": self.portal_or_offline_te,
            "caution_warning": self.caution_warning_te if is_te else self.caution_warning_en,
            "caution_warning_en": self.caution_warning_en,
            "caution_warning_te": self.caution_warning_te
        }
