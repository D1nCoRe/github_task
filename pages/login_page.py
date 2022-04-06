from .base_page import BasePage
from .locators import LoginPageLocators
from ..utils.browser_helper import BrowserHelper
import allure


class LoginPage(BasePage):
    @allure.step("Should be login page")
    def should_be_login_page(self):
        self.should_be_username_blank()
        self.should_be_password_blank()

    def should_be_username_blank(self):
        assert BrowserHelper.is_element_present(BrowserHelper(self.browser), *LoginPageLocators.LOGIN_BLANK)

    def should_be_password_blank(self):
        assert BrowserHelper.is_element_present(BrowserHelper(self.browser), *LoginPageLocators.PASSWORD_BLANK)

    @allure.step("Signing in")
    def sign_in(self, login, password):
        BrowserHelper.send_keys(BrowserHelper(self.browser), *LoginPageLocators.LOGIN_BLANK, login)
        BrowserHelper.send_keys(BrowserHelper(self.browser), *LoginPageLocators.PASSWORD_BLANK, password)
        BrowserHelper.click_element(BrowserHelper(self.browser), *LoginPageLocators.LOGIN_BUTTON)
