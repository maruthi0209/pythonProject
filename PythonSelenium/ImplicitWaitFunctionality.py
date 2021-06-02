import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# implicit wait code
driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input[type='search']").send_keys("be")
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(buttons))
for button in buttons:
    button.click()
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
text = driver.find_element_by_css_selector("span[class='promoInfo']").text
print(text)
assert "Code applied" in text


time.sleep(2)
driver.close()