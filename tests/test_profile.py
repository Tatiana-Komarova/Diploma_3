from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *
import allure
import pytest
from locators.profile_page_locators import ProfilePageLocators
from pages.profile_page import ProfilePage
from pages.main_page import MainPage

class TestProfile:
    @allure.title('переход по клику на «Личный кабинет»')
    def test_click_to_profile(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_profile()

        current_url = main_page.get_current_url()

        assert current_url == login_personal_account

    @allure.title('переход в раздел «История заказов»')
    def test_go_to_orders(self, login):
        driver = login
        main_page = MainPage(login)
        main_page.main_page_loading_wait()
        main_page.go_to_profile()
        main_page.go_to_profile()
        profile_page = ProfilePage(login)
        profile_page.go_to_orders()

        current_url = main_page.get_current_url()

        assert current_url == order_story


    @allure.title('выход из аккаунта')
    def test_logout_profile(self, login):
        driver = login
        main_page = MainPage(login)
        main_page.main_page_loading_wait()
        main_page.go_to_profile()
        main_page.go_to_profile()
        profile_page = ProfilePage(login)
        profile_page.wait_for_element(ProfilePageLocators.BUTTON_LOGOUT)
        profile_page.logout_profile()
        WebDriverWait(login, 10).until(EC.url_to_be(login_personal_account))

        current_url = main_page.get_current_url()

        assert current_url == login_personal_account
