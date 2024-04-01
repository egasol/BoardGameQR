from pathlib import Path
import hashlib
import os
from elevenlabs import play, save, stream
from elevenlabs.client import ElevenLabs


ELEVEN_API_KEY = os.environ.get("ELEVEN_API_KEY")
ELEVEN_VOICE = "Dave"
ELEVEN_VERSION = "eleven_multilingual_v2"
ELEVEL_CACHE = "Audio"


class TextToSpeech:
    def __init__(self):
        self.client = client = ElevenLabs(api_key=ELEVEN_API_KEY)

    def generate_audio(self, dialogue, play_audio=True):
        audio_hash = hashlib.sha256(dialogue.encode("utf8")).hexdigest()
        audio_path = ELEVEL_CACHE / Path(audio_hash + ".mp3")

        if audio_path.exists():
            if play_audio:
                with open(audio_path, "rb") as f:
                    audio = f.read()
                play(audio)
        else:
            audio = self.client.generate(
                text=dialogue,
                voice=ELEVEN_VOICE,
                model=ELEVEN_VERSION
            )

            audio_bytes = b"".join(audio)
            if play_audio:
                play(audio_bytes)
            save(audio_bytes, audio_path)

        print(dialogue)
