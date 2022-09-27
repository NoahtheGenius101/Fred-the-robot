'''
Face Tracking with OpenCV and Pan-Tilt controled servos 
    Based on a face detection tutorial on pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/
Developed by Marcelo Rovai - MJRoBot.org @ 7Feb2018 
'''

import numpy as np
import cv2
import os
import time
import pyfirmata
from pyfirmata import ArduinoMega, SERVO, util
board = ArduinoMega('/dev/ttyACM0')

# define servos GPIO
pinPan = 4
board.digital[pinPan].mode = SERVO
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

cap = cv2.VideoCapture(0)

# Defining and initializing globals
global panServoAngle
panServoAngle = 90
board.digital[pinPan].write(90)

# positioning servos at 105-90 degrees
print("\n [INFO] Positioning servos to initial position ==> Press 'ESC' to quit Program \n")

    
# Position servos to capture object at center of screen
def servoPosition (x):
    global panServoAngle
    
    if (x < 250):
        panServoAngle += 5
        if panServoAngle > 65:
            panServoAngle = 65
        board.digital[pinPan].write(panServoAngle)
        print("Head move to 65")
    
    if (x > 262):
        panServoAngle -= 5
        if panServoAngle < 82:
            panServoAngle = 82
        board.digital[pinPan].write(panServoAngle)
        print("Head move to 82")
    
    if (x > 275):
        panServoAngle -= 5
        if panServoAngle < 90:
            panServoAngle = 90
        board.digital[pinPan].write(panServoAngle)
        print("Head move to 90")
  
    if (x > 287):
        panServoAngle -= 5
        if panServoAngle < 95:
            panServoAngle = 95
        board.digital[pinPan].write(panServoAngle)
        print("Head move to 95")
  
    if (x > 300):
        panServoAngle -= 5
        if panServoAngle < 100:
            panServoAngle = 100
        board.digital[pinPan].write(panServoAngle)
        print("Head move to 100")


while 1:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        servoPosition(int(x+y/1))
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #servoPosition(int(x+w/2), int(y+h/2))
        print (int(x+w/2), int(y+h/2))
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

# do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff \n")
panServoAngle = 90
board.digital[pinPan].write(panServoAngle)
cap.release()
cv2.destroyAllWindows()
