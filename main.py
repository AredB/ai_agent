import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if len(sys.argv) < 2:
    print("Error: No prompt provided.")
    sys.exit(1)

verbose = False
args = sys.argv[1:]
if "--verbose" in args:
    verbose = True
    args.remove("--verbose")

prompt = " ".join(sys.argv[1:])

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

prompt_tokens = getattr(response.usage_metadata, "prompt_token_count", "N/A")
response_tokens = getattr(response.usage_metadata, "candidates_token_count", "N/A")

print("Generated Response:", response.text)

if verbose:
    print(f'User prompt: "{prompt}"')
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")