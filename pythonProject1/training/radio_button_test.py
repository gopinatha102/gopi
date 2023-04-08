import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Demo_Radio_Button:

    def demo_radio_button(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/radio.html")
        driver.maximize_window()
        befor_select = driver.find_element(By.XPATH, "//input[@id='vfb-7-1']").is_selected()
        print(befor_select)
        driver.find_element(By.XPATH, "//input[@id='vfb-7-1']").click()
        time.sleep(10)
        after_select = driver.find_element(By.XPATH, "//input[@id='vfb-7-1']").is_selected()
        print(after_select)
        driver.close()


obj = Demo_Radio_Button()
obj.demo_radio_button()
