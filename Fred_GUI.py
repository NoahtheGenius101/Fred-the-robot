# importing easygui module
import subprocess
from easygui import *


TinMan = 'python TinMan.py'
Fred_Main = 'python Fred_Main.py'
# message to be displayed 
text = "Click on a button to set fred's mode"
  
# window title
title = "Run Fred"
  
# button list
button_list = []
  
# button 1
button1 = "Fred_Main"
  
# second button
button2 = "TinMan"
  
  

# appending button to the button list
button_list.append(button1)
button_list.append(button2)
  
# creating a button box
output = buttonbox(text, title, button_list)
  
# printing the button pressed by the user
if output == "Fred_Main":
    print("Fred_Main")
    F = subprocess.Popen(Fred_Main,shell=True)
elif output == "TinMan":
    print("TinMan")
    T = subprocess.Popen(TinMan,shell=True)