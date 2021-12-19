from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/write-xpath-table.html")
driver.maximize_window()
rows = len(driver.find_elements_by_xpath("/html/body/center/table/tbody/tr"))  # count no rows in table
cols = len(driver.find_elements_by_xpath("/html/body/center/table/tbody/tr[1]/td"))  # count no columes in table
print(rows)
print(cols)

# read the table data
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        value = driver.find_element_by_xpath("/html/body/center/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end=" ")
    print()