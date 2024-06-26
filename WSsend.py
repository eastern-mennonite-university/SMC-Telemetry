import time
import asyncio
import json
import websockets
import tm1637
import DECUread
import DGPSread

#initialize TM1637 display
#NOTE THAT SIXFAB HAT HAS PINS THAT DO THINGS
tm_speed = tm1637.TM1637(clk = 23, dio = 24)
tm_rpm = tm1637.TM1637(clk = 25, dio = 16)
tm_speed.brightness(val=2)
tm_rpm.brightness(val=2)

rpm = None
speed = None

payload_data = dict()

'''
async def send_data():
    try:
        url = 'wss://84436788-f699-4fda-98e3-4f0bed88db2b-00-u8599ttrqb23.picard.replit.dev/'
        async with websockets.connect(url) as websocket:
            while True:
                ecu_data = ECUdata()
                if ecu_data:
                    payload_data.update(ecu_data)

                gps_data = parseGPS()
                if gps_data:
                    payload_data['speed'] = str(gps_data)

                await websocket.send(json.dumps(payload_data))
                time.sleep(0.1)
    except Exception as e:
        print(e)
'''
def Dashboard():
    global speed

    DGPSread.parseGPS()
    speed = float(DGPSread.knots)*1.151
    print(speed)
    tm_speed.number(int(speed)) #library doesn't work with decimals
def ECU():
    DECUread.ECUdata()
    print(DECUread.data)
if __name__ == '__main__':
    #asyncio.run(send_data())
    while 1:
        Dashboard()
        ECU()
        with open("data.txt", 'w') as output:
            output.write(str(speed))
            output.write(str(DECUread.data))