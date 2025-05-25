from selenium.webdriver.common.by import By

class ConstructorLocators:
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class,'Modal_modal__container')]") # Модальное окно ингредиента
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") # Кнопка закрытия модального окна ингредиента

