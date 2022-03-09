import time

from POM.ALL_Modules import Test_All_Modules
from utilities.BaseClass import Baseclass


class Test_case_005(Baseclass):

    def test_all_button(self):
        self.driver.implicitly_wait(10)
        Test = Test_All_Modules(self.driver)
        Test.all_button_click()


