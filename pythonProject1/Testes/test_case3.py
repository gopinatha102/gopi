import time

import pytest

from POM.Register_Account import Register_Account, Account,Next_Page_click
from utilities.BaseClass import Baseclass


class Test_case_003(Baseclass):

    def test_register_account(self):
        register = Register_Account(self.driver)
        register.register_click_button().click()
        register.email_text_field().send_keys("gopinatha@gmail.com")
        register.continue_button().click()
        register.details_Button().click()
        register.check_box().click()
        time.sleep(5)
        text_details = register.text_details_button().text
        print(text_details)


class Test_Account_004(Baseclass):

    def test_account_list(self):
        account_test = Account(self.driver)
        txt = account_test.action_chain_function()
        assert "Wish List" == txt


class Test_Next(Baseclass):

    def test_next(self):
        test_next_page = Next_Page_click(self.driver)
        count = 0
        for i in range(9):
            test_next_page.next_page().click()
            count = count+1
        print(count)
        assert count <= 9





