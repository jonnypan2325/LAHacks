import boto3
from playsound import playsound
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

ACCESS_KEY = os.getenv('BOTO_ACCESS_KEY')
SECRET_KEY = os.getenv('BOTO_SECRET_KEY')

language_dict = {
    'Arabic': 'arb',
    'Chinese': 'cmn-CN',
    'Danish': 'da-DK',
    'German': 'de-DE',
    'English': 'en-US',
    'Spanish': 'es-ES',
    'French': 'fr-FR',
    'Italian': 'it-IT',
    'Japanese': 'ja-JP',
    'Hindi': 'hi-IN',
    'Korean': 'ko-KR',
    'Norwegian Bokmål': 'nb-NO',
    'Dutch': 'nl-NL',
    'Polish': 'pl-PL',
    'Portuguese (Portugal)': 'pt-PT',
    'Swedish': 'sv-SE',
    'Turkish': 'tr-TR',
    'Cantonese': 'yue-CN',
    'Finnish': 'fi-FI',
}

voices = {'Male': 'Joey', 'Female': 'Joanna'}
poly = boto3.client('polly', region_name='us-east-1', aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY)

def play_sound(text, language, voice):
    response = poly.synthesize_speech(Text=text, OutputFormat="mp3",
                                       VoiceId=voices[voice], LanguageCode=language_dict[language], Engine='neural')
    if "AudioStream" in response:
        with response["AudioStream"] as stream:
            output_file = "speech.mp3"
            try:
                # Open a file for writing the output as a binary stream
                with open(output_file, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")

    playsound(output_file)