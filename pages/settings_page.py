import allure
from pages.base_page import BasePage
from pages.locators import DeleteRepositoryLocators, CreateRepositoryLocators, RenameRepositoryLocators
from tests.test_data.repositories import repository_new_name
from utils.browser_helper import BrowserHelper


class SettingsPage(BasePage):
    def delete_repository(self):
        BrowserHelper.click_element(BrowserHelper(self.browser), *DeleteRepositoryLocators.DELETE_BUTTON)

    def confirm_delete(self):
        text_for_confirm = BrowserHelper.find_visible_element(BrowserHelper(self.browser), *DeleteRepositoryLocators.TEXT_FOR_CONFIRM).text
        BrowserHelper.send_keys(BrowserHelper(self.browser), *DeleteRepositoryLocators.CONFIRM_DELETE_BLANK, text_for_confirm)
        BrowserHelper.click_element(BrowserHelper(self.browser), *DeleteRepositoryLocators.BUTTON_DELETE_REPOSITORY)
        return text_for_confirm

    @allure.step("Should be deleted repository")
    def repository_should_be_deleted(self):
        assert BrowserHelper.is_not_element_present(BrowserHelper(self.browser), *CreateRepositoryLocators.REPOSITORY_LINK)

    def rename_repository(self):
        BrowserHelper.clear_blank(BrowserHelper(self.browser), *RenameRepositoryLocators.REPOSITORY_NEW_NAME)
        BrowserHelper.send_keys(BrowserHelper(self.browser), *RenameRepositoryLocators.REPOSITORY_NEW_NAME, repository_new_name)
        BrowserHelper.click_element(BrowserHelper(self.browser), *RenameRepositoryLocators.BUTTON_RENAME_REPOSITORY)
