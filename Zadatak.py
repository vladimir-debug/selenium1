from pyautogui import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep, time

driver= webdriver.Chrome(options=webdriver.ChromeOptions(),service=Service())
driver.maximize_window()
driver.get('//www.b92.net/')

try:
    cookie_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Prihvatam')]")
    cookie_button.click()
except:
    print("Nema banera za kolačiće.")


driver.find_element(By.PARTIAL_LINK_TEXT,'bacio zenu u bunar').click()

driver.minimize_window()
time.sleep(2)
driver.find_element(By.TAG_NAME,'img').click()
driver.find_element(By.TAG_CLASS,'lazyload').click()
driver.quit()

