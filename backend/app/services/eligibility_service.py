from app.models.scheme import GovernmentScheme
from app.models.eligibility import EligibilityCriterion

class EligibilityEvaluator:
    @staticmethod
    def evaluate(scheme_id, user_answers, lang="te"):
        """
        Evaluates user answers for a scheme's criteria.
        user_answers: dict of {rule_code: value}
        """
        is_te = lang == "te"
        scheme = GovernmentScheme.query.get(scheme_id)
        if not scheme:
            return {
                "status": "error",
                "message": "పథకం కనుగొనబడలేదు (Scheme not found)" if is_te else "Scheme not found"
            }

        criteria = EligibilityCriterion.query.filter_by(scheme_id=scheme_id).all()
        if not criteria:
            return {
                "status": "unclear",
                "scheme_id": scheme.id,
                "scheme_name": scheme.name_te if is_te else scheme.name_en,
                "summary": "ఈ పథకానికి ప్రత్యేక అర్హత నిబంధనలు నమోదు చేయబడలేదు." if is_te else "No specific eligibility rules recorded for this scheme.",
                "satisfied_conditions": [],
                "unmet_conditions": [],
                "pending_conditions": []
            }

        satisfied = []
        unmet = []
        pending = []

        for c in criteria:
            rule_code = c.rule_code
            user_val = user_answers.get(rule_code)

            rule_display = {
                "rule_code": rule_code,
                "question": c.question_te if is_te else c.question_en,
                "expected": c.expected_value,
                "user_value": user_val,
                "explanation": c.explanation_te if is_te else c.explanation_en,
                "is_mandatory": c.is_mandatory
            }

            if user_val is None or user_val == "":
                pending.append(rule_display)
                continue

            # Evaluate condition
            is_met = False
            ctype = c.condition_type

            try:
                if ctype == "boolean":
                    # Parse user boolean
                    val_bool = str(user_val).lower().strip() in ["true", "1", "yes", "అవును"]
                    exp_bool = str(c.expected_value).lower().strip() in ["true", "1", "yes", "అవును"]
                    is_met = (val_bool == exp_bool)

                elif ctype == "numeric_min":
                    u_num = float(user_val)
                    e_num = float(c.expected_value)
                    is_met = (u_num >= e_num)

                elif ctype == "numeric_max":
                    u_num = float(user_val)
                    e_num = float(c.expected_value)
                    is_met = (u_num <= e_num)

                elif ctype == "choice":
                    is_met = str(user_val).lower().strip() == str(c.expected_value).lower().strip()

                else:
                    is_met = str(user_val).strip().lower() == str(c.expected_value).strip().lower()

            except Exception:
                is_met = False

            if is_met:
                satisfied.append(rule_display)
            else:
                unmet.append(rule_display)

        # Determine overall preliminary status
        if unmet:
            # Check if any mandatory condition is unmet
            mandatory_unmet = [u for u in unmet if u["is_mandatory"]]
            if mandatory_unmet:
                status = "ineligible"
                status_label = "ఒకటి లేదా అంతకంటే ఎక్కువ తప్పనిసరి నిబంధనలు సరిపోలడం లేదు (May not meet one or more conditions)" if is_te else "May not meet one or more mandatory conditions"
            else:
                status = "conditional"
                status_label = "కొన్ని షరతులతో అర్హత ఉండవచ్చు (Conditional eligibility)" if is_te else "Conditional eligibility"
        elif pending:
            status = "unclear"
            status_label = "మరింత సమాచారం అవసరం (More information is required)" if is_te else "More information is required"
        else:
            status = "eligible"
            status_label = "అందించిన సమాచారం ప్రకారం ప్రాథమికంగా అర్హులుగా కనిపిస్తున్నారు (Appears eligible based on the information provided)" if is_te else "Appears eligible based on the information provided"

        disclaimer = (
            "గమనిక: ఇది కేవలం ప్రాథమిక మార్గదర్శకత్వం మాత్రమే. ఇది అధికారిక నిర్ణయం కాదు. మీ గ్రామ/వార్డు సచివాలయం లేదా అధికారిక పోర్టల్ ద్వారా అసలైన అర్హతను నిర్ధారించుకోండి."
            if is_te else
            "Note: This is preliminary guidance only and not an official government decision. Please verify final eligibility at your Grama/Ward Sachivalayam or official portal."
        )

        return {
            "status": status,
            "status_label": status_label,
            "scheme_id": scheme.id,
            "scheme_name": scheme.name_te if is_te else scheme.name_en,
            "official_url": scheme.official_url,
            "satisfied_conditions": satisfied,
            "unmet_conditions": unmet,
            "pending_conditions": pending,
            "total_rules": len(criteria),
            "disclaimer": disclaimer
        }
