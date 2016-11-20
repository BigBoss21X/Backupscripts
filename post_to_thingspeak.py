import httplib, urllib
from time import sleep

readwait = open("/home/pi/RelayTemp/config.txt","r").readlines()[2] 
wait = float(readwait)
key = open("/home/pi/RelayTemp/config.txt","r").readlines()[3].rstrip()

def thermometer():
    while True:
        for line in open("/home/pi/RelayTemp/changelog.txt","r"):
            last = line
        temp = last[11:16]


#        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        params = urllib.urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print temp
            print response.status, response.reason
            data = response.read()
            conn.close()

        except:
            print "connection failed"
        break

if __name__ == '__main__':
    while True:
        thermometer()
        sleep(wait)
