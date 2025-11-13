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

def test_performance_glitch_user():
    driver = open_browser("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR,"input[name='user-name']").send_keys("performance_glitch_user")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[name='login-button']").click()
    sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "login error"
    driver.save_screenshot("performance_glitch_user.png")
    close_browser(driver)

def test_problem_user():
    driver = open_browser("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR,"input[name='user-name']").send_keys("problem_user")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[name='login-button']").click()
    sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "login error"
    driver.save_screenshot("problem_user.png")
    close_browser()

def test_login_standard_user():
    driver = open_browser("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR,"input[name='standard_user']").click()
    driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR,"input[name='login-button']").click()
    sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "login error"
    driver.save_screenshot("login_standard_user.png")
    close_browser(driver)

def test_login_standard_user():
    driver = open_browser("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR,"input[name='majmun_user']").click()
    driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR,"input[name='login-button']").click()
    sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "login error"
    driver.save_screenshot("majmun_user.png")
    close_browser(driver)

def test_login_standard_user():
    driver = open_browser("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "input[name='standard_name']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[name='login-button']").click()
    driver.find_element(By.CSS_SELECTOR,"input[name='Sauce_Labs_Backpack']").click()
    driver.find_element(By.CLASS_NAME, "inventory_item_img").click()

    sleep(1)
    driver.save_screenshot("Sauce_Labs_Backpack.png")


def close_browser(driver):
    driver.quit()
