import serial

def GPS():
    try:
        serGPS = serial.Serial('/dev/ttyACM0', 115200)
        while True:
            try:
                rawdata = serGPS.readline()
                mph = float(rawdata) * 1.151
                print(mph)
            except ValueError as ve:
                print(ve)
    except serial.serialutil.SerialException as se:
        print(se)

while 1:
    GPS()