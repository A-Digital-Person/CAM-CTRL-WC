from Adafruit_MotorHAT import Adafruit_MotorHAT
import time

hat = Adafruit_MotorHAT(addr=0x60)

M1 = 3
M2 = 4

leftM = hat.getMotor(M1)
rightM = hat.getMotor(M2)

speed = 100 #Range of 0 - 255

leftM.setSpeed(speed)
rightM.setSpeed(speed)

time.sleep(2)

leftM.run(hat.FORWARD)

time.sleep(2)

leftM.run(hat.RELEASE)
