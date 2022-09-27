import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from time import sleep
from bs4 import BeautifulSoup
import requests
from pyfirmata import ArduinoMega, SERVO
board = ArduinoMega('/dev/ttyACM0')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 50)
print("Booting Up")
city = "MiddleTown weather"
pin = 5
board.digital[pin].mode = SERVO
board.digital[pin].write(100)
Robot_Name = "Fred"

def talk(text):
    board.digital[pin].write(50)
    engine.say(text)
    engine.runAndWait()
    board.digital[pin].write(100)
  
  
def weather(city):
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching in google......\n")
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()  
    time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    Weather1 = (location+" "+info+" "+weather+"°C")
    Forcast = str(Weather1)
    talk(Forcast)

  
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if Robot_Name in command:
                command = command.replace(Robot_Name, '')
                print(command)
                    
    except:
        pass
    return command


def run_Action():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The Current time is ' + time)
    elif 'weather' in command:
        weather(city)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'day' in command:
        Date = datetime.datetime.now().strftime('%A %x')
        print(Date)
        talk('Today is' + Date)
    elif 'what is your name' in command:
        talk('My name is Fred')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'cancel' in command:
        talk("Canceling")
    else:
        talk('Please say the command again.')


while True:
    run_Action()
