import hid
import sys
import time

# Set Verbosity (leave False unless you want to debug)
verbose = False

serECU = None

def ECUdata():
    global serECU
    try:
        # Reads the ECU device (given the Vendor and Product ID, as below)
        if not serECU:
            serECU = hid.Device(22616,6)
        variables = dict()

        #time.sleep(0.5)
        rawdata = serECU.read(41)

        # Statically mapping bytes as fw revision V1.51
        # * Rotation Per Minute
        rpm=int.from_bytes(rawdata[6:8], byteorder="big")
        rpm=round(rpm*0.25)
        rpm=str(rpm)
        variables['rpm']=rpm

        # * Manifold Air Pressure
        map=int.from_bytes(rawdata[8:10], byteorder="big")
        map=round(map*0.0039)
        map=str(map)
        variables['map']=map

        # * Throttle Position
        tps=int.from_bytes(rawdata[10:12], byteorder="big")
        tps=round(tps*0.0015)
        tps=str(tps)
        variables['tps']=tps

        # * Engine Temperature
        ect=int.from_bytes(rawdata[12:14], byteorder="big")
        ect=round((ect*1.25)+40)
        ect=str(ect)
        variables['ect']=ect

        # * Intake Air Temperature
        iat=int.from_bytes(rawdata[14:16], byteorder="big")
        iat=round((iat*1.35)+40)
        iat=str(iat)
        variables['iat']=iat

        # * Voltage Signal from the Lambda Sensor
        o2s=int.from_bytes(rawdata[16:18], byteorder="big")
        o2s=round(o2s*0.0012)
        o2s=str(o2s)
        variables['o2s']=o2s

        #Spark Advence, dgree before TDC
        spark=int.from_bytes(rawdata[18:20], byteorder="big")
        spark=round(spark*0.75)
        spark=str(spark)
        variables['spark']=spark

        #Fuel Pluse Width, Injector #1
        fuelpw1=int.from_bytes(rawdata[20:22], byteorder="big")
        fuelpw1=round(fuelpw1*0.001)
        fuelpw1=str(fuelpw1)
        variables['fuelpw1']=fuelpw1

        #Fuel Pulse Width, Injector #2
        fuelpw2=int.from_bytes(rawdata[22:24], byteorder="big")
        fuelpw2=round(fuelpw2*0.001)
        fuelpw2=str(fuelpw2)
        variables['fuelpw2']=fuelpw2

        # * Battery Voltage
        ubAdc=int.from_bytes(rawdata[24:26], byteorder="big")
        ubAdc=round(ubAdc*0.00625)
        ubAdc=str(ubAdc)
        variables['ubAdc']=ubAdc

        # * Fuel Level %
        fuelLvl=int.from_bytes(rawdata[26:27], byteorder="big")
        fuelLvl=round(fuelLvl*0.4)
        fuelLvl=str(fuelLvl)
        variables['fuelLvl']=fuelLvl

        #Barometric Pressure
        baro=int.from_bytes(rawdata[27:29], byteorder="big")
        baro=round(baro*0.0039)
        baro=str(baro)
        variables['baro']=baro

        # * Fuel Mass Flow Rate, g/min
        fuelCon=int.from_bytes(rawdata[29:31], byteorder="big")
        fuelCon=round(fuelCon*0.0116)
        fuelCon=str(fuelCon)
        variables['fuelCon']=fuelCon

        #Desired RPM from Autopiolt
        drpmFromAPS=int.from_bytes(rawdata[31:33], byteorder="big")
        drpmFromAPS=round(drpmFromAPS*0.25)
        drpmFromAPS=str(drpmFromAPS)
        variables['drpmFromAPS']=drpmFromAPS

        # * ECU internal state (bit field)
        ecuState=int.from_bytes(rawdata[33:34], byteorder="big")
        ecuState=round(ecuState*1)
        ecuState=str(ecuState)
        variables['ecuState']=ecuState

        #ECU Engine Number
        engNum=int.from_bytes(rawdata[34:35], byteorder="big")
        engNum=round(engNum*1)
        engNum=str(engNum)
        variables['engNum']=engNum

        #Fuel Mass Accumulated (grams)
        mFuel=int.from_bytes(rawdata[35:37], byteorder="big")
        mFuel=str(mFuel)
        variables['mFuel']=mFuel

        #RESERVED
        reserved=int.from_bytes(rawdata[37:39], byteorder="big")
        reserved=str(reserved)
        # variables.append(reserved)

        #ON time, servo PWM control output (ECU drives servo)
        tOnServoCtrl=int.from_bytes(rawdata[39:41], byteorder="big")
        tOnServoCtrl=str(tOnServoCtrl)
        variables['tOnServoCtrl']=tOnServoCtrl

        # Just for debugging and see all the bytes
        for x in range(128):
            if (verbose and rawdata[x:x+1]!= b''):
                IntConverted = int.from_bytes(rawdata[x:x+1], byteorder="big")
                print("Rawbyte " + str(x) + " = " + str(rawdata[x:x+1]) + "Int = " + str(IntConverted))
        return variables
    except hid.HIDException:
        return None
