import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

windowid = driver.current_window_handle

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDS = driver.window_handles

# approach 1
parentwindowID = windowIDS[0]
childwindowID = windowIDS[1]
driver.switch_to.window(childwindowID)
print("child : ",driver.title)
driver.switch_to.window(parentwindowID)
print("parent : ",driver.title)

# approach2
for winid in windowIDS:
    driver.switch_to.window(winid)
    print(driver.title)

# closing  specific window
for winid in windowIDS:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM" or driver.title == "OrangeGRM":
        print(driver.title)
        driver.close()

time.sleep(5)