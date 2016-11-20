#setup
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#relay sig pin 11
#button input pin 13
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,0)

#start
status = 0 
try:
    while True:
        input = GPIO.input(13) 


	if input == 1:
            if (status == 1):
	        status = 0
                sleep(0.2)
            elif (status == 0):
                status = 1
                sleep(0.2)
	if status == 1:
	    GPIO.output(11,1)
            sleep(0.1)
        elif status == 0:
            GPIO.output(11,0)
            sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
