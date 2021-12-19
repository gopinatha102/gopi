from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)
time.sleep(5)
driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)
time.sleep(5)
driver.back()
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)
driver.close()