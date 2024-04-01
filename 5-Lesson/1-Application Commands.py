from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

# get
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# title
print(driver.title)

# current URL
print(driver.current_url)

# page source
print(driver.page_source)

