import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/login")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("abc.com")
time.sleep(5)
email=driver.find_element(By.XPATH,"//input[@id='Email']").text
print(email)      # None

email=driver.find_element(By.XPATH,"//input[@id='Email']").get_attribute("value")
print(email)    # abc.com

email=driver.find_element(By.XPATH,"//input[@id='Email']").get_attribute("id")
print(email)     # Email








