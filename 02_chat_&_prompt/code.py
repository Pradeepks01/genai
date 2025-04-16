from chat import client
from google import genai
from google.genai import types
from pydantic import BaseModel


# code execution

# response = client.models.generate_content(
#     model='gemini-2.0-flash',
#     contents='What is the sum of the first 50 prime numbers? Generate and run '
#             'code for the calculation, and make sure you get all 50.',
#     config=types.GenerateContentConfig(
#         tools=[types.Tool(code_execution=types.ToolCodeExecution)],
#     ),
# )



class CountryInfo(BaseModel):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int


# response = client.models.generate_content(
#     model='gemini-2.0-flash',
#     contents='What is the Google stock price and current timme in india?',
#     config=types.GenerateContentConfig(
#         tools=[
#             types.Tool(
#                 google_search=types.GoogleSearch()
#             )
#         ],
#         'response_mime_type': 'application/json', # type: ignore
#         'response_schema': CountryInfo, 
#     ),
    
    
# )

response = client.models.embed_content(
  model='text-embedding-004',
  contents='Hello world',
)

print(response)