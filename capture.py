from picamera import PiCamera
from time import sleep

from PIL import Image, ImageTk
import tkinter as tk

camera = PiCamera()

camera.start_preview()
# Change 300 below to how many images you want captured
for i in range (300):
	# Set sleep time between captures
	sleep(5)
	# Set save directory, this is my local dir on RPi4 Buster
	camera.capture('/home/pi/images/image%s.jpg' % i)
	print('Camera Capturing image%s' % i)
	camera.stop_preview
	
	# Note: You need Direct capture turned OFF for this to work as images and not just show a video window
	window = tk.Tk()
	# 2000 below is how long the window will be open for you to view the image before being destroyed.
	window.after(2000, lambda: window.destroy())
	imagefile = ('/home/pi/images/image%s.jpg' % i)
	img = ImageTk.PhotoImage(Image.open(imagefile))
	lbl = tk.Label(window, image = img).pack()
	window.mainloop()
