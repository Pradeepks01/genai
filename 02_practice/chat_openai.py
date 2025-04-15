from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    n=1,
    messages=[
        {"role": "user", "content": "what is 2+2"},
    ]

)

print(response.choices[0].message)