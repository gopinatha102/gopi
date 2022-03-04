class Search_Page:
    search = "//input[@id='twotabsearchtextbox']"
    text = "iphone X"
    submit_button = "//input[@type='submit']"

    def __init__(self, driver):
        self.driver = driver


    def search_text(self):
        return self.driver.find_element_by_xpath(Search_Page.search)

    def submit(self):
        return self.driver.find_element_by_xpath(Search_Page.submit_button)