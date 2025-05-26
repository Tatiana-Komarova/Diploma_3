from selenium.webdriver.common.by import By

class AuthLocators:
    PERSONAL_ACCOUNT_LINK = ("xpath", "//header//a[@href='/account']") # Кнопка перехода в личный кабинет
    LOGIN_BUTTON_MAIN = ("xpath", "//button[text()='Войти в аккаунт']")  # Кнопка входа на главной странице
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")  # Поле ввода email
    PASSWORD = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")  # Поле ввода пароля
    LOGIN_FORM_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа в форме авторизации

