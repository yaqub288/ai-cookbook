import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.responses.create(
    model="gemini-3.8-flash",
    reasoning={"effort": "low"},
    tools=[
        {
            "type": "web_search",
            "filters": {
                "allowed_domains": [
                    "pubmed.ncbi.nlm.nih.gov",
                    "clinicaltrials.gov",
                    "www.who.int",
                    "www.cdc.gov",
                    "www.fda.gov",
                ]
            },
        }
    ],
    tool_choice="auto",
    include=["web_search_call.action.sources"],
    input="Please perform a web search on how semaglutide is used in the treatment of diabetes.",
)

print(response.output_text)
