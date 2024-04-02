import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

#### install requests module first from setting

alllinks=driver.find_elements(By.TAG_NAME,"a")
count=0

for link in alllinks:
    url=link.get_attribute("href")
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url," is broken")
        count+=1
    else:
        print(url," is valid")
print("number of broken links : ",count)
