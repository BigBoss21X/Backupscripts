#to start enumerate over, sudo rm /home/pi/Documents/pic_temp.txt
#** this will start overwriting any pics that exist in Desktop/Pictures dir.

from picamera import PiCamera
from time import sleep
import os
from subprocess import call
import sys
from datetime import datetime
import requests
import os

localuser = os.path.dirname(os.path.realpath(__file__)).split('/')[2]
#current_dir = os.path.dirname(os.path.realpath(__file__))
filename = '/home/' + localuser + '/Documents/instantpic_temp.txt'
integconfig = '/home/' + localuser + '/Desktop/integ.txt'
camera = PiCamera()
camera.rotation = 180
camera.resolution = (1280, 720)

endurl = '/accounts/api/peekin'


def setup2():
    with open(filename,"w") as writefile:
        writefile.write("0")
        writefile.close()
    setup()


def setup():
    if os.path.exists(filename) != 1:
        setup2()
    else:
        global picnum
        global host
        global port
        global server
        picnum = int(open(filename,"r").readlines()[0])    
        with open(integconfig) as integconf:
            contents = integconf.read()
            host = contents.split("\n")[2]
            port = contents.split("\n")[1]
            server = contents.split("\n")[3] + endurl


def loop(picnum):

    try:
            timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = {'host': host, 'timenow': timenow, 'port': port}
            picnum += 1
            camera.annotate_text=str(timenow)
            picfile = '/home/' + localuser + '/Desktop/Pictures/image%s.jpg' % picnum
            camera.capture(picfile)
            with open(filename,"w") as writefile:
                writefile.write(str(picnum))
                writefile.close()

            files = {'file':(picfile, open(picfile, 'rb'))}

            try:
#                print(host,port)
                conn = requests.post(server, data=data, files=files)
            except:
                print "upload failed"
                destroy()
            destroy()
    except:
        destroy()


def destroy():
    sys.exit()


if __name__ == '__main__':
    setup()
    try:
        loop(picnum)
    except KeyboardInterrupt:
        destroy()
