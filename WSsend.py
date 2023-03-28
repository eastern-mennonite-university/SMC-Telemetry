import asyncio
import json
import websockets

from DECUread import *
from DGPSread import *

payload_data = dict()

ecu_flag = False

async def send_data():
    url = 'ws://localhost:8000/send_data/'
    async with websockets.connect(url) as websocket:
        while True:
            ecu_data = ECUdata()
            if ecu_data:
                payload_data.update(ecu_data)
                ecu_flag = True

            gps_data = GPSdata()
            if gps_data:
                payload_data['speed'] = str(gps_data)

            if ecu_flag:
                await websocket.send(json.dumps(payload_data))

if __name__ == '__main__':
    asyncio.run(send_data())
