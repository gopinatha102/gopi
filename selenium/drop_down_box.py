from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

driver.find_element_by_link_text("REGISTER").click()
driver.maximize_window()
element=driver.find_element(By.NAME,"country")
drp=Select(element)

#select by visible_text
#drp.select_by_visible_text("ANTARCTICA")

#select by index
#drp.select_by_index(4)

#select by value
#drp.select_by_value("AUSTRIA")

#count number of options
#element=drp.options
#print(len(element))

#capture the all options
all_options=drp.options

for options in all_options:
    print(options.text)