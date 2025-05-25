import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Переход в личный кабинет')
    def go_to_profile(self):
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL)

    @allure.step('Переход в конструктор')
    def go_to_constructor(self):
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Переход на ленту заказов')
    def go_to_feed(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self, index = 0):
        self.wait_for_element(MainPageLocators.INGREDIENT_TILE)
        elements = self.find_all_elements(MainPageLocators.INGREDIENT_TILE)
        elements[index].click()

    def get_counter(self, ingredient_name):
        locator = (By.XPATH, MainPageLocators.INGREDIENT_NAME[1].format(ingredient_name=ingredient_name))
        elements = self.find_all_elements(locator)
        return int(elements[0].text) if elements else 0


    @allure.step('Положить ингредиент в корзину')
    def put_ingredient_into_basket(self, ingredient_name):
        ingredient = self.find_element(MainPageLocators.ingredient_card(ingredient_name))
        basket = self.find_element(MainPageLocators.CART_TARGET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Оформление заказа')
    def place_order(self):
        self.find_element(MainPageLocators.BUTTON_PLACE_ORDER)
        self.click_on_element(MainPageLocators.BUTTON_PLACE_ORDER)

    @allure.step('Ожидаем модальное окно заказа')
    def wait_for_order_modal(self):
        return self.wait_for_element(MainPageLocators.MODAL_WINDOW_ORDER)

    @allure.step('Закрытие модального окна заказа')
    def close_order_modal(self):
        self.wait_for_element(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step('Ожидаем прогрузки спиннера')
    def wait_loading_spinner(self):
        return self.wait_for_element_hide(MainPageLocators.LOADING_SPINNER)

    @allure.step('Получить номер заказа из модального окна')
    def get_order_number_from_modal(self) -> str:
        element = self.find_element(MainPageLocators.ORDER_NUMBER)
        return element.text.strip()



