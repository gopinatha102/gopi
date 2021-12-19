from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get(" http://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
ele=driver.find_element_by_xpath("//*[@id='authentication']/button")

action=ActionChains(driver)
action.double_click(ele).perform()