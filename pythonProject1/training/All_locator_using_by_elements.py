import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoElements:

    def locater_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_elements(By.ID, "login-input")
        driver.maximize_window()
        driver.close()

    def locater_by_name_demo(self):

        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_elements(By.NAME, "login-input")
        driver.maximize_window()
        driver.close()

    def locater_by_xpath_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_elements(By.XPATH, "//input[@id='login-input']")
        driver.maximize_window()
        driver.close()

    def locater_by_css_selector_demo(self):
        driver =webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_elements(By.CSS_SELECTOR, "input#login-input")
        driver.maximize_window()
        driver.close()

    def locater_by_link_text_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        driver.find_elements(By.LINK_TEXT, "Hotels")
        time.sleep(4)
        driver.close()

    def locater_by_partial_link_text_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        driver.find_elements(By.PARTIAL_LINK_TEXT, "Hote")
        time.sleep(4)
        driver.close()

    def locater_by_tag_name_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_elements(By.TAG_NAME, "input")
        driver.close()

    def locater_by_class_name(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_elements(By.CLASS_NAME, "email-login-box")
        driver.close()

find_id = DemoElements()
find_id.locater_by_id_demo()
find_id.locater_by_name_demo()
find_id.locater_by_xpath_demo()
find_id.locater_by_css_selector_demo()
find_id.locater_by_link_text_demo()
find_id.locater_by_tag_name_demo()
find_id.locater_by_class_name()