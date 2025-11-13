from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pyautogui as pg
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service('chromedriver.exe'))

driver.maximize_window()

driver.get('https://www.instagram.com/')
time.sleep(2)

assert driver.title=='Instagram','Naslov nije ispravan'
print('Naslov stranice je Instagram')
pg.screenshot('testcase4.png',region=(0,0,1920,1080))
driver.minimize_window()


driver.quit()
print('Test case 4 passed')