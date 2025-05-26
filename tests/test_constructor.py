from curl import *
import allure
import pytest
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage
from data import *


class TestConstructor:
    @allure.story('Переход по клику на «Конструктор»')
    def test_click_on_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_profile()
        main_page.go_to_constructor()

        current_url = main_page.get_current_url()

        assert current_url == main_site

    @allure.story('Переход по клику на «Лента заказов»')
    def test_go_to_orders(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_feed()

        current_url = main_page.get_current_url()

        assert current_url == orders

    @allure.story('При клике на ингредиент, появится всплывающее окно с деталями')
    def test_click_on_ingredient_window_open(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        main_page.go_to_constructor()
        main_page.click_on_ingredient(0)
        modal_window = constructor_page.check_window_open()

        assert modal_window.is_displayed()

    @allure.story('всплывающее окно закрывается кликом по крестику')
    def test_window_closed(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        main_page.go_to_constructor()
        main_page.click_on_ingredient(0)
        constructor_page.check_window_open()
        constructor_page.close_window()

        assert constructor_page.check_window_closed()

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @pytest.mark.parametrize("ingredient_name,expected_delta", ingredient_counter_test_data )
    def test_counter_increase(self, driver, ingredient_name, expected_delta):
        main_page = MainPage(driver)
        main_page.go_to_constructor()
        initial_count = main_page.get_counter(ingredient_name)
        main_page.put_ingredient_into_basket(ingredient_name)
        main_page.main_page_loading_wait()
        final_count = main_page.get_counter(ingredient_name)

        assert final_count == initial_count + expected_delta


    @allure.title('залогиненный пользователь может оформить заказ')
    @pytest.mark.parametrize('ingredient_name', ingredient_order_data )
    def test_auth_user_can_do_order(self, driver, login, ingredient_name):
        driver = login
        main_page = MainPage(login)
        main_page.put_ingredient_into_basket(ingredient_name)
        main_page.main_page_loading_wait()
        main_page.place_order()
        modal = main_page.wait_for_order_modal()

        assert modal.is_displayed()

