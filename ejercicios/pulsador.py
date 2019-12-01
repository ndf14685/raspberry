#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(11, GPIO.OUT)


try:
   while True:
      if GPIO.input(3):
         GPIO.output(11, False)
      else:
         GPIO.output(11, True)


except KeyboardInterrupt:
   print ""
   print "-----------------------------------------------------------------------"
   print "Corte por teclado"
#   print "El numero de veces ejecutado es: ", counter
   print "-----------------------------------------------------------------------"




finally:
   print "-----------------------------------------------------------------------"
   print "Cerramos los puertos GPIO"
   print "-----------------------------------------------------------------------"
   GPIO.cleanup() # this ensures a clean exit

