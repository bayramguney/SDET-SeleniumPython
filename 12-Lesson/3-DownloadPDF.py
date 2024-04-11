import time

from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\chromedriver.exe")
    # download in desired location
    prefs = {"download.default_directory":location,"plugins.always.open_pdf_externally":True}
    options=webdriver.ChromeOptions()
    options.add_experimental_option("prefs",prefs)
    driver= webdriver.Chrome(service=serv_obj,options=options)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\Drivers\msedgefriver.exe")

    # download in desired location
    prefs = {"download.default_directory":location,"plugins.always.open_pdf_externally":True}
    options=webdriver.EdgeOptions()
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Edge(service=serv_obj,options=options)
    return driver


def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\Drivers\geckofriver.exe")
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    options.set_preference("browser.download.manager.showWhenStarting",False)
    options.set_preference("browser.download.folderList",2) # 0 for desktop 1 for download 2 for desired location
    options.set_preference("browser.download.dir",location)
    options.set_preference("pdfjs.disabled",True)
    driver = webdriver.Firefox(service=serv_obj,options=options)
    return driver

driver = chrome_setup()
driver.implicitly_wait(10)

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[3]/a").click()

time.sleep(30)