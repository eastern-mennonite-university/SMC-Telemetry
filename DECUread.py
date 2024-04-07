import serial
import cantools
import can
from can.interfaces.serial import SerialBus

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
        can_bus = SerialBus("/dev/ttyACM0")
        message = can_bus.recv()
        data = db.decode_message(message.arbitration_id, message.data)
        print(data)
        return data
    except Exception as e:
        print(e)
