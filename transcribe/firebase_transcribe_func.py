import firebase_admin
from firebase_admin import credentials, storage
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech as cloud_speech_types

# Initialize Firebase
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'your-storage-bucket-url.appspot.com'
})

def download_audio(source_blob_name):
    """Downloads a blob from the bucket."""
    bucket = storage.bucket()
    blob = bucket.blob(source_blob_name)
    return blob.download_as_bytes()

def transcribe_streaming_v2(
    project_id: str,
    audio_data: bytes,
) -> cloud_speech_types.StreamingRecognizeResponse:
    """Transcribes audio from audio file stream.

    Args:
        project_id: The GCP project ID.
        audio_data: The bytes content of the audio file.

    Returns:
        The response from the transcribe method.
    """
    client = SpeechClient()

    # In practice, stream should be a generator yielding chunks of audio data
    chunk_length = len(audio_data) // 5
    stream = [
        audio_data[start : start + chunk_length]
        for start in range(0, len(audio_data), chunk_length)
    ]
    audio_requests = (
        cloud_speech_types.StreamingRecognizeRequest(audio=audio) for audio in stream
    )

    recognition_config = cloud_speech_types.RecognitionConfig(
        auto_decoding_config=cloud_speech_types.AutoDetectDecodingConfig(),
        language_codes=["en-US"],
        model="long",
    )
    streaming_config = cloud_speech_types.StreamingRecognitionConfig(
        config=recognition_config
    )
    config_request = cloud_speech_types.StreamingRecognizeRequest(
        recognizer=f"projects/{project_id}/locations/global/recognizers/_",
        streaming_config=streaming_config,
    )

    def requests(config: cloud_speech_types.RecognitionConfig, audio: list) -> list:
        yield config
        yield from audio

    # Transcribes the audio into text
    responses_iterator = client.streaming_recognize(
        requests=requests(config_request, audio_requests)
    )
    responses = []
    for response in responses_iterator:
        responses.append(response)
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")

    return responses

# Example usage
audio_bytes = download_audio('audio.wav')
transcribe_streaming_v2('your-project-id', audio_bytes)
