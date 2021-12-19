from  selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
source_ele=driver.find_element_by_id("box6")
target_ele=driver.find_element_by_xpath("//*[@id='box106']")
action=ActionChains(driver)
action.drag_and_drop(source_ele,target_ele).perform()