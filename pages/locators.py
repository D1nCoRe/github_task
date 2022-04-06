from selenium.webdriver.common.by import By
from tests.test_data.repositories import repository_name


class LoginPageLocators:
    LOGIN_LINK = (By.XPATH, "//*[contains(text(), 'Sign in')]")
    LOGIN_BLANK = (By.XPATH, "//input[@name='login']")
    PASSWORD_BLANK = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@name='commit']")


class MainPageLocators:
    USER_ICON = (By.XPATH, "//div[@class='Header-item position-relative mr-0 d-none d-md-flex']")
    USERNAME_ON_PAGE = (By.XPATH, "//*[@class='css-truncate-target']")
    DROPDOWN_MENU = (By.XPATH, "//*[@class='avatar avatar-small circle']")
    NEW_REPOSITORY_BUTTON = (By.XPATH, "//a[@class='btn btn-sm btn-primary']")


class CreateRepositoryLocators:
    REPOSITORY_NAME_BLANK = (By.XPATH, "//*[@class='form-control js-repo-name js-repo-name-auto-check short']")
    DESCRIPTION_BLANK = (By.XPATH, "//*[@class='form-control long']")
    BUTTON_CREATE_REPOSITORY = (By.XPATH, "//*[@class='btn-primary btn']")
    README_LINK = (By.XPATH, "//a[contains(@href, 'readme')]")
    README_FILE = (By.XPATH, "//a[@class='Link--primary']")
    REPOSITORY_LINK = (By.XPATH, f"//a[contains(@href, 'Ufortest/{repository_name}')]")


class RenameRepositoryLocators:
    REPOSITORY_NAME_IN_ACC = (By.XPATH, "//*[@class='mr-2 flex-self-stretch']/a")
    CHANGE_REPOSITORY_NAME_BLANK = (By.XPATH, "//input[@name='new_name']")
    BUTTON_RENAME_REPOSITORY = (By.XPATH, "//button[@class='flex-self-end btn']")


class DeleteRepositoryLocators:
    SETTINGS_BUTTON = (By.XPATH, "//*[@id='settings-tab']")
    DELETE_BUTTON = (By.XPATH, "//summary[contains(text(),'Delete')]")
    CONFIRM_DELETE_BLANK = (By.XPATH, "//div[@class='Box-body overflow-auto']/form/p/input[@name='verify']")
    BUTTON_DELETE_REPOSITORY = (By.XPATH, "//div[@class='Box-body overflow-auto']/form/button")
    TEXT_FOR_CONFIRM = (By.XPATH, "//div[@class='Box-body overflow-auto']/p/strong[2]")


class CreateReadmeLocators:
    README_DESCRIPTION = (By.XPATH, "//div[@class='CodeMirror-scroll']")
    BUTTON_CREATE_README = (By.XPATH, "//button[@id='submit-file']")
