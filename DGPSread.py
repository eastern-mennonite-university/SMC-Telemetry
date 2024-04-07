import serial

serGPS = None

def GPSdata():
    global knots

    go = False
    knots = 0

    try:
        serGPS = serial.Serial('/dev/ttyACM0', 9600)
        serGPS.write("$PMTK_SET_NMEA_OUTPUT_RMCGGA\r\n")
        while True:
            try:
                rawdata = serGPS.readline()
                splitdata=rawdata.split(b',')
                
                nema = splitdata[0]

                if nema.find(b'GGA') > 0:
                    if splitdata[6] == b'0':
                        print("-1")
                    elif splitdata[6] == b'1':
                        go = True
                    elif splitdata[6] == b'2':
                        go = True
                if go:
                    if nema.find(b'RMC') > 0:
                        knots = splitdata[7]
                        return float(knots.decode())
            except ValueError as ve:
                print(ve)
    except serial.serialutil.SerialException as se:
        print(se)