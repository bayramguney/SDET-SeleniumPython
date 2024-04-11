import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@class='uprcse semi-bold']").click()
driver.find_element(By.XPATH,"//*[@id='file-upload']").send_keys("C:\Selenium\sample.pdf")