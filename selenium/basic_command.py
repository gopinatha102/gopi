from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Index.html")
print(driver.title)#title of page is display
print(driver.current_url)#current url page is displayed

driver.close()#this command is closed only specied browser is closed
driver.quit()#this command is closed all browser pages closed 