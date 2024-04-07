import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# find row and column number
noOfRow = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noOfCol = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print("Row : ",noOfRow," Column : ",noOfCol)

# read specific row&column data
data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print("Data : ",data)

# read all the rows and columns data
print("Printing all the rows and columns data")
for r in range(2,noOfRow+1):
    for c in range(1,noOfCol+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='          ')
    print()

# read data based on  condition(list book name whose author is mukesh)
print("\nread data based on  condition(list book name whose author is mukesh)")
for r in range(2,noOfRow+1):
    authorName = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName == 'Mukesh':
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text

        print(bookName,"      ",authorName,"       ",price)



