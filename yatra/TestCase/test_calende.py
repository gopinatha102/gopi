import time

import pytest
from selenium.webdriver.common.by import By
from Base.Base_driver import BaseDriver


@pytest.mark.usefixtures("setup")
class Calender(BaseDriver):
    def test_calender_demo(self):
        self.driver.find_element(By.XPATH,"//input[@id='second_date_picker']").click()
        time.sleep(5)
        dates = self.driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//td[contains(@class,'ui-datepicker-other-month ')]")
        print(len(dates))
        for all_dates in dates:
            print(all_dates.text)
            all_dates.click()