import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_answer(question, context):
    prompt = f"""
You're an insurance expert assistant. Given the context from an insurance document, answer the user's question.

Context:
\"\"\"
{context}
\"\"\"

Question:
{question}

Answer:"""

    response = model.generate_content(prompt)
    return response.text.strip()
