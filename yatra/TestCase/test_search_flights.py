# import time
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from POM.yatra_launch_page import LaunchPage
import time
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_Case_searching_Flight:

    def test_case_launchpage(self):
        # Provide going from Location
        lp = LaunchPage(self.driver)
        lp.enterDepartFromlocation("New Delhi")

        # Provide going to Location
        lp.enterGoingToLocation("New York")
        lp.getDepatureDateField()
        # Select the departure Data
        for i in range(0,31):
            lp.enterDepartureDate()
            time.sleep(5)
        # month date_selection
        # lp.entermonthDate()

        # click on the search  button
        #lp.clicksearch()

    @pytest.mark.skip
    def test_calender_demo(self):
        self.driver.find_element(By.XPATH, "//input[@id='second_date_picker']").click()
        time.sleep(5)
        dates = self.driver.find_elements(By.XPATH,
                 "//table[@class='ui-datepicker-calendar']//td[not(contains(@class,'ui-datepicker-other-month '))]")
        time.sleep(5)
        print(len(dates))
        for all_dates in dates:
            print("Loop Enter ")
            all_dates.click()
            print(" click is completed  ")
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//input[@id='second_date_picker']").clear()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//input[@id='second_date_picker']").click()
            time.sleep(5)

