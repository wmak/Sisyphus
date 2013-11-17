import subprocess
import time

while 1:
	hour = time.localtime().tm_hour
	background="file:////home/wmak/Pictures/backgrounds/" + str(hour) + ".jpg"
	subprocess.call(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', background])
	time.sleep(300)