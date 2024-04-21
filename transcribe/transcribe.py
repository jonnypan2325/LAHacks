import io
from google.oauth2 import service_account
from google.cloud import speech 
import json

client_file = '.\\creds.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

# load the audio file
audio_file = '.\\test1.mp3'
with io.open(audio_file, 'rb') as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz=44100,
    language_code = 'en-US'
)

operation = client.long_running_recognize(config=config, audio=audio)
response = operation.result(timeout=90)


for result in response.results:
    print('running')
    print(result.alternatives[0].transcript)
    with open("results.json", "w") as json_file:
        json.dump(result.alternatives[0].transcript, json_file, indent=4)
