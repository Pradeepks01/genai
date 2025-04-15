from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json
load_dotenv()


#  chain of thought

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

system_prompt = """
you are an AI Assistant who is specialized in breaking down complex problems.

For the given input, analyse it and break it down step by step. Think through at least 5-6 steps.

Steps to follow in exact order: "analyse", "think", "output", "validate", and finally "result".

Rules:
1. Follow strict JSON output like: {"step":"string", "content":"string"}
2. Always perform only one step at a time and wait for the next input.
3. Think deeply before responding.

Example:
Input: what is 2 + 2
Output: {"step":"analyse", "content":"User asked a basic math problem"}
Output: {"step":"think", "content":"To solve this, I should perform addition"}
Output: {"step":"output", "content":"4"}
Output: {"step":"validate", "content":"4 is correct for 2+2"}
Output: {"step":"result", "content":"2+2=4, calculated by simple addition"}
"""

chat = client.chats.create(
    model="gemini-2.0-flash",
    config={
        "system_instruction": system_prompt,
        "temperature": 0.9,
        "response_mime_type": 'application/json',
    }
)

query = input(">>> ")
step_input = query

while True:
    response = chat.send_message(step_input)
    if response.text is None:
        raise ValueError("Response text is None, cannot parse JSON.")
    output = json.loads(response.text)
    step = output.get("step")
    content = output.get("content")

    emoji = "🧠"
    print(emoji, f"{content}")

    if step == "result":
        emoji = "😎"
        print(emoji, f"{content}")
        break
   