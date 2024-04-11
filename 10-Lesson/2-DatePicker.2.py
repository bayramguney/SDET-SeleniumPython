import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Date of Birth

driver.find_element(By.XPATH,"//input[@id='dob']").click()

datepicker_month = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text("Dec")     # month selected

datepicker_year = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
datepicker_year.select_by_visible_text("1990")     # year selected

dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in dates:
    if date.text == "25":
        date.click()
        break

time.sleep(30)