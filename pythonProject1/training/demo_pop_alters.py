import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Demo_JS_Pops:

    def demo_java_pop_alters(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/delete_customer.php")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@name='submit']").click()
        time.sleep(2)
        #driver.switch_to.alert.accept()
        driver.switch_to.alert.dismiss()
        time.sleep(2)
        driver.close()



auto_suggest = Demo_JS_Pops()
auto_suggest.demo_java_pop_alters()
