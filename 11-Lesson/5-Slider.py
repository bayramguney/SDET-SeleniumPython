import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH, "//body//div/span[1]")
max_slider = driver.find_element(By.XPATH, "//body//div/span[2]")

print("Location of sliders before sliding.....")
print(min_slider.location)  # x =59  y = 250
print(max_slider.location)  # x =510  y = 250

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -39, 0)

time.sleep(10)

print("Location of sliders after sliding.....")
print(min_slider.location)  # x =158  y = 250
print(max_slider.location)  # x =510  y = 250
