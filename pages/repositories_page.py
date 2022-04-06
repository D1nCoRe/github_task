import allure
from .base_page import BasePage
from .locators import CreateRepositoryLocators
from .locators import RenameRepositoryLocators
from .locators import DeleteRepositoryLocators
from tests.test_data.repositories import repository_name, repository_new_name
from ..utils.browser_helper import BrowserHelper


class RepositoriesPage(BasePage):
    @allure.step("Should be new repository page")
    def should_be_create_new_repository_page(self):
        self.should_be_repository_name_blank()
        self.should_be_description_blank()

    @allure.step("Should be repository name blank")
    def should_be_repository_name_blank(self):
        assert BrowserHelper.is_element_present(BrowserHelper(self.browser), *CreateRepositoryLocators.REPOSITORY_NAME_BLANK)

    @allure.step("Should be repository description blank")
    def should_be_description_blank(self):
        assert BrowserHelper.is_element_present(BrowserHelper(self.browser), *CreateRepositoryLocators.DESCRIPTION_BLANK)

    def create_new_repository(self):
        BrowserHelper.send_keys(BrowserHelper(self.browser), *CreateRepositoryLocators.REPOSITORY_NAME_BLANK, repository_name)
        BrowserHelper.click_element(BrowserHelper(self.browser), *CreateRepositoryLocators.BUTTON_CREATE_REPOSITORY)

    @allure.step("Should be right repository name")
    def repository_name_should_match(self):
        repository_in_account = BrowserHelper.find_visible_element(BrowserHelper(self.browser), *RenameRepositoryLocators.REPOSITORY_NAME_IN_ACC).text
        assert repository_name == repository_in_account

    @allure.step("Should be right new repository name")
    def repository_new_name_should_match(self):
        repository_in_account = BrowserHelper.find_visible_element(BrowserHelper(self.browser), *RenameRepositoryLocators.REPOSITORY_NAME_IN_ACC).text
        assert repository_new_name == repository_in_account

    def go_to_settings(self):
        BrowserHelper.click_element(BrowserHelper(self.browser), *DeleteRepositoryLocators.SETTINGS_BUTTON)

    def create_readme(self):
        BrowserHelper.click_element(BrowserHelper(self.browser), *CreateRepositoryLocators.README_LINK)

    @allure.step("Should be readme file")
    def should_be_readme_file(self):
        BrowserHelper.find_visible_element(BrowserHelper(self.browser), *CreateRepositoryLocators.README_FILE)


