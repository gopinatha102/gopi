import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Demo_Is_Display:

    def is_display_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        hiden=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(hiden)
        driver.find_element(By.XPATH,"//button[contains(text(),'Toggle Hide and Show')]").click()
        after_hiden_click = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(after_hiden_click)
        driver.close()

obj = Demo_Is_Display()
obj.is_display_demo()