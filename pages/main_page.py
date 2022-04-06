import allure
from tests.test_data.users import username
from .base_page import BasePage
from .locators import MainPageLocators
from ..utils.browser_helper import BrowserHelper


class MainPage(BasePage):
    @allure.step("Should be user icon")
    def should_be_user_icon(self):
        assert BrowserHelper.is_element_present(BrowserHelper(self.browser), *MainPageLocators.USER_ICON)

    @allure.step("opening user list")
    def open_user_list(self):
        BrowserHelper.click_element(BrowserHelper(self.browser), *MainPageLocators.DROPDOWN_MENU)

    @allure.step("Should be right username")
    def username_should_match(self):
        username_in_account = BrowserHelper.find_visible_element(BrowserHelper(self.browser), *MainPageLocators.USERNAME_ON_PAGE).text
        assert username == username_in_account

    def go_to_create_repository_page(self):
        BrowserHelper.click_element(BrowserHelper(self.browser), *MainPageLocators.NEW_REPOSITORY_BUTTON)
