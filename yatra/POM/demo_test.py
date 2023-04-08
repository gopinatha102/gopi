import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Demo_test:
    @pytest.mark.skip
    def test_searching_flight_Normal_logic(self):
        depart_from = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(4)
        going_to = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(4)

        search_results = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        for results in search_results:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break

        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
        time.sleep(4)
        all_dates = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for data in all_dates:
            print(data.get_attribute("data-date"))
            if data.get_attribute("data-date") == "18/04/2022":
                data.click()
                time.sleep(4)
                break

        self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
        time.sleep(20)

    @pytest.mark.skip
    def test_searching_flight_Synch_logic(self):
        # Provide going from location
        wait = WebDriverWait(self.driver, 10)
        depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)

        # Provide going to location
        going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        going_to.click()
        time.sleep(2)
        going_to.send_keys("New York")
        search_results = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]")))
        for results in search_results:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()

        # date_origin = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        # self.driver.execute_script("arguments[0].click();", date_origin)
        time.sleep(3)
        all_dates = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))) \
            .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        time.sleep(4)
        for data in all_dates:
            print(data.get_attribute("data-date"))
            if data.get_attribute("data-date") == "18/04/2022":
                data.click()
                time.sleep(4)
                break

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Search Flights']"))).click()
        time.sleep(5)