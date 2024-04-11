import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# scroll dow by pixel
driver.execute_script("window.scrollBy(0,5000)","")
value = driver.execute_script("return window.pageYOffset;")
print("Pixel value : ",value)

# scroll till element visible
flag = driver.find_element(By.XPATH,"//img[@alt='Flag of Turkey']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageYOffset;")
print("Pixel value : ",value)

# scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Pixel value : ",value)

# scroll up to starting point
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Pixel value : ",value)