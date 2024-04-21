import json
from tts_translate import transalte_tts

def get_extension(file_path='..\\chrome_extension\\user_input.json') -> dict:
    # Open the JSON file
    with open(file_path, 'r') as f:
        # Load the JSON data into a dictionary
        data = json.load(f)

    return data

def get_text_stream(file_path='..\\transcribe\\results.txt') -> str:
    # Open the JSON file
    with open(file_path, 'r') as f:
        data = f.readline()

    return data[1:-1]

if __name__ == '__main__':
    data_extension = get_extension()
    inp_lang = data_extension["starting_language"]
    out_lang = data_extension["output_language"]
    gender = data_extension["gender"]
    while (True):
        text = get_text_stream()
        print(text)
        transalte_tts(inp_lang, out_lang, gender, text)