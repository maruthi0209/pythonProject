import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(8)
driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text
    if product_name == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_css_selector("input[id='country']").send_keys("ind")
driver.find_element_by_link_text("India").click()
driver.find_element_by_css_selector("div[class='checkbox checkbox-primary'").click()
driver.find_element_by_css_selector("input[type='submit']").click()
message = driver.find_element_by_css_selector("div[class*='alert-success']").text
assert "Success" in message
driver.get_screenshot_as_file("clip.png")

time.sleep(2)
driver.close()
