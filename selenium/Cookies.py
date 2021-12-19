from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")

#capture all the cookies creeated by Browser
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
#add new cookies to the broweser
cokie={'name':'mycookies','value':'123443255'}
driver.add_cookie(cokie)
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#delete cookies
driver.delete_cookie("mycookies")
sleep(3)
cokies=driver.get_cookies()
print(len(cokies))

#delete all cookies]
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
