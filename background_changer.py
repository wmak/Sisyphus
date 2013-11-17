import subprocess
import time
import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read("config.ini")
path = config.get("Settings", "image_folder")

while 1:
	hour = time.localtime().tm_hour
	picture = os.path.join(path, str(hour) + ".jpg")
	background="file:///" + picture
	subprocess.call(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', background])
	time.sleep(300)