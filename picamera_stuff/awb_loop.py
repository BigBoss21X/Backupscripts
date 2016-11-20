from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180


camera.start_preview()



for effect in camera.AWB_MODES:
    
    camera.awb_mode=effect
    camera.annotate_text="Testing AutoWhiteBalance Mode: %s" % effect
    sleep(2.5)
   
camera.stop_preview()
