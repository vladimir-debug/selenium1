from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

driver=webdriver.Chrome(options=Options(),service=Service())
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
sleep(1)
driver.find_element(By.CSS_SELECTOR,"input[name='user-name']").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR,"input[name='login-button']").click()
sleep(1)
assert driver.current_url == "https://www.saucedemo.com/inventory.html","login eror"
driver.save_screenshot("screenshot_tc1.png")

driver.minimize_window()
driver.quit()