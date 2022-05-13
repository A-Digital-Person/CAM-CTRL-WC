# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#
# Camera Controlled Wheelchair - (CAM CTRL WC)
#
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

import cv2 #Image data
import yaml #Data mangement
import time #Delay/Logging
import numpy #Image data
import os #File mangement
import re #Clean Strings
from datetime import datetime #Getting the date for logs
import sys #Kill code
from Adafruit_MotorHAT import Adafruit_MotorHAT #Motor CTRL

version = '0.0.1' #Code Version

#INIT Code
#Creats a log folder if not found and make a new log file
if not os.path.exists(os.getcwd() + '/logs'):
    os.makedirs(os.getcwd() + '/logs')
loglocation = "logs/CAMCTRLWC" + str(datetime.now()) + '.log'
loglocation = re.sub(':', '', loglocation)
log = open(loglocation, "w")
log.write("STARTING CAM CTRL WC - " + str(version) + "...\n")
log.close()

# Sets up the tail
tailpointsx = [0,0,0,0,0,0,0,0,0,0]
tailpointsy = [0,0,0,0,0,0,0,0,0,0]

#Sets the max speed the motors will be allowed to move
maxspeed = 100 #Range of 0 - 255

#Sets the motors pins
hat = Adafruit_MotorHAT(addr=0x60)
M1 = 3
M2 = 4

#Gets the x,y cords from the frame and find the way it should go
def finddriection():
    pass

#Next three functions print information to the log file for debugging
#If something goes worng the file can be sent to devs to trbleshoot
def logwarn(msg):
    dadate = str(datetime.now())
    dadate = re.sub(':', '', dadate)
    log = open(loglocation, "a")
    log.write(str(dadate) + " Warn: " + str(msg) + '\n')
    log.close()
    print(str(dadate) + " Warn: " + str(msg) + '\n')

def logerror(msg):
    dadate = str(datetime.now())
    dadate = re.sub(':', '', dadate)
    log = open(loglocation, "a")
    log.write(str(dadate) + " Error: " + str(msg) + '\n')
    log.close()
    print(str(dadate) + " Error: " + str(msg) + '\n')

def loginfo(msg):
    dadate = str(datetime.now())
    dadate = re.sub(':', '', dadate)
    log = open(loglocation, "a")
    log.write(str(dadate) + " Info: " + str(msg) + '\n')
    log.close()
    print(str(dadate) + " Info: " + str(msg) + '\n')

#Prevents the bot from moving if emergency stopped
def estop():
    try:
        leftM.run(hat.RELEASE)
        rightM.run(hat.RELEASE)
    except:
        logwarn('Something went wrong. Be carefull!') #If something goes wrong in the motors let the user know to be carefull | Motors should not ever move

#Checks the state of a button and returns the output
def testbutton(din, state): #din = pin and state = up or down
    bstate = mech.read_pin(din)
    if state == 'down': #Check if switch is down
        if bstate == True:
            output = True
        else:
            output = False
    elif state == 'up': #Check if switch is up
        if bstate == False:
            output = True
        else:
            output =  False
    return output

#Moves the bot into the wanted path
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
        
#Draws a cursor tail to show direction of travel
def tail():
    global tailpointsx
    global tailpointsy
    global frame
    
