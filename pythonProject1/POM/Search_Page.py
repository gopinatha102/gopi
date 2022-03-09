class Search_Page:
    search = "//input[@id='twotabsearchtextbox']"
    text = "iphone X"
    submit_button = "//input[@type='submit']"
    Today_deal_Check_Box="//span[contains(text(),'Get It by Tomorrow')]"
    Pay_On_Delivery_check_Box = "Eligible for Pay On Delivery"
    Include_Out_of_Stock = "Include Out of Stock"
    Prices = "//span[@class='a-price']"
    save_amount = "//span[contains(text(),'Save ₹3,000')]"
    save_coupon = "//span[contains(text(),' with coupon')]"

    def __init__(self, driver):
        self.driver = driver

    def search_text(self):
        return self.driver.find_element_by_xpath(Search_Page.search)

    def submit(self):
        return self.driver.find_element_by_xpath(Search_Page.submit_button)

    def today_deal_check_box(self):
        return self.driver.find_element_by_xpath(Search_Page.Today_deal_Check_Box)

    def pay_on_delivery_check_box(self):
        return self.driver.find_element_by_link_text(Search_Page.Pay_On_Delivery_check_Box)


    def include_out_of_stock(self):
        return self.driver.find_element_by_link_text(Search_Page.Include_Out_of_Stock)

    def prices(self):
        return self.driver.find_elements_by_xpath(Search_Page.Prices)

    def save_amount_list(self):
        return self.driver.find_elements_by_xpath(Search_Page.save_amount)

    def save_coupon_list(self):
        return self.driver.find_elements_by_xpath(Search_Page.save_coupon)
