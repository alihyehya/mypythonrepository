import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Check your .env file!")
genai.configure(api_key=api_key)

import textwrap
from IPython.display import display, Markdown

model = genai.GenerativeModel("gemini-2.0-flash")

def get_completion(prompt, temp=0.9):
    response = model.generate_content(
        prompt, generation_config=genai.types.GenerationConfig(temperature=temp)
    )
    return response.text

def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

if __name__ == "__main__":
    response = get_completion("Hello, tell me anything about Advanced Python Programming for AI")
    print(response)
