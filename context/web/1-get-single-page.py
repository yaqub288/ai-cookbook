import os

from dotenv import load_dotenv
from docling.document_converter import DocumentConverter
from openai import OpenAI
from pydantic import BaseModel, HttpUrl

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
converter = DocumentConverter()

MODEL = "gemini-3.8-flash"

# --------------------------------------------------------------
# Define the output model
# --------------------------------------------------------------


class Source(BaseModel):
    url: HttpUrl


class Summary(BaseModel):
    summary: str


# --------------------------------------------------------------
# Extract content from a web page
# --------------------------------------------------------------

test_url = "https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence"

source = Source(url=test_url)
page_content = converter.convert(str(source.url))
markdown_content = page_content.document.export_to_markdown()
print(markdown_content)

# --------------------------------------------------------------
# Generate summary using OpenAI responses API
# --------------------------------------------------------------

response = client.responses.parse(
    model=MODEL,
    input=f"Please give a short summary of this website content:\n\n{markdown_content}",
    instructions="You are an assistant that retrieves the content of a web page and answers questions about it.",
    text_format=Summary,
)

result = response.output[-1].content[-1].parsed
print(result.summary)
