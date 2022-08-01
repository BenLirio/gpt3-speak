import uuid
from google.cloud import texttospeech
import os

DEFAULT_VOICE = ('en-US-Neural2-A', 0.000016)
DEFAULT_PITCH = 0
DEFAULT_SPEAKING_RATE = 1

class TextToSpeechClient():
    def __init__(self,
            cost,
            pitch=DEFAULT_PITCH,
            speaking_rate=DEFAULT_SPEAKING_RATE,
            voice=DEFAULT_VOICE
            ):
        self.cost = cost
        voice_name,voice_cost = voice
        self.voice_name = voice_name
        self.voice_cost = voice_cost
        self.speaking_rate = speaking_rate
        self.pitch = pitch
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", name=self.voice_name
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=self.speaking_rate,
            pitch=self.pitch
        )

    def TextToAudioFile(self,text,output_name):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )
        with open(output_name, "wb") as out:
            out.write(response.audio_content)

    def Say(self, text):
        output_name = f"audio_tmp_{uuid.uuid4()}.mp3"

        self.cost.Add(len(list(text)) * self.voice_cost)
        self.TextToAudioFile(text,output_name)

        os.system(f'afplay {output_name}')
        os.remove(output_name)
