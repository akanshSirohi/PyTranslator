from LiveRecogniser import RecogniseSpeech
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

translator = Translator()
tmp_file = "temp.mp3"

while True:
    text=RecogniseSpeech()
    if len(text) > 0:
        t_txt = translator.translate(text, dest='hi')
        print("Translated: ",t_txt.text)
        tts = gTTS(t_txt.text)
        tts.save(tmp_file)
        playsound(tmp_file)
        os.remove(tmp_file)