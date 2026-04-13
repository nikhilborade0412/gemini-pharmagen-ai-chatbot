import os
from dotenv import load_dotenv
from google import genai


class GeminiClient:
    """
    Handles communication with Gemini API using official SDK.
    """

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("GOOGLE_API_KEY")  # ✅ consistent with .env
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")

        # Initialize client
        self.client = genai.Client(
            api_key=api_key,
            http_options={"api_version": "v1"}
        )

    def generate_response(self, prompt: str, history: list):
        """
        Generate response from Gemini
        """

        # Combine history + prompt (better context)
        full_prompt = ""

        for msg in history:
            role = msg["role"]
            text = msg["parts"][0]

            if role == "user":
                full_prompt += f"User: {text}\n"
            else:
                full_prompt += f"Assistant: {text}\n"

        full_prompt += f"User: {prompt}\nAssistant:"

        response = self.client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=full_prompt
        )

        return response.text
