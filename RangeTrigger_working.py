#setup
from time import sleep
import datetime
import RPi.GPIO as GPIO
import os
import httplib, urllib
dir_path = os.path.dirname(os.path.realpath(__file__))


readwait = open(dir_path + "/config.txt","r").readlines()[2]
wait = float(readwait)

key = open(dir_path + "/config.txt","r").readlines()[3].rstrip()
log = open(dir_path + "/changelog.txt","w")
date_time = datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y %H:%M:%S")
log.write("Range triggered at 00.00 CM " + date_time + "\n")
rangestate = 0
readfile = "/home/pi/Documents/range_median_value.txt"
xrange = open(dir_path + "/config.txt","r").readlines()[0]
maxrange = float(xrange)
toread = open(dir_path + "/config.txt","r").readlines()[1]
timetoread = float(toread)
#global triggeredlast
triggeredlast = 0
def read():
    with open(readfile,"r") as infile:
        try:
            data = [float(n) for n in infile.read().split()]
            latestdata = data[len(data)-1]
        
            return latestdata

        except (IOError, ValueError):
            destroy()

def loop(rangestate):
    while True:
            if read() != None:
                if triggeredlast >= 1:
                    readagain(rangestate)
                else:
                    print "Basing action on: %0.2f" % read()
                    print "Main loop triggeredlast: " + str(triggeredlast)
#            if triggeredlasthour(triggeredlast) >= 1:
#            if triggeredlast == 1:    
#                readagain(rangestate,triggeredlast)
#            else:

                    if read() >= maxrange:
                        if (rangestate == 0):
              
                            rangestate = 1
                            date_time = datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y %H:%M:%S")
                            log.write("Range triggered at " + str(read()) + " CM " + date_time + "\n")
                            log.flush()
                            os.fsync(log)
                            sleep(0.2)
                            poston()

                        elif (rangestate == 1):
                            rangestate = 1
                            sleep(0.2)
                    elif read() <= maxrange:
                        if (rangestate == 1):
                            rangestate = 0
                            date_time = datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y %H:%M:%S")
                            log.write("Range triggered at " + str(read()) + " CM " + date_time + "\n")
                            log.flush()
                            os.fsync(log)
                            sleep(0.2)
                            postoff()


                        elif (rangestate == 0):
                            rangestate = 0
                            sleep(0.2)
#            GPIO.output(11,rangestate)       
                    sleep(timetoread)

def readagain(rangestate):
    while True:
#        for i in range(20):
        global triggeredlast
#            triggered()
        triggeredlast -= 1
        if triggeredlast == 0:
            loop(rangestate)
        else:
            if read() != None:
#            print "Basing action on: %0.2f" % read()
                print read()
                print (read() - read()/10)
                print (read() + read()/10)
                print "triggeredlast: " + str(triggeredlast)
                if (read() - read()/10) >= maxrange:
                    if (rangestate == 0):

                        rangestate = 1
                        date_time = datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y %H:%M:%S")
                        log.write("Range triggered at " + str(read()) + " CM " + date_time + "\n")
                        log.flush()
                        os.fsync(log)
                        sleep(0.2)
                        poston()
                    elif (rangestate == 1):
                        rangestate = 1
                        sleep(0.2)
                elif (read() + read()/10) <= maxrange:
                    if (rangestate == 1):
                        rangestate = 0
                        date_time = datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y %H:%M:%S")
                        log.write("Range triggered at " + str(read()) + " CM " + date_time + "\n")
                        log.flush()
                        os.fsync(log)
                        sleep(0.2)
                        postoff()
                    elif (rangestate == 0):
                        rangestate = 0
                        sleep(0.2)
#            GPIO.output(11,rangestate)       
#            triggeredlast -= 1
#            print triggeredlast
                sleep(timetoread)

#def triggered(triggeredlast):
#    global triggeredlast
#    triggeredlast = 1
#    print triggeredlast

def triggered():
#    for i in range(1,20):
        global triggeredlast
        triggeredlast = 20
        print "Triggered function about to minus 1 from " + str(triggeredlast)

        triggeredlast -= 1
        return triggeredlast

#    else:
#        print "Triggered function returning 0"
#        return 0

def poston():
    while True:
#        for line in open("/home/pi/RelayTemp/changelog.txt","r"):
#            last = line
#        temp = last[11:16]

        temp = 0
#        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        params = urllib.urlencode({'field2': temp, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
#            print temp
#            print response.status, response.reason
            data = response.read()
            conn.close()

            os.system('/home/pi/pushbullet.sh "Water Bucket LOW"')
#            sleep(60)
            global triggeredlast
            triggeredlast = 200 #change for longer buffer/ 7 is ~ 1min
#            print str(triggeredlast)
            triggered()
        except:
            print "connection failed"
        break    

def postoff():
    while True:
#        for line in open("/home/pi/RelayTemp/changelog.txt","r"):
#            last = line
#        temp = last[11:16]

        temp = 1
#        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        params = urllib.urlencode({'field2': temp, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
#            print temp
#            print response.status, response.reason
            data = response.read()
            conn.close()

            os.system('/home/pi/pushbullet.sh "Water Bucket FULL"')
#            sleep(60)
            global triggeredlast
            triggeredlast = 200 #change for longer buffer/ 7 is ~ 1min
            triggered()
#            print str(triggeredlast)
        except:
            print "connection failed"
        break

def destroy():
    data = []
    log.close()
    pass

if __name__ == '__main__':
    try:
#        if triggered() == 0:
            loop(rangestate)
#        elif triggered() >= 1:
#            readagain(rangestate)
    except KeyboardInterrupt:
        destroy()
