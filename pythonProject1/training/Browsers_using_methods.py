from selenium import webdriver
from selenium.webdriver.common.by import By


class Demo_Browser:

    def max_window(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        driver.close()

    def min_window(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.minimize_window()
        driver.close()

    def refer_window(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.refresh()
        driver.close()

    def url_cuurent_window(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        title = driver.current_url
        print(title)
        driver.close()

    def back_window(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.back()
        driver.close()

    def forward_window(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.forward()
        driver.close()


    def title_window(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        d=driver.title
        print(d)
        driver.close()

    def full_screen(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.fullscreen_window()
        driver.close()

    def quit(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.quit()

browser = Demo_Browser()
browser.max_window()
browser.min_window()
browser.title_window()
browser.refer_window()
browser.back_window()
browser.forward_window()
browser.full_screen()
browser.quit()
browser.url_cuurent_window()