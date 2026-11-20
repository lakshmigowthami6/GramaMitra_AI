from app.tools.scheme_tool import SchemeTool
from app.tools.eligibility_tool import EligibilityTool
from app.tools.document_tool import DocumentTool
from app.tools.application_tool import ApplicationTool
from app.tools.faq_tool import FaqTool
from app.tools.learning_tool import LearningTool
from app.tools.portal_error_tool import PortalErrorTool

class ToolRouter:
    @staticmethod
    def execute_plan(plan, lang="te"):
        results = {}
        for item in plan:
            tool_name = item.get("tool")
            args = item.get("args", {}).copy()
            args["lang"] = lang

            if tool_name == "SchemeTool":
                results["schemes"] = SchemeTool.execute(**args)
            elif tool_name == "EligibilityTool":
                results["eligibility"] = EligibilityTool.get_scheme_criteria(**args)
            elif tool_name == "DocumentTool":
                results["documents"] = DocumentTool.get_documents_for_scheme(**args)
            elif tool_name == "ApplicationTool":
                results["application"] = ApplicationTool.get_application_guide(**args)
            elif tool_name == "FaqTool":
                results["faqs"] = FaqTool.search(**args)
            elif tool_name == "LearningTool":
                results["lessons"] = LearningTool.get_lessons(**args)
            elif tool_name == "PortalErrorTool":
                results["portal_error"] = PortalErrorTool.analyze_error(**args)

        return results
