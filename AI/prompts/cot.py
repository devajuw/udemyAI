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

EXAMPLE: Hey, can you solve 9+8+0-8*9
{"step": "PLAN", "content": "Seems like user is interested in math problem"}
{"step": "PLAN", "content": "Looking at the problem, we should solve using BODMAS"}
{"step": "PLAN", "content": "The BODMAS is correct thing to be done here"}
{"step": "PLAN", "content": "First we must multiply 8*9"}
{"step": "PLAN", "content": "Then add all the numbers with + signs"}
{"step": "PLAN", "content": "At last we must perform the subtraction"}
{"step": "PLAN", "content": "Great, we have solved the sum and got 89 as answer"}
{"step": "OUTPUT", "content": "89"}
"""

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "What is (A+B+C)^2?"}
    ]
)

print(response.choices[0].message.content)
