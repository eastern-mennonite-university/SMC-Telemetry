#SMC RGB Indicator

'''This code provides the conditions for which the LED will change color,
indicating to the driver that they either need to switch the engine on
and accelerate (GREEN) or switch the engine off and coast. This code is
a temporary way to test the conditional statements using the shell, but
will then be modified to show up on the LED itself using the velocity
taken from the GPS.'''

#resistor values
    # R: 100 Ohm
    # G: 220 Ohm
    # B: 220 Ohm
    
#import libraries
import RPi.GPIO as GPIO
import sys
import time

#stop warnings from previous pin settings
GPIO.setwarnings(False)

#set colors to pins
redPin = 36
greenPin = 38
bluePin = 40

#set number of blinks
numBlinks = 10

#set max and min velocities -- need to be changed if v thresholds
#change based on driving strategy
vmax = 20
vmin = 10


##Assign LED Functions

#Function "blink" turns LED on, "turnOff" turns LED off
def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

#assign blinking to colors
def redOn():
    blink(redPin)
    
def redOff():
    turnOff(redPin)
    
def greenOn():
    blink(greenPin)

def greenOff():
    turnOff(greenPin)
    
def blueOn():
    blink(bluePin)

def blueOff():
    turnOff(bluePin)



#Main Loop
while True:
    
    v = float(input("Enter velocity: "))  #set variable input as integer
    
    if v >= vmax:  #condition for upper v threshold
        print(v)
        print("RED")
        for i in range(numBlinks):
            greenOff()
            redOn()
            time.sleep(0.15)
            redOff()
            time.sleep(0.15)
        '''else:
            redOn()'''
            
    elif 0 < v <= vmin:  #condition for lower v threshold
        print(v)
        print("GREEN")
        for i in range(numBlinks):
            redOff()
            greenOn()
            time.sleep(0.15)
            greenOff()
            time.sleep(0.15)
        '''else:
            greenOn()'''
        
else:
    print("While loop false")





