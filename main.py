import speech_recognition as s_r
import wikipedia
import pyttsx3
import os
# output of any text in speech
converter = pyttsx3.init()
converter.setProperty('rate', 130)
converter.setProperty('voice', 'english')


def say(text):
    converter.say(text)
    converter.runAndWait()


# main function
def main():
    # setting up the recognizer i.e it will recogniz the audio and convert it into text
    r = s_r.Recognizer()
    my_mic = s_r.Microphone()


    while True:
        
        with my_mic as source:
            os.system('clear')
            print('listening!!')
            r.adjust_for_ambient_noise(source)
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                if text == "stop the program":
                    print('stopping the program')
                    break
                else:
                    pass
            except:
                say("please repeat it again")
                pass
        
        try:
            result = wikipedia.summary(text, sentences = 2)
        except wikipedia.exceptions.PageError:
            result = "Sorry, couldn't find results"

        print('===============================')
        print(f"You: {text}")
        print('===============================')
        print(f"James: {result}")
        say(result)


    





if __name__ == "__main__":
    main()
