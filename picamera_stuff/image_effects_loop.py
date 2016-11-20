from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180


camera.start_preview()



for effect in camera.IMAGE_EFFECTS:
    
    camera.image_effect=effect
    camera.annotate_text="Testing effect: %s" % effect
    sleep(2.5)
   
camera.stop_preview()
