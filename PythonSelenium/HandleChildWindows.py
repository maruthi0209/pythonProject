import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://the-internet.herokuapp.com/windows")

# implicit wait code
driver.implicitly_wait(8)

driver.find_element_by_link_text("Click Here").click()
parent_window = driver.window_handles[0]
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
child_window_text = driver.find_element_by_tag_name("h3").text
driver.close()
driver.switch_to.window(parent_window)
parent_window_text = driver.find_element_by_tag_name("h3").text
print(child_window_text)
print(parent_window_text)


time.sleep(2)
driver.close()