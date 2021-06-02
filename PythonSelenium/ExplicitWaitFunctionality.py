import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

wait = WebDriverWait(driver, 8)

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input[type='search']").send_keys("be")
time.sleep(4)
#wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='product-action']/button")))
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(buttons))
for button in buttons:
    button.click()
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(2)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
text = driver.find_element_by_css_selector("span[class='promoInfo']").text
print(text)
assert "Code applied" in text


time.sleep(2)
driver.close()