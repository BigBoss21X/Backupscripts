#setup
from time import sleep
#import datetime
import RPi.GPIO as GPIO
import os
import httplib, urllib
GPIO.setmode(GPIO.BOARD)

readwait = 120
wait = float(readwait)
key = 'T4X6ZKAUDN9HEABD'
ds18b20 = ''

def setup():
        global ds18b20
        for i in os.listdir('/sys/bus/w1/devices'):
                if i != 'w1_bus_master1':
                        ds18b20 = i

def read():
        global ds18b20
        location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
        tfile = open(location)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return temperature


def loop():
    while True:
        if read() != None:
#                    date_time = datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y %H:%M:%S")
                    data = read()
                    post(data)
#                    print(data)
                    sleep(wait)

def post(reading):
    while True:
        temp = reading
        params = urllib.urlencode({'field1': temp, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
#            print temp
#            print response.status, response.reason
            data = response.read()
            conn.close()

#            os.system('/home/pi/pushbullet.sh "Fan turned ON"')

        except:
            print "connection failed"
        break    


def destroy():
    pass


if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
