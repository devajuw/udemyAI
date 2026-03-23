# Weather Agent using Ollama (local, no quota limits!)
import json
import requests
from pydantic import BaseModel, Field
# Ollama uses an OpenAI-compatible API running locally
from openai import OpenAI
from typing import Optional
client = OpenAI(

# Part - Meaning
# localhost	- Your own machine (no internet needed)
# 11434	- The default port Ollama listens on
# /v1 - OpenAI-compatible API path 

    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

MODEL = "gemma3:1b"  

SYSTEM_PROMPT = """
You're an expert AI assistant in resolving user queries using chain of thought, you work on START, PLAN, and output steps.
You need to first PLAN what needs to be done. The plan can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.
You can also call a tool if required from the list of tools available tools.
For every tool call wait for the observe step which is the output for the called tool
Rules:
 - Strictly follow the JSON output format.
 - Only run ONE step at a time and return ONLY ONE single JSON object per response. Do NOT return multiple JSON objects.
 - Always respond with a single valid JSON object and nothing else.
 - The Sequence of steps is START (where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is gonna be displayed to the user).

Output JSON Format:
{"step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content":"string", "tool": "string", "input": "string"}

Available Tools:
{"name":"get_weather", "description":"Get the weather of a city", "parameters":{"city":"string"}}

EXAMPLE 1:
START: Hey, can you solve 9+8+0-8*9?
{"step": "PLAN", "content": "Seems like user is interested in math problem"}
{"step": "PLAN", "content": "Looking at the problem, we should solve using BODMAS"}
{"step": "PLAN", "content": "First we must multiply 8*9 = 72"}
{"step": "PLAN", "content": "Then add: 9 + 8 + 0 = 17. Then subtract: 17 - 72 = -55"}
{"step": "OUTPUT", "content": "-55"}

EXAMPLE 2:
START: What is the weather in Delhi?
{"step": "PLAN", "content": "Seems like user is interested in weather of Delhi"}
{"step": "PLAN", "content": "I have a get_weather tool available for this query"}
{"step": "TOOL", "tool": "get_weather", "input": "Delhi"}
{"step": "PLAN", "content": "I have received the weather info for Delhi from the tool"}
{"step": "OUTPUT", "content": "The current weather in Delhi is ..."}
"""

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return f"Could not get weather for {city}"

available_tools = {
    "get_weather": get_weather,
}

print("\n\n\n\n")

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN,OUTPUT,TOOL")
    content: Optional[str]= Field(None, description="The optional string content for the step")
    tool: Optional[str]= Field(None, description="The ID of the tool to call")
    input: Optional[str]= Field(None, description="The input params for the tool")

# Build message history using OpenAI-style dicts (Ollama is OpenAI-compatible)
message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉 ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.parse(
        model=MODEL,
        messages=message_history,
        response_format=MyOutputFormat,
    )

    message = response.choices[0].message
    
    # Append the raw text content to history, NOT the parsed object
    message_history.append({"role": "assistant", "content": message.content})

    # Safely get the parsed result as a dictionary
    if message.parsed:
        # Convert Pydantic object to dict so your .get() calls work
        parsed_result = message.parsed.model_dump()
    else:
        # Fallback for manual parsing if automatic parsing failed
        try:
            parsed_result = json.loads(message.content)
        except Exception:
            print(f"⚠️ Error: Could not parse model response as JSON: {message.content}")
            continue

    step = parsed_result.get("step")
    print(f"🤔 {step}: {parsed_result.get('content') or parsed_result.get('input', '')}")

    if step == "OUTPUT":
        print(f"\n✅ Final Answer: {parsed_result.get('content')}")
        break

    if step == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        print(f"🔨 Calling tool: {tool_to_call}({tool_input})")
        tool_response = available_tools[tool_to_call](tool_input)
        print(f"📦 Tool result: {tool_response}")
        message_history.append({
            "role": "user",
            "content": json.dumps({
                "step": "observe",
                "tool": tool_to_call,
                "input": tool_input,
                "output": tool_response
            })
        })
        continue
