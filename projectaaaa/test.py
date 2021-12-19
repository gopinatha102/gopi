from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
#**************************************dynamically changing******************************************
#driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
#driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")
#driver.find_element_by_xpath("//button[text()='Get New User']").click()
#time.sleep(5)
#first=driver.find_element_by_xpath("//div[@id='loading']//text()[2]//..").text
#first=driver.find_element_by_xpath("//div[contains(text(),'First Name')]").text

#***********************************************Facebook new account creating********************************
driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://en-gb.facebook.com/")
driver.find_element_by_xpath("//a[text()='Create New Account']").click()
#driver.find_element_by_xpath("//div[text()='Date of birth']").click()
#driver.implicitly_wait(5)
#driver.find_element_by_xpath("//a[@id='birthday-help']//i").click()
#text_field=driver.find_element_by_xpath("//div[@class='_9hzn']").text
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[@id='gender-help']//i").click()
var = driver.find_element_by_xpath("//div[@class='_9hzn']//..").text
#print(text_field)

print()
print(var)














