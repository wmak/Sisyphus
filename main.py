import subprocess
import time
import datetime
import os
from config import parse_config

def change_background():
	hour = time.localtime().tm_hour # get current hour
	picture = os.path.join(path, str(hour) + ".jpg") # get the corresponding picture
	background="file://" + picture
	subprocess.call(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', background]) #Change the picture

if __name__ == "__main__":
	config = parse_config()
	path = config.get("Settings", "image_folder")
	print path
	# main loop
	while 1:
		change_background()
		wait = 60 - datetime.datetime.today().time().minute #Calculate how long to wait
		time.sleep(wait*60)