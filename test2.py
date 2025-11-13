from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


print('test case 2 je poceo sa izvrsvanjem')


driver=webdriver.Chrome(service=Service('chromedriver.exe'))## ovo je skracena inicijalizacija Chrome-a

driver.maximize_window()

driver.get('https://www.google.com/')
print('google Chrome stranica je ucitana')
time.sleep(2)

driver.minimize_window()
driver.quit()
print('test case je uspesno izvrsen')