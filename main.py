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