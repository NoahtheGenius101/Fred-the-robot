from flask import Flask, render_template_string, Response, request   # Importing the Flask modules 
import pyfirmata
from pyfirmata import ArduinoMega, SERVO,OUTPUT ,util
import pyttsx3
import cv2
video_path = 0
cam = cv2.VideoCapture(video_path)
board = ArduinoMega('/dev/ttyACM0')
from time import sleep      # Import sleep module from time library 
pin3 = 4
pin = 5
# GPIO Pin where sero is connected
# Defing Servo Pin as output pin
board.digital[pin3].mode = SERVO
board.digital[pin].mode = SERVO
# Setting up voice
engine = pyttsx3.init()
engine.setProperty('rate', 50)
board.digital[pin3].write(90)
app = Flask(__name__)
#HTML Code 
TPL = '''
<html>
     <img src="https://iotdesignpro.com/sites/default/files/Iot%20Design%20Pro%20Logo_0.png" alt="">
    <head><title>Web Page Controlled Robot</title></head>
    <body>
    <h2> Web Page to Control Fred</h2>
        <form method="POST" action="test">
            <h3> Video feed  </h3>
            <img src="{{ url_for('video')}}">
            <h3> Use the Text to speech bubble  </h3>
            <label for="speech">"Speech"</label>
            <input type="text" placeholder="Speech" name="speech">
            <p>Slider   <input type="range" min="1" max="180" name="slider" /> </p>
            <input type="submit" value="submit" />
        </form>
    </body>
</html>

'''

def stream():
    while 1 :
        __,frame = cam.read()
        imgencode = cv2.imencode('.jpg',frame)[1]
        strinData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')

@app.route('/video')
def video():
    return Response(stream(),mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/test", methods=["POST"])
def test():
    # Get Values
    slider = request.form["slider"]
    speech = request.form["speech"]
    # Change duty cycle
    text(speech)
    print(speech)
    board.digital[pin3].write(slider)
    sleep(1)
    # Pause the servo
    board.digital[pin3].write(slider)
    return render_template_string(TPL)

def text(speech):
    board.digital[pin].write(50)
    engine.say(speech)
    engine.runAndWait()
    board.digital[pin].write(100)
    
# Run the app on the local development server
if __name__ == "__main__":
    app.run(host="0.0.0.0")
