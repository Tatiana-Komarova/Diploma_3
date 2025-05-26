import pytest
from selenium import webdriver
from curl import *
from pages.auth_page import AuthPage
from data import Credentials

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login(driver):
    auth_page = AuthPage(driver)
    auth_page.auth(Credentials.email,Credentials.password)

    return driver
