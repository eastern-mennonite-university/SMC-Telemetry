import time
import RPi.GPIO as GPIO
import tm1637
import board
import adafruit_adxl34x
import csv
from DECUread import *
from DGPSread import *

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
    payload_data = dict()
    ecu_data = ECUdata() # Collect ECU Data
    if ecu_data:
        payload_data.update(ecu_data)

    gps_data = GPSdata() #collect GPS data
    if gps_data:
        payload_data['speed'] = str(gps_data)
        tm_vel.number(round(gps_data*10)) #dispay on seven seg
        
    forward_acc = accelerometer.acceleration[2] #acceleration data
    payload_data['acceleration'] = str(forward_acc)
    tm_acc.number(round(forward_acc*10)) #dispay on seven seg
    
#     data = [1,2,2,3,4,5]
    #write to csv
    file = open('testdata','w+', newline = '')
    with file:
        write = csv.writer(file)
        write.writerow(payload_data)
