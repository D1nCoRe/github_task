from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import default_timeout
from loguru import logger

logger.add("logs/logs.log", level="DEBUG")


class BrowserHelper:
    def __init__(self, browser):
        self.browser = browser

    def is_element_present(self, strategy, selector):
        try:
            logger.debug(f"{strategy}, {selector}, Finding element")
            WebDriverWait(self.browser, default_timeout).until(EC.visibility_of_element_located((strategy, selector)))
        except TimeoutException:
            logger.error("Element not present")
            return False
        return True

    def is_not_element_present(self, strategy, selector):
        try:
            logger.debug(f"{strategy}, {selector}, Finding element")
            WebDriverWait(self.browser, default_timeout).until_not(EC.visibility_of_element_located((strategy, selector)))
        except TimeoutException:
            logger.error("Element present")
            return False
        return True

    def find_visible_element(self, strategy, selector):
        element = WebDriverWait(self.browser, default_timeout).until(EC.visibility_of_element_located((strategy, selector)))
        return element

    def send_keys(self, strategy, selector, text):
        self.find_visible_element(strategy, selector).send_keys(text)

    def click_element(self, strategy, selector):
        element = WebDriverWait(self.browser, default_timeout).until(EC.element_to_be_clickable((strategy, selector)))
        element.click()

    def clear_blank(self, strategy, selector):
        element = self.find_visible_element(strategy, selector)
        element.clear()
