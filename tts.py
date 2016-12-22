from gtts import gTTS
import os

tts = gTTS(text="", lang="en")
tts.save("t.mp3")
os.system("mpg321 t.mp3")
