import os
from dotenv import load_dotenv
from openai import OpenAI

try:
    from utils.prompt_templates import PIXAR_PROMPT
except ImportError:
    from prompt_templates import PIXAR_PROMPT


class SoraDirector:
    def __init__(self):
        load_dotenv()
        self.openai = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )

    def generate_sora_prompt(
        self, idea: str, prompt_template: str = PIXAR_PROMPT
    ) -> str:
        print("Generating Sora prompt...")
        response = self.openai.responses.create(
            model="gemini-3.8-flash",
            input=idea,
            instructions=prompt_template,
        )
        return response.output_text


if __name__ == "__main__":
    director = SoraDirector()
    prompt = director.generate_sora_prompt(
        "An intro for a YouTube video about OpenAI's Sora 2 API."
    )
    print(prompt)
