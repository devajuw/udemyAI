from random import choice
from dns import message
from dotenv import load_dotenv
import speech_recognition as sr
import os
load_dotenv()
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def main():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2
        
        print("speak karo:")
        audio = r.listen(source)
        
        print("Processing Audio...(STT)")
        stt = r.recognize_google(audio)
        
        print("You said", stt)
        
        SYSTEM_PROMPT = f"""
        you are an expert voice agent, you are given the transcript of what user has said
        using voice.
        You need to output as if you are an voice agent and whatever you speak 
        will be converetd back to audio using AI and played back to USER.
        """
        # using GROQs as i am broke and cannot afford openAI api
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": stt}
            ]
        )
        
        print("AI response:", response.choices[0].message.content)

main()