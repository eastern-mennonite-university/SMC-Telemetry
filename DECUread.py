import serial
import cantools
from pprint import pprint

'''
# CAN messages we need:
#   gp0 - Uptime and RPM
#   gp2 - Baro, MAP
#   gp3 - tps, batt
#   gp4 - air density
#   gp5 - tpsaccel barocor
#   gp6 - totalcor
#   gp7 - TPSdot MAPdot RPMdot
#   gp11 - airtemp
'''

def ECUdata():
    global serECU
    global db
    variables = dict()
    db = cantools.database.load_file('Megasquirt_CAN.dbc')
    try:
        if not serECU:
            serECU = serial.Serial('/dev/ttyAMC1', 115200)
            serECU.reset_input_buffer()
        if serECU.in_waiting() > 0:
            message = serECU.read(serECU.in_waiting)
            if message == "None":
                print("None")
            else:
                db.decode_message(message.arbitration_id, message.data)

        
        

    except serial.serialutil.SerialException:
        pass