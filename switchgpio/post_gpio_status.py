from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
import requests
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

localuser = os.path.dirname(os.path.realpath(__file__)).split('/')[2]
integconfig = '/home/' + localuser + '/Desktop/integ.txt'
endurl = '/accounts/api/update_status'
timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open(integconfig) as integconf:
    contents = integconf.read()
    host = contents.split("\n")[2]
    port = contents.split("\n")[1]
    server = contents.split("\n")[3] + endurl


pins = [11,12,13,15,16,18,22,29,31,32,33,35,36,37,38,40]
on_pins = []


for pin in pins:

    GPIO.setup(pin,GPIO.OUT)
    pin_state = GPIO.input(pin)
    if pin_state:
        on_pins.append(pin)

print(on_pins)
dict = {'host': host, 'ping': timenow, 'port': port, 'on_pins': on_pins}

conn = requests.get(server, params=dict)
print(conn.url)







