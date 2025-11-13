from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('chromedriver.exe')
driver=webdriver.Chrome(service=s) ## Inicijalizujemo Chrome

driver.get('https://www.google.com/') #kazemo browser-u da ode na odredjenu stranicu

driver.close() #gasi google Chrome

