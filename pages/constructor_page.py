import allure
from .base_page import BasePage
from locators.constructor_locators import ConstructorLocators

class ConstructorPage(BasePage):
    @allure.step('Проверка, что открылось окно с деталями')
    def check_window_open(self):
        return self.wait_for_element(ConstructorLocators.MODAL_WINDOW)

    @allure.step('Закрыть окно деталей')
    def close_window(self):
        self.click_on_element(ConstructorLocators.CLOSE_BUTTON)

    @allure.step('Проверка, что модальное окно закрыто')
    def check_window_closed(self):
        return self.wait_for_element_hide(ConstructorLocators.MODAL_WINDOW)

