from time import sleep
import RPi.GPIO as GPIO
import os

RelayPin = 11
MotionPin = 31

current_dir = os.path.dirname(os.path.realpath(__file__))
#wait = int(open(current_dir + "/config.txt","r").readlines()[0])
wait = 10


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MotionPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RelayPin,GPIO.OUT)
    GPIO.output(RelayPin,GPIO.LOW)

def loop():
#    GPIO.add_event_detect(MotionPin, GPIO.RISING, bouncetime=2000, callback=resettimer)  
  while True:
    print "Light off"
    relayoff()
    GPIO.wait_for_edge(MotionPin, GPIO.RISING)
    relayon()
    resettimer()    

#    while True:
#        pass

def cnt(ev=None):
                status = GPIO.input(RelayPin)
                if status == 1:
                    resettimer()
                    
                elif status == 0:
                    relayon()

def resettimer():
    
  localcount = wait
  GPIO.add_event_detect(MotionPin, GPIO.RISING, bouncetime=2000, callback=cnt)
  while True:
    sleep(1)
    localcount -= 1
    print localcount
    if localcount == 0:
#        nomotion()
        return

def nomotion():
#    sleep(wait)
    for i in range(0,wait):

        sleep(1)
        print i
    relayoff()
def relayoff():
    GPIO.output(RelayPin,GPIO.LOW)
    sleep(1)

def relayon():
    GPIO.output(RelayPin,GPIO.HIGH)
    sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':  
        setup()
        try:
                loop()
        except KeyboardInterrupt: 
                destroy()
