from InstagramAPI import InstagramAPI #https://github.com/LevPasha/Instagram-API-python
from glob import glob
import random
import os
import time
import webbrowser

InstagramAPI = InstagramAPI(<Instadram ID>, <Instadram PW>)
time.sleep(2)
InstagramAPI.login()  # login


time.sleep(1)
files = []
for file in glob('upload/*.jpg'):
	files.append(file)

photo_path = random.choice(files)
caption = "#supreme #supremenyc #automation #objectdetection"
InstagramAPI.uploadPhoto(photo_path, caption=caption)


time.sleep(1)
webbrowser.open('https://www.instagram.com/suprememebot/')
os.remove(photo_path)




