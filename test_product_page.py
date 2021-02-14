from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

"""
Можно реализовать с помощью цикла "for", зная базовый линк, с помощью f-строки добавляем
диапазон id промо акции от 0 до 9

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
"""

# pytest -v --tb=line --language=en test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page
# pytest -v --tb=line --language=en -m login_user test_product_page.py

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_product_added()
    page.check_basket_price()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link2)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                           # открываем страницу
    page.go_to_basket_page()              # выполняем метод страницы — переходим на страницу логина
    basket = BasketPage(browser, browser.current_url)    # Инициализируем BasketPage в теле теста
    basket.should_be_basket_page()        # проверка страницы корзины


@pytest.mark.login_user                   # маркировка для запуска тестов внутри класса
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)   # фикстура для выполнения сэтапа по регистрации нового пользователя
    def setup(self, browser):
        page = LoginPage(browser, login_link)         # инициализируем страницу логина и открываем
        page.open()
        email = str(time.time()) + "@fakemail.org"    # генерируем емейл
        password = str(time.time())                   # генерируем пароль
        page.register_new_user(email, password)       # регистрируем нового пользователя

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_product_added()
        page.check_basket_price()
