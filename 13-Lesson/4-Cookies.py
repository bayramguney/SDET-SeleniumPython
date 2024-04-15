from selenium.webdriver.chrome.service import Service
from selenium import webdriver

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# capture cookies
cookies = driver.get_cookies()
print(len(cookies))   # 3
for cookie in cookies:
    print(cookie)

print(cookies[0].get('name'), "-", cookies[1].get('domain'))  # .Nop.Antiforgery - demo.nopcommerce.com

# add new cookie
driver.add_cookie({"name": "mycookie", "value": "123456"})
cookies = driver.get_cookies()
print(len(cookies))  # 4

# delete specific cookie
driver.delete_cookie("mycookie")
cookies = driver.get_cookies()
print(len(cookies))  # 3

# delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))  # 0
