import time

import pytest
from selenium.webdriver.support.ui import Select

from POM.Home__Page import Home_page
from POM.Log_in_Saucedemo import Login
from Test_Data.Home_Page_Data import Home_Page_Data
from utilities.BaseClass import Baseclass


class Test_case_0007(Baseclass):
    @pytest.mark.skip
    def test_login_page(self, getData):
        self.driver.implicitly_wait(10)
        login = Login(self.driver)
        login.log_in_name().clear()
        login.log_in_name().send_keys(getData["user_name"])
        login.log_in_password().clear()
        login.log_in_password().send_keys(getData["password"])
        login.log_in_button().click()

        current_url_txt = self.driver.current_url

        if current_url_txt == "https://www.saucedemo.com/inventory.html":
            print(current_url_txt)
            assert True
        else:
            act_text = login.log_in_error().text
            if act_text == "Epic sadface: Username is required":
                print(act_text)
                assert True
            elif act_text == "Epic sadface: Password is required":
                print(act_text)
                assert True

            elif act_text == "Epic sadface: Username is required":
                print(act_text)
                assert True

            elif act_text == "Epic sadface: Username and password do not match any user in this service":
                print(act_text)
                self.driver.save_screenshot("image1.png")
                assert True

            else:
                self.driver.save_screenshot("image.png")
            self.driver.refresh()

    def test_case_home_page(self):
        self.driver.implicitly_wait(10)
        log = Login(self.driver)
        log.Login_setup()
        """login=Login(self.driver)
        login.log_in_name().send_keys("standard_user")
        login.log_in_password().send_keys("secret_sauce")
        login.log_in_button().click()"""
        home_page = Home_page(self.driver)
        home_page.open_menu_click().click()
        home_page.All_items_click().click()
        Total_list = home_page.Add_cart_list()

        count = 0
        for items in Total_list:
            items.click()
            count += 1
        print(count)
        assert count > 5

    def test_Cart_list(self):
        self.driver.implicitly_wait(10)
        log = Login(self.driver)
        log.Login_setup()
        Cart_list = Home_page(self.driver)
        time.sleep(10)
        Add = Cart_list.Add_cart_list()
        for Add_items in Add:
            Add_items.click()

        Cart_list.list_Add_cart().click()
        time.sleep(10)
        Cart_list.remove_list_cart().click()
        time.sleep(10)
        total_cart_list = Cart_list.total_cart_list()
        count = 0
        for items in total_cart_list:
            count += 1
        count = count + 1
        print(count)
        assert count <= 6

    def test_total_no_items(self):
        log = Login(self.driver)
        log.Login_setup()
        total_no = Login(self.driver)
        total = total_no.total_items_no()
        count = 0
        l = []
        for items in total:
            l.append(items.text)
            count += 1
        print(l)
        assert count >= 5

    # @pytest.fixture(params=Home_Page_Data.getTestData("Testcase4"))
    @pytest.fixture(params=Home_Page_Data.Home_Page_Data)
    def getData(self, request):
        return request.param












