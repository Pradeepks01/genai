from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json
from openai import OpenAI
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Iterative 

client = genai.Client(api_key=api_key)

system_prompt = """

you are an AI Assistant who is specalized in breaking down the complex probles and resolving them

for the given input , analyse the input and break down the problem step by step
atleat think 5-6 steps on how to solve the problem before solving it down

this steps are you get user input , you analyse, you think , you again think for severaltimes and give me the proper output with explaination and then finally you validate the output as well before giving final result

Follow the steps in sequence that is "analyse", "think", "output", "validate", and finally "result"

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format:
{{step:"string", content:"string"}}

Example:
Input: what is 2 +2,
Output:{{step:"analyse", content:"Alright! the user is intrested in maths query and he is asking basic arthematic operation"}} 
Output:{{step:"think", content:"To perform the addition i must go from left to right and add all operands"}}
Output:{{step:"output",content:"4"}}
Output:{{step:"validate,content:"seems like 4 is correct ans for 2+2"}}
Output:{{step:"result",content:"2+2 = 4 and that is calculated by adding all numbers"}}

"""

# response = client.models.generate_content(
#     model='gemini-2.0-flash',
#     contents='write the code to make a game of snake',
#     config={
#         'max_output_tokens': 200,
#         'temperature': 0.9,
#         'system_instruction':system_prompt
#     }
# )

chat = client.chats.create(

    model="gemini-2.0-flash",
    config={
        "system_instruction":system_prompt,
        "temperature":0.9,
        "response_mime_type":'application/json',
        
    }
)
response = chat.send_message(message='what is 10 + 12')

response= chat.send_message(message=json.dumps({
  "step": "analyse",
  "content": "The user is asking for the sum of two numbers, 10 and 12. This is a basic addition problem."
}))

response= chat.send_message(message=json.dumps({

  "step": "think",
  "content": "To solve this, I need to add the two numbers together. I can do this mentally or using a calculator. The operation is straightforward."
  
}))

response= chat.send_message(message=json.dumps({
    
  "step": "output",
  "content": "22"
}))

response= chat.send_message(message=json.dumps({
    
 "step": "validate",
"content": "Let's verify: 10 + 12 indeed equals 22. The answer is correct and within the expected range for this type of problem."
}))

print(response.text)


