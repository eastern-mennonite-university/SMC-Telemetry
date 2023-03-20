import serial

serGPS = None

def GPSdata():
    try:
        global serGPS
        if not serGPS:
            serGPS = serial.Serial('/dev/ttyACM0', 115200)
            serGPS.reset_input_buffer()
        try:
            if serGPS.in_waiting > 0:
                speed = serGPS.read(serGPS.in_waiting)
                serGPS.reset_input_buffer()
                try:
                    return float(speed.decode())
                except ValueError:
                    pass
        except OSError:
            pass
    except serial.serialutil.SerialException:
        pass
    return None
