import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Register").send_keys(Keys.CONTROL+Keys.RETURN)  # open in new tab

# new tab selenium 4
driver.get("https://opencart.com/")
driver.switch_to.new_window('tab')
# driver.switch_to.new_window('window')
driver.get("https://orangehrm.com/")

