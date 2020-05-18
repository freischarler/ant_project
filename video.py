import os
from picamera import PiCamera
from time import sleep
from subprocess import call

#sudo apt-get install gpac


camera=PiCamera()
camera.resolution = (640,480)

camera.crop =(0.0,0.5,0.2,0.2) #crop

#camera.zoom =(0.0,0.0,1.0,1.0) #default(x, y, w, h)
#cant pix / 640 = 0.078
#cant pix / 480 = 0.104



camera.start_preview()
camera.start_recording("pythonVideo.h264")
sleep(5)
camera.stop_recording()
camera.stop_preview()







# The camera is now closed.

print("We are going to convert the video.")
# Define the command we want to execute.
command = "MP4Box -add pythonVideo.h264 convertedVideo.mp4"
# Execute our command
call([command], shell=True)
# Video converted.
print("Video converted.")


#delete file
import os
os.remove("pythonVideo.h264")
print("File Removed!")