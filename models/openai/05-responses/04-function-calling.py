import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

tools = [
    {
        "type": "function",
        "name": "send_email",
        "description": "Send an email to a given recipient with a subject and message.",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "The recipient email address."},
                "subject": {"type": "string", "description": "Email subject line."},
                "body": {"type": "string", "description": "Body of the email message."},
            },
            "required": ["to", "subject", "body"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gemini-3.8-flash",
    input="Can you send an email to ilan@example.com and katia@example.com saying hi?",
    tools=tools,
)

print(response.output)
print(response.output[0].model_dump_json(indent=2))
print(response.output[1].model_dump_json(indent=2))
