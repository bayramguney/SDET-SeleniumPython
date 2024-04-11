import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("welcome to selenium")

act = ActionChains(driver)
# select text
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# copy text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# move next window
act.send_keys(Keys.TAB).perform()
# paste text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(10)


