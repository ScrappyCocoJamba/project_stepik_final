from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_page_header()
        self.should_be_basket_empty_msg()
        self.should_not_be_items()

    def should_be_basket_url(self):
        self.url = self.browser.current_url
        assert "basket" in self.url, f"'basket' isn't present in the url, got {self.url}"

    def should_be_basket_empty_msg(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket isn't empty"

    def should_be_basket_page_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT), "I didn't see text"

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"
