import random
import time

from django_eventstream import send_event

def emulate_lora():
    while True:
        send_event('driving-data', 'message', {
            'rpm': random.randint(1500, 2500),
            'speed': random.randint(20, 30),
            'voltage': random.random() + 13.5,
            'o2s': random.random() * 0.25 + 0.375,
            'econ': random.random() * 0.25 + 0.375,
            'temp-air': random.randint(95,100),
            'temp-engine': random.randint(205, 215),
        })
        time.sleep(1)
