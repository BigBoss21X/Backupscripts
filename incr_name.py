from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180


camera.start_preview()



for i in range(3):
    
    i = i+1
    camera.annotate_text="Testing %s" % i
    sleep(3)
    camera.capture('/home/pi/CameraTest/image%s.jpg' % i)
camera.stop_preview()
