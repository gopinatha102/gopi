import pytest

from POM.Search_Page import Search_Page
from utilities.BaseClass import Baseclass
import time


class Test_001(Baseclass):

    def test_case(self,getData):
        search = Search_Page(self.driver)
        self.driver.implicitly_wait(10)
        search.search_text().clear()
        search.search_text().send_keys(getData)
        search.submit().click()
        time.sleep(2)
        search.today_deal_check_box().click()
        time.sleep(2)
        search.pay_on_delivery_check_box().click()
        time.sleep(2)
        search.include_out_of_stock().click()
        time.sleep(2)
        l = search.prices()
        print(len(l))
        for i in l:
            if i.text > "₹30000":
                print(i.text)
        save = search.save_amount_list()
        print("*" * 30)
        for m in save:
            print(m.text)
        save_coupon = search.save_coupon_list()
        print("*" * 30)
        for c in save_coupon:
            print(c.text)

        assert len(l) < 20

    @pytest.fixture(params=[("iphone X"), ("Samsung")])
    def getData(self, request):
        return request.param






