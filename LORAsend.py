import time
import busio
import serial
from digitalio import DigitalInOut, Direction, Pull

import board
import adafruit_rfm9x
#import importlib

from DGPSread import *
from DECUread import *
#importlib.import_module('DGPSread')
#importlib.import_module('DECUread')


# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None
packet = None
dataNewECU = 0
dataNewGPS = 0

payload_data = dict()

ecu_flag = False

while True:
    ecu_data = ECUdata()
    if ecu_data:
        packet = None
        payload_data.update(ecu_data)
        print('ECU data updated', end=' ')
        print(payload_data)
        ecu_flag = True
        dataNewECU = True
    elif dataNewECU == True:
        dataNewECU = False
        print("ECU is disconnected")
        time.sleep(0.2)
    elif dataNewECU == 0:
        dataNewECU = False
        print("Please connect the ECU")
        time.sleep(0.2)


    time.sleep(0.2)
    if ecu_flag:
        payload = payload_data['rpm'] + ',' + payload_data['fuelCon'] + ',' + payload_data['ect'] + ',' + payload_data['iat'] + ',' + payload_data['o2s'] + ',' + payload_data['ubAdc']
        print(payload)
        rfm9x.send(payload.encode())

    #Logging code
    if dataNewECU == True:
        #print to file
        #DON'T FORGET TO DECODE THE STRINGS
        print
    if dataNewGPS == True:
        #print to file
        print

'''
Extra LoRa Commands: Sending message
check for packet rx
    packet = rfm9x.receive()
    if packet is None:
        print('- Waiting for PXT -')
    else:
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        print("RX: \n")
        print(packet_text)
        time.sleep(1)
'''
