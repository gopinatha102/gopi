from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/delete_customer.php")
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/input").send_keys("gopinatha")
sleep(1)
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]/input[1]").click()
sleep(5)
driver.switch_to_alert().accept() #closed the alert window  used ok button
#driver.switch_to_alert().dismiss()#it is used for cancled button
#sleep(5)
#driver.switch_to_alert().accept()