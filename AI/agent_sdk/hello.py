# This guy is broke and doesnot have any money to buy a model, so he is using the free model from groq.
import os
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
    openai_client=AsyncOpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    ),
)

agent = Agent(name="GroqAgent", instructions="You are a helpful assistant.", model=model)
print(Runner.run_sync(agent, "greet me romantically in under 10 words").final_output)