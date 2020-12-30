from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):         # класс MainPage наследник класса BasePage

    def go_to_login_page(self):
        # браузер хранится как аргумент класса BasePage, обращаться к нему нужно с помощью self
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером,
        # а в качестве url передаем текущий адрес.
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
