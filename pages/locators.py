from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM_LINK = (By.CSS_SELECTOR, '#register_form')
    EMAIL_LINK = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_LINK = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_LINK_CHECKS = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators():
    ADD_BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, '.alert-success')
    NAME_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '#messages div.alertinner strong')
    NAME_BOOK_ORIG = (By.CSS_SELECTOR, '.product_main h1')
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, '.alert-info')
    PRICE_FROM_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRICE_BOOK = (By.CSS_SELECTOR, '.product_main .price_color')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    TEXT_NO_PRODUCTS_IN_THE_BASKET = (
        By.CSS_SELECTOR, '#content_inner > p')
    BLOCK_ABOUT_PROD_IN_BASKET = (By.CSS_SELECTOR, '.basket-items > .row')
