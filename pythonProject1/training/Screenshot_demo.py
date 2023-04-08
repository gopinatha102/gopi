import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Demo_Screenshot:

    def demo_screenshot(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        continue_button = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continue_button.screenshot(".\\test.png")
        continue_button.click()
        driver.get_screenshot_as_file(".\\test2.png")
        driver.save_screenshot(".\\test3.png")
        time.sleep(2)
        driver.close()

auto_suggest = Demo_Screenshot()
auto_suggest.demo_screenshot()
