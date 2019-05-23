import time, os, requests, sys, subprocess
from io import BytesIO
from PIL import Image, ImageTk

#GLOBALS	
URL = 'http://srvr-lamp/eboard/?kiosk=Jesse&guid=woohoo&slide=f&reindex=f'

#Functions
def getImg(URL):
	try:
		response = requests.get(URL)
	except:
		print("Error: " + response.status_code + ". Cannot establish connection to the server")
	return response;

def prepImg(response):
	try:
		img = Image.open(BytesIO(response.content))
		img.save("/var/ramdisk/tmp", "jpeg")
	except:
		print("Encountered an error while converting image")
	return;

def displayImg():
	try:
		image = subprocess.Popen(["pqiv", "-fts", "/var/ramdisk/tmp"])
	except:
		print("Encountered an error while displaying image")
	return;

def wait(sec):
	time.sleep(sec)

def loop():
	i = 1
	while i > 0:
		prepImg(getImg(URL))
		wait(30)
		i = i+1
	return;

def cleanup():
	image.terminate()
	image.wait()
	return 0;

prepImg(getImg(URL))
displayImg()
wait(30);
loop()
cleanup()


