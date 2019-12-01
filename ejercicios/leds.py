#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

counter = 0

try:
   while True:

      print("Prendo Rojo")
      GPIO.output(17, GPIO.HIGH)
      print ("Apago amarillo")
      GPIO.output(27, GPIO.LOW)
      print("Apago Amarillo")
      GPIO.output(22, GPIO.LOW)

      #GPIO.output(11, GPIO.HIGH)
      #GPIO.output(13, GPIO.LOW)
      #GPIO.output(15, GPIO.LOW)
      time.sleep(5)
      print("Apago Rojo")
      GPIO.output(17, GPIO.LOW)
      print ("Prendo amarillo")
      GPIO.output(27, GPIO.HIGH)
      print("Apago Amarillo")
      GPIO.output(22, GPIO.LOW)
 

      #GPIO.output(11, GPIO.LOW)
      #GPIO.output(13, GPIO.HIGH)
      #GPIO.output(15, GPIO.LOW)
      time.sleep(1)
      print("Apago Rojo")
      GPIO.output(17, GPIO.LOW)
      print ("Apago amarillo")
      GPIO.output(27, GPIO.LOW)
      print("Prendo Amarillo")
      GPIO.output(22, GPIO.HIGH)

      #GPIO.output(11, GPIO.LOW)
      #GPIO.output(13, GPIO.LOW)
      #GPIO.output(15, GPIO.HIGH)
      time.sleep(5)
      counter += 1
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.LOW)
      GPIO.output(22, GPIO.LOW)
      time.sleep(1)
      GPIO.output(17, GPIO.HIGH)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.HIGH)
      time.sleep(1)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.LOW)
      GPIO.output(22, GPIO.LOW)
      time.sleep(1)
      print "Target reached: %d" % counter

except KeyboardInterrupt:
   print ""
   print "-----------------------------------------------------------------------"
   print "Corte por teclado"
   print "El numero de veces ejecutado es: ", counter
   print "-----------------------------------------------------------------------"




finally:
   print "Cerramos los puertos GPIO"
   GPIO.cleanup() # this ensures a clean exit
