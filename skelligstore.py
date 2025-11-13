from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def open_browser(url):
    options = Options()
    driver = webdriver.Chrome(options=options, service=Service())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver

def close_browser(driver):
    driver.quit()

def wait_scroll_click(driver, by, selector, timeout=20):
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, selector)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.execute_script("arguments[0].click();", element)
    return element

def test_1_open_main_page():
    driver = open_browser("https://skelligexperience.com/")
    WebDriverWait(driver, 10).until(lambda d: "Skellig Experience" in d.title)
    driver.save_screenshot("1_main_page.png")
    close_browser(driver)





def test_5_open_product_details():
    driver = open_browser("https://skelligexperience.com/shop/")
    product = wait_scroll_click(driver, By.CSS_SELECTOR, "ul.products li a.woocommerce-LoopProduct-link")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product")))
    driver.save_screenshot("5_product_details.png")
    close_browser(driver)

def test_choose_size():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://skelligexperience.com/product/skellig-beehive-t-shirt-navy/")

    wait = WebDriverWait(driver, 10)
    size_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-selection")))
    size_dropdown.click()
    time.sleep(1)
    option_m = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@id,'select2-pa_size-result') and text()='M']")))
    option_m.click()
    time.sleep(1)
    selected_size = driver.find_element(By.CSS_SELECTOR, ".select2-selection__rendered").text
    assert selected_size == "M", f"Expected size 'M', but got '{selected_size}'"
    close_browser(driver)






def test_choose_color_or_size():
    driver = open_browser("https://skelligexperience.com/shop/")
    product = wait_scroll_click(driver, By.CSS_SELECTOR, "ul.products li a.woocommerce-LoopProduct-link")
    selects = driver.find_elements(By.CSS_SELECTOR, "span.select2-selection")
    if selects:
        selects[0].click()
        option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.select2-results__option")))
        driver.execute_script("arguments[0].scrollIntoView(true);", option)
        driver.execute_script("arguments[0].click();", option)
    driver.save_screenshot("6_choose_option.png")
    close_browser(driver)


def test_add_product_to_cart():
    driver = open_browser("https://skelligexperience.com/shop/")
    product = wait_scroll_click(driver, By.CSS_SELECTOR, "ul.products li a.woocommerce-LoopProduct-link")

    selects = driver.find_elements(By.CSS_SELECTOR, "span.select2-selection")
    for s in selects:
        s.click()
        option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.select2-results__option")))
        driver.execute_script("arguments[0].scrollIntoView(true);", option)
        driver.execute_script("arguments[0].click();", option)
        time.sleep(0.5)
    add_btn = wait_scroll_click(driver, By.NAME, "add-to-cart")
    driver.save_screenshot("7_add_to_cart.png")
    close_browser(driver)

def test_remove_product_from_cart():
    driver = open_browser("https://skelligexperience.com/shop/")
    driver.get("https://skelligexperience.com/cart/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-empty, .cart_item"))
    )
def test_book_a_tour():
    driver = open_browser("https://skelligexperience.com/")
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[4]/div/div/div[1]/div/div/div[7]/a ").click()

def test_add_person():
    driver = open_browser("https://skelligexperience.com/")
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[4]/div/div/div[1]/div/div/div[7]/a ").click()
    driver.find_element(By.CSS_SELECTOR, "#nadults_plus").click()
    time.sleep(4)
    driver.close()
def test_FAQ_s():
    driver = open_browser("https://skelligexperience.com/skellig-experience-about/")
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[1]/h4/a/i").click()
    time.sleep(4)
    driver.close()
def test_Galery():
    driver = open_browser("https://skelligexperience.com/")
    driver.get("https://skelligexperience.com/gallery/")
    EC.presence_of_element_located((By.CLASS_NAME,"gallery"))
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[4]/div[1]/div/div/a").click()
    time.sleep(4)
    driver.close()
def test_contact_page():
    driver = open_browser("https://skelligexperience.com/")
    driver.get("https://skelligexperience.com/skellig-experience-contact-us/")
    time.sleep(4)
    wait = WebDriverWait(driver, 10)

    name_field = wait.until(EC.visibility_of_element_located((By.ID, "input_1_1")))
    name_field.send_keys("Vladimir Bogosavljević")

    email_field = driver.find_element(By.ID, "input_1_3")
    email_field.send_keys("vladimir@example.com")

    message_field = driver.find_element(By.ID, "input_1_4")
    message_field.send_keys("Pozdrav!Testiramo ispis poruke.")

    time.sleep(7)
    driver.close()
def test_instagram():
    driver = open_browser("https://skelligexperience.com/")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    driver.find_element(By.CLASS_NAME, "fa-instagram").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-instagram")))
    time.sleep(9)
    driver.close()

def test_facebook_page():
    driver = open_browser("https://skelligexperience.com/")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    driver.find_element(By.CLASS_NAME, "fa-facebook").click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-facebook")))
    time.sleep(9)
    driver.close()
def test_twitter_page():
    driver = open_browser("https://skelligexperience.com/")
    driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "fa-twitter").click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-twitter")))
    time.sleep(9)
    driver.close()
def test_privacy_policy_page():
    driver = open_browser("https://skelligexperience.com/")
    driver.get("https://skelligexperience.com/privacy-policy/")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.close()
def test_proceed_checkout():
    driver = open_browser("https://skelligexperience.com/")
    driver.get("https://skelligexperience.com/shop/")
    wait = WebDriverWait(driver, 15)
    product = wait.until( EC.element_to_be_clickable((By.CSS_SELECTOR, "a.woocommerce-LoopProduct-link.woocommerce-loop-product__link")))
    product.click()
    dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select2-selection")))
    dropdown.click()
    size_m = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'M')]")))

    size_m.click()
    time.sleep(6)
    driver.quit()