from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os
import pyaudio
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

audio = client.text_to_speech.convert(
    text="Hello",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

sound = AudioSegment.from_mp3(BytesIO(audio))
play(sound)