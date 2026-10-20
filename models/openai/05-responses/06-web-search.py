import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


# --------------------------------------------------------------
# Basic web search
# --------------------------------------------------------------

response = client.responses.create(
    model="gemini-3.8-flash",
    tools=[
        {
            "type": "web_search_preview",
        }
    ],
    input="What are the best restaurants around de Dam?",
)

print(response.output_text)

# --------------------------------------------------------------
# Basic web search with location
# --------------------------------------------------------------

response = client.responses.create(
    model="gemini-3.8-flash",
    tools=[
        {
            "type": "web_search_preview",
            "user_location": {
                "type": "approximate",
                "country": "NL",
                "city": "Amsterdam",
            },
        }
    ],
    input="What are the best restaurants around de Dam?",
)

print(response.output_text)
response.output[1].content[0].annotations
response.output[1].content[0].annotations[0].url
