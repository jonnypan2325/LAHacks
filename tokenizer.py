import json
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from nltk.tokenize import sent_tokenize

class JSONHandler(FileSystemEventHandler):
    def __init__(self, input_file):
        print('initialized handler 1')
        super().__init__()
        self.input_file = input_file
        print('initialized handler 2')

    def on_modified(self, event):
        print("Event detected:", event)
        if event.src_path == self.input_file:
            print("Input JSON file modified. Processing...")
            main(self.input_file)

def split_text_into_sentence_pairs(text):
    sentences = sent_tokenize(text)
    sentence_pairs = [(sentences[i], sentences[i+1]) for i in range(0, len(sentences)-1, 2)]
    return sentence_pairs

def main(input_file):
    # Load input JSON file
    print("Loading input JSON file:", input_file)
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Create output directory if it doesn't exist
    output_dir = 'text_output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each text entry in the input JSON
    for i, entry in enumerate(data):
        text = entry['text']
        print("Processing text:", text)
        sentence_pairs = split_text_into_sentence_pairs(text)
        
        # Write sentence pairs to separate JSON files
        for j, pair in enumerate(sentence_pairs):
            sentence_pair_str = " ".join(pair)
            output_file = os.path.join(output_dir, f'{i}_{j}.json')
            print("Writing to output file:", output_file)
            with open(output_file, 'w') as out:
                json.dump({'sentence_pair': sentence_pair_str}, out, indent=4)

def start_observer(input_file):
    observer = Observer()
    handler = JSONHandler(input_file) 
    observer.schedule(handler, path=os.path.dirname(input_file), recursive = True)
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
    input_file = 'input.json'  # Change this to your input JSON file
    start_observer(input_file)
