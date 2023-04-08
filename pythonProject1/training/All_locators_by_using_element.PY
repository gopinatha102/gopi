import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoElements:

    def locater_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID, "login-input").send_keys("gopin@gamil.com")
        driver.maximize_window()
        driver.close()

    def locater_by_name_demo(self):

        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.NAME, "login-input").send_keys("gopinarrr@gmail.com")
        driver.maximize_window()
        driver.close()

    def locater_by_xpath_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.XPATH, "//input[@id='login-input']").clear()
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("gopinatha@gggg.com")
        driver.maximize_window()
        driver.close()

    def locater_by_css_selector_demo(self):
        driver =webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR, "input#login-input").clear()
        driver.find_element(By.CSS_SELECTOR, "input#login-input").send_keys("test@test.com")
        driver.maximize_window()
        driver.close()

    def locater_by_link_text_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Hotels").click()
        time.sleep(4)
        driver.close()

    def locater_by_partial_link_text_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        driver.find_element(By.PARTIAL_LINK_TEXT, "Hote").click()
        time.sleep(4)
        driver.close()

    def locater_by_tag_name_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.TAG_NAME, "input").send_keys("test@test.com")
        driver.close()

    def locater_by_class_name(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys("test@test.com")
        driver.close()

find_id = DemoElements()
find_id.locater_by_id_demo()
find_id.locater_by_name_demo()
find_id.locater_by_xpath_demo()
find_id.locater_by_css_selector_demo()
find_id.locater_by_link_text_demo()
find_id.locater_by_tag_name_demo()
find_id.locater_by_class_name()