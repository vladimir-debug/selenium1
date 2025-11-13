#za sajt po izboru (bez goriscenja sajta saucedemo ili demoblaze)
#napisati 10 tc koji ce se izvrsavati preko komande sa pytest-om
#na kraju izbaciti izvestaj u html formi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

from time import sleep



def open_browser(url):
    driver = webdriver.Chrome(options=Options(), service=Service())
    driver.get(url)
    driver.maximize_window()
    return driver


def test_otvaranje_pocetne():
    driver = open_browser("https://www.mitrosmusic.com/")
    assert "Mitros Music" in driver.title
    driver.save_screenshot("01_pocetna.png")
    driver.minimize_window()
    driver.close

def test_pretraga_gitara():
    driver = open_browser("https://www.mitrosmusic.com/")
    driver.find_element(By.NAME, "search").send_keys("Gitara ")
    driver.find_element(By.NAME, "search").click()
    sleep(2)
    rezultati = driver.find_elements(By.CSS_SELECTOR, ".product-name ")

    driver.save_screenshot("02_pretraga_gitara.png")
    driver.minimize_window()
    driver.close()


def test_otvaranje_proizvoda():
    driver = open_browser("https://www.mitrosmusic.com/")

    # pretraga
    driver.find_element(By.NAME, "search").send_keys("gitara", Keys.ENTER)

    # čekaj dok se prvi proizvod ne pojavi
    proizvod = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href^='/proizvod/']"))
    )

    print(proizvod.text)  # ispis naziva proizvoda
    driver.quit()

def test_dodavanje_u_korpu():
    driver = open_browser("https://www.mitrosmusic.com/")
    wait = WebDriverWait(driver, 10)

    try:
        # Unos pojma u pretragu
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "search")))
        search_box.send_keys("gitara")
        search_box.submit()

        # Klik na prvi proizvod
        product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-name a")))
        product.click()

        # Dodavanje u korpu
        add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
        add_to_cart.click()

        # Provera korpe
        korpa = wait.until(EC.presence_of_element_located((By.ID, "cart-total"))).text
        assert "1" in korpa or "1 proizvod" in korpa.lower()

        driver.save_screenshot("04_dodavanje_u_korpu.png")

    except TimeoutException as e:

        driver.save_screenshot("greska_timeout.png")

