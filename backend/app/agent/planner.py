class Planner:
    @staticmethod
    def create_plan(intent, scheme_id, category, query_text):
        tasks = []

        if intent == "portal_error":
            tasks.append({"tool": "PortalErrorTool", "args": {"error_text": query_text}})
            tasks.append({"tool": "FaqTool", "args": {"category": "Portal Errors"}})

        elif intent == "eligibility":
            if scheme_id:
                tasks.append({"tool": "EligibilityTool", "args": {"scheme_id": scheme_id}})
            else:
                tasks.append({"tool": "SchemeTool", "args": {"query": query_text}})

        elif intent == "documents":
            if scheme_id:
                tasks.append({"tool": "DocumentTool", "args": {"scheme_id": scheme_id}})
            else:
                tasks.append({"tool": "SchemeTool", "args": {"query": query_text}})

        elif intent == "application_steps":
            if scheme_id:
                tasks.append({"tool": "ApplicationTool", "args": {"scheme_id": scheme_id}})
            else:
                tasks.append({"tool": "SchemeTool", "args": {"query": query_text}})

        elif intent == "digital_literacy":
            tasks.append({"tool": "LearningTool", "args": {"query": query_text}})
            tasks.append({"tool": "FaqTool", "args": {"category": "Digital Safety"}})

        elif intent == "greeting":
            # Handled directly by conversational response
            pass

        elif intent == "scheme_details" and scheme_id:
            tasks.append({"tool": "SchemeTool", "args": {"scheme_id": scheme_id}})

        else:  # scheme_discovery or fallback
            tasks.append({"tool": "SchemeTool", "args": {"query": query_text, "category": category}})
            tasks.append({"tool": "FaqTool", "args": {"query": query_text}})

        return tasks
