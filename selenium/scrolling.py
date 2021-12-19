from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(
    executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# scroll Down the pages By  pixels
#driver.execute_script("window.scrollBy(0,2000)", "")

#scroll down page till the element is visible
#flage=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flage)

#scroll Down page Till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")