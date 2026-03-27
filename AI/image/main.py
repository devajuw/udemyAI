import base64
import requests
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)
MODEL = "gemma3:1b"  

# 1. Ollama's OpenAI endpoints DO NOT support URLs. 
# We must download the image first and convert it to base64.
image_url = "https://images.pexels.com/photos/36538802/pexels-photo-36538802.jpeg"
response = requests.get(image_url)
base64_image = base64.b64encode(response.content).decode('utf-8')

# 2. Format the base64 string as required by the Vision API
base64_url = f"data:image/jpeg;base64,{base64_image}"

# 3. Request completion
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Generate a caption for this image in about 50 words"},
                {"type": "image_url", "image_url": {"url": base64_url}}
            ]
        }
    ]
)
print("Response: ", response.choices[0].message.content)