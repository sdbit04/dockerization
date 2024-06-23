import time

import pytest
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FfService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from src.login_page import LoginPage
from src.home_page import HomePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser.lower() == "chrome":
        # driver = Chrome(service=ChromeService(ChromeDriverManager().install()))\
        option = webdriver.ChromeOptions()
    else:
        # driver = Firefox(service=FfService(GeckoDriverManager().install()))
        option = webdriver.FirefoxOptions()
    driver = WebDriver(command_executor="http://192.168.1.64:4444", keep_alive=False, options=option)
    yield driver
    driver.quit()


def test_home_page(setup):
    driver = setup
    home_page = HomePage(driver_instance=driver)
    home_page.get_home_page()
    time.sleep(4)
    assert True


def test_login_page(setup):
    driver = setup
    login_page = LoginPage(driver_instance=driver)
    login_page.get_login_page()
    time.sleep(4)
    assert True


def test_home_page_1(setup):
    driver = setup
    home_page = HomePage(driver_instance=driver)
    home_page.get_home_page()
    time.sleep(4)
    assert True


def test_login_page_1(setup):
    driver = setup
    login_page = LoginPage(driver_instance=driver)
    login_page.get_login_page()
    time.sleep(4)
    assert True


