import pytest
import faker

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

f = faker.Faker()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):  # должен упасть, так как нет исчезающих сообщений
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_be_item_add_to_basket()
    page.name_from_message_equals_name_item()
    page.should_be_message_with_price()
    page.price_basket_equals_price_item()


@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.open_basket_page()
        page.should_be_text_is_basket_empty()
        page.no_products_in_the_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(f.email(), password='1234567890B')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()
        page.should_be_item_add_to_basket()
        page.name_from_message_equals_name_item()
        page.should_be_message_with_price()
        page.price_basket_equals_price_item()
