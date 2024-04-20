import boto3
from translate import translate


poly = boto3.client('polly')

'''
def play_sound(text):
    response = poly.synthesize_speech(text=text, VoiceId='Joey', LanguageCode='es-ES', OutputFormat='mp3')
    body = response['AudioStream'].read()
  '''

while (True):
    # generate audio from text
    print("Start typing")
    inp_lang = "english"
    out_lang = "chinese"

    text_prompt = translate(inp_lang, out_lang, input())

    print(text_prompt)