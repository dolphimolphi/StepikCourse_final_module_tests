from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET_LINK)
        basket_link.click()

    def should_be_item_add_to_basket(self):
        # Сообщение о том, что товар добавлен в корзину.
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), 'No message'

    def name_from_message_equals_name_item(self):
        # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_MESSAGE).text == self.browser.find_element(
            *ProductPageLocators.NAME_BOOK_ORIG).text, 'Name of the books not equal'

    def should_be_message_with_price(self):
        # Сообщение со стоимостью корзины.
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRICE), 'No message with price'

    def price_basket_equals_price_item(self):
        # Стоимость корзины совпадает с ценой товара.
        assert self.browser.find_element(*ProductPageLocators.PRICE_FROM_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text, 'Prices do not match'
