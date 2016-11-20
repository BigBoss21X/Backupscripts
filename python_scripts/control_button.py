#setup
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,0)

#start
try:
    while True:
        if (GPIO.input(11) == 1):
	    GPIO.output(12,1)
	else:
	    GPIO.output(12,0)

except KeyboardInterrupt:
    GPIO.cleanup()
