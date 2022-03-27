import time

import pytest

from POM.Searching_Page import Search_Page
from utilities.BaseClass import Baseclass



class Test(Baseclass):


    def test_01(self):
        search=Search_Page(self.driver)
        search.search_text().send_keys("iphone X")
        search.submit().click()


        #self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("iphone X")

        #self.driver.find_element_by_xpath("//input[@type='submit']").click()

        # driver.find_element_by_link_text("Get It Today").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[contains(text(),'Get It by Tomorrow')]").click()
        # driver.find_element_by_link_text("Today's Deals").click()

        time.sleep(2)
        self.driver.find_element_by_xpath("//li[@id='p_n_specials_match/21618256031']/span/a/div/label/i").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Eligible for Pay On Delivery").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("Include Out of Stock").click()
        time.sleep(2)

        # driver.find_element_by_link_text("Samsung Galaxy M32 5G (Sky Blue, 8GB RAM, 128GB Storage)").click()

        l = self.driver.find_elements_by_xpath("//span[@class='a-price']")
        print(len(l))
        for i in l:
            if i.text > "₹30000":
                print(i.text)
        save = self.driver.find_elements_by_xpath("//span[contains(text(),'Save ₹3,000')]")
        print("*" * 30)
        for m in save:
            print(m.text)
        save_With_cou = self.driver.find_elements_by_xpath("//span[contains(text(), ' with coupon')]")
        print("*" * 30)
        for c in save_With_cou:
            print(c.text)

        assert len(l) < 20
