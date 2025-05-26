from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    LAST_ORDER = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby:first-child")

    COUNT_DONE_ALL = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ.text_type_digits-large")

    COUNT_DONE_TODAY = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ.text_type_digits-large")

    MODAL_TITLE = (By.XPATH, "//div[contains(@class,'Modal_orderBox')]")

    WORK_IN_PROGRESS_SECTION = (By.XPATH, "//p[normalize-space()='В работе:']/following-sibling::ul[contains(@class,'OrderFeed_orderList__cBvyi')]")

    WORK_IN_PROGRESS_ITEMS = (By.XPATH, "//p[normalize-space()='В работе:']" "/following-sibling::ul[contains(@class,'OrderFeed_orderList__cBvyi')]/li")

    ALL_FEED_ORDER_ITEMS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]/li" "[contains(@class,'text_type_digits-default')]")

    ORDER_NUMBER_DIGITS = (By.CSS_SELECTOR, "li.text.text_type_digits-default.mb-2")
