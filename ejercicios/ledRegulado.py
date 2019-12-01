#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

led = GPIO.PWM(11, 100)

try:
   while True:
      led.start(0)
      for i in range(0, 100, 25):
         led.ChangeDutyCycle(i)
         time.sleep(0.5)

except KeyboardInterrupt:
   print ""
   print "-----------------------------------------------------------------------"
   print "Corte por teclado"
   print "-----------------------------------------------------------------------"

finally:
   print "-----------------------------------------------------------------------"
   print "Cerramos los puertos GPIO"
   print "-----------------------------------------------------------------------"
   GPIO.cleanup() # this ensures a clean exit

