import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

RelayPin = 12

GPIO.setup(RelayPin,GPIO.OUT)

try:
    current_state = GPIO.input(RelayPin)
    if not current_state:
        GPIO.output(RelayPin,1)

    else:
        GPIO.output(RelayPin,0)

except KeyboardInterrupt:
    exit()
