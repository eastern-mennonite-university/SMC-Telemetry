import time
import asyncio
import json
import websockets

from DECUread import *
from DGPSread import *

payload_data = dict()

async def send_data():
    url = 'wss://84436788-f699-4fda-98e3-4f0bed88db2b-00-u8599ttrqb23.picard.repl.co/'
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

if __name__ == '__main__':
    asyncio.run(send_data())
