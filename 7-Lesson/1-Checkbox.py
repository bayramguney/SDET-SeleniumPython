import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://itera.azurewebsites.net/home/automation")
driver.maximize_window()

# select specific checkbox
driver.find_element(By.XPATH,"//input[@id='monday']").click()

# select all the checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
for checkbox in checkboxes:
    checkbox.click()

# select multiple checkboxes by choice
for checkbox in checkboxes:
    day = checkbox.get_attribute("id")
    if day == 'monday' or day == 'sunday':
        checkbox.click()

# select last 2 checkboxes
for i in range(len(checkboxes)-2,len(checkboxes)):   # range(5,7)     6,7
    checkboxes[i].click()

# select first 2 checkboxes
for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()

# clear all the check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

