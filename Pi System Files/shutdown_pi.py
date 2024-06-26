#!/bin/python
# Simple script for shutting down the Raspberry Pi at the press of a button.
# by Iderpreet Singh

import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def Shutdown(channel):
    os.system("sudo shutdown -h now")

# Add out function to execute when the button pressed event happens
GPIO.add_event_detect(27 , GPIO.FALLING, callback = Shutdown, bouncetime = 2000)