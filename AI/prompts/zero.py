#zero shot prompting example
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.getenv("API_KEY"),
     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEM_PROMPT = "you are an expert master in maths and only ans maths query, if not asked about maths, say I am sorry, I can only answer questions about maths."
#zero shot prompting : giving the direct system prompt to the model without any prior examples
response = client.chat.completions.create(
    model="gemini-2.0-flash", messages=[
        { "role": "system", "content": SYSTEM_PROMPT } #system prompt  
    ,{"role": "user", "content": "define euclidean distance."}]) #user prompt
    
print(response.choices[0].message.content)