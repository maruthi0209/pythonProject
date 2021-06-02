import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(checkboxes))
for box in checkboxes:
    box.click()
    assert box.is_selected()

time.sleep(2)
driver.close()