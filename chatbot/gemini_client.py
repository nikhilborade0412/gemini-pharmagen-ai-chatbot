import os
from dotenv import load_dotenv
from google import genai
import time


class GeminiClient:

    def __init__(self):
        load_dotenv()

        # ✅ Use correct env variable (keep same as your setup)
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")

        self.client = genai.Client(api_key=api_key)

    def generate_response(self, prompt: str, history: list):

        # 🔹 Build full conversation context
        full_prompt = ""

        for msg in history:
            role = msg["role"]
            text = msg["parts"][0]

<<<<<<< HEAD
        except Exception as e:
            return f"Error communicating with Gemini API: {str(e)}"
=======
            if role == "user":
                full_prompt += f"User: {text}\n"
            else:
                full_prompt += f"Assistant: {text}\n"

        full_prompt += f"User: {prompt}\nAssistant:"

        # ✅ YOUR AVAILABLE MODELS (from test.py)
        models = [
            "models/gemini-flash-latest",   # 🔥 BEST (use this)
            "models/gemini-2.0-flash",      # fallback
            "models/gemini-2.5-flash"       # fallback (may be busy)
        ]

        # 🔁 Retry + fallback system
        for model in models:
            for i in range(2):  # retry each model
                try:
                    response = self.client.models.generate_content(
                        model=model,
                        contents=full_prompt
                    )
                    return response.text

                except Exception as e:
                    print(f"Retry {i+1} failed for {model}:", e)
                    time.sleep(2)

        # ❌ If all models fail
        return "⚠️ All Gemini models are busy. Please try again in a few seconds."
>>>>>>> f92b8c9 (Initial Commit)
