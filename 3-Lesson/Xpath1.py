import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Absolute xpath
# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("laptop")
# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

# Relative xpath
driver.find_element(By.XPATH,"//input[@id='small-searchterms' and @name='q']").send_keys("Laptop")
driver.find_element(By.XPATH,"//button[@type='submit']")
time.sleep(5)

# //*[contains(@id,'st')
# //*[starts-with(@id,'st')
# //*[ends-with(@id,'op')
# //*[@id='start' or @id='stop']
# //*[text()='stop']
