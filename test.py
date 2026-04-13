from google import genai

client = genai.Client(api_key="AIzaSyCgZbYGWXWqamsCg9PF_FmC6xuhKYBydRM")

models = client.models.list()

for m in models:
    print(m.name)