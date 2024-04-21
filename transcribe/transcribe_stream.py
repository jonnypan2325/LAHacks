import pyaudio
import time
import io
from google.oauth2 import service_account
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech as cloud_speech_types
from google.cloud import speech
import google.api_core.exceptions

# Set up credentials using a service account key
service_account_file = ".\\creds.json"
credentials = service_account.Credentials.from_service_account_file(service_account_file)

# Initialize Google Cloud Speech-to-Text client with credentials
client = SpeechClient(credentials=credentials)

# Function to stream audio from a microphone
def stream_audio_from_mic():
    print("taking in mic")
    try:
        sample_rate = 16000  # Sample rate in Hz
        chunk_size = 1024  # Chunk size in bytes
        audio_format = pyaudio.paInt16  # 16-bit PCM
        channels = 1  # Mono audio

        # Initialize PyAudio for microphone input
        pyaudio_instance = pyaudio.PyAudio()

        # Open the microphone stream
        stream = pyaudio_instance.open(
            format=audio_format,
            channels=channels,
            rate=sample_rate,
            input=True,
            frames_per_buffer=chunk_size,
        )
    except google.api_core.exceptions.InternalServerError as e:
         print("Internal server error encountered:", str(e))
    except google.api_core.exceptions.GoogleAPIError as e:
         print("Google API error encountered:", str(e))

    # Continuously yield audio chunks from the microphone
    try:
        while True:
            audio_chunk = stream.read(chunk_size, exception_on_overflow=False)
            if not audio_chunk:
                input()  # Skip if the chunk is empty
            yield audio_chunk
            print('mic')
    except google.api_core.exceptions.InternalServerError as e:
         print("Internal server error encountered:", str(e))
    except google.api_core.exceptions.GoogleAPIError as e:
         print("Google API error encountered:", str(e))
    finally:
        # Clean up the stream and PyAudio instance
        print('mic closed')
        stream.stop_stream()
        stream.close()
        pyaudio_instance.terminate()

# Configuration for speech recognition
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",  # Language for transcription
)

print('config initialized')

try:
    audio_chunks = stream_audio_from_mic()

    # Streaming configuration
    streaming_config = speech.StreamingRecognitionConfig(config=config, interim_results=True)
    streaming_requests = (speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in audio_chunks)

    # Configuration request for streaming
    responses = client.streaming_recognize(streaming_requests)
except google.api_core.exceptions.InternalServerError as e:
    print("Internal server error encountered:", str(e))
except google.api_core.exceptions.GoogleAPIError as e:
    print("Google API error encountered:", str(e))

# Print transcriptions in real-time as they are received
try:
    for response in responses:
        if response.results:
            # Print each result
            for result in response.results:
                print("Transcript:", result.alternatives[0].transcript)
except google.api_core.exceptions.InternalServerError as e:
    print("Internal server error encountered:", str(e))
except google.api_core.exceptions.GoogleAPIError as e:
    print("Google API error encountered:", str(e))
except KeyboardInterrupt:
    print("Stopped streaming transcription.")