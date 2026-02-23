import os
from dotenv import load_dotenv
from google import genai


class GeminiClient:
    """
    Handles communication with Gemini API using official SDK.
    """

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        # Force stable API version
        self.client = genai.Client(
            api_key=api_key,
            http_options={"api_version": "v1"}
        )

    def generate_response(self, prompt: str, history: list):

        try:
            response = self.client.models.generate_content(
                model="models/gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:
            return f"Error communicating with Gemini API: {str(e)}"