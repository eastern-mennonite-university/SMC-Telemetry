import time
import asyncio
import json
import websockets
import tm1637

from DECUread import *
from DGPSread import *

#initialize TM1637 display
tm_speed = tm1637.TM1637(clk = 19, dio = 16) #choose display pins
tm_rpm = tm1637.TM1637(clk = 26, dio = 20) #choose display pins
tm_speed.brightness(val=2)
tm_rpm.brightness(val=2)

rpm = None
speed = None

payload_data = dict()

async def send_data():
    try:
        url = 'wss://84436788-f699-4fda-98e3-4f0bed88db2b-00-u8599ttrqb23.picard.replit.dev/'
        async with websockets.connect(url) as websocket:
            while True:
                ecu_data = ECUdata()
                if ecu_data:
                    payload_data.update(ecu_data)

                gps_data = GPSdata()
                if gps_data:
                    payload_data['speed'] = str(gps_data)

                await websocket.send(json.dumps(payload_data))
                time.sleep(0.1)
    except Exception as e:
        print(e)

def Dashboard():
    speed = GPSdata()*1.151
    tm_speed.number(int(speed)) #library doesn't work with decimals

if __name__ == '__main__':
    asyncio.run(send_data())
    Dashboard()
