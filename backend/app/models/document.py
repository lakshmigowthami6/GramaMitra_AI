from app.extensions import db

class RequiredDocument(db.Model):
    __tablename__ = "required_documents"

    id = db.Column(db.Integer, primary_key=True)
    scheme_id = db.Column(db.String(64), db.ForeignKey("government_schemes.id"), nullable=False, index=True)
    document_name_en = db.Column(db.String(255), nullable=False)
    document_name_te = db.Column(db.String(255), nullable=False)
    purpose_en = db.Column(db.Text, nullable=False)
    purpose_te = db.Column(db.Text, nullable=False)
    issuing_authority_en = db.Column(db.String(255), nullable=False)
    issuing_authority_te = db.Column(db.String(255), nullable=False)
    preparation_tips_en = db.Column(db.Text, nullable=False)
    preparation_tips_te = db.Column(db.Text, nullable=False)
    is_mandatory = db.Column(db.Boolean, default=True)

    scheme = db.relationship("GovernmentScheme", back_populates="documents")

    def to_dict(self, lang="te"):
        is_te = lang == "te"
        return {
            "id": self.id,
            "scheme_id": self.scheme_id,
            "document_name": self.document_name_te if is_te else self.document_name_en,
            "document_name_en": self.document_name_en,
            "document_name_te": self.document_name_te,
            "purpose": self.purpose_te if is_te else self.purpose_en,
            "purpose_en": self.purpose_en,
            "purpose_te": self.purpose_te,
            "issuing_authority": self.issuing_authority_te if is_te else self.issuing_authority_en,
            "issuing_authority_en": self.issuing_authority_en,
            "issuing_authority_te": self.issuing_authority_te,
            "preparation_tips": self.preparation_tips_te if is_te else self.preparation_tips_en,
            "preparation_tips_en": self.preparation_tips_en,
            "preparation_tips_te": self.preparation_tips_te,
            "is_mandatory": self.is_mandatory
        }
