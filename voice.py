#!/usr/bin/python3

import speech_recognition as  sr

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say Something!")
        audio = r.listen(source)

try:

	print("google thinks you said:" +r.recognize_google(audio))
except:
	print("Google Speech Recognition could not understand audio")
	pass

