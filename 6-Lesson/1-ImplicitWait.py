import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)    # Implicit wait  applicable all actions

driver.get("https://www.google.com")
driver.maximize_window()

search=driver.find_element(By.NAME,"q")
search.send_keys("Selenium")
search.submit()

# time.sleep()

driver.find_element(By.XPATH,"//h3[text()='Selenium")