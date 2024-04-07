import serial
import cantools
import can
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
    global data
    data = 0
    variables = dict()
    db = cantools.database.load_file('Megasquirt_CAN.dbc')
    try:
        can_bus = can.interfaces.serial.serial_can.SerialBus("/dev/ttyAMC0")
        message = can_bus.recv()
        data = db.decode_message(message.arbitration_id, message.data)
        print(data)
        return data
    except:
        pass
