import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com")
driver.maximize_window()

# tag and id
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abs")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abs")     # tag

# tag and class
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("bcd")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys

# tag and attribute
driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal_email']").send_keys("abs")
# driver.find_element(By.CSS_SELECTOR,"[data-testid='royal_email']").send_keys("abs")

# tag ,class and  attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid='royal_email']").send_keys("dse")
# driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid='royal_email']").send_keys("dse")


