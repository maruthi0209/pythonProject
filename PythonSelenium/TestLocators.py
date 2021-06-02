import time

from selenium import webdriver
#import selenium.webdriver.support.select.Select()

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_css_selector("input[name='name']").send_keys("rahul")
driver.find_element_by_name("email").send_keys("example@abc.com")
driver.find_element_by_xpath("//input[@type='submit']").click()
#message = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']")
message = driver.find_element_by_class_name("alert-success").text
driver.find_element_by_link_text("Shop").click()
time.sleep(2)
driver.back()
driver.find_element_by_xpath("//a[text()='Home']").click()
time.sleep(2)
driver.back()
label = driver.find_element_by_xpath("//div[@class='form-group']/label").text
print(label)
time.sleep(2)
assert "Success" in message
driver.close()