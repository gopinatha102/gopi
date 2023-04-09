import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demo_Explicitly_Wait:

    def demo_explicitly_wait(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("BLR")
        depart_from.send_keys(Keys.ENTER)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New")
        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for result in search_result:
            if "New York (JFK)" in result.text:
                result.click()
                break
        #orgin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        #orgin.click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@ id='BE_flight_origin_date']"))).click()
        # driver.find_element(By.XPATH, "//td[@id='08/04/2023']").click()
        all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))).find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        #all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") in "09/04/2023":
                date.click()
                break

demo_obj = Demo_Explicitly_Wait()
demo_obj.demo_explicitly_wait()