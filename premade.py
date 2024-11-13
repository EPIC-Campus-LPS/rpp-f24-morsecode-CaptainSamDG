import RPi.GPIO as GPIO
from pydub import AudioSegment
from pydub.playback import play


dot_sound = AudioSegment.from_file("short.mp3", format="mp3")  # sot
dash_sound = AudioSegment.from_file("long.mp3", format="mp3")  # dash

# dict for all important morse char
morse_dict = {
    "A": (dot_sound, dash_sound),         # .- (dot-dash)
    "B": (dash_sound, dot_sound, dot_sound, dot_sound),   # -... (dash-dot-dot-dot)
    "C": (dash_sound, dot_sound, dash_sound, dot_sound),  # -.-. (dash-dot-dash-dot)
    "D": (dash_sound, dot_sound, dot_sound),             # -.. (dash-dot-dot)
    "E": (dot_sound,),                                  # . (dot)
    "F": (dot_sound, dot_sound, dash_sound, dot_sound),  # ..-. (dot-dot-dash-dot)
    "G": (dash_sound, dash_sound, dot_sound),           # --. (dash-dash-dot)
    "H": (dot_sound, dot_sound, dot_sound, dot_sound),  # .... (dot-dot-dot-dot)
    "I": (dot_sound, dot_sound),                       # .. (dot-dot)
    "J": (dot_sound, dash_sound, dash_sound, dash_sound),  # .--- (dot-dash-dash-dash)
    "K": (dash_sound, dot_sound, dash_sound),           # -.- (dash-dot-dash)
    "L": (dot_sound, dash_sound, dot_sound, dot_sound),  # .-.. (dot-dash-dot-dot)
    "M": (dash_sound, dash_sound),                     # -- (dash-dash)
    "N": (dash_sound, dot_sound),                      # -. (dash-dot)
    "O": (dash_sound, dash_sound, dash_sound),          # --- (dash-dash-dash)
    "P": (dot_sound, dash_sound, dash_sound, dot_sound),  # .--. (dot-dash-dash-dot)
    "Q": (dash_sound, dash_sound, dot_sound, dash_sound),  # --.- (dash-dash-dot-dash)
    "R": (dot_sound, dash_sound, dot_sound),           # .-. (dot-dash-dot)
    "S": (dot_sound, dot_sound, dot_sound),            # ... (dot-dot-dot)
    "T": (dash_sound,),                                # - (dash)
    "U": (dot_sound, dot_sound, dash_sound),           # ..- (dot-dot-dash)
    "V": (dot_sound, dot_sound, dot_sound, dash_sound),  # ...- (dot-dot-dot-dash)
    "W": (dot_sound, dash_sound, dash_sound),           # .-- (dot-dash-dash)
    "X": (dash_sound, dot_sound, dot_sound, dash_sound),  # -..- (dash-dot-dot-dash)
    "Y": (dash_sound, dot_sound, dash_sound, dash_sound),  # -.-- (dash-dot-dash-dash)
    "Z": (dash_sound, dash_sound, dot_sound, dot_sound),  # --.. (dash-dash-dot-dot)
    "1": (dot_sound, dash_sound, dash_sound, dash_sound, dash_sound),  # .---- (dot-dash-dash-dash-dash)
    "2": (dot_sound, dot_sound, dash_sound, dash_sound, dash_sound),  # ..--- (dot-dot-dash-dash-dash)
    "3": (dot_sound, dot_sound, dot_sound, dash_sound, dash_sound),  # ...-- (dot-dot-dot-dash-dash)
    "4": (dot_sound, dot_sound, dot_sound, dot_sound, dash_sound),  # ....- (dot-dot-dot-dot-dash)
    "5": (dot_sound, dot_sound, dot_sound, dot_sound, dot_sound),  # ..... (dot-dot-dot-dot-dot)
    "6": (dash_sound, dot_sound, dot_sound, dot_sound, dot_sound),  # -.... (dash-dot-dot-dot-dot)
    "7": (dash_sound, dash_sound, dot_sound, dot_sound, dot_sound),  # --... (dash-dash-dot-dot-dot)
    "8": (dash_sound, dash_sound, dash_sound, dot_sound, dot_sound),  # ---.. (dash-dash-dash-dot-dot)
    "9": (dash_sound, dash_sound, dash_sound, dash_sound, dot_sound),  # ----. (dash-dash-dash-dash-dot)
    "0": (dash_sound, dash_sound, dash_sound, dash_sound, dash_sound),  # ----- (dash-dash-dash-dash-dash)
}



user = input("what? ")
user = user.replace(" ", "")
user = user.upper()
for char in user: #for every char in user
	if char in morse_dict: #if char is in the dict
		for sound in morse_dict[char]: #make sound if in dict
			play(sound)  #play the sound
