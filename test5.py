import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

s=Service('chromedriver.exe')
driver=webdriver.Chrome(service=s)

driver.maximize_window()
print('Test Case 5 je poceo sa izvrsavanjem')

driver.get('https://www.google.com/')
print('Google Chrome stranica je ucitana')
time.sleep(6)

driver.find_element(By.NAME,'q').send_keys('Python')
time.sleep(5)

driver.find_element(By.NAME,'q').send_keys(Keys.ENTER)
time.sleep(4)

driver.save_screenshot('test_case_5.png')

driver.quit()
print('Test Case 5 is passed')