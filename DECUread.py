import serial
import cantools
from pprint import pprint

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