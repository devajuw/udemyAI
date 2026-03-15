from google import genai
from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in your .env file")

client = genai.Client(api_key=api_key)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    else:
        return "Someting went wrong"
available_tools =
{
    "get_weather" :get_weather
}    
def main():
    user_query = input("> ")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_query,
    )
    print(f"Bot: {response.text}")
print(get_weather("New York"))

if __name__ == "__main__":
    main()

