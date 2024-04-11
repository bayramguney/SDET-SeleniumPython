import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/30/2024")   # mm/dd/yyyy

year = "2025"
month = "May"
day = "05"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/div/a[2]/span").click()   # next arrow
        # driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/div/a[1]/span").click()   # previous arrow

# select day
dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text == day:
        ele.click()
        break
time.sleep(30)
