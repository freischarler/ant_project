import os
import datetime
from subprocess import Popen
from subprocess import call
import subprocess

class main():
	start_time=1
	end_time=2
	duration=3
	resolution=4
	
	p= subprocess.Popen(['python','/home/pi/Desktop/ant_project/video.py'])
	
	def pressedStopRecord(self):
        	os.system ("sudo pkill -9 -f video.py")
