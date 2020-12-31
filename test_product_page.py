from .pages.product_page import ProductPage

# pytest -v --tb=line --language=en test_product_page.py

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_product_added()
    page.check_basket_price()

