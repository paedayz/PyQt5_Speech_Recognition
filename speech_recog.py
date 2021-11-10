from os import supports_bytes_environ
import speech_recognition as sr

# print(sr.Microphone.list_microphone_names())

def speech_recog_function():
    mic = sr.Microphone(1)
    recog = sr.Recognizer()

    with mic as source :
        audio = recog.listen(source)
        text = recog.recognize_google(audio, language="th")
        return text

# print(speech_recog_function())