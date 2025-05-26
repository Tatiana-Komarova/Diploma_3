import allure
from .base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators

class RecoveryPage(BasePage):
    @allure.step("Перейти на страницу восстановления пароля")
    def go_to_recover(self):
        self.click_on_element(RecoveryPageLocators.BUTTON_RECOVER_LINK)

    @allure.step("Ввести email для восстановления: {email}")
    def enter_email(self, email):
        self.click_on_element(RecoveryPageLocators.EMAIL_INPUT)
        self.send_keys_to_input(RecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step("Нажать Восстановить")
    def submit_recovery(self):
        self.click_on_element(RecoveryPageLocators.BUTTON_RECOVER)

    @allure.step('Ожидаем прогрузку overley на странице')
    def wait_loading(self):
        self.wait_for_element_hide(RecoveryPageLocators.OVERLAY)

    @allure.step('Ожидаем загрузку страницы восстановления пароля')
    def wait_loading_page(self, timeout=10):
        return self.find_element(RecoveryPageLocators.RESET_FORM)

    @allure.step("Получить атрибут type у поля пароля")
    def get_password_field_type(self) -> str:
        return self.find_element(RecoveryPageLocators.PASSWORD_FIELD).get_attribute("type")

    @allure.step("Переключить видимость поля пароля")
    def toggle_password_visibility(self):
        self.wait_for_element(RecoveryPageLocators.TOGGLE_PASSWORD_BUTTON)
        self.click_on_element(RecoveryPageLocators.TOGGLE_PASSWORD_BUTTON)

