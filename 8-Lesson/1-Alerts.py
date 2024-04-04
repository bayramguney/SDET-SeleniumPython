import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# open alert window
driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Prompt')]").click()
time.sleep(5)
alertWindow = driver.switch_to.alert
print(alertWindow.text)
alertWindow.send_keys("Welcome")
alertWindow.accept()
# alertWindow.dismiss()     # cancel

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(5)
driver.switch_to.alert.accept()




