from translate import translate
from text_to_speech import play_sound

def transalte_tts(inp_lang, out_lang, voice, text):
    # generate audio from text

    text_prompt = translate(inp_lang, out_lang, text)
    play_sound(text_prompt, out_lang, voice)