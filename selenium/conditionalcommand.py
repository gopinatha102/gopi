from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
ele=driver.find_element_by_name("userName")
print(ele.is_displayed()) #return value is true/false based on element staues
print(ele.is_enabled()) #return value true/false

password=driver.find_element_by_name("password")
print(password.is_enabled())
print(password.is_displayed())

submit=driver.find_element_by_name("submit")

ele.send_keys("mercury")
password.send_keys("mercury")
submit.click()
print("*"*30)
link=driver.find_element_by_link_text("Flights").click()
roundtrip_radio=driver.find_element_by_css_selector("input[value='roundtrip'")
print(roundtrip_radio.is_selected())
onewaytrip_radio=driver.find_element_by_css_selector("input[value='oneway'")
print(onewaytrip_radio.is_selected())
#onewaytrip_radio.click()
elem=driver.find_element_by_name("passCount")
drp=Select(elem)

drp.select_by_visible_text("3")