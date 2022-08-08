from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET_LINK)
        basket_link.click()

    def should_be_item_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), 'No message'

    def name_from_message_equals_name_item(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_MESSAGE).text == self.browser.find_element(
            *ProductPageLocators.NAME_BOOK_ORIG).text, 'Name of the books not equal'

    def should_be_message_with_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRICE), 'No message with price'

    def price_basket_equals_price_item(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_FROM_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text, 'Prices do not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            'Message is not disappeared'
