import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
dropdowns = driver.find_elements_by_id("ctl00_mainContent_ddl_originStation1")
for i in dropdowns:
    print(i.text)
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    print(country.text)
    if country.text == "India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"
time.sleep(2)
driver.close()