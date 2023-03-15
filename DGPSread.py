import serial

serGPS = None

def GPSdata():
    global serGPS
    if not serGPS:
        serGPS = serial.Serial('/dev/ttyACM0', 115200)
    newbytes = serGPS.inWaiting()
    speed = str(serGPS.read(newbytes), 'UTF-8')
    if len(speed) > 0:
        return speed
    return None
