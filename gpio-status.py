from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
import requests


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
host = 'biologywatcher.ddns.net'
port = '2122'
pins = [7,11,12,13,15,16,18,22,29,31,32,33,35,36,37,38,40]
on_pins = []


for pin in pins:

    GPIO.setup(pin,GPIO.OUT)
    pin_state = GPIO.input(pin)
    if pin_state:
        on_pins.append(pin)

print(on_pins)
dict = {'host': host, 'ping': timenow, 'port': port, 'on_pins': on_pins}

conn = requests.get('http://integratedtech.ddns.net/accounts/api/update_status', params=dict)
print(conn.url)







