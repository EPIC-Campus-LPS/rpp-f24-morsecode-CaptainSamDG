import RPi.GPIO as GPIO
from pydub import AudioSegment
from pydub.playback import play

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = GPIO.setup(25,GPIO.IN) #button

x = 0
while x == 0:
	if not GPIO.input(25):

		sound =  AudioSegment.from_file("general-lee-horn.mp3", format="mp3")
		play(sound)
		x += 1
