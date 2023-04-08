import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Demo_Double_click:

    def demo_double_click(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        actionchain = ActionChains(driver)
        double_click_element = driver.find_element(By.XPATH, "//button[contains(text(),'Double-Click Me To See Alert')]")
        actionchain.double_click(double_click_element).perform()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)

auto_suggest = Demo_Double_click()
auto_suggest.demo_double_click()