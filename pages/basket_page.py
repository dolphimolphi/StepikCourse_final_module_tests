from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def no_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BLOCK_ABOUT_PROD_IN_BASKET), 'Block basket in the page'

    def should_be_text_is_basket_empty(self):
        assert self.browser.find_element(
            *BasketPageLocators.TEXT_NO_PRODUCTS_IN_THE_BASKET), 'No text about products in the basket'
