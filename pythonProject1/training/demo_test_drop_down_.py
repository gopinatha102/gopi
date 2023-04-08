import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Demo_Drop_Down:

    def demo_drop_down(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/newtours/register.php")
        drop_down = driver.find_element(By.XPATH,"//select[@name='country']")
        drop_down_obj = Select(drop_down)
        drop_down_obj.select_by_visible_text("ANGOLA")
        time.sleep(10)
        drop_down_obj.select_by_index(2)
        time.sleep(10)
        drop_down_obj.select_by_value("ANTIGUA AND BARBUDA")
        driver.close()

    def demo_drop_down_multi_selection(self):
        driver = webdriver.Chrome()
        driver.get("https://semantic-ui.com/modules/dropdown.html")
        drop_down_element = driver.find_element(By.XPATH, "//div[@class='ui fluid dropdown selection multiple']")
        drop_down_select_obj = Select(drop_down_element)
        drop_down_select_obj.select_by_value("angular")
        time.sleep(2)
        drop_down_select_obj.select_by_index(2)
        time.sleep(5)
        drop_down_select_obj.select_by_visible_text("Information Architecture")
        time.sleep(5)
        drop_down_select_obj.deselect_by_index(2)
        time.sleep(5)
        driver.close()

obj = Demo_Drop_Down()
obj.demo_drop_down_multi_selection()