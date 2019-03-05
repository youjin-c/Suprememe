from InstagramAPI import InstagramAPI #https://github.com/LevPasha/Instagram-API-python
from glob import glob
import random
import os
import time

InstagramAPI = InstagramAPI(<INSTAGRAM ID>, <INSTAGRAM PW>)
time.sleep(2)
InstagramAPI.login()  # login


time.sleep(1)
files = []
for file in glob('upload/*.jpg'):
	files.append(file)

photo_path = random.choice(files)
caption = "#supreme #supremenyc #automation #ImageAI"
InstagramAPI.uploadPhoto(photo_path, caption=caption)

time.sleep(1)
os.remove(photo_path)




