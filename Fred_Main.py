import subprocess
import time
ChatBot = 'python Fred_ChatBot.py'
Face_Dection = 'python CV2_Face_Recognition.py'
F = subprocess.Popen(Face_Dection,shell=True)
C = subprocess.Popen(ChatBot,shell=True)
import pyfirmata
from pyfirmata import ArduinoMega, SERVO,OUTPUT ,util
board = ArduinoMega('/dev/ttyACM0')
pin3 = 3
board.digital[pin3].mode = SERVO
print("Start")

def BlinkMove():
    time.sleep(0.5)
    board.digital[pin3].write(90)
    time.sleep(10)
    board.digital[pin3].write(0)

while 1:
    BlinkMove()
    
    
print("Stoped")
F = subprocess.Popen(Face_Dection,shell=False)
C = subprocess.Popen(ChatBot,shell=False)