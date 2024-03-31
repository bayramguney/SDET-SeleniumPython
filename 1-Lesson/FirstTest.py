# SDET Selenium with python
# https://www.youtube.com/watch?v=2DD-ynCIZ4w&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa
# www.selenium.dev/downloads      for drivers
# download selenium python
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

# serv_obj=Service("C:\Drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.CSS_SELECTOR, "input[name='username']").clear()
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Admin")
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
act_title = driver.title
exp_title = "ORANGEHRM"
if act_title == exp_title:
    print("Login passed")
else:
    print("Login failed")
driver.close()
