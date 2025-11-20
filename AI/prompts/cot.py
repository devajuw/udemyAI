# few shot prompting example
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.getenv("API_KEY"),
     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEM_PROMPT = """
You're an expert AI assistant in resolving user queries using chain of thought, you work on START, PLAN, and output steps.
You need to first PLAN what needs to be done. The plan can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
 - Strictly follow the JSON output format.
 - Only run one step at a time.
 - The Sequence of steps is START (where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is gonna be displayed to the user).

Output JSON Format:
{"step": "START" | "PLAN" | "OUTPUT", "content":"string"}

EXAMPLE:
START :Hey, can you solve 9+8+0-8*9?
PLAN:{"step": "PLAN", "content": "Seems like user is interested in math problem"}
PLAN:{"step": "PLAN", "content": "Looking at the problem, we should solve using BODMAS"}
PLAN:{"step": "PLAN", "content": "The BODMAS is correct thing to be done here"}
PLAN:{"step": "PLAN", "content": "First we must multiply 8*9"}
PLAN:{"step": "PLAN", "content": "Then add all the numbers with + signs"}
PLAN:{"step": "PLAN", "content": "At last we must perform the subtraction"}
PLAN:{"step": "PLAN", "content": "Great, we have solved the sum and got 89 as answer"}
OUTPUT:{"step": "OUTPUT", "content": "89"}
"""

message_history=[
    {"role": "system", "content": SYSTEM_PROMPT},
]
user_query = input("👉 ")
message_history.append({"role":"user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        response_format={"type": "json_object"},
        messages=message_history
            )

raw_result : (response.choices[0].message.content)
message_history.append({"role":"assistant", "content":raw_result})
parsed_result = json.loads(raw_result)

if parsed_result.get("step")== "START":
    print("🔥",parsed_result.get(content))
          


response = client.chat.completions.create(
    model="gemini-2.0-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you solve 9+8+0-8*9"},
        # Manualy keep adding messages to the history
        {"role" : "assistant" , "content" : json.dumps({"step": "PLAN", "content": "The user wants me to evaluate the arithmetic expression 9 + 8 + 0 - 8 * 9. I need to apply the order of operations (PEMDAS/BODMAS) correctly."}) },
        {"role" : "assistant" , "content" : json.dumps({"step": "PLAN", "content": "First, perform the multiplication: 8 * 9 = 72"})},
        {"role" : "assistant" , "content" : json.dumps({"step": "PLAN", "content": "Next, perform the addition from left to right: 9 + 8 + 0 = 17"})},
         {"role" : "assistant" , "content" : json.dumps({"step": "PLAN", "content": "Finally, perform the subtraction: 17 - 72 = -55"})},
         {"role" : "assistant" , "content" : json.dumps({"step": "OUTPUT", "content": "-55"})},


    ]
)

print(response.choices[0].message.content)
