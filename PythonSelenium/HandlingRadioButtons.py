import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radioButtons = driver.find_elements_by_css_selector("input[type='radio']")
print(len(radioButtons))
for button in radioButtons:
    if button.get_attribute("value") == "radio1":
        button.click()
        break

assert radioButtons[0].is_selected()


time.sleep(2)
driver.close()