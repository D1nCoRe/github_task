import allure
from pages.base_page import BasePage
from pages.locators import DeleteRepositoryLocators, CreateRepositoryLocators, RenameRepositoryLocators
from tests.test_data.repositories import repository_new_name
from utils.browser_helper import BrowserHelper


class SettingsPage(BasePage):
    @allure.step("Delete repository")
    def delete_repository(self):
        BrowserHelper.click_element(BrowserHelper(self.browser), *DeleteRepositoryLocators.DELETE_BUTTON)
        text_for_confirm = BrowserHelper.find_visible_element(BrowserHelper(self.browser), *DeleteRepositoryLocators.TEXT_FOR_CONFIRM).text
        BrowserHelper.send_keys(BrowserHelper(self.browser), *DeleteRepositoryLocators.CONFIRM_DELETE_BLANK, text_for_confirm)
        BrowserHelper.click_element(BrowserHelper(self.browser), *DeleteRepositoryLocators.BUTTON_DELETE_REPOSITORY)
        return text_for_confirm

    @allure.step("Should not be deleted repository")
    def repository_should_be_deleted(self):
        assert BrowserHelper.is_not_element_present(BrowserHelper(self.browser), *CreateRepositoryLocators.REPOSITORY_LINK)

    @allure.step("Rename repository")
    def rename_repository(self):
        BrowserHelper.clear_blank(BrowserHelper(self.browser), *RenameRepositoryLocators.CHANGE_REPOSITORY_NAME_BLANK)
        BrowserHelper.send_keys(BrowserHelper(self.browser), *RenameRepositoryLocators.CHANGE_REPOSITORY_NAME_BLANK, repository_new_name)
        BrowserHelper.click_element(BrowserHelper(self.browser), *RenameRepositoryLocators.BUTTON_RENAME_REPOSITORY)
