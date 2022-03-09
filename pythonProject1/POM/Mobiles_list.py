class Mobiles_page:
    mobile_click = "Mobiles"
    made_for_Amazon = "//*[@id='s-refinements']/div[2]/ul/li"
    next_button = "//a[contains(text(),'Next')]"


    def __init__(self, driver):
        self.driver = driver

    def mobile_click_button(self):
        return self.driver.find_element_by_link_text(Mobiles_page.mobile_click)

    def made_Amazon(self):
        #return self.driver.find_element_by_link_text(Mobiles_page.made_for_Amazon)
        return self.driver.find_element_by_xpath(Mobiles_page.made_for_Amazon)

    def next_function_button(self):
        return self.driver.find_element_by_xpath(Mobiles_page.next_button)

    def current_url(self):
        return self.driver.title


