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

#driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q=white+t+shirt&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiOkdDxitDaAhUJsFMKHe8ZCPIQ_AUICigB&biw=1045&bih=810')

ranint = random.randint(0, 30)
driver.execute_script("document.querySelectorAll('.rg_ic.rg_i')[arguments[0]].click()",ranint)
time.sleep(1)



img = driver.find_element_by_css_selector('.irc_mi')
url = img.get_attribute('src')
savedname = 'tshirts/'+str(ranint)+'.jpg'

try:
    filename = downloadimg.download_file(url,savedname)
    # subprocess.call(['convert',savedname,'-resize','293x293',savedname]) #RESIZING

except Exception as e:
    print(e)
driver.quit()
