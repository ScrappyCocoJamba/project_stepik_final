from .base_page import BasePage
from .locators import MainPageLocators

""" 
 При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы 
 с браузером, а в качестве url передаем текущий адрес.
 Здесь в функции go_to_login_page добавляется запись
 return LoginPage(browser=self.browser, url=self.browser.current_url)
 
 а в файле test_main_page.py код будет выглядеть так:
 
 def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
"""

class MainPage(BasePage):         # класс MainPage наследник класса BasePage

    def go_to_login_page(self):
        # браузер хранится как аргумент класса BasePage, обращаться к нему нужно с помощью self
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
