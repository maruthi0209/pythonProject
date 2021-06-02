import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://the-internet.herokuapp.com/iframe")
# implicit wait code
driver.implicitly_wait(8)

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("body[id='tinymce']").clear()
driver.find_element_by_css_selector("body[id='tinymce']").send_keys("this is a simple text")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)


time.sleep(2)
driver.close()