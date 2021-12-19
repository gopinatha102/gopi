from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/guru99home/")
driver.switch_to_frame("a077aa5e")
driver.find_element_by_xpath("/html/body/a").click()
driver.switch_to_default_content()