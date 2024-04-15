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

driver.save_screenshot(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_png()
driver.get_screenshot_as_base64()