import os
from dotenv import load_dotenv
from google import genai


class GeminiClient:
    """
    Handles communication with Gemini API with fallback support.
    """

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")

        self.client = genai.Client(
            api_key=api_key,
            http_options={"api_version": "v1"}
        )

    def generate_response(self, prompt: str, history: list):
        """
        Generate response using multiple Gemini models with fallback
        """

        # ✅ Build full prompt with chat history
        full_prompt = ""

        for msg in history:
            role = msg["role"]
            text = msg["parts"][0]

            if role == "user":
                full_prompt += f"User: {text}\n"
            else:
                full_prompt += f"Assistant: {text}\n"

        full_prompt += f"User: {prompt}\nAssistant:"

        # ✅ Multi-model fallback system
        models = [
            "models/gemini-2.5-flash",   # fast but unstable
            "models/gemini-1.5-flash",   # stable
            "models/gemini-pro"          # backup
        ]

        for model_name in models:
            try:
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=full_prompt
                )
                return response.text

            except Exception as e:
                print(f"{model_name} failed: {e}")

        # ✅ Final fallback if all models fail
        return "⚠️ All AI models are currently busy. Please try again in a few seconds."
