#setup
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,0)

#start 
#not started yet
try:
    


except KeyboardInterrupt:
    GPIO.cleanup()






GPIO.cleanup()
