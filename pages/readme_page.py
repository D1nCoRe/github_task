from utils.browser_helper import BrowserHelper
from .base_page import BasePage
from .locators import CreateReadmeLocators
from tests.test_data.repositories import repository_description


class ReadmePage(BasePage):
    def add_description(self):
        BrowserHelper.send_keys(BrowserHelper(self.browser), *CreateReadmeLocators.README_DESCRIPTION, repository_description)
        BrowserHelper.click_element(BrowserHelper(self.browser), *CreateReadmeLocators.BUTTON_CREATE_README)
