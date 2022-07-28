from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')  # создание пары селекторов
    

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM_LINK = (By.CSS_SELECTOR, '#register_form')
