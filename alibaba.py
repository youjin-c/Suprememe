import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import downloadimg
import subprocess

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

# driver = webdriver.Chrome()
driver.get('https://www.alibaba.com')
#login not required

letters = 'abcdefghijklmnopqrstuvwxyz'

time.sleep(1)
searchbar = driver.find_element_by_css_selector('.ui-searchbar-keyword')
query = random.choice(letters) + random.choice(letters)
searchbar.send_keys(query)
time.sleep(1)

autocompelte = driver.find_elements_by_css_selector('.ui-searchbar-dynamic-item')
random.choice(autocompelte).click()
time.sleep(1)



items = driver.find_elements_by_css_selector("h2 a")
random.choice(items).click()
time.sleep(1)


productimg = driver.find_elements_by_css_selector('img')[0] #'.pic' #'.dot-app-pd img'
url = productimg.get_attribute('src').split(".jpg")[0]+".jpg"

savedname = 'img/'+query+'.jpg'

try:
    filename = downloadimg.download_file(url,savedname)
    # subprocess.call(['convert',savedname,'-resize','293x293',savedname]) #RESIZING

except Exception as e:
    print(e)
driver.quit()
