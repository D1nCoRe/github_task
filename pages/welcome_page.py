import allure

from .base_page import BasePage
from .locators import LoginPageLocators
from ..utils.browser_helper import BrowserHelper


class WelcomePage(BasePage):
    def go_to_login_page(self):
        BrowserHelper.click_element(BrowserHelper(self.browser), *LoginPageLocators.LOGIN_LINK)
