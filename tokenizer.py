import json
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from nltk.tokenize import sent_tokenize

class JSONHandler(FileSystemEventHandler):
    def __init__(self, input_file):
        super().__init__()
        self.input_file = input_file

    def on_modified(self, event):
        if event.src_path == self.input_file:
            print("Input JSON file modified. Processing...")
            main(self.input_file)

def split_text_into_sentences(text):
    sentences = sent_tokenize(text)
    return sentences

def main(input_file):
    # Load input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Create output directory if it doesn't exist
    output_dir = 'output_sentences'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each text entry in the input JSON
    for i, entry in enumerate(data):
        text = entry['text']
        sentences = split_text_into_sentences(text)
        
        # Write sentences to separate JSON files
        for j, sentence in enumerate(sentences):
            output_data = {'id': f'{i}_{j}', 'sentence': sentence}
            output_file = os.path.join(output_dir, f'{i}_{j}.json')
            with open(output_file, 'w') as out:
                json.dump(output_data, out, indent=4)

if __name__ == "__main__":
    input_file = 'input.json'  # Change this to your input JSON file
    
    # Start the observer to monitor file changes
    observer = Observer()
    observer.schedule(JSONHandler(input_file), path=os.path.dirname(input_file))
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
