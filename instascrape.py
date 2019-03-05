from selenium import webdriver
import os
import requests
import time
import subprocess
import sys
import glob
import fnmatch
import os
import downloadimg
import random
from selenium.webdriver.firefox.options import Options


options = Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options)
# driver = webdriver.Firefox()
#StaleElementError -> firefox
def insta_gif(tags): 
##scrape instagram with a tag and download all the images with the size of 293x293
	driver.get('https://www.instagram.com/explore/tags/'+tags+'/')
	#driver.get('https://www.instagram.com/'+tags+'/')

	for x in range(0,1):
		driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
		time.sleep(2)

	images = driver.find_elements_by_css_selector('img')
	url = random.choice(images).get_attribute('src')
	savedname = 'insta/'+str(time.time())+'.jpg'
	try:
		filename = downloadimg.download_file(url,savedname)
		# subprocess.call(['convert',savedname,'-resize','293x293',savedname]) #RESIZING
	except Exception as e:
		print(e)
	driver.quit()


# tag = sys.argv[1] 
# tags = ['glitch','90s','nostalgia']
# insta_gif(tags[random.randint(0,2)]) #90s,nostalgia
insta_gif('glitch')


