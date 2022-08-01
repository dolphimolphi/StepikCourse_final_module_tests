import pytest
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_item_add_to_basket()
    page.name_from_message_equals_name_item()
    page.should_be_message_with_price()
    page.price_basket_equals_price_item()
