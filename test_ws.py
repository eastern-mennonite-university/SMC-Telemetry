import asyncio
import json
import websockets
import random
import time

async def send_data():
    url = 'wss://SMC-Telemetry.emu-super-mileage-car.repl.co/send_data/'
    async with websockets.connect(url) as websocket:
        while True:
            await websocket.send(json.dumps({
            'rpm': random.randint(1500, 2500),
            'speed': random.randint(20, 30),
            'voltage': random.random() + 13.5,
            'o2s': random.random() * 0.25 + 0.375,
            'econ': random.random() * 0.25 + 0.375,
            'temp-air': random.randint(95, 100),
            'temp-engine': random.randint(205, 215),
            }))
            time.sleep(0.1)

if __name__ == '__main__':
    asyncio.run(send_data())