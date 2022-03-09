from selenium.webdriver.support.ui import Select


class Home_page:
    open_menu = "//button[contains(text(),'Open Menu')]"
    All_items = "//a[contains(text(),'All Items')]"
    Add_cart = "//button[contains(text(),'Add to cart')]"
    cart_list = "//a[@class='shopping_cart_link']"
    remove_cart_list = "//div[text()='Sauce Labs Backpack']/../..//button[text()='Remove']"
    car_total_list = "//div[@class='cart_item']"


    def __init__(self, driver):
        self.driver = driver

    def open_menu_click(self):
        return self.driver.find_element_by_xpath(Home_page.open_menu)

    def All_items_click(self):
        return self.driver.find_element_by_xpath(Home_page.All_items)

    def Add_cart_list(self):
        total = self.driver.find_elements_by_xpath(Home_page.Add_cart)
        return total

    def list_Add_cart(self):
        return self.driver.find_element_by_xpath(Home_page.cart_list)

    def remove_list_cart(self):
        return self.driver.find_element_by_xpath(Home_page.remove_cart_list)

    def total_cart_list(self):
        total_list = self.driver.find_elements_by_xpath(Home_page.car_total_list)
        return total_list



