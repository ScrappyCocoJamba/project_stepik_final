from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.url = self.browser.current_url
        assert "login" in self.url, f"'login' isn't present in the url, got {self.url}"

    def should_be_login_form(self):
        form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)  # проверка, что есть форма логина
        assert form, f"login form isn't present on the page, used locator {LoginPageLocators.LOGIN_FORM}"

    def should_be_register_form(self):
        form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)  # проверка, что есть форма регистрации
        assert form, f"login form isn't present on the page, used locator {LoginPageLocators.REGISTER_FORM}"
