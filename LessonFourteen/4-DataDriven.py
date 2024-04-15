import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.select import Select

from LessonFourteen import  ExcelUtil
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get('https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BS8001.html')
driver.maximize_window()

file = "C:\\sdet\\SdetSeleniumPython\\LessonFourteen\\data3.xlsx"
rows = ExcelUtil.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    prin = ExcelUtil.readData(file,"Sheet1",r,1)
    rate = ExcelUtil.readData(file, "Sheet1", r, 2)
    per1 = ExcelUtil.readData(file, "Sheet1", r, 3)
    per2 = ExcelUtil.readData(file, "Sheet1", r, 4)
    fre = ExcelUtil.readData(file, "Sheet1", r, 5)
    exp_val = ExcelUtil.readData(file, "Sheet1", r, 6)

    # passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(prin)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

    perioddrp = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)

    fredrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    fredrp.select_by_visible_text(fre)

    driver.find_element(By.XPATH,"//form[@id='fdMatVal']/div[2]/a[1]/img").click() # calculate
    act_val = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    # validation
    if float(exp_val) == float(act_val):
        print("test passed")
        ExcelUtil.writeData(file,"Sheet1",r,8,'Passed')
        ExcelUtil.fillGreenColor(file,"Sheet1",r,8)
    else:
        ExcelUtil.fillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//form[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)

driver.quit()


