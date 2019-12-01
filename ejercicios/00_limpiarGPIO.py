#!/usr/bin/python

import RPi.GPIO as GPIO
#import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

print "Cerramos los puertos GPIO"
GPIO.cleanup() # this ensures a clean exit