#     cv2.circle(frame, (int(tailpointsx[9]),int(tailpointsy[9])),12,(0,0,0),-1) #Starts the 'tail' part
#     cv2.circle(frame, (int(tailpointsx[9]),int(tailpointsy[9])),10,(20,0,0),-1)
# 
#     cv2.circle(frame, (int(tailpointsx[8]),int(tailpointsy[8])),10,(0,0,0),-1)
#     cv2.circle(frame, (int(tailpointsx[8]),int(tailpointsy[8])),8,(40,0,0),-1)
#     
#     cv2.circle(frame, (int(tailpointsx[7]),int(tailpointsy[7])),10,(0,0,0),-1)
#     cv2.circle(frame, (int(tailpointsx[7]),int(tailpointsy[7])),8,(60,0,0),-1)
# 
#     cv2.circle(frame, (int(tailpointsx[6]),int(tailpointsy[6])),10,(0,0,0),-1)
#     cv2.circle(frame, (int(tailpointsx[6]),int(tailpointsy[6])),8,(80,0,0),-1)
    
    cv2.circle(frame, (int(tailpointsx[5]),int(tailpointsy[5])),10,(0,0,0),-1)
    cv2.circle(frame, (int(tailpointsx[5]),int(tailpointsy[5])),8,(0,42,0),-1)
    
    cv2.circle(frame, (int(tailpointsx[4]),int(tailpointsy[4])),10,(0,0,0),-1)
    cv2.circle(frame, (int(tailpointsx[4]),int(tailpointsy[4])),8,(0,85,0),-1)
    
    cv2.circle(frame, (int(tailpointsx[3]),int(tailpointsy[3])),10,(0,0,0),-1)
    cv2.circle(frame, (int(tailpointsx[3]),int(tailpointsy[3])),8,(0,127,0),-1)
    
    cv2.circle(frame, (int(tailpointsx[2]),int(tailpointsy[2])),10,(0,0,0),-1)
    cv2.circle(frame, (int(tailpointsx[2]),int(tailpointsy[2])),8,(0,170,0),-1)
    
    cv2.circle(frame, (int(tailpointsx[1]),int(tailpointsy[1])),10,(0,0,0),-1)
    cv2.circle(frame, (int(tailpointsx[1]),int(tailpointsy[1])),8,(0,212,0),-1)
    
    cv2.circle(frame, (int(tailpointsx[0]),int(tailpointsy[0])),10,(0,0,0),-1) #Draws a dot onto the screen first a black and then a colored circle is drawn on top
    cv2.circle(frame, (int(tailpointsx[0]),int(tailpointsy[0])),8,(255,0,0),-1)
    
    tailpointsx = tailpointsx[:-1]
    tailpointsy = tailpointsy[:-1] #Removes last tail point

#Get the screen size
#screen = ctypes.windll.user32
#Reference = screen.GetSystemMetrics(0) | 0 = width 1 = height

#Find a aviable camera
# cap = cv2.VideoCapture(0)
# if cap is None or not cap.isOpened():
#     cap = cv2.VideoCapture(1)
#     if cap is None or not cap.isOpened():
#         cap = cv2.VideoCapture(2)
#         if cap is None or not cap.isOpened():
#             sys.exit
            
cv2.namedWindow("Capture")
cv2.resizeWindow("Capture", 300, 300)

#Cleaning size
kernel = numpy.ones((3,3), numpy.uint8)

cap = cv2.VideoCapture(0)
#Main loop
while True:
    ret, frame = cap.read()
    frame = frame[::3, ::3]
    frame = cv2.flip(frame, 1)
    hsvframe = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Set colors
    colorlow = [0,0,0] #HSV
    colorhigh = [180,255,255]
    
    #Set arrays
    colorlow = numpy.array(colorlow, dtype = "uint8")
    colorhigh = numpy.array(colorhigh, dtype = "uint8")
    
    #Find the color
    mask = cv2.inRange(hsvframe, colorlow, colorhigh)
    mask = cv2.bitwise_or(hsvframe, hsvframe, mask = mask)
    
    #Switch to HSV and clean mask
    mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations = 1)
    mk = cv2.moments(mask)
    
    #Find an image
    if mk["m00"] != 0:
        ctx = mk["m10"]/mk["m00"]
        cty = mk["m01"]/mk["m00"]
    else:
        ctx = 320 #If no color found place on the center of the screen so bot will stop
        cty = 240
        
    try:
        tailpointsx.insert(0, int(ctx)) #adds point to tail
        tailpointsy.insert(0, int(cty))
    except:
        logerror("Tail failed to insert " + str(int(ctx)) + " | " + str(int(cty)))
    
    tail()
    path('forward')
 
    cv2.imshow("Capture", frame)
    
    
    
    keypress = cv2.waitKey(30)
    
    if keypress == 27:
        break

estop()
cap.release()
cv2.destroyAllWindows()