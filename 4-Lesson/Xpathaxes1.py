from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# self
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'CarTrade Tech')]/self::a").text
print(text_msg)   # CarTrade Tech

# parent
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'CarTrade Tech')]/parent::td").text
print(text_msg)   # CarTrade Tech

# child
children=driver.find_elements(By.XPATH, "//a[contains(text(),'CarTrade Tech')]/ancestor::tr/child::td")
print(len(children))   # 5
for i in children:
    print(i.text)    # CarTrade Tech  A     637.35     705.50   + 10.69


# ancestor
text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'CarTrade Tech')]/ancestor::tr").text
print(text_msg)   # CarTrade Tech A 637.35 705.50 + 10.69

# descendant
text_msg=driver.find_elements(By.XPATH, "//a[contains(text(),'CarTrade Tech')]/ancestor::tr/descendant::*")
print(len(text_msg))   # 7

# following
text_msg=driver.find_elements(By.XPATH, "//a[contains(text(),'CarTrade Tech')]/ancestor::tr/following::*")
print(len(text_msg))   # 4712

# following-sibling
text_msg=driver.find_elements(By.XPATH, "//a[contains(text(),'CarTrade Tech')]/ancestor::tr/following-sibling::tr")
print(len(text_msg))   # 566

# preceding
text_msg=driver.find_elements(By.XPATH, "//a[contains(text(),'CarTrade Tech')]/ancestor::tr/preceding::*")
print(len(text_msg))   # 319

# following-sibling
text_msg=driver.find_elements(By.XPATH, "//a[contains(text(),'CarTrade Tech')]/ancestor::tr/preceding-sibling::tr")
print(len(text_msg))   # 15



