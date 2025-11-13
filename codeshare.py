from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

def open_browser(url):
    driver = webdriver.Chrome(options=Options(), service=Service())
    driver.get(url)
    driver.maximize_window()
    return driver

def test_login_standard_user():
    driver = open_browser("https://saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "input[name='user-name']").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[name='login-button']").click()
    sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login error"
    driver.save_screenshot("login_standard_user.png")
    close_browser(driver)

def test_login_locked_out_user():
    driver = open_browser("https://saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "input[name='user-name']").send_keys("locked_out_user")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[name='login-button']").click()
    sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login error"
    driver.save_screenshot("login_locked_out_user.png")
    close_browser(driver)

def close_browser(driver):
    driver.minimize_window()
    driver.quit()