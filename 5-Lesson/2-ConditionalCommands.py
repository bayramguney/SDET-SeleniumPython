from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# is_displayed
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print(search_box.is_displayed())  # True
# is_enabled
print(search_box.is_enabled())  # True
# is_selected
newsletter = driver.find_element(By.XPATH, "//input[@id='Newsletter']")
print(newsletter.is_selected())  # True
newsletter.click()
print(newsletter.is_selected())  # False
