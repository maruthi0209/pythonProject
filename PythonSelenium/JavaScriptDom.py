import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("headless")
#chrome_options.add_argument("")

driver = webdriver.Chrome(PATH, options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click()", shopButton)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

time.sleep(2)
driver.close()