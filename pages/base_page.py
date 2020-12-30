from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, browser, url, timeout=10):  #конструктор — метод, который вызывается, когда мы создаем объект
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):                             #открывает нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        # Чтобы перехватывать исключение, нужна конструкция try/except
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
