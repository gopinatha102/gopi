import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Demo_Mouseover:

    def demo_mouse_over(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        more_element = driver.find_element(By.XPATH,"//li[@class='list-more-tab']")
        action_cha = ActionChains(driver)
        action_cha.move_to_element(more_element).perform()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[@id='booking_engine_adventures']").click()
        time.sleep(2)
        driver.close()


auto_suggest = Demo_Mouseover()
auto_suggest.demo_mouse_over()