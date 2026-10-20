"""
Validation: Ensures LLM outputs match predefined data schemas.
This component provides schema validation and structured data parsing to guarantee consistent data formats for downstream code.

More info: https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
from pydantic import BaseModel


class TaskResult(BaseModel):
    """
    More info: https://docs.pydantic.dev
    """

    task: str
    completed: bool
    priority: int


def structured_intelligence(prompt: str) -> TaskResult:
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    response = client.responses.parse(
        model="gemini-3.8-flash",
        input=[
            {
                "role": "system",
                "content": "Extract task information from the user input.",
            },
            {"role": "user", "content": prompt},
        ],
        text_format=TaskResult,
    )
    return response.output_parsed


if __name__ == "__main__":
    result = structured_intelligence(
        "I need to complete the project presentation by Friday, it's high priority"
    )
    print("Structured Output:")
    print(result.model_dump_json(indent=2))
    print(f"Extracted task: {result.task}")
