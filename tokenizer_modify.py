import json
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from nltk.tokenize import sent_tokenize

class JSONHandler(FileSystemEventHandler):
    def __init__(self, input_file, output_file):
        super().__init__()
        self.input_file = input_file
        self.output_file = output_file

    def on_modified(self, event):
        if event.src_path == self.input_file:
            print("Input JSON file modified. Processing...")
            main(self.input_file, self.output_file)

def split_text_into_sentence_pairs(text):
    sentences = sent_tokenize(text)
    sentence_pairs = [(sentences[i], sentences[i+1]) for i in range(0, len(sentences)-1, 2)]
    return sentence_pairs

def main(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading input JSON file: {e}")
        return  # Stop further processing if an error occurs
    
    output_data = []
    for entry in data:
        text = entry.get('text', '')
        sentence_pairs = split_text_into_sentence_pairs(text)
        for pair in sentence_pairs:
            output_data.append({'sentences': f"{pair[0]} {pair[1]}"})

    with open(output_file, 'w') as out:
        json.dump(output_data, out, indent=4)


def start_observer(input_file, output_file):
    observer = Observer()
    handler = JSONHandler(input_file, output_file)
    observer.schedule(handler, path=os.path.dirname(input_file), recursive=True)
    observer.start()

    try:
        while not os.path.exists(input_file):
            print("Waiting for input JSON file...")
            time.sleep(1)
        
        print("Input JSON file found. Starting observer.")
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    input_file = '.\\input.json'  # Change this to your input JSON file
    output_file = '.\\output.json'  # Change this to your desired output JSON file
    start_observer(input_file, output_file)
