import json
from typing import List

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
from pydantic import BaseModel

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# --------------------------------------------------------------
# Using a JSON Schema
# --------------------------------------------------------------

response = client.responses.create(
    model="gemini-3.8-flash",
    input=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    text={
        "format": {
            "type": "json_schema",
            "name": "calendar_event",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "date": {"type": "string"},
                    "participants": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["name", "date", "participants"],
                "additionalProperties": False,
            },
            "strict": True,
        }
    },
)

event = json.loads(response.output_text)

# --------------------------------------------------------------
# Using a Pydantic model (and simple response format)
# --------------------------------------------------------------

"""
https://news.ycombinator.com/item?id=43336251
"""


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: List[str]


response = client.responses.parse(
    model="gemini-3.8-flash",
    input="Alice and Bob are going to a science fair on Friday",
    instructions="Extract the event information",
    text_format=CalendarEvent,
)

response_model = response.output[0].content[0].parsed

print(type(response_model))
print(response_model.model_dump_json(indent=2))
