from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv(dotenv_path='../.env')

client = OpenAI()

# open_ai_api_key = os.getenv("OPENAI_API_KEY")

# print(open_ai_api_key)

text = "Avengers is og movie"

response = client.embeddings.create(
    input=text,
    model='text-embedding-3-small'
)


print('vecor embedings => ', response.data[0].embedding)