import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_id("name").send_keys("sethu")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
time.sleep(2)
print(alert.text)
assert "Hello sethu" in alert.text
alert.accept()

driver.find_element_by_css_selector("input[id='confirmbtn']").click()
alert2 = driver.switch_to.alert
time.sleep(2)
print(alert2.text)
assert " Are you sure" in alert2.text
alert2.accept()

driver.find_element_by_css_selector("input[id='confirmbtn']").click()
alert3 = driver.switch_to.alert
time.sleep(2)
print(alert3.text)
assert " Are you sure" in alert3.text
alert3.dismiss()

time.sleep(2)
driver.close()