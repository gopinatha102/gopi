import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Demo_Check_Box:

    def demo_checkbox(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        befor_select = driver.find_element(By.XPATH,
                                           "//a[@title='Non Stop Flights']//i[@class='ico ico-checkbox']").is_selected()
        print(befor_select)
        driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']//i[@class='ico ico-checkbox']").click()
        time.sleep(10)
        after_select = driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").is_selected()
        print(after_select)
        driver.close()

obj = Demo_Check_Box()
obj.demo_checkbox()
