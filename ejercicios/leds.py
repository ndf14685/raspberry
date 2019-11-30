import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

while True:
   GPIO.output(11, GPIO.HIGH)
   GPIO.output(13, GPIO.LOW)
   GPIO.output(15, GPIO.LOW)
   time.sleep(5)
   GPIO.output(11, GPIO.LOW)
   GPIO.output(13, GPIO.HIGH)
   GPIO.output(15, GPIO.LOW)
   time.sleep(1)
   GPIO.output(11, GPIO.LOW)
   GPIO.output(13, GPIO.LOW)
   GPIO.output(15, GPIO.HIGH)
   time.sleep(5)

