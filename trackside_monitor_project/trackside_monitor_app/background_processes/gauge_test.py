import random
import time

from trackside_monitor_app.models import LoraThread

from django_eventstream import send_event

def flag_check():
    lora_thread = LoraThread.objects.get(thread_name='lora')
    return lora_thread.thread_flag


def emulate_lora():
    while True:

        send_event('driving-data', 'message', {
            'rpm': random.randint(1500, 2500),
            'speed': random.randint(20, 30),
            'voltage': random.random() + 13.5,
            'o2s': random.random() * 0.25 + 0.375,
            'econ': random.random() * 0.25 + 0.375,
            'temp-air': random.randint(95, 100),
            'temp-engine': random.randint(205, 215),
        })
        time.sleep(1)
        if flag_check():
            break
