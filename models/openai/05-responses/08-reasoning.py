import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

"""
https://platform.openai.com/docs/guides/reasoning?api-mode=responses
"""

prompt = """
Write a bash script that takes a matrix represented as a string with 
format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
"""

response = client.responses.create(
    model="o3-mini",
    reasoning={"effort": "medium"},
    input=[{"role": "user", "content": prompt}],
)

print(response.output_text)
