import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")
print(driver.title)
search = driver.find_element_by_id("pg-6-3")

main = driver.find_elements_by_id("main")
print(main)

time.sleep(10)

driver.close()