import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# login
driver.find_element(By.CSS_SELECTOR, "input[name='username']").clear()
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Admin")
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Admin -- user management -- users
admin = driver.find_element(By.XPATH,"//*[@id='menu_admin-viewAdminModule']/b")
usermgmt = driver.find_element(By.XPATH,"//*[@id='menu_admin-UserManagement']")
users = driver.find_element(By.XPATH,"//*[@id='menu_admin-viewSystemUsers']")

# Mouse hover
act = ActionChains(driver)
act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()