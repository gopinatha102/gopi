from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
"""driver.get("http://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10)
assert "Welcome: Mercury Tours" in driver.title
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()"""
#*********************************************************************
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("test")
driver.find_element_by_xpath("//*[@id='nav-search-submit-button']").click()
print(driver.find_element_by_xpath("html/body/div/div[2]/span/div").text)
