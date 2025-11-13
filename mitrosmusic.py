import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Setup browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.mitrosmusic.com/")
    yield driver
    driver.quit()

# 1. Test da li se otvara početna stranica
def test_homepage_title(driver):
    assert "MitrosMusic" in driver.title

# 2. Test pretrage proizvoda klikom na ikonu lupe
def test_search_product(driver):
    search_icon = driver.find_element(By.CSS_SELECTOR, ".icon-search")
    search_icon.click()
    search_box = driver.find_element(By.NAME, "s")
    search_box.send_keys("gitara")
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".products"))
    )
    assert "gitara" in driver.page_source.lower()

# 3. Test filtera po ceni (samo na listi proizvoda)
def test_price_filter(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    filter_button = driver.find_element(By.CSS_SELECTOR, "select.orderby")
    filter_button.click()
    option = driver.find_element(By.CSS_SELECTOR, "select.orderby option[value='price']")
    option.click()
    assert option.is_selected()

# 4. Test da li link "O nama" radi
def test_about_link(driver):
    about_link = driver.find_element(By.XPATH, "//a[contains(text(),'O nama')]")
    about_link.click()
    WebDriverWait(driver, 10).until(EC.title_contains("O nama"))
    assert "O nama" in driver.title

# 5. Test dodavanja proizvoda u korpu
def test_add_to_cart(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    product = driver.find_element(By.CSS_SELECTOR, ".products .product a")
    product.click()
    add_button = driver.find_element(By.CSS_SELECTOR, "button.single_add_to_cart_button")
    add_button.click()
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-count"))
    )
    assert int(cart_count.text) > 0

# 6. Test uklanjanja proizvoda iz korpe
def test_remove_from_cart(driver):
    driver.get("https://www.mitrosmusic.com/cart/")
    remove_btn = driver.find_element(By.CSS_SELECTOR, ".remove")
    remove_btn.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-empty"))
    )
    assert "korpa je prazna" in driver.page_source.lower()

# 7. Test otvaranja detalja proizvoda
def test_open_product_details(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    product = driver.find_element(By.CSS_SELECTOR, ".products .product a")
    product.click()
    assert "Dodaj u korpu" in driver.page_source

# 8. Test navigacije ka kategoriji gitare
def test_category_navigation(driver):
    category = driver.find_element(By.XPATH, "//a[contains(text(),'Gitare')]")
    category.click()
    assert "gitare" in driver.current_url.lower()

# 9. Test prikaza broja proizvoda u listi
def test_products_count(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    products = driver.find_elements(By.CSS_SELECTOR, ".products .product")
    assert len(products) > 0

# 10. Test pretrage koja ne postoji
def test_search_no_results(driver):
    search_icon = driver.find_element(By.CSS_SELECTOR, ".icon-search")
    search_icon.click()
    search_box = driver.find_element(By.NAME, "s")
    search_box.send_keys("nepostojeci-proizvod")
    search_box.send_keys(Keys.RETURN)
    assert "nije pronađen nijedan proizvod" in driver.page_source.lower()

# 11. Test da li menu radi
def test_menu_navigation(driver):
    menu_item = driver.find_element(By.XPATH, "//a[contains(text(),'Kontakt')]")
    menu_item.click()
    assert "kontakt" in driver.title.lower()

# 12. Test prikaza proizvoda po stranama
def test_pagination(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    next_btn = driver.find_element(By.CSS_SELECTOR, ".next.page-numbers")
    next_btn.click()
    assert "strana" in driver.page_source.lower() or driver.current_url != "https://www.mitrosmusic.com/shop/"

# 13. Test prikaza cene proizvoda
def test_product_price_display(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    product = driver.find_element(By.CSS_SELECTOR, ".products .product a")
    product.click()
    price = driver.find_element(By.CSS_SELECTOR, ".price")
    assert price.text != ""

# 14. Test da li search box može da se resetuje
def test_search_reset(driver):
    driver.get("https://www.mitrosmusic.com/")
    search_icon = driver.find_element(By.CSS_SELECTOR, ".icon-search")
    search_icon.click()
    search_box = driver.find_element(By.NAME, "s")
    search_box.send_keys("gitara")
    search_box.clear()
    assert search_box.text == ""

# 15. Test filtriranja po popularnosti
def test_filter_popularity(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    filter_button = driver.find_element(By.CSS_SELECTOR, "select.orderby")
    filter_button.click()
    option = driver.find_element(By.CSS_SELECTOR, "select.orderby option[value='popularity']")
    option.click()
    assert option.is_selected()

# 16. Test da li se može otvoriti kontakt forma
def test_contact_form(driver):
    contact = driver.find_element(By.XPATH, "//a[contains(text(),'Kontakt')]")
    contact.click()
    form = driver.find_element(By.CSS_SELECTOR, "form.wpcf7-form")
    assert form.is_displayed()

# 17. Test da li breadcrumb radi
def test_breadcrumb(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    product = driver.find_element(By.CSS_SELECTOR, ".products .product a")
    product.click()
    breadcrumb = driver.find_element(By.CSS_SELECTOR, ".woocommerce-breadcrumb")
    assert breadcrumb.is_displayed()

# 18. Test sortiranja proizvoda po nazivu
def test_sort_by_name(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    filter_button = driver.find_element(By.CSS_SELECTOR, "select.orderby")
    filter_button.click()
    option = driver.find_element(By.CSS_SELECTOR, "select.orderby option[value='name']")
    option.click()
    assert option.is_selected()

# 19. Test dodavanja više proizvoda u korpu
def test_add_multiple_products(driver):
    driver.get("https://www.mitrosmusic.com/shop/")
    products = driver.find_elements(By.CSS_SELECTOR, ".products .product a")[:2]
    for product in products:
        product.click()
        add_button = driver.find_element(By.CSS_SELECTOR, "button.single_add_to_cart_button")
        add_button.click()
        driver.back()
    cart_count = driver.find_element(By.CSS_SELECTOR, ".cart-count")
    assert int(cart_count.text) >= 2

# 20. Test da li se može otvoriti strana sa popustom
def test_sale_page(driver):
    sale_link = driver.find_element(By.XPATH, "//a[contains(text(),'Akcija')]")
    sale_link.click()
    assert "akcija" in driver.title.lower()

# ✅ Run with:
# pytest mitrosmusic_tests.py --html=report.html
