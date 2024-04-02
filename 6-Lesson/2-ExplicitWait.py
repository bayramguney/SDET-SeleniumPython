import time

from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# mywait=WebDriverWait(driver,10)    # Explicit wait    BASIC
mywait = WebDriverWait(driver, 10, poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                       ElementNotVisibleException,
                                                       Exception])

driver.get("https://www.google.com")
driver.maximize_window()

search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium")
search.submit()

# time.sleep()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))

searchlink.click()
