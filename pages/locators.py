from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')  # создание пары селекторов


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM_LINK = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')  # селектор уникальный
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, '.alert-success')  # списком перебираем и берем первый
    NAME_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '#messages div.alertinner strong')  #
    NAME_BOOK_ORIG = (By.CSS_SELECTOR, '.product_main h1')  # селектор уникальный
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, '.alert-info')  # селектор уникальный
    PRICE_FROM_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')  # выбираем первый по поиску
    PRICE_BOOK = (By.CSS_SELECTOR, '.product_main .price_color')  # списком выбираем второй
