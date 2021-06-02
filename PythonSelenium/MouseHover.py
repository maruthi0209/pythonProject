import time

from selenium import webdriver
from selenium.webdriver import ActionChains

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)

# When i comment this code the double click functionality throws error in action.double_click(double_click_button).perform() line
'''
action.move_to_element(driver.find_element_by_id("mousehover")).perform()
top_option = driver.find_element_by_link_text("Top")
action.move_to_element(top_option).click()
time.sleep(2)

action.move_to_element(driver.find_element_by_id("mousehover")).perform()
reload_option = driver.find_element_by_link_text("Reload")
action.move_to_element(reload_option).click()
'''
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
double_click_button = driver.find_element_by_id("double-click")
action.double_click(double_click_button).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

time.sleep(2)
driver.close()