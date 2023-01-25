import hid
#import usb.core
#import serial
import sys
import time

# Reads the ECU device (given the Vendor and Product ID, as below)
serECU = hid.Device(22616, 6)

# Set Verbosity (leave False unless you want to debug)
verbose = False


while 1:
    variables = []
    #time.sleep(0.5)SECUread.py
    rawdata = serECU.read(41)
    #print(rawdata)
    rawprint = int.from_bytes(rawdata, byteorder="big")
    
    
    # Statically mapping bytes as fw revision V1.51
    # * Rotation Per Minute
    rpm=int.from_bytes(rawdata[6:8], byteorder="big")
    variables.append(rpm)
    
    # * Manifold Air Pressure
    map=int.from_bytes(rawdata[8:10], byteorder="big")
    variables.append(map)
    
    # * Throttle Position
    tps=int.from_bytes(rawdata[10:12], byteorder="big")
    variables.append(tps)
    
    # * Engine Temperature
    ect=int.from_bytes(rawdata[12:14], byteorder="big")
    variables.append(ect)
        
    # * Intake Air Temperature
    iat=int.from_bytes(rawdata[14:16], byteorder="big")
    variables.append(iat)
        
    # * Voltage Signal from the Lambda Sensor
    o2s=int.from_bytes(rawdata[16:18], byteorder="big")
    variables.append(o2s)
        
    #Spark Advence, dgree before TDC
    spark=int.from_bytes(rawdata[18:20], byteorder="big")
    variables.append(spark)
    
    #Fuel Pluse Width, Injector #1
    fuelpw1=int.from_bytes(rawdata[20:22], byteorder="big")
    variables.append(fuelpw1)
        
    #Fuel Pulse Width, Injector #2
    fuelpw2=int.from_bytes(rawdata[22:24], byteorder="big")
    variables.append(fuelpw2)
        
    # * Battery Voltage
    ubAdc=int.from_bytes(rawdata[24:26], byteorder="big")
    variables.append(ubAdc)
        
    # * Fuel Level %
    fuelLvl=int.from_bytes(rawdata[26:27], byteorder="big")
    variables.append(fuelLvl)
        
    #Barometric Pressure
    baro=int.from_bytes(rawdata[27:29], byteorder="big")
    variables.append(baro)
        
    # * Fuel Mass Flow Rate, g/min
    fuelCon=int.from_bytes(rawdata[29:31], byteorder="big")
    variables.append(fuelCon)
        
    #Desired RPM from Autopiolt
    drpmFromAPS=int.from_bytes(rawdata[31:33], byteorder="big")
    variables.append(drpmFromAPS)
        
    # * ECU internal state (bit field)
    ecuState=int.from_bytes(rawdata[33:34], byteorder="big")
    variables.append(ecuState)
        
    #ECU Engine Number
    engNum=int.from_bytes(rawdata[34:35], byteorder="big")
    variables.append(engNum)
        
    #Fuel Mass Accumulated (grams)
    mFuel=int.from_bytes(rawdata[35:37], byteorder="big")
    variables.append(mFuel)
        
    #RESERVED
    reserved=int.from_bytes(rawdata[37:39], byteorder="big")
    variables.append(reserved)
        
    #ON time, servo PWM control output (ECU drives servo)
    tOnServoCtrl=int.from_bytes(rawdata[39:41], byteorder="big")
    variables.append(tOnServoCtrl)
        
    print(variables)
    

    # Just for debugging and see all the bytes
    for x in range(128):
        if (verbose and rawdata[x:x+1]!= b''):
            IntConverted = int.from_bytes(rawdata[x:x+1], byteorder="big")
            print("Rawbyte " + str(x) + " = " + str(rawdata[x:x+1]) + "Int = " + str(IntConverted))
