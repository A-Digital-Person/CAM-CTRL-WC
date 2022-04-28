#Thinking of what libs I might need
import cv2 #Image data
import yaml #Data mangement
import time #Delay/Logging
import numpy #Image data
import os #File mangement

def capcolor():
    pass

def cutscreen():
    pass

def finddriection():
    pass

def logwarn(msg):
    pass

def logerror(msg):
    pass

def loginfo(msg):
    pass

def estop():
    pass

def testbuttin(din, state):
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

def tail:
    pass
