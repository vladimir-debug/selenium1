# izabrati sajt koji testiramo i izabrati sajt po izboru koji testiramo
# ispisati test plan od 20 TC sa izabranog sajta
from chromedriver import CHROMEDRV_PATH
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

Keys.ENTER

ActionChains(driver).key_down(Keys.SHIFT).perform()
CHROMEDRV_PATH.get("https://skelligexperience.com/")

