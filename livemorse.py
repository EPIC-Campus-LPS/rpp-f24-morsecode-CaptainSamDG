import RPi.GPIO as GPIO
from pydub import AudioSegment
from pydub.playback import play
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.IN)  # button

# Pre-load sounds to reduce loading time on each press
short_sound = AudioSegment.from_file("short.mp3", format="mp3")
long_sound = AudioSegment.from_file("long.mp3", format="mp3")

x = 0

def pressed():
    global x
    while not GPIO.input(25):
        x = x + 0.2

    print(f"Button pressed. x = {x}")

    if x > 30000:
        # Play the long sound
        play(long_sound)
        x = 0
    elif x < 30000:
        # Play the short sound
        play(short_sound)
        x = 0

while True:
    if not GPIO.input(25):  # Button is pressed (active low)
        pressed()
