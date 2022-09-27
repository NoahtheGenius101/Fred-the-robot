import os
import pyttsx3
import pyfirmata
from pyfirmata import ArduinoMega, SERVO,OUTPUT ,util
board = ArduinoMega('/dev/ttyACM0')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
engine.setProperty('rate', 50)
Action = "normal"
pin = 5
pin6 = 6
pin7 = 7    
board.digital[pin6].mode = SERVO
board.digital[pin6].write(90)
board.digital[pin7].mode = SERVO
board.digital[pin7].write(90)
board.digital[pin].mode = SERVO
board.digital[pin].write(90)
true = True

print("Starting")
print("Start Action")

if 'mad' in Action:
       board.digital[pin6].write(110)
       board.digital[pin7].write(70)
       board.digital[pin].write(100)
elif 'sad' in Action:
       board.digital[pin6].write(60)
       board.digital[pin7].write(120)
       board.digital[pin].write(100)
elif 'surprised' in Action:
       board.digital[pin6].write(53)
       board.digital[pin7].write(125)
       board.digital[pin].write(50)
elif 'normal' in Action:
       board.digital[pin6].write(90)
       board.digital[pin7].write(90)
       board.digital[pin].write(100)
else:
            talk("I can't do that")


