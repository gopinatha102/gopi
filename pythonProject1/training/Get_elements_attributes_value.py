from selenium import webdriver
from selenium.webdriver.common.by import By


class Demo_Text:

    def taken_text(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        Actual_text = driver.find_element(By.XPATH, "(//input[@id='BE_flight_flsearch_btn'])[1]").get_attribute("value")
        print(Actual_text)
        driver.close()


obj = Demo_Text()
obj.taken_text()