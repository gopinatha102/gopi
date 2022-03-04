from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


# declare runtime variable browser_name and storing it

def pytest_addoption(parser):
    return parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

"""
# using  multiple browser Code 
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        s = Service("C:\\Users\\DELL\\PycharmProjects\\DemoProject\\Drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
    elif browser_name == "Firefox":
        print("firefox")
        f = Service("C:\\Users\\DELL\\PycharmProjects\\DemoProject\\Drivers\\geckodriver.exe")
        driver = webdriver.Firefox(service=f)
        driver.maximize_window()

    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
"""

@pytest.fixture(scope="class")
def setup(request):
    s = Service("C:\\Users\\DELL\\PycharmProjects\\DemoProject\\Drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()