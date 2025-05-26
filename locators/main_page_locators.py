from selenium.webdriver.common.by import By

class MainPageLocators:

    BUTTON_PERSONAL =  ("xpath", "//header//a[@href='/account']")

    BUTTON_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")

    BUTTON_ORDER_FEED = (By.XPATH, "(//a[@href='/feed'])[1]")

    INGREDIENT_TILE = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")

    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")

    LOADING_SPINNER = (By.CSS_SELECTOR, "img[class*='Modal_modal__loading']")

    CART_TARGET = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket__list')]")

    BUTTON_PLACE_ORDER = (By.XPATH, "//button[normalize-space(text())='Оформить заказ']")

    MODAL_WINDOW_ORDER = (By.XPATH, "//div[contains(@class,'Modal_modal__container')]")

    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")

    COUNTER_BADGE = (By.CSS_SELECTOR, "p[class^='counter_counter__num']")

    ORDER_NUMBER = (By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m.text_type_digits-large")

    INGREDIENT_NAME = (By.XPATH, "//a[contains(@class,'BurgerIngredient_ingredient') and .//img[@alt='{ingredient_name}']]//p[contains(@class,'counter_counter__num')]")

    @staticmethod
    def ingredient_card(ingredient_name):
        return (
            By.XPATH,
            f"//p[text()='{ingredient_name}']/ancestor::a"
            f"[contains(@class,'BurgerIngredient_ingredient')]"
        )

    @staticmethod
    def counter_badge(ingredient_name):
        return (By.XPATH,
                f"//p[text()='{ingredient_name}']"
                "/ancestor::div[contains(@class,'ingredient-card')]"
                "//span[contains(@class,'counter')]")
