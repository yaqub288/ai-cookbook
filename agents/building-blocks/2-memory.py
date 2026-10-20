"""
Memory: Stores and retrieves relevant information across interactions.
This component maintains conversation history and context to enable coherent multi-turn interactions.

More info: https://platform.openai.com/docs/guides/conversation-state?api-mode=responses
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def ask_joke_without_memory():
    response = client.responses.create(
        model="gemini-3.8-flash",
        input=[
            {"role": "user", "content": "Tell me a joke about programming"},
        ],
    )
    return response.output_text


def ask_followup_without_memory():
    response = client.responses.create(
        model="gemini-3.8-flash",
        input=[
            {"role": "user", "content": "What was my previous question?"},
        ],
    )
    return response.output_text


def ask_followup_with_memory(joke_response: str):
    response = client.responses.create(
        model="gemini-3.8-flash",
        input=[
            {"role": "user", "content": "Tell me a joke about programming"},
            {"role": "assistant", "content": joke_response},
            {"role": "user", "content": "What was my previous question?"},
        ],
    )
    return response.output_text


if __name__ == "__main__":
    # First: Ask for a joke
    joke_response = ask_joke_without_memory()
    print(joke_response, "\n")

    # Second: Ask follow-up without memory (AI will be confused)
    confused_response = ask_followup_without_memory()
    print(confused_response, "\n")

    # Third: Ask follow-up with memory (AI will remember)
    memory_response = ask_followup_with_memory(joke_response)
    print(memory_response)
