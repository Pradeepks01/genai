
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.types import HarmCategory
import os
import asyncio
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") # type: ignore


client = genai.Client(api_key=api_key)

# response = client.models.generate_content(
#     model='gemini-2.0-flash',
#     contents='king and lion',
#     config=types.GenerateContentConfig(
    #   safety_settings= [
    #       types.SafetySetting(
    #           category='HARM_CATEGORY_HATE_SPEECH', # # type: ignore
    #           threshold='BLOCK_ONLY_HIGH' #type: ignore
    #       ),
    #   ],
    #   system_instruction='you are a story teller for kids under 5 years old',
    #   max_output_tokens= 40,
    #   top_k= 2,
    #   top_p= 0.5,
    #   temperature= 0.5,
    #   response_mime_type= 'application/json',
    #   stop_sequences= ['\n'],
    #   seed=42,
#   ),
# )



# print(response.model_dump_json(
#     exclude_none=True, indent=4))



## using async

# async def main():
#     response = await client.aio.models.generate_content(
#         model='gemini-2.0-flash',
#         contents="what is one and one sum"
#     )
#     print(response.text)

# asyncio.run(main())


# chat = client.chats.create(model='gemini-2.0-flash')

# response = chat.send_message(message="tell me a story in 10 words")
# print(response.text)
# response = chat.send_message(
#     message='What happened after that?')

# print(response.text)