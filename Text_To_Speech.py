import win32com.client as wincl

text2speech = wincl.Dispatch("SAPI.SpVoice")
speech = input('Type text to speech : ')
print('Saying : ' + speech)
text2speech.Speak(speech)