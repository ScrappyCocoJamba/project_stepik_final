from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def check_product_added(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert name == alert_product_name, f"{name} isn't added to basket, {alert_product_name}"

    def check_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_product_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert price == alert_product_price, f"basket price {price} not equals {alert_product_price}"
