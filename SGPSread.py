import serial
import time
serGPS = serial.Serial('/dev/ttyACM0', 9600)

variableGGA = []
variableGSA = []
#variableGSV = []
variableRMC = []
variableVTG = []
go = 0
while go == 0:
    rawdata = serGPS.readline()
    splitdata=rawdata.split(b',')
    time.sleep(0.5)
    
    description = splitdata[0]
    try:
        print(splitdata[6])
    except:
        print("Just Started")

    if description.find(b"GGA") > 0:
        if splitdata[6] == b'0':
            print("NO FIX")
        elif splitdata[6] == b'1':
            go = 1
            print("FIX")
            break
        elif splitdata[6] == b'2':
            go = 1
            print("FIX")
            break
        
        
while go == 1:

    rawdata = serGPS.readline()
    splitdata=rawdata.split(b',')
    time.sleep(0.5)
    
    description = splitdata[0]

    if description.find(b"GGA") > 0:
        #   0         1         2     3     4      5 6 7   8     9   10  11 12 13  14
        #  GNGGA,215018.090,3828.1826,N,07852.6571,W,1,05,2.29,507.3,M,-33.0,M, , *47
    
        prefG= splitdata[0]
        limeG= splitdata[1]
        latiG= splitdata[2]
        hemiNSG= splitdata[3]
        longiG= splitdata[4]
        hemiEWG= splitdata[5]
        quality= splitdata[6]
        numSatView= splitdata[7]
        horiDilute= splitdata[8]
        altitAnt= splitdata[9]
        unitAnt= splitdata[10]
        geoSep= splitdata[11]
        unitSep= splitdata[12]
        ageDiffer= splitdata[13]
        checksumG = splitdata[14]
        
        variableGGA.append([prefG, limeG, latiG, hemiNSG, longiG, hemiEWG, quality,
                        numSatView, horiDilute, altitAnt, unitAnt, geoSep, unitSep,
                        ageDiffer, checksumG])
        print(variableGGA)
        variableGGA.clear()

    elif description.find(b"GSA") > 0:
        #    0   1 2 3  4  5  6   7    8    9    10   11   12   13   14   15   16   17
        #  GPGSA,A,2,30,21,07,01,    ,    ,    ,    ,    ,    ,    ,    ,2.50,2.29,1.00*0A
    
        prefGS= splitdata[0]
        selMode= splitdata[1]
        mode= splitdata[2]
        id1= splitdata[3]
        id2= splitdata[4]
        id3= splitdata[5]
        id4= splitdata[6]
        id5= splitdata[7]
        id6= splitdata[8]
        id7= splitdata[9]
        id8= splitdata[10]
        id9= splitdata[11]
        id10= splitdata[12]
        id11= splitdata[13]
        id12 = splitdata[14]
        pdop = splitdata[15]
        hdop = splitdata[16]
        vdopCheck = splitdata[17]
        
        variableGSA.append([prefGS, selMode, mode, id1, id2, id3, id4, id5, id6, id7, 
                            id8, id9, id10, id11, id12, pdop, hdop, vdopCheck])
        print(variableGSA)
        variableGSA.clear()

    elif description.find(b"RMC") > 0:
        #  0        2     3     4     5     6      7  8     9      10   11 12  13
        #GNRMC,215018.090,A,3828.1826,N,07852.6571,W,0.32,213.34,020222,  ,  ,A*63
        prefR = splitdata[0]
        limeR = splitdata[1]
        stat = splitdata[2]
        latiR = splitdata[3]
        hemiNSR = splitdata[4]
        longiR = splitdata[5]
        hemiEWR = splitdata[6]
        speed = splitdata[7]
        track = splitdata[8]
        date = splitdata[9]
        magVar = splitdata[10]
        ewCheck = splitdata[11]

        variableRMC.append([prefR, limeR, stat, latiR, hemiNSR, longiR, hemiEWR, speed, track, date, magVar, 
                            ewCheck])
        print(variableRMC)
        variableRMC.clear()

    elif description.find(b"VTG") > 0:
        #   0      1   2 3 4  5   6  7   8  9
        # GNVTG,213.34,T, ,M,0.32,N,0.60,K,A*23
        prefV = splitdata[0]
        courseT = splitdata[1]
        refT = splitdata[2]
        courseM = splitdata[3]
        refM = splitdata[4]
        speedK = splitdata[5]
        unitK = splitdata[6]
        speedKH = splitdata[7]
        unitKH = splitdata[8]
        modeCheck = splitdata[9]
        
        variableVTG.append([prefV, courseT, refT, courseM, refM, speedK, unitK, speedKH, unitKH, modeCheck])

        print(variableVTG)
        variableVTG.clear()


#There is an indefinet amount of satalites that it can get, and I have no idea how to loop/make
#multiple variables for each. Will probably leave GSV alone since it's not mission critical

    #elif description.find(b"GPGSV") > 0:
        #    0   1 2 3  4  5   6  7   8  9  10 11 12 13 14  15 16 17 18  19  
        # GPGSV,2,1,06,30,69,269,34,07,65,188,31,21,51,081,31,01,50,136,36*74

    #    while splitdata.find(b'*') < 0:
    #        prefGS= splitdata[0]
    #        messAmou= splitdata[1]
    #        messNum= splitdata[2]
    #        satView= splitdata[3]
    #        satNum= splitdata[4]
    #        elev= splitdata[5]
    #        azimu= splitdata[6]
    #        snr= splitdata[7]
    #        satNum1= splitdata[8]
    #    elev1= splitdata[9]
    #    azimu1= splitdata[10]
    #    snr1= splitdata[11]
    #    satNum2= splitdata[12]
    #    elev2= splitdata[13]
    #    azimu2= splitdata[14]
    #    snr2= splitdata[15]
    #    satNum3= splitdata[16]
    #    elev3= splitdata[17]
    #    azimu3= splitdata[18]
    #    snr3Check = splitdata[19]
    #    
    #    variableGSV.append([prefGS, messAmou, messNum, satNum, elev, azimu, snr, satNum1, elev1, azimu1, snr1,
    #                        satNum2, elev2, azimu2, snr2, satNum3, elev3, azimu3, snr3Check])
    #    print(variableGSV)
    #    variableGSV.clear()       

    #elif description.find(b"GLGSV") > 0:
        #    0   1 2  3  4 5   6  7
        # GLGSV,1,1,01,79,41,113,28*56
    
    #    prefGS= splitdata[0]
    #    messAmou= splitdata[1]
    #    messNum= splitdata[2]
    #    satView= splitdata[3]
    #    satNum= splitdata[4]
    #    elev= splitdata[5]
    #    azimu= splitdata[6]
    #    snrCheck= splitdata[7]
    #    variableGSV.append([prefGS, messAmou, messNum, satNum, elev, azimu, snrCheck])

    #    print(variableGSV)
    #    variableGSV.clear()       
