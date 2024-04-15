import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"https://www.dummyticket.com/dummy-ticket-for-visa-application/").click()
countrlist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrlist))

for country in countrlist:
    if country.text == 'India':
        country.click()
        break