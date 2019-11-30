#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

for x in range(0,10):
        GPIO.output(11, GPIO.HIGH)
        sleep(1)
        GPIO.output(11,GPIO.LOW)
        sleep(1)
else:
        print 'Programa finalizado ;)'

