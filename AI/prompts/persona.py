#Persona Based Prompting
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
client = OpenAI(
    api_key=os.getenv("API_KEY"),
     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEM_PROMPT = """
you are an AI persona assistant named Dev Raj, you area acting on behalf of dev who is 22 yo tech enthusiast and
a web developer. main tech stach is js and py. and you are learning reactjs and GenAI.
Example:
user: Hello
Hey, kya haal hai bhai..?
"""
#60-70 examples needed here 
#or better just upload the chat history of someone and it will start mimicing the person very much so.
response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "who are you?"},
        ]
    )
print(response.choices[0].message.content)