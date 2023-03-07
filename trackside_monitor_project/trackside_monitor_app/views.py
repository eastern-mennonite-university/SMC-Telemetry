import threading

from django.http import HttpResponse
from django.template import loader

from .background_processes.receive_lora import receive_transmissions
from trackside_monitor_app.models import LoraThread


def validate_db(flag):
    objects = LoraThread.objects.all()
    if objects.count() == 1:
        return
    objects.delete()
    LoraThread(thread_name='lora', thread_flag=flag).save()


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def start_lora(request):
    lora_running = False

    # Check if the lora script is running
    for thread in threading.enumerate():
        if thread.getName() == 'lora':
            lora_running = True
            break

    # Ensure that the thread_flag is set properly
    validate_db(not lora_running)

    if not lora_running:
        lora_thread = LoraThread.objects.get(thread_name='lora')
        lora_thread.thread_flag = False
        lora_thread.save()

        # Start the LoRa reading process in a separate thread
        lora_thread_process = threading.Thread(
            target=receive_transmissions, name='lora', daemon=True)
        lora_thread_process.start()

    return HttpResponse(status=200)


def stop_lora(request):
    validate_db(True)

    lora_thread = LoraThread.objects.get(thread_name='lora')
    lora_thread.thread_flag = True
    lora_thread.save()

    for thread in threading.enumerate():
        if thread.getName() == 'lora':
            while (True):
                if not thread.is_alive():
                    thread.join()
                    break

    return HttpResponse(status=200)
