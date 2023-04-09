import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class Demo_Implicitly_Wait:

    def demo_implicitly_wait(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        depart_from=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
        driver.implicitly_wait(5)
        depart_from.send_keys("BLR")
        driver.implicitly_wait(5)
        depart_from.send_keys(Keys.ENTER)
        driver.implicitly_wait(5)
        going_to = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        driver.implicitly_wait(3)
        search_result = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for result in search_result:
            if "New York (JFK)" in result.text:
                result.click()
                driver.implicitly_wait(15)
                break

auto_suggest = Demo_Implicitly_Wait()
auto_suggest.demo_implicitly_wait()