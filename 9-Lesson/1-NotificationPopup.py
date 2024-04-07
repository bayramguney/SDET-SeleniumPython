import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")   # disable any notification popups

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=opts)
driver.implicitly_wait(10)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
