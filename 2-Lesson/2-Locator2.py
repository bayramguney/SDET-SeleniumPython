import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print("length of slider : ",len(sliders))

links=driver.find_elements(By.TAG_NAME,"a")
print("length of links : ",len(links))