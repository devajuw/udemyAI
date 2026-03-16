# few shot prompting example
import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in your .env file")

client = genai.Client(api_key=api_key)
SYSTEM_PROMPT = """
You're an expert AI assistant in resolving user queries using chain of thought, you work on START, PLAN, and output steps.
You need to first PLAN what needs to be done. The plan can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.
You can also call a tool if required from the list of tools available tools.
For every tool call wait for the observe step which is the output for the called tool
Rules:
 - Strictly follow the JSON output format.
 - Only run one step at a time.
 - The Sequence of steps is START (where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is gonna be displayed to the user).

Output JSON Format:
{"step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content":"string", "tool": "string", "input": "string"}

Available Tools:
{"name":"get_weather", "description":"Get the weather of a city", "parameters":{"city":"string"}}

EXAMPLE 1:
START :Hey, can you solve 9+8+0-8*9?
PLAN:{"step": "PLAN", "content": "Seems like user is interested in math problem"}
PLAN:{"step": "PLAN", "content": "Looking at the problem, we should solve using BODMAS"}
PLAN:{"step": "PLAN", "content": "The BODMAS is correct thing to be done here"}
PLAN:{"step": "PLAN", "content": "First we must multiply 8*9"}
PLAN:{"step": "PLAN", "content": "Then add all the numbers with + signs"}
PLAN:{"step": "PLAN", "content": "At last we must perform the subtraction"}
PLAN:{"step": "PLAN", "content": "Great, we have solved the sum and got 89 as answer"}
OUTPUT:{"step": "OUTPUT", "content": "89"}

EXAMPLE 2:
START :What is the weather in Delhi?
PLAN:{"step": "PLAN", "content": "Seems like user is interested in weather of Delhi"}
PLAN:{"step": "PLAN", "content": "Lets see , if we have list of avaialble tool from the list of available tools"}
PLAN:{"step": "PLAN", "content": "Great, we have get_weather tool available for this query"}
PLAN:{"step": "PLAN", "content": "I need to call the tool get_weather with the city name Delhi as input for city"}
PLAN:{"step": "PLAN", "tool": "get_weather", "parameters":{"city":"Delhi"}}
PLAN:{"step": "PLAN", "observe": "tool : get_weather, "output":"The Temperature of Delhi is cloudy with 20 degrees Celsius"}
PLAN:{"step": "PLAN", "content": "Great, I have got the weather info about delhi"}
OUTPUT:{"step": "OUTPUT", "content": "The Current weather in delhi is 20 C with some cloudy sky."}
"""

message_history = []
user_query = input("👉 ")
message_history.append(types.Content(role="user", parts=[types.Part.from_text(text=user_query)]))

while True:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=message_history,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
        ),
    )

    raw_result = response.text
    message_history.append(types.Content(role="model", parts=[types.Part.from_text(text=raw_result)]))
    parsed_result = json.loads(raw_result)
    
    print(f"{parsed_result.get('step')}: {parsed_result.get('content')}")
    continue
    if parsed_result.get("step") == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        print(f"🔨: {tool_to_call} ({tool_input}")
        tool_response = available_tools[tool_to_call](tool_input)
        print(f"🔨: {tool_to_call} ({tool_input}) = {tool_response}")
        message_history.append(types.Content(role="user", parts=[types.Part.from_text(text=json.dumps(
            {
                "step": "observe", "tool" : tool_to_call, "input": tool_input, "output": tool_response
            }
        ))]))
        continue

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Content(role="user", parts=[types.Part.from_text(text="Hey, can you solve 9+8+0-8*9")]),
        # Manually keep adding messages to the history
        types.Content(role="model", parts=[types.Part.from_text(text=json.dumps({"step": "PLAN", "content": "The user wants me to evaluate the arithmetic expression 9 + 8 + 0 - 8 * 9. I need to apply the order of operations (PEMDAS/BODMAS) correctly."}))]),
        types.Content(role="model", parts=[types.Part.from_text(text=json.dumps({"step": "PLAN", "content": "First, perform the multiplication: 8 * 9 = 72"}))]),
        types.Content(role="model", parts=[types.Part.from_text(text=json.dumps({"step": "PLAN", "content": "Next, perform the addition from left to right: 9 + 8 + 0 = 17"}))]),
        types.Content(role="model", parts=[types.Part.from_text(text=json.dumps({"step": "PLAN", "content": "Finally, perform the subtraction: 17 - 72 = -55"}))]),
        types.Content(role="model", parts=[types.Part.from_text(text=json.dumps({"step": "OUTPUT", "content": "-55"}))]),
    ],
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        response_mime_type="application/json",
    ),
)

print(response.text)
