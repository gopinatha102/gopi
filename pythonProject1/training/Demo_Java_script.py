import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Demo_JS:

    def demo_java_scripts(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        continue_button = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        
auto_suggest = Demo_JS()
auto_suggest.demo_java_scripts()