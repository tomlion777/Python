import speech_recognition as sr
import win32com.client as wincl

while True:
    r = sr.Recognizer()
    text2speech = wincl.Dispatch("SAPI.SpVoice")
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))

            if "Hello" or "hello" in text:
                print('Saying : Hello')
                text2speech.Speak("Hello")

            if text == "Quit" or "quit":
                print("BYE...")
                text2speech.Speak("BYE...")
                break
        except:
            print("Sorry could not recognize what you said")
            text2speech.Speak("Sorry could not recognize what you said")