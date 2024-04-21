import speech_recognition as sr

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to speech
def record_text():
    # Use the microphone as source for input.
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        
        # Indefinitely listen for speech
        print("Listening for speech...")
        while True:
            try:
                audio = r.listen(source, phrase_time_limit=5)  # Adjust the time limit as needed
                recognized_text = r.recognize_google(audio)
                print("Detected speech:", recognized_text)
            except sr.UnknownValueError:
                print("Speech not recognized")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

# Call the function to start recording text
record_text()
