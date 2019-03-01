import pytest
from selenium import webdriver
import time

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    baseURL = "https://example.com/login"
    if browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running tests on FF")
    else:
        driver = webdriver.Chrome()
        driver.get(baseURL)
        print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver
    exp_date = time.time() + 60000
    cookie_dict = {
        "name": 'cookie_example',
        "value": 'true',
        "path": '/',
        "domain": 'example.com',
        "expires": exp_date
    }
    driver.add_cookie(cookie_dict)
    print("adding necessary cookies")

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")