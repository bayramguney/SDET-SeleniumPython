import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[name='username']").clear()
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Admin")
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a").click()

# number of row
noOfRow = len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div"))
print("Row : ",noOfRow)

count= 0
for r in range(1,noOfRow+1):
    status = driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[5]").text
    if status == 'Enabled':
        count += 1
print("enabled user count : ",count)



