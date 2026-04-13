import os
from dotenv import load_dotenv
from groq import Groq


class GeminiClient:   # keep same name to avoid changing app.py

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables.")

        self.client = Groq(api_key=api_key)

    def generate_response(self, prompt: str, history: list):

        messages = []

        # Add history
        for msg in history:
            role = msg["role"]
            content = msg["parts"][0]

            if role == "user":
                messages.append({"role": "user", "content": content})
            else:
                messages.append({"role": "assistant", "content": content})

        # Add current prompt
        messages.append({"role": "user", "content": prompt})

        # 🔥 Call Groq API
        response = self.client.chat.completions.create(
            model="llama3-70b-8192",   # BEST model
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message.content
