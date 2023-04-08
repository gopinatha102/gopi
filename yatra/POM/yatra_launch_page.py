import time
from threading import Thread

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Base.Base_driver import BaseDriver


class LaunchPage(BaseDriver):
    Depart_from_field = "//input[@id='BE_flight_origin_city']"
    Going_to_field = "//input[@id='BE_flight_arrival_city']"
    Going_To_Result_Field = "//div[@class='viewport']//div[1]"
    Select_Date_field = "//input[@id='BE_flight_origin_date']"
    All_Dates = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    Search_Button = "//input[@value='Search Flights']"
    Month_selection = "//div[@id='monthWrapper']//div[@id='month-scroll0']//tbody//td[@class!='inActiveTD']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.Depart_from_field)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.Going_to_field)

    def getGoingToResult(self):
        return self.wait_from_presence_of_all_elements(By.XPATH, self.Going_To_Result_Field)

    def getDepatureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.Select_Date_field)

    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.All_Dates)

    def getOnemonthAllDates(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.Month_selection)

    def getSearchButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.Search_Button)

    def enterDepartFromlocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        time.sleep(2)
        self.getGoingToField().send_keys(goingtolocation)
        search_results = self.getGoingToResult()
        for results in search_results:
            if goingtolocation in results.text:
                results.click()
                break

    def enterDepartureDate(self):
        self.getDepatureDateField().click()
        all_dates = self.getAllDatesField().find_elements(By.XPATH, self.All_Dates)
        #all_dates = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//div["
         #                                               "@id='month-scroll0']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            print(date.get_attribute("data-date"))
            date.click()
            time.sleep(5)
            self.getDepatureDateField().click()

    def clicksearch(self):
        self.getSearchButton().click()
        time.sleep(4)










