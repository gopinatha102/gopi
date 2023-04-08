import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Demo_JS:

    def demo_java_scripts(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        parent_handle = driver.current_window_handle
        driver.maximize_window()
        print(parent_handle)
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
        all_hander = driver.window_handles
        print(all_hander) 
        for handle in all_hander:
            if parent_handle != handle:
                driver.switch_to.window(handle)
                time.sleep(5)
                break
        driver.switch_to.window(parent_handle)
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
        time.sleep(2)

auto_suggest = Demo_JS()
auto_suggest.demo_java_scripts()