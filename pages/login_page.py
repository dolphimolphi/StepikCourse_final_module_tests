from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_LINK), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_LINK).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_LINK).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_LINK_CHECKS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
