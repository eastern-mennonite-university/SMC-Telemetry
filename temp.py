from DGPSread import GPSdata

import serial

serGPS = serial.Serial('/dev/ttyACM0', 9600)

while True:
    speed = GPSdata()
    if speed:
        print(speed)

# while True:
#     print(GPSdata())