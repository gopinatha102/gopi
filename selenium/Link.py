from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links is",len(links))

#link capcture by websit
for link in links:
    print(link.text)

#click link
#driver.find_element(By.LINK_TEXT,"SUPPORT").click()
#partial link text
driver.find_element(By.PARTIAL_LINK_TEXT,"SUP").click()
