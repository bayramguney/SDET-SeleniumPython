import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.maximize_window()

# frame i frame or form

driver.switch_to.frame("packageListFrame")    # name , id ,index or webelement
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()   # go back main page

driver.switch_to.frame("packageFrame")    # name , id ,index or webelement
driver.find_element(By.LINK_TEXT,"Webdriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")    # name , id ,index or webelement
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
