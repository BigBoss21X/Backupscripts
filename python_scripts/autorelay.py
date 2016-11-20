#setup
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#relay sig pin 11
#button input pin 13
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,0)

global relaystate
relaystate = 0
readfile = "/home/pi/Documents/last_ten_average_temp.txt"
usertemp = raw_input("What temp to switch?")
maxtemp = float("{0:.2f}".format(float(usertemp)))
timetoread = int(raw_input("How long inbetween readings? (secs)"))

def read():
    with open(readfile,"r") as infile:
        try:
            data = [float(n) for n in infile.read().split()]
            latestdata = data[len(data)-1]
        
            return latestdata

        except (IOError, ValueError):
            destroy()
def loop(relaystate):
    while True:
        if read() != None:
            print "Basing action on: %0.2f" % read()
            if read() >= maxtemp:
                if (relaystate == 0):
              
                    relaystate = 1
                    sleep(0.2)
#                    GPIO.output(11,1)
#                    print "Fan on"
                elif (relaystate == 1):
                    relaystate = 1
                    sleep(0.2)
            elif read() <= maxtemp:
                if (relaystate == 1):
                    relaystate = 0
                    sleep(0.2)
#                    GPIO.output(11,0)
#                    print "Fan off"
                elif (relaystate == 0):
                    relaystate = 0
                    sleep(0.2)
            GPIO.output(11,relaystate)       
            sleep(timetoread)
def destroy():
    data = []
#    avgfile.close()
    pass

if __name__ == '__main__':
    try:

        loop(relaystate)
    except KeyboardInterrupt:
        destroy()




#start
#status = 0 
#try:
#    while True:
#        input = GPIO.input(13) 


#	if input == 1:
#            if (status == 1):
#                status = 0
#                sleep(0.2)
#            elif (status == 0):
#                status = 1
#                sleep(0.2)
#	if status == 1:
#            GPIO.output(11,1)
#            sleep(0.1)
#        elif status == 0:
#            GPIO.output(11,0)
#            sleep(0.1)
#except KeyboardInterrupt:
#    GPIO.cleanup()
