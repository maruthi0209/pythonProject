import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
#PATH = "C:\Program Files (x86)\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Chrome(PATH)
#driver = webdriver.Edge(PATH)
#driver.get("https://techwithtim.net")
driver.get("https://www.rahulshettyacademy.com")
print(driver.title)
driver.maximize_window()
print(driver.current_url)
#time.sleep(10)
driver.get("https://rahulshettyacademy.com/blog/")
driver.refresh()
time.sleep(2)
driver.minimize_window()
driver.back()
driver.close()