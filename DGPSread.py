# Based off of SixFab's GPS example code (https://docs.sixfab.com/page/read-gnss-gps-data-with-sixfab-hat)
# Sixfab - Reading GPS data with Python
# 2020

from time import sleep
import serial

portwrite = "/dev/ttyUSB2"
port = "/dev/ttyUSB1"

def parseGPS():
    global knots
    knots = 0

    try:
        ser = serial.Serial(port, baudrate = 115200, timeout = 0.5,rtscts=True, dsrdtr=True)
        data = ser.readline().decode('utf-8')
    except Exception as e:
        print(e)

    #print(data, end='') #prints raw data
    if data[0:6] == "$GPRMC":
        sdata = data.split(",")
        if sdata[2] == 'V':
            print("\nNo satellite data available.\n")
            return
        #print("-----Parsing GPRMC-----")
        #time = sdata[1][0:2] + ":" + sdata[1][2:4] + ":" + sdata[1][4:6]
        #lat = decode(sdata[3]) #latitude
        #dirLat = sdata[4]      #latitude direction N/S
        #lon = decode(sdata[5]) #longitute
        #dirLon = sdata[6]      #longitude direction E/W
        knots = sdata[7]       #Speed in knots
        #trCourse = sdata[8]    #True course
        #date = sdata[9][0:2] + "/" + sdata[9][2:4] + "/" + sdata[9][4:6] #date
        #variation = sdata[10]  #variation
        #degreeChecksum = sdata[13] #Checksum
        #dc = degreeChecksum.split("*")
        #degree = dc[0]        #degree
        #checksum = dc[1]      #checksum

        #latitude = lat.split() # parsing latitude
        #longitute = lon.split() # parsing longitute

        #print("\nLatitude: " + str(int(latitude[0]) + (float(latitude[2])/60)) + dirLat) 

        #print("Longitute: " + str(int(longitute[0]) + (float(longitute[2])/60)) + dirLon)

        print("knots : %s"%   (knots))


def decode(coord):
    #Converts DDDMM.MMMMM -> DD deg MM.MMMMM min
    x = coord.split(".")
    head = x[0]
    tail = x[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + " deg " + min + "." + tail + " min"

print("Connecting Port..")
try:
    serw = serial.Serial(portwrite, baudrate = 115200, timeout = 1,rtscts=True, dsrdtr=True)
    serw.write('AT+QGPS=1\r'.encode())
    serw.close()
    sleep(1)
except Exception as e: 
    print("Serial port connection failed.")
    print(e)