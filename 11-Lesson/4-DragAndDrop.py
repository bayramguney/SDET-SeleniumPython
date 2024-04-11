import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source = driver.find_element(By.XPATH,"//div[@id='box6']")
target = driver.find_element(By.XPATH,"//div[@id='box106']")

act = ActionChains(driver)
act.drag_and_drop(source,target).perform()    # dtag and drop

time.sleep(10)