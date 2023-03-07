import time

from trackside_monitor_app.models import LoraThread

from django_eventstream import send_event

# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None

def flag_check():
    lora_thread = LoraThread.objects.get(thread_name='lora')
    return lora_thread.thread_flag

def receive_transmissions():
    while True:
        packet = rfm9x.receive()
        if packet:
            try:
                packet_data = str(packet, 'utf-8').split(',')
                if packet_data[0] == '1':
                    send_event('driving-data', 'message', {
                        'rpm': int(packet_data[1]),
                        'speed': int(packet_data[7]),
                        'voltage': int(packet_data[6]),
                        'o2s': int(packet_data[5]),
                        'econ': int(packet_data[2]),
                        'temp-air': int(packet_data[4]),
                        'temp-engine': int(packet_data[3]),
                    })
                else:
                    send_event('driving-data', 'message', {
                        'rpm': int(packet_data[1]),
                        'voltage': int(packet_data[6]),
                        'o2s': int(packet_data[5]),
                        'econ': int(packet_data[2]),
                        'temp-air': int(packet_data[4]),
                        'temp-engine': int(packet_data[3]),
                    })
            except UnicodeDecodeError:
                print('UnicodeDecodeError')
                pass
        if flag_check():
            break
