import time
import mysql.connector

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get(
    'https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BS8001.html')
driver.maximize_window()

con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")

curs = con.cursor()
curs.execute("select * from caldata")
for row in curs:
    prin = row[0]
    rate = row[1]
    per1 = row[2]
    per2 = row[3]
    fre = row[4]
    exp_val = row[5]

    # passing data to the application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(prin)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

    perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)

    fredrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    fredrp.select_by_visible_text(fre)

    driver.find_element(By.XPATH, "//form[@id='fdMatVal']/div[2]/a[1]/img").click()  # calculate
    act_val = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # validation
    if float(exp_val) == float(act_val):
        print("test passed")

    else:
        print("test failed")
    driver.find_element(By.XPATH, "//form[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)
con.close()

driver.quit()
