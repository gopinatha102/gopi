from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
#driver =webdriver.edge(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\edgedriver_win64\msedgedriver.exe")

#driver =webdriver.edge("./msedgedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
#driver.get("https://www.youtube.com/")
print(driver.current_url)
print(driver.title) #title of broweser
driver.close() # close the browser
