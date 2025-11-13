from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pyautogui as pg

s=Service('chromedriver.exe')
driver=webdriver.Chrome(service=s) ##inicijalizujemo Chrome

driver.maximize_window()## fullscreen prozora

driver.get('https://www.instagram.com/')##idemo na instagram

time.sleep(2)

assert driver.title == 'Instagram', 'Naslov nije Instagram'
print('Naslov stranice je Instagram')

pg.screenshot('testcase4.png',region=(8,6,244,31))
print('Skrinsot je sacuvan')

driver.minimize_window()
driver.quit()
print('Test Case 4 is passed')

