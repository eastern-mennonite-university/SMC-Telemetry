import asyncio
import json
from channels.consumer import AsyncConsumer
from random import randint
from time import sleep
from django_eventstream import send_event


class DataConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        # when websocket connects
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        # when messages is received from websocket
        data = json.loads(event['text'])
        send_event('driving-data', 'message', data)

    async def websocket_disconnect(self, event):
        # when websocket disconnects
        pass
