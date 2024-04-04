import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# frame i frame or form

driver.find_element(By.XPATH,"//a[contains(text(),'Iframe with in an Iframe')]").click()

outerframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")    # name , id ,index or webelement
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")

time.sleep(5)

driver.switch_to.parent_frame()     # inner to outer





