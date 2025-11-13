from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pyautogui import screenshot

print('test case 3 je poceo sa izvrsavanjem')

driver = webdriver.Chrome(service=Service('chromedriver.exe'))

driver.maximize_window()

driver.get('https://www.instagram.com/')
print('Instagram stranica je ucitana')

time.sleep(2)

assert driver.title=='Instagram','Title is wrong'
print('naslov stranice je instagram')


screenshot('testcase3.png',region=(0,0,1920,1080))
# driver.save_screenshot('testcase3.png')
print('Skrinsot sacuvan')

driver.minimize_window()
driver.quit()
print('test case 3 je uspesno zavrsen')