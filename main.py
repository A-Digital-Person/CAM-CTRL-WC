#Thinking of what libs I might need
import cv2 #Image data
import yaml #Data mangement
import time #Delay/Logging
import numpy #Image data
import os #File mangement
import re #Clean Strings\
import datetime
from Adafruit_MotorHAT import Adafruit_MotorHAT

version = '0.0.1'

#INIT Code
if not os.path.exists(os.getcwd() + '/logs'):
    os.makedirs(os.getcwd() + '/logs')
loglocation = "logs/" + str(datetime.now()) + '.log'
loglocation = re.sub(':', '', loglocation)
log = open(loglocation, "w")
log.write("STARTING CAM CTRL WC - " + str(version) + "...")
log.close()

maxspeed = 100 #Range of 0 - 255

hat = Adafruit_MotorHAT(addr=0x60)
M1 = 3
M2 = 4

def errorwindow(msglist, msgcolorlist, dur): #List of error | Text color | Time in milliseconds
    root = Tk()
    root.geometry('500x300')
    root.after(dur, root.destroy)

def capcolor():
    pass

def cutimg(camin):
    return camin[::2, ::2]

def finddriection():
    pass

def logwarn(msg):
    pass

def logerror(msg):
    pass

def loginfo(msg):
    pass

def estop():
    try:
        leftM.run(hat.RELEASE)
        rightM.run(hat.RELEASE)
    except:
        estop()

def testbutton(din, state):
    if state == 'down':
        if din == True:
            output = True
        else:
            output = False
    elif state == 'up':
        if din == False:
            output = True
        else:
            output =  False
    return output

def path(use):
    try:
        if use == 'arcleft':
            leftM.setSpeed(maxspeed/1.5)
            rightM.setSpeed(maxspeed)
            
            leftM.run(hat.FORWARD)
            rightM.run(hat.FORWARD)
        elif use == 'arcright':
            leftM.setSpeed(maxspeed)
            rightM.setSpeed(maxspeed/1.5)
            
            leftM.run(hat.FORWARD)
            rightM.run(hat.FORWARD)
        elif use == 'rarcleft':
            leftM.setSpeed(maxspeed/1.5)
            rightM.setSpeed(maxspeed)
            
            leftM.run(hat.BACKWARD)
            rightM.run(hat.BACKWARD)
        elif use == 'rarcright':
            leftM.setSpeed(maxspeed)
            rightM.setSpeed(maxspeed/1.5)
            
            leftM.run(hat.BACKWARD)
            rightM.run(hat.BACKWARD)
        elif use == '0left':
            leftM.setSpeed(maxspeed/2)
            rightM.setSpeed(maxspeed/2)
            
            leftM.run(hat.BACKWARD)
            rightM.run(hat.FORWARD)
        elif use == '0right':
            leftM.setSpeed(maxspeed/2)
            rightM.setSpeed(maxspeed/2)
            
            leftM.run(hat.FORWARD)
            rightM.run(hat.BACKWARD)
        elif use == 'forward':
            leftM.setSpeed(maxspeed)
            rightM.setSpeed(maxspeed)
            
            leftM.run(hat.FORWARD)
            rightM.run(hat.FORWARD)
        elif use == 'backward':
            leftM.setSpeed(maxspeed/1.5)
            rightM.setSpeed(maxspeed/1.5)
            
            leftM.run(hat.BACKWARD)
            rightM.run(hat.BACKWARD)
    except:
        logerror('Pathing error in direction "' + str(use) + '"')
def tail:
    pass

cap = cv2.VideoCapture(0)
if cap is None or not cap.isOpened():
    cap = cv2.VideoCapture(1)
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(2)
        if cap is None or not cap.isOpened():
            