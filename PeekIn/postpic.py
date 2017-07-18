#to start enumerate over, sudo rm /home/pi/Documents/pic_temp.txt
#** this will start overwriting any pics that exist in Desktop/Pictures dir.

from picamera import PiCamera
from time import sleep
import os
from subprocess import call
import sys
from datetime import datetime
import requests


current_dir = os.path.dirname(os.path.realpath(__file__))
filename = "/home/master/Documents/instantpic_temp.txt"
camera = PiCamera()
camera.rotation = 180

host = 'biologywatcher.ddns.net'
port = '2122'
server = 'http://integratedtech.ddns.net/accounts/api/peekin'

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
        picnum = int(open(filename,"r").readlines()[0])    

def loop(picnum):
#            uppath = current_dir + "/dropbox_uploader.sh upload "
#    while True:
    try:
            timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = {'host': host, 'timenow': timenow, 'port': port}
            picnum += 1
            camera.annotate_text=str(timenow)
            picfile = '/home/master/Desktop/Pictures/image%s.jpg' % picnum

            camera.capture(picfile)
            with open(filename,"w") as writefile:
                writefile.write(str(picnum))
                writefile.close()

            files = {'file':(picfile, open(picfile, 'rb'))}

            try:
#                call([uppath + picfile + " image" + str(picnum) + ".jpg"],shell=True)
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
