from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.b92.net")
time.sleep(3)

# Prihvatanje kolačića (ako se pojavi)
try:
    cookie_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Prihvatam')]")
    cookie_button.click()
except:
    print("Nema banera za kolačiće.")

# Otvaranje polja za pretragu
try:
    search_icon = driver.find_element(By.CSS_SELECTOR, "button.header__search-toggle")
    search_icon.click()
    time.sleep(1)
except:
    print("Dugme za pretragu nije pronađeno.")

# Unos termina za pretragu
query = input("Unesi temu koju želiš da tražiš na B92 (npr. Novak Đoković): ")

search_input = driver.find_element(By.NAME, "q")
search_input.send_keys(query)
search_input.send_keys(Keys.RETURN)
time.sleep(3)

# Prikaz svih pronađenih vesti
articles = driver.find_elements(By.CSS_SELECTOR, "a.article__link")
print("\nPronađene vesti:")
for i, article in enumerate(articles[:10]):  # prikazuje do 10
    print(f"{i+1}. {article.text}")

# Biranje vesti po želji
choice = int(input("\nIzaberi broj vesti koju želiš da otvoriš: ")) - 1
if 0 <= choice < len(articles):
    articles[choice].click()
    print("✅ Otvorena izabrana vest.")
else:
    print("❌ Pogrešan izbor.")

time.sleep(10)
driver.quit()
