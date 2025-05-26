import allure
from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):
    @allure.step('Перейти в историю заказов')
    def go_to_orders(self):
        self.click_on_element(ProfilePageLocators.TAB_ORDERS)

    @allure.step('Выход из аккаунта')
    def logout_profile(self):
        self.wait_for_element(ProfilePageLocators.BUTTON_LOGOUT)
        self.find_element(ProfilePageLocators.BUTTON_LOGOUT)
        self.click_on_element(ProfilePageLocators.BUTTON_LOGOUT)

    @allure.step('Получить номера всех заказов пользователя')
    def get_all_user_order_numbers(self) -> list[int]:
        elements = self.find_all_elements(ProfilePageLocators.ORDER_HISTORY_ITEMS)
        return [
            int(element.text.strip().lstrip('#0') or '0')
            for element in elements
        ]


