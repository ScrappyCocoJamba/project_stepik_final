from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import  pytest

# pytest -v --tb=line --language=en test_main_page.py::test_guest_cant_see_product_in_basket_opened_from_main_page
# pytest -v --tb=line --language=en -m login_guest test_main_page.py

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                             # открываем страницу
        page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина
        login = LoginPage(browser, browser.current_url)  # Инициализируем LoginPage в теле теста
        login.should_be_login_page()            # проверка ссылки на авторизацию

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.go_to_basket_page()                # выполняем метод страницы — переходим на страницу логина
    basket = BasketPage(browser, browser.current_url)    # Инициализируем BasketPage в теле теста
    basket.should_be_basket_page()          # проверка страницы корзины
