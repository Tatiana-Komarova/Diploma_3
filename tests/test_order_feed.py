import allure
import pytest
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestOrderFeed:
    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_modal(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order()
        modal = order_feed_page.modal_window_order_open()

        assert modal.is_displayed()


    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_in_feed(self, login):
        driver = login
        main_page = MainPage(login)
        profile_page = ProfilePage(login)
        order_feed_page = OrderFeedPage(login)
        main_page.main_page_loading_wait()
        main_page.go_to_profile()
        profile_page.go_to_orders()
        history_orders = profile_page.get_all_user_order_numbers()

        main_page.go_to_feed()
        main_page.main_page_loading_wait()

        feed_orders = order_feed_page.get_all_orders_numbers()

        missing = set(history_orders) - set(feed_orders)
        assert missing


    @allure.title('при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @pytest.mark.parametrize('ingredient_name', [
        'Флюоресцентная булка R2-D3'])
    def test_new_order_increase_counter_for_all_time(self, login, ingredient_name):
        driver = login
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)
        #получаем исходное значение
        main_page.main_page_loading_wait()
        main_page.go_to_feed()
        order_feed_page.wait_for_counter_all_visible()
        all_before = order_feed_page.total_orders_for_all_time()
        #создаем заказ
        main_page.go_to_constructor()
        main_page.put_ingredient_into_basket(ingredient_name)
        main_page.place_order()
        main_page.wait_for_order_modal()
        main_page.wait_loading_spinner()
        main_page.close_order_modal()
        main_page.main_page_loading_wait()
        main_page.go_to_feed()

        order_feed_page.wait_for_counter_all_visible()
        all_after = order_feed_page.total_orders_for_all_time()

        assert all_after == all_before + 1



    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @pytest.mark.parametrize('ingredient_name', [
        'Флюоресцентная булка R2-D3'])
    def test_new_order_increase_counter_for_today(self, login, ingredient_name):
        driver = login
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)
        # получаем исходное значение
        main_page.main_page_loading_wait()
        main_page.go_to_feed()
        order_feed_page.wait_for_counter_today_visible()
        today_before = order_feed_page.total_orders_for_today()
        # создаем заказ
        main_page.go_to_constructor()
        main_page.put_ingredient_into_basket(ingredient_name)
        main_page.place_order()
        main_page.wait_for_order_modal()
        main_page.wait_loading_spinner()
        main_page.close_order_modal()
        main_page.wait_loading_spinner()
        main_page.go_to_feed()

        order_feed_page.wait_for_counter_today_visible()
        today_after = order_feed_page.total_orders_for_today()

        assert today_after == today_before + 1

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    @pytest.mark.parametrize('ingredient_name', [
        'Флюоресцентная булка R2-D3'])
    def test_new_order_in_modal_in_process(self, login, ingredient_name):
        driver = login
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)
        main_page.main_page_loading_wait()
        main_page.go_to_constructor()
        main_page.put_ingredient_into_basket(ingredient_name)
        main_page.place_order()
        main_page.wait_for_order_modal()
        main_page.wait_loading_spinner()
        order_numb = main_page.get_order_number_from_modal().lstrip('#')
        main_page.close_order_modal()
        main_page.main_page_loading_wait()
        main_page.go_to_feed()
        order_feed_page.wait_for_processing_section_visible()
        order_feed_page.wait_order_number()
        orders_in_process = order_feed_page.get_orders_in_process()
        order_numb_int = int(order_numb)
        orders_int = {int(x) for x in orders_in_process}

        assert order_numb_int in orders_int



