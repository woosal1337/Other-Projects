import sounddevice as sd
from numpy import linalg as LA
import numpy as np
import speech_recognition as sr

duration = 100000  # seconds


def recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

def print_sound(indata, outdata, frames, time, status):
    global volume_norm
    volume_norm = np.linalg.norm(indata) * 10
    print(int(volume_norm))

    if volume_norm >= 100:
        recognition()
    else:
        print_sound()


with sd.Stream(callback=print_sound):
    print_sound()