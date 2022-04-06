import allure
import pytest
from pages.readme_page import ReadmePage
from .test_data.links import link
from .test_data.users import username, password
from ..pages.welcome_page import WelcomePage
from ..pages.login_page import LoginPage
from ..pages.main_page import MainPage
from ..pages.repositories_page import RepositoriesPage
from ..pages.settings_page import SettingsPage


@allure.feature("Login")
def test_correct_user_is_logged_in(browser):
    welcome_page = WelcomePage(browser, link)
    welcome_page.open()
    welcome_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()
    login_page.sign_in(username, password)
    main_page = MainPage(browser, link)
    main_page.should_be_user_icon()
    main_page.open_user_list()
    main_page.username_should_match()


class TestCreateRepository:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        rep_page = RepositoriesPage(browser, link)
        yield
        settings_page = SettingsPage(browser, link)
        rep_page.go_to_settings()
        settings_page.delete_repository()

    @allure.feature("Create repository")
    def test_create_repository(self, browser):
        welcome_page = WelcomePage(browser, link)
        welcome_page.open()
        welcome_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.sign_in(username, password)
        main_page = MainPage(browser, link)
        main_page.go_to_create_repository_page()
        rep_page = RepositoriesPage(browser, link)
        rep_page.should_be_create_new_repository_page()
        rep_page.create_new_repository()
        rep_page.repository_name_should_match()


class TestRenameRepository:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        welcome_page = WelcomePage(browser, link)
        welcome_page.open()
        welcome_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.sign_in(username, password)
        main_page = MainPage(browser, link)
        main_page.go_to_create_repository_page()
        rep_page = RepositoriesPage(browser, link)
        rep_page.create_new_repository()
        yield
        settings_page = SettingsPage(browser, link)
        rep_page.go_to_settings()
        settings_page.delete_repository()

    @allure.feature("Rename repository")
    def test_rename_repository(self, browser):
        rep_page = RepositoriesPage(browser, link)
        rep_page.go_to_settings()
        settings_page = SettingsPage(browser, link)
        settings_page.rename_repository()
        rep_page.repository_new_name_should_match()

    @allure.feature("Create readme file")
    def test_create_readme_in_repository(self, browser):
        rep_page = RepositoriesPage(browser, link)
        rep_page.create_readme()
        readme_page = ReadmePage(browser, link)
        readme_page.add_description()
        rep_page.should_be_readme_file()


class TestDeleteRepository:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        welcome_page = WelcomePage(browser, link)
        welcome_page.open()
        welcome_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.sign_in(username, password)
        main_page = MainPage(browser, link)
        main_page.go_to_create_repository_page()
        rep_page = RepositoriesPage(browser, link)
        rep_page.create_new_repository()
        yield

    @allure.feature("Delete repository")
    def test_delete_repository(self, browser):
        rep_page = RepositoriesPage(browser, link)
        rep_page.go_to_settings()
        settings_page = SettingsPage(browser, link)
        settings_page.delete_repository()

