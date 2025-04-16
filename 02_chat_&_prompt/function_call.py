from chat import client
from google import genai
from google.genai import types
import requests

def get_current_weather(location:str)->str: # type: ignore
    """get the current wheather in the give location
    
    Args:
        location:required, the city and state, town, e., san franciso, CA unit:celsius or fahrenhit
    """
    print(f'called with:{location=}')
    url = f"https://wttr.in/{location}?fromat=%C+%t"
    response = requests.get(url)
    print(response.content)
    if requests.status_codes == 200:
        return f"the weather in {location} is {response.text}"
    return "something went wrong"

          
response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather] 
  ),
)

print(response.text)

# function_call = response.candidates[0].content.parts[0].function_call # type: ignore