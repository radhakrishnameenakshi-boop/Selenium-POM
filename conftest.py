from selenium import webdriver
from time import sleep
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",dest='Br',default="Chrome",choices=["chrome","edge","firefox"])
@pytest.fixture(autouse=True)

def sam(request):
    browser = request.config.getoption("--browser").lower()
    browser1 = request.config.option.Br.lower()
    if browser1 == "chrome":
        driver = webdriver.Chrome()
    elif browser1 == "edge":
        driver = webdriver.Edge()
    elif browser1 == "firefox":
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    sleep(2)
    yield driver
    sleep(2)

    driver.close()