from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# pytest -v --tb=line --language=en test_main_page.py::test_guest_cant_see_product_in_basket_opened_from_main_page

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина
    login = LoginPage(browser, browser.current_url)  # Инициализируем LoginPage в теле теста
    login.should_be_login_page()            # проверка ссылки на авторизацию


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.go_to_basket_page()         # выполняем метод страницы — переходим на страницу логина
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_basket_page()
