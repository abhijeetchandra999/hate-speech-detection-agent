import os
from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if gemini_api_key:
    llm = LLM(
        model="gemini/gemini-3.5-flash",
        api_key=gemini_api_key,
    )
elif openai_api_key:
    llm = LLM(
        model="gpt-4o",
        api_key=openai_api_key,
    )
elif openrouter_api_key:
    llm = LLM(
        model="openai/gpt-4o",
        api_key=openrouter_api_key,
        base_url="https://openrouter.ai/api/v1",
    )
else:
    raise ValueError("Set GEMINI_API_KEY, OPENAI_API_KEY or OPENROUTER_API_KEY in .env")

# Define your agent with OpenAI LLM
hate_speech_detector = Agent(
    role="Hate Speech Detector",
    goal="Analyse the text and identify if any hate speech / offensive language is present",
    llm=llm,
    backstory=(
        "You are a Hate Speech Detector for Twitter who understands details very well and is highly experienced. "
        "You can identify hate speech / offensive language in given tweet."
    ),
)
