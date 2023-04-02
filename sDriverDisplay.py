## Class for on board driver indicators for speed and acceleration.
# This is a dependent class that will be run on LORAsend so that 
# it is running on the onboard pi. Velocity and acceleration will then be displayed
# in the LORAsend class using the TM1637 library to display on seven segment LED.
from DGPSread import *
import time
import RPi.GPIO as GPIO
import tm1637
import board
import adafruit_adxl34x

#initialize TM1637 display
tm_vel = tm1637.TM1637(clk = 19, dio = 16) #choose display pins
tm_acc = tm1637.TM1637(clk = 26, dio = 20) #choose display pins
tm_vel.brightness(val=2)
tm_acc.brightness(val=2)

# Initialize Accelerometer
i2c = board.I2C()  # uses board.SCL and board.SDA
accelerometer = adafruit_adxl34x.ADXL345(i2c)
accelerometer.enable_motion_detection(threshold = 20)

while True:
    print(accelerometer.acceleration)
#     time.sleep(.5)
#     print("Motion detected: %s" % accelerometer.events["motion"])
    forward_acc = accelerometer.acceleration[2]
    tm_acc.number(round(forward_acc*10))
    velocity = GPSdata()
    print(velocity)
    if velocity:
        tm_vel.number(round(velocity*10)) #multiply by 10 to get an extra decimal since library doesn't work with decimals
