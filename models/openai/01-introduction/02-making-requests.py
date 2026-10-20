import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Use the Gemini API key through the OpenAI-compatible client.
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
