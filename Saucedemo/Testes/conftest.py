import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from POM.Log_in_Saucedemo import Login


@pytest.fixture(scope="function", autouse=True)
def setup(request, browser):
    if browser == "Firefox":
        print("Firefox Driver Start Welcome ")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()

    elif browser == "Chrome":
        print("Chrome Driver Start Welcome ")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Chrome(
        #    executable_path="C:\\Users\\DELL\\PycharmProjects\\DemoProject\\Drivers\\chromedriver.exe")
        driver.maximize_window()
    # driver.get(url)
    # driver.get("https://www.amazon.in/")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")





"""
@pytest.fixture(scope="class",autouse=True)
def url(request):
    return request.config.getoption("--url")
"""
