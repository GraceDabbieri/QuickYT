import platform
import subprocess
import pytchat
SYSTEM = platform.system()
ID = input("Please type the URL of the video: ")
WantsSpeech = input("Would you like each chat to be spoken aloud?\ny/n: ").lower()
def speak(text):
	print(text)
	if WantsSpeech not in ("y", "yes"):
		return
	if SYSTEM == "Windows":
		escaped = text.replace("'", "''")
		cmd = f"powershell -c \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{escaped}')\""
		subprocess.run(cmd, shell=True)
	elif SYSTEM == "Darwin":
		subprocess.run(["say", text])
	elif SYSTEM == "Linux":
		subprocess.run(["spd-say", "-r", "55", text])
	else:
		print("Unsupported OS for speech output.")
chat = pytchat.create(video_id=ID)
speak("Starting")
while chat.is_alive():
	for c in chat.get().sync_items():
		speak(c.author.name + ": " + c.message)
speak("Exiting.")
