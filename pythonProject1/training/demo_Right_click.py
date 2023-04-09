import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Demo_Right_click:

    def demo_right_click(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        action = ActionChains(driver)
        element_for_click = driver.find_element(By.XPATH, "//span[contains(text(),'right click me')]")
        action.context_click(element_for_click).perform()
        time.sleep(5)
        driver.close()

auto_suggest = Demo_Right_click()
auto_suggest.demo_right_click()