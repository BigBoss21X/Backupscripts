from time import sleep
from datetime import datetime
import requests
import os

wait = 3600
localuser = os.path.dirname(os.path.realpath(__file__)).split('/')[2]
endurl = '/accounts/api/auto_checkin'
integconfig = '/home/' + localuser + '/Desktop/integ.txt'

with open(integconfig) as integconf:
    contents = integconf.read()
    host = contents.split("\n")[2]
    port = contents.split("\n")[1]
    server = contents.split("\n")[3] + endurl


def loop():
        while True:
                ping()
                sleep(wait)


def ping():
        try:
            timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dict = {'host': host, 'ping': timenow, 'port': port}
            conn = requests.get(server, params=dict)

        except:
            pass

def destroy():
        pass


if __name__ == '__main__':
        try:
                loop()
        except KeyboardInterrupt:
                destroy()

