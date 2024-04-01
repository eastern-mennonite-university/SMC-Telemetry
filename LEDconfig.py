import time
import RPi.GPIO as GPIO
import tm1637
from DGPSread_mod import *


#initialize TM1637 display
tm_acc = tm1637.TM1637(clk = 13, dio = 6) #choose display pins
tm_vel = tm1637.TM1637(clk = 5, dio =0) #choose display pins

while True:
    tm_vel.show('vel')
    tm_acc.show('acc')
#     gps_data = GPSdata()
#     if gps_data:
#        tm_vel.number(round(gps_data*10))
