import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Demo_Is_Enable:

    def is_enable_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        befor_enable = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print("Before Enter value text file :", befor_enable)
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("gopi")
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("gopiatha")
        after_enable = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(after_enable)
        driver.find_element(By.XPATH, "//input[@id='login_button']").click()
        time.sleep(10)
        driver.close()


obj = Demo_Is_Enable()
obj.is_enable_demo()