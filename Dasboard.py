## Class for on board driver indicators for speed and acceleration.
# This is a dependent class that will be run on LORAsend so that 
# it is running on the onboard pi. Speed and acceleration will then be displayed
# in the LORAsend class using the TM1637 library to display on seven segment LED.
from DGPSread import *
import RPi.GPIO as GPIO
from DECUread import rpm
from DGPSread import speed
import tm1637

#initialize TM1637 display
tm_speed = tm1637.TM1637(clk = 19, dio = 16) #choose display pins
tm_rpm = tm1637.TM1637(clk = 26, dio = 20) #choose display pins
tm_speed.brightness(val=2)
tm_rpm.brightness(val=2)


while True:
    rotations = rpm
    tm_rpm.number(round(rotations))
    sp = speed
    tm_speed.number(round(sp*10)) #multiply by 10 to get an extra decimal since library doesn't work with decimals
