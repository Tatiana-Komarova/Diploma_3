from curl import *
import allure
from pages.recovery_page import RecoveryPage
from pages.main_page import MainPage
from data import Credentials

class TestRecovery:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recovery(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.go_to_profile()
        recovery_page.go_to_recover()

        current_url = main_page.get_current_url()

        assert current_url == forgot_password

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_and_submit_email(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.go_to_profile()
        recovery_page.go_to_recover()
        recovery_page.enter_email(Credentials.email)
        recovery_page.submit_recovery()
        recovery_page.wait_loading_page()

        current_url = main_page.get_current_url()

        assert current_url == reset_password

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_toggle_password(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.go_to_profile()
        recovery_page.go_to_recover()
        recovery_page.enter_email(Credentials.email)
        recovery_page.submit_recovery()
        recovery_page.wait_loading_page()
        recovery_page.wait_loading()
        recovery_page.toggle_password_visibility()
        recovery_page.toggle_password_visibility()

        assert recovery_page.get_password_field_type() == "password"
