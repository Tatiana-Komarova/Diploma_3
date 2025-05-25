from selenium.webdriver.common.by import By

class RecoveryPageLocators:

    BUTTON_RECOVER_LINK = (By.LINK_TEXT, "Восстановить пароль")

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")

    BUTTON_RECOVER = (By.XPATH, "//button[text()='Восстановить']")

    TOGGLE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon-action > svg[viewBox='0 0 24 24']")

    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")

    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"

    RESET_FORM = (By.XPATH, "//form[.//button[contains(text(),'Сохранить')]]")

