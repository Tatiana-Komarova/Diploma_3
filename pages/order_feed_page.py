import allure
from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    @allure.step('Открыть детали заказа')
    def open_order(self):
        self.click_on_element(OrderFeedPageLocators.LAST_ORDER)

    @allure.step('Получить "За все время выполнено"')
    def total_orders_for_all_time(self):
        return int(self.find_element(OrderFeedPageLocators.COUNT_DONE_ALL).text)

    @allure.step('Получить "Сегодня выполнено"')
    def total_orders_for_today(self):
        return int(self.find_element(OrderFeedPageLocators.COUNT_DONE_TODAY).text)

    @allure.step('Окно заказа открыто')
    def modal_window_order_open(self):
        return self.find_element(OrderFeedPageLocators.MODAL_TITLE)

    @allure.step('Ожидаем появление счетчика всех заказов')
    def wait_for_counter_all_visible(self):
        return self.find_element(OrderFeedPageLocators.COUNT_DONE_ALL)

    @allure.step('Ожидаем появление счетчика заказов за сегодня')
    def wait_for_counter_today_visible(self):
        return self.find_element(OrderFeedPageLocators.COUNT_DONE_TODAY)

    @allure.step('Ожидаем видимости секции с заказами В Работе')
    def wait_for_processing_section_visible(self, timeout=10):
        return self.find_element(OrderFeedPageLocators.WORK_IN_PROGRESS_SECTION)

    @allure.step('Получить заказы, которые в рабоет')
    def get_orders_in_process(self) -> list[str]:
        elements = self.find_all_elements(OrderFeedPageLocators.WORK_IN_PROGRESS_ITEMS)
        numbers = []
        for element in elements:
            text = element.text.strip()
            if text.isdigit():
                numbers.append(text)
        return numbers

    @allure.step('Получить номера всех заказов')
    def get_all_orders_numbers(self) -> list[int]:
        elements = self.find_all_elements(OrderFeedPageLocators.ALL_FEED_ORDER_ITEMS)
        return [int(element.text.strip()) for element in elements]

    @allure.step('Ожидаем видимости номера заказа')
    def wait_order_number(self):
        return self.find_element(OrderFeedPageLocators.ORDER_NUMBER_DIGITS)
