import io
import json
from google.cloud import speech, pubsub_v1, storage
from google.oauth2 import service_account

# Load credentials and initialize clients
client_file = '.\\creds.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
speech_client = speech.SpeechClient(credentials=credentials)
pubsub_client = pubsub_v1.SubscriberClient(credentials=credentials)
storage_client = storage.Client(credentials=credentials)

# Configuration for Pub/Sub
project_id = 'lingolive-db334'
subscription_id = 'your-subscription-id'
bucket_name = 'lingolive-db334.appspot.com'
subscription_path = pubsub_client.subscription_path(project_id, subscription_id)
bucket = storage_client.bucket(bucket_name)

def process_audio_file(file_path):
    # Retrieve the audio file from Firebase Storage
    blob = bucket.blob(file_path)
    audio_content = blob.download_as_bytes()
    
    # Create RecognitionAudio object
    audio = speech.RecognitionAudio(content=audio_content)

    # Configure the recognizer
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=44100,
        language_code='en-US'
    )

    # Start the recognition process
    operation = speech_client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)

    # Print and save results
    for result in response.results:
        print('Running')
        print(result.alternatives[0].transcript)
        with open("results.json", "w") as json_file:
            json.dump(result.alternatives[0].transcript, json_file, indent=4)

def callback(message):
    data = json.loads(message.data.decode('utf-8'))
    file_path = data['filePath']
    print(f"Received a new file for processing: {file_path}")
    
    # Process the file using the function defined above
    process_audio_file(file_path)
    
    message.ack()

# Listen to the Pub/Sub subscription for new messages
streaming_pull_future = pubsub_client.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}...")

# Keep the main thread running to listen indefinitely (or handle exceptions appropriately)
try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()
except Exception as e:
    print(f"Listening for messages on {subscription_path} threw an exception: {e}.")
    streaming_pull_future.cancel()
