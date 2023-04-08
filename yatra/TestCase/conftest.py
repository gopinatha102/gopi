import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #wait = WebDriverWait(driver,8)
    driver.get("https://www.yatra.com/")
    #driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
    driver.maximize_window()
    request.cls.driver = driver
    #request.cls.wait = wait
    yield
    driver.close()
