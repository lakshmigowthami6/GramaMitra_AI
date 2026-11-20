import logging
from app.config import Config

logger = logging.getLogger(__name__)

class GeminiService:
    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        self.client = None
        if self.api_key:
            try:
                from google import genai
                self.client = genai.Client(api_key=self.api_key)
                logger.info("Google Gemini Client initialized successfully.")
            except Exception as e:
                logger.warning(f"Could not initialize Google GenAI Client: {e}")
                self.client = None

    def is_available(self):
        return bool(self.client and self.api_key)

    def generate_response(self, prompt, grounded_context="", language="te", conversation_history=None):
        if not self.is_available():
            logger.info("Gemini API key not configured or client unavailable. Returning None for factual fallback.")
            return None

        is_te = language == "te"

        system_instruction = f"""
You are "GramaMitra AI" (గ్రామమిత్ర AI), an intelligent, highly accessible, and trustworthy digital e-governance and digital literacy assistant.
This application was developed as a Community Service Project (CSP) specifically for rural citizens of Konanki Village, Martur Mandal, Bapatla District, Andhra Pradesh, India.
Your target users are rural citizens, farmers, elderly people, homemakers, and first-time smartphone users who need simple, respectful, and crystal-clear guidance.

CRITICAL INSTRUCTIONS:
1. Primary Language: Respond in { 'fluent, respectful, simple spoken Telugu (తెలుగు) that rural citizens easily understand' if is_te else 'simple, plain, respectful English' }.
2. GROUNDING RULE: You must ONLY use the verified facts provided below under "GROUNDED GOVERNMENT KNOWLEDGE BASE". NEVER hallucinate or invent eligibility rules, document lists, benefit amounts, application deadlines, or official URLs.
3. If the user asks about a scheme or service NOT present in the grounded knowledge base, politely state that verified official details are not currently in our database, and guide them to visit their local Grama Sachivalayam (గ్రామ సచివాలయం) or MeeSeva centre.
4. Structure your response clearly using bullet points, numbered steps, and bold section headings.
5. Emphasize digital safety: Warn users never to share Aadhaar OTPs, bank passwords, or PINs with anyone.
6. When explaining technical or government terms (e.g., eKYC, OTP, portal), explain them in very simple everyday village terms.
7. Tone: Warm, respectful ("నమస్కారం", "అయ్యా/అమ్మా"), encouraging, patient, and empowering.

GROUNDED GOVERNMENT KNOWLEDGE BASE:
{grounded_context if grounded_context else "No specific database records matched."}
"""

        try:
            full_prompt = f"{prompt}\n\nPlease provide a clear, helpful response in { 'Telugu' if is_te else 'English' }:"

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=full_prompt,
                config={
                    "system_instruction": system_instruction,
                    "temperature": 0.2,  # Low temperature for factual consistency
                }
            )

            if response and response.text:
                return response.text.strip()
            return None
        except Exception as e:
            logger.error(f"Gemini generation error: {e}")
            return None
