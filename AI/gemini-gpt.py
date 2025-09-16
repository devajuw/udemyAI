import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
response = client.chat.completions.create(
    model="gemini-2.0-flash", messages=[
        { "role": "system", "content": "you are an expert master in maths and only ans maths query, if not asked about maths, say I am sorry, I can only answer questions about maths." } #system prompt  
    ,{"role": "user", "content": "define love."}]) #user prompt
    
print(response.choices[0].message.content)