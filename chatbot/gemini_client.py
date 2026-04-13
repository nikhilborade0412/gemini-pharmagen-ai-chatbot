import os
from dotenv import load_dotenv
from google import genai


class GeminiClient:

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

        full_prompt = ""

        for msg in history:
            role = msg["role"]
            text = msg["parts"][0]

            if role == "user":
                full_prompt += f"User: {text}\n"
            else:
                full_prompt += f"Assistant: {text}\n"

        full_prompt += f"User: {prompt}\nAssistant:"

        # 🚨 NO try-except here
        response = self.client.models.generate_content(
            model="models/gemini-1.5-flash",  # ✅ more stable
            contents=full_prompt
        )

        return response.text
