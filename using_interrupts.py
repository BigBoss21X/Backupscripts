#setup
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,0)

#start
count = 0 
def toggleLEDcallback(channel):
    if (GPIO.input(11)==1):
        GPIO.output(12,0)
    else:
        GPIO.output(12,1)
GPIO.add_event_detect(11, GPIO.RISING, callback=toggleLEDcallback, bouncetime=100)

while 1:
    
    print "The current count is " + str(count)
    sleep(1)
    count += 1







GPIO.cleanup()
