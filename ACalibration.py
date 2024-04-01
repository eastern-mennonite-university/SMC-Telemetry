#Acceleration calibration for ADXL345: not necessary, code does not run

import adafruit_adxl34x
import board
import time
import numpy as np
i2c = board.I2C()  # uses board.SCL and board.SDA
accelerometer = adafruit_adxl34x.ADXL345(i2c)

xacc = []
yacc = []
zacc = []

i = 0
while i<=1000:
    time.sleep(1)
    print(accelerometer.acceleration)

    print(accelerometer.acceleration)
    xread= accelerometer.acceleration[0]
    yread = accelerometer.acceleration[1]
    zread = accelerometer.acceleration[2]
    
    xacc = np.append(xacc,xread)
    yacc = np.append(yacc,yread)
    zacc = np.append(zacc,zread)
    i+=1
    
else:
    maxX = max(xacc)
    minX = min(xacc)
    maxY = max(yacc)
    minY = min(yacc)
    maxZ = max(zacc)
    minZ = min(zacc)

    
    
