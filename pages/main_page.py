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

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
