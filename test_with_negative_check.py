from .pages.product_page import ProductPage

#pytest -v --tb=line --language=en test_with_negative_check.py

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()
