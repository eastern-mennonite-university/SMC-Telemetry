import time
import json
import websockets

import random

async def send_data():
    uri = 'ws://localhost:8000/send_data/'
    async with websockets.connect(uri) as websocket:
        while True:
            data = {
                'rpm': random.randint(1500, 2500),
                'speed': random.randint(20, 30),
                'voltage': random.random() + 13.5,
                'o2s': random.random() * 0.25 + 0.375,
                'econ': random.random() * 0.25 + 0.375,
                'temp-air': random.randint(95, 100),
                'temp-engine': random.randint(205, 215),
            }

            await websocket.send(json.dumps(data))
            time.sleep(0.01)
