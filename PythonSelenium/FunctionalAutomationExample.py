import time

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
# implicit wait code
driver.implicitly_wait(8)


driver.find_element_by_css_selector("input[type='search']").send_keys("be")
time.sleep(5)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#print(len(buttons))
added_to_cart = []
for button in buttons:
    added_to_cart.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(added_to_cart)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
list_of_tr = driver.find_elements_by_xpath("//p[@class='product-name']")
list_of_items = []
#for tr in list_of_tr:
    #list_of_items.append(tr.text)
    #print(tr.text)
#print(list_of_items)
#for item in list_of_cart_items:
#    print(item.text)
#assert added_to_cart == list_of_items

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
text = driver.find_element_by_css_selector("span[class='promoInfo']").text
print(text)
#assert "Code applied" in text

total_amount = float(driver.find_element_by_xpath("//span[@class='totAmt']").text)
after_discount_amount = float(driver.find_element_by_css_selector("span[class='discountAmt']").text)
#assert total_amount > after_discount_amount

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for i in amounts:
    sum += float(i.text)
assert sum == total_amount


time.sleep(2)
driver.close()