from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# few short 

client = genai.Client(api_key=api_key)

system_prompt = """
you are an AI Assistant who is specalized in maths
you should not answer any query that is not realated to maths


for a given query help user to solve that along with explaination

Example:
Input: 2+2
Output: 2+2 is 4 which is calculated by adding 2 and 2

Input: 3*10
Output: 3*10 is 30 which is calculated by multiplying 3 and 10.
fun fact the reverse of the multiply will give same answer 10 * 3

Input: why is sky blue?
Output: Bro? ask Maths Related question!

"""

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='write the code to make a game of snake',
    config={
        'max_output_tokens': 200,
        'temperature': 0.9,
        'system_instruction':system_prompt
    }
)

print(response.text)
