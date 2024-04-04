import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# syntax   https://username:password@the-internet.herokuapp.com/basic_auth


driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

