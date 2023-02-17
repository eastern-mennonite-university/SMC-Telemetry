import threading

from django.http import HttpResponse
from django.template import loader

from .background_processes.gauge_test import emulate_lora

def index(request):
    lora_running = False

    for thread in threading.enumerate():
        if thread.getName() == 'lora':
            lora_running = True
            break

    if not lora_running:
        lora_listener = threading.Thread(target=emulate_lora, name='lora', daemon=True)
        lora_listener.start()

    template = loader.get_template('index.html')
    return HttpResponse(template.render())
