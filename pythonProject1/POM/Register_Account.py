from selenium.webdriver.common.action_chains import ActionChains


class Register_Account:
    sign_in_button="//a[@id='nav-link-accountList']"
    email_text = "//input[@name='email']"
    Continue_button = "//input[@id='continue']"
    Details_Button = "//a[@id='remember_me_learn_more_link']"
    Check_box = "//input[@type='checkbox']"
    Text_details_button = "//div[@class='a-popover-content']"

    def __init__(self, driver):
        self.driver = driver

    def register_click_button(self):
        return self.driver.find_element_by_xpath(Register_Account.sign_in_button)

    def email_text_field(self):
        return self.driver.find_element_by_xpath(Register_Account.email_text)

    def continue_button(self):
        return self.driver.find_element_by_xpath(Register_Account.Continue_button)

    def details_Button(self):
        return self.driver.find_element_by_xpath(Register_Account.Details_Button)

    def check_box(self):
        return self.driver.find_element_by_xpath(Register_Account.Check_box)

    def text_details_button(self):
        return self.driver.find_element_by_xpath(Register_Account.Text_details_button)


class Account:
    account_list = "//a[@id='nav-link-accountList']"
    create_wish_list = "//span[contains(text(), 'Create a Wish List')]"
    save_text = "//div[@id='al-intro-benefit-1']"
    next_page_click = "//a[@class='a-carousel-goto-nextpage']"

    def __init__(self, driver):
        self.driver = driver

    def action_chain_function(self):
        m = self.driver.find_element_by_xpath(Account.account_list)
        b = self.driver.find_element_by_xpath(Account.create_wish_list)
        a = ActionChains(self.driver)
        a.move_to_element(m).move_to_element(b).click().perform()
        txt = self.driver.find_element_by_xpath(Account.save_text).text
        page_title = self.driver.title
        return page_title


class Next_Page_click:

    def __init__(self, driver):
        self.driver = driver


    def next_page(self):
        return self.driver.find_element_by_xpath(Account.next_page_click)


