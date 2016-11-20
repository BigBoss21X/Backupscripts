#setup
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,0)

#start
status = 0 
try:
    while True:
        input = GPIO.input(11) 


	if input == 1:
            if (status == 1):
	        status = 0
                sleep(0.2)
            elif (status == 0):
                status = 1
                sleep(0.2)
	if status == 1:
	    GPIO.output(12,1)
            sleep(0.1)
            execfile("/home/pi/scripts/piggy_scripts/temperature_onbutton.py")
        elif status == 0:
            GPIO.output(12,0)
            sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
