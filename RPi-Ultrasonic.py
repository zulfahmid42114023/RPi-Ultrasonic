import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 12
ECHO = 16
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:

 GPIO.output(TRIG, False)
 #print "menunggu"
 #time.sleep(0.5)

 GPIO.output(TRIG, True)
 time.sleep(0.5)
 GPIO.output(TRIG, False)

 while GPIO.input(ECHO) == 0:
  start = time.time()

 while GPIO.input(ECHO) == 1:
  end = time.time()

 duration = end - start
 distance = duration * 17150
 distance = round(distance, 1)
 
# if distance > 20 and distance <30:
 print "jarak = ", distance, "cm"
 # os.system(' fswebcam -r 640*360 /home/zulfahmi/Foto/photo.jpg')
 #time.sleep(0.5)
