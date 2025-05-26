from selenium.webdriver.common.by import By

class ProfilePageLocators:

    TAB_ORDERS = (By.LINK_TEXT, "История заказов")

    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")

    ORDER_HISTORY_ITEMS = (By.XPATH, "//ul[contains(@class,'OrderHistory_profileList__')]/li//p[contains(@class,'text_type_digits-default')]")
