from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import subprocess
import requests

load_dotenv()

# Initialize Gemini client
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# --- Tool Implementations ---
def get_weather(location: str) -> str:
    """Fetches current weather for a given location via wttr.in."""
    print("🔨 Tool Called: get_weather", location)
    url = f"https://wttr.in/{location}?format=%C+%t"
    resp = requests.get(url)
    if resp.status_code == 200:
        return f"The weather in {location} is {resp.text.strip()}."
    return "Something went wrong fetching weather."

def run_command(command: str) -> str:
    """Runs a shell command and returns its stdout."""
    print("🔨 Tool Called: run_command", command)
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return f"Command failed with exit {e.returncode}: {e.output.strip()}"

# --- Tool Declarations for Gemini ---
weather_fn = {
    "name": "get_weather",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

run_cmd_fn = {
  "name": "run_command",
  "description": "Executes any shell command on the host system—creating directories, files, or performing other terminal actions—and returns the command’s output or error message.",
  "parameters": {
    "type": "object",
    "properties": {
      "command": {
        "type": "string",
        "description": "The exact shell command to run, e.g., 'mkdir -p project/src' or 'echo \"Hello\" > file.txt'."
      }
    },
    "required": ["command"]
  }
}


tool_decl = types.Tool(function_declarations=[weather_fn, run_cmd_fn])  # type: ignore
config = types.GenerateContentConfig(tools=[tool_decl])

# --- Conversation Loop ---
while True:
    user_query = input(">>> ").strip()
    if not user_query:
        continue

    # 1) Ask Gemini how to respond
    first_response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_query,
        config=config,
    )
    candidate = first_response.candidates[0].content.parts[0]
    fn_call = candidate.function_call

    if fn_call:
        # 2) Gemini wants to call a tool
        print(f"📞 Function call requested: {fn_call.name}")
        print(f"   with args: {fn_call.args}")

        # 3) Execute the requested tool
        args = fn_call.args
        if fn_call.name == "get_weather":
            tool_result = get_weather(**args)
        elif fn_call.name == "run_command":
            tool_result = run_command(**args)
        else:
            tool_result = f"Error: unknown function {fn_call.name}"

        print(f"🛠️ Tool result: {tool_result}")
        continue


        
    else:
        # 5) No function call: just print Gemini's direct answer
        answer = candidate.text
        print(answer)