import apiai
import json
import pyttsx
from gtts import gTTS
import os

def speakG(text):
	tts = gTTS(text=text, lang="en-us")
	tts.save("t.mp3")
	os.system("mpg321 -q t.mp3")

def speakT(text):
	tts = pyttsx.init("espeak")
	tts.setProperty("rate", 150)
	tts.say(text)
	tts.runAndWait()

client_access_token = "2f61024d8e5b4ac08393c521a0c740b3"

agent = apiai.ApiAI(client_access_token)

user_inp = "Hi"
session_id = None

while True:
	request = agent.text_request()
	request.query = user_inp
	if session_id:
		request.session_id = session_id
	response_data = json.loads(request.getresponse().read())
	response_message = response_data['result']['fulfillment']['speech']
	session_id = response_data['sessionId']
	print " > Bot : " + response_message
	speakT(response_message)
	user_inp = raw_input(" > You : ")
	if(user_inp == "exit"):
		break