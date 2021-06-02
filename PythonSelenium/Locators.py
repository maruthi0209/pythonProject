import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
#PATH = "C:\Program Files (x86)\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Chrome(PATH)
#driver = webdriver.Edge(PATH)
driver.get("https://www.google.com/")
#driver.find_element_by_name("q").send_keys("YouTube")
#driver.find_element_by_css_selector("input[name='q']").send_keys("Weather")
driver.find_element_by_xpath("//input[@name='q']").send_keys("Restaurants near me")
driver.find_element_by_link_text("About").click()
#print(driver.find_element_by_xpath("//div[@id='SIvCob']").text)
time.sleep(10)
driver.close()