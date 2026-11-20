from app.extensions import db

class EligibilityCriterion(db.Model):
    __tablename__ = "eligibility_criteria"

    id = db.Column(db.Integer, primary_key=True)
    scheme_id = db.Column(db.String(64), db.ForeignKey("government_schemes.id"), nullable=False, index=True)
    rule_code = db.Column(db.String(64), nullable=False)
    question_en = db.Column(db.Text, nullable=False)
    question_te = db.Column(db.Text, nullable=False)
    condition_type = db.Column(db.String(32), nullable=False, default="boolean")  # boolean, numeric_max, numeric_min, choice
    expected_value = db.Column(db.String(128), nullable=False)  # "true", "60", "500000", etc.
    options_json = db.Column(db.Text, nullable=True)  # JSON for choices if applicable
    explanation_en = db.Column(db.Text, nullable=False)
    explanation_te = db.Column(db.Text, nullable=False)
    is_mandatory = db.Column(db.Boolean, default=True)

    scheme = db.relationship("GovernmentScheme", back_populates="criteria")

    def to_dict(self, lang="te"):
        is_te = lang == "te"
        return {
            "id": self.id,
            "scheme_id": self.scheme_id,
            "rule_code": self.rule_code,
            "question": self.question_te if is_te else self.question_en,
            "question_en": self.question_en,
            "question_te": self.question_te,
            "condition_type": self.condition_type,
            "expected_value": self.expected_value,
            "explanation": self.explanation_te if is_te else self.explanation_en,
            "explanation_en": self.explanation_en,
            "explanation_te": self.explanation_te,
            "is_mandatory": self.is_mandatory
        }
