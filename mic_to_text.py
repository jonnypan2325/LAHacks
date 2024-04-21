
import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def record_text():
	# Loop infinitely for user to
    # speak

    while(True): 
        # Exception handling to handle
        # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input 
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)

                print(MyText)
                return MyText
                
                
                # MyText = MyText.lower()

                # print("Detection: ",MyText)
                # SpeakText(MyText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")

def output_text(text):
    f = open(".\\output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(True):
    text = record_text()
    output_text(text)
    print("Wrote text")