from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpdwnctry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
drpdwnctry=Select(drpdwnctry_ele)

# select option from dropdown
drpdwnctry.select_by_visible_text("India")
drpdwnctry.select_by_value("10")
drpdwnctry.select_by_index(13)

# capture all options and print
alloptions=drpdwnctry.options
print(len(alloptions))
for option in alloptions:
    print(option.text)

# select option from dropwown without built in method
for option in alloptions:
    if option.text == "India":
        option.click()
        break


# without using select clas
alloptions=driver.find_elements(By.XPATH,"//*[@id='input-country']/option")
print(len(alloptions))