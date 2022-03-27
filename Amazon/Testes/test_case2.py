import time

from POM.Mobiles_list import Mobiles_page
from utilities.BaseClass import Baseclass


class Test_case_0002(Baseclass):

    def test_mobile_click(self):
        global name
        mobile = Mobiles_page(self.driver)

        mobile.mobile_click_button().click()
        mobile.made_Amazon().click()
        mobile.next_function_button().click()
        time.sleep(2)
        mobile.next_function_button().click()
        time.sleep(2)
        mobile.next_function_button().click()
        txt = mobile.current_url()
        assert "Amazon.in: Made for Amazon - Mobiles & Accessories: Electronics" == txt

