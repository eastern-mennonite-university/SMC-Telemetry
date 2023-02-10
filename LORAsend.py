'''
Explaining the logic:
When the script tries to call DECU or DGPS, there is an if statement alongside the first call.
This has a counterpart, if you will, in the DECU or DGPS file in the form of a try-except check. This does two things. 
One, the code will not error out if the GPS or ECU is not connected, so you can still get data from one or ther other, 
    or you just know that both aren't working for some reason.
Two, this keeps the script from putting gibberish/the same thing over and over again into the log file.

When the if() statement runs, this will run the depended file. If the command does not throw an except(), the code directly under the if() will run. 
    If the code does throw an except(), it will look to the elif().
There are two elif() statements: one with dataNew***==True and one with dateNew***==0. 
When dataNew is equal to True, the code has run before andthere is data cached in the log string. 
    This elif() will set dataNew to False. 
When dataNew is equal to 0, the code hasn't run yet and there is no data cached. I think this is just an extra catch, so it doesn't error.
'''

#Written by Jacob Hess

import time
import busio
import serial
from digitalio import DigitalInOut, Direction, Pull
import datetime as dt

import board
import adafruit_rfm9x
#import importlib

from DGPSread import *
from DECUread import *
#importlib.import_module('DGPSread')
#importlib.import_module('DECUread')

#Create log file at start
d = dt.combine(dt.date, dt.time)
log = open('{}'.format(d), 'w', encoding="utf-8")

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None
packet = None

#dateNew 'bools' are defined. Quotes because I'm setting it to 0
dataNewECU = 0
dataNewGPS = 0

#logging strings are defined. Need to figure out file naming logic somewhere
logECU = ''
logGPS=''

#Makes sure the GUI knows that there is not a Fix. Should be the default state in GUI.
rfm9x.send(b'NO FIX')

#Start of program
while True:

    #ECU part
    if ECUdata():
        packet = None
        from DECUread import rpm, fuelCon, ect, iat, o2s, ubAdc
        rfm9x.send(rpm.encode() + fuelCon.encode() + ect.encode() + iat.encode() + o2s.encode() + ubAdc.encode())
        logECU = ""
        dataNewECU = True
    elif dataNewECU == True:
        dataNewECU = False
        rfm9x.send(b"EU: ECU disconnected or off")
        print("ECU is disconnected")
        logECU='{}, {}, {}, {}, {}, {}'.format(rpm, fuelCon, ect, iat, o2s, ubAdc)
        time.sleep(0.2)
    elif dataNewECU == 0:
        dataNewECU = False
        rfm9x.send(b"EU: Please connect the ECU")
        print("Please connect the ECU")
        time.sleep(0.2)

    #GPS part
    #dataNew is going to be weird on this one. It is in the go check, because if it isn't the script just thinks the Arduino isn't connected
    #until it gets a fix
    if FixCheck():
        from DGPSread import go
        #Checks for fix
        if go == 0:
            FixCheck()
            print('NO FIX')
            dataNewGPS = True
        else:
            #Once there's a fix, get data from NEMA code
            VTGdata()
            from DGPSread import courseT, courseM, speedKH
            packet = None
            rfm9x.send(courseT + courseM + speedKH)
            sent = True
            logGPS = '{}, {}, {}'.format(courseT, courseM, speedKH)
    elif dataNewGPS == True:
        dataNewGPS = False
        rfm9x.send(b"EA: Arduino disconnected or off")
        time.sleep(0.2)
    elif dataNewGPS == 0:
        dataNewGPS = False
        rfm9x.send(b"EA: Please connect the Arduino")
        print("Please connect the Arduino")
        time.sleep(0.2)       

    time.sleep(0.2)

    #Logging code
    if dataNewECU == True:
        log.write(logECU)
        #print to file
        #DON'T FORGET TO DECODE THE STRINGS
        print
    if dataNewGPS == True:
        log.write(logGPS)
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