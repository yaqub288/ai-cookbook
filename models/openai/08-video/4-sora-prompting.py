from utils.director import SoraDirector
from utils.downloader import download_sora_video
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
director = SoraDirector()
# --------------------------------------------------------------
# Generate a Sora prompt
# --------------------------------------------------------------

prompt = director.generate_sora_prompt(
    "A YouTuber excitedly showing OpenAI's new Sora 2 API release to generate hyper-realistic videos with just a few lines of code."
)
print(prompt)


# --------------------------------------------------------------
# Generate a video
# --------------------------------------------------------------

video = openai.videos.create(
    model="sora-2",
    prompt=prompt,
    size="720x1280",
    seconds="4",
)

print("Video generation started:", video)

# --------------------------------------------------------------
# Download the video
# --------------------------------------------------------------

video = download_sora_video(video=video, output_folder="./output")
