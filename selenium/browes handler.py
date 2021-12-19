from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get(" http://demo.guru99.com/popup.php/")
driver.find_element_by_link_text("Click Here").click()
print(driver.current_window_handle)
handle=driver.window_handles
for handles in handle:
    driver.switch_to_window(handles)
    print("Titles of handlers:",driver.title)
driver.quit()
