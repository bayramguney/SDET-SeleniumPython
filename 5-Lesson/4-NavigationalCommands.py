import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.amazon.com/")
driver.get("https://www.snapdeal.com/")

driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()





