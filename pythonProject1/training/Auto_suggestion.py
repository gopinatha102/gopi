import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Demo_Auto_Suggestion:

    def demo_auto_suggestio(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        depart_from=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("BLR")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)
        going_to = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(5)
        search_result = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for result in search_result:
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(5)
                break

auto_suggest = Demo_Auto_Suggestion()
auto_suggest.demo_auto_suggestio()