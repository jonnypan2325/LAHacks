from tts_translate import transalte_tts

if __name__ == '__main__':
    inp_lang = input('Enter starting language: ')
    out_lang = input('Enter output language: ')
    gender = input('Male or Female?: ')
    while (True):
        text = input('Enter text: ')
        transalte_tts(inp_lang, out_lang, gender, text)