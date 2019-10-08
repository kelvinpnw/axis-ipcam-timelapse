import urllib
import time
#Cameras are formatted as an array, with the first string being the name of the camera and the second being the URL from which to pull JPGs from.
#A folder must exist for each camera to store images in.
cameras=[["camera_1","http://10.9.57.10/axis-cgi/jpg/image.cgi"]]
def getImages():
	for camera in cameras:
		print "Getting image from camera "+camera[0]
		timelapseimage = urllib.URLopener()
		timelapseimage.retrieve(camera[1], camera[0]+"/"+time.strftime("%Y%m%d-%H%M%S")+".jpg")
while True:
	getImages()
	time.sleep(15)