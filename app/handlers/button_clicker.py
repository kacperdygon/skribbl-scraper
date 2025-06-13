"""Button clicker class"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    NoSuchElementException
)
from app.handlers.ad_handler import AdHandler
from app.globals import print_error

class ButtonClicker:
    """Handles clicking buttons"""
    def __init__(self, driver: WebDriver, config: dict):
        self.wait = WebDriverWait(driver, config["timeout"])
        self.driver = driver
        self.config = config

    @staticmethod
    def handle_popup(func):
        """Runs check for popups so they won't block a button"""
        def wrapper(self: 'ButtonClicker', *args, **kwargs):

            if self.config["check_for_popups"]:
                ad_handler = AdHandler(self.driver)
                ad_handler.check_and_close_ads()

            return func(self, *args, **kwargs)
        return wrapper

    @staticmethod
    def catch_common_errors(func):
        """Catches common errors:\n
        TimeoutException,\n
        ElementClickInterceptedException"""
        def wrapper(self, *args, **kwargs):
            by_selector = args[0]
            selector = args[1]
            try:
                return func(self, *args, **kwargs)
            except TimeoutException:
                print_error(f'No such element: {by_selector} {selector}')
                return False
            except ElementClickInterceptedException:
                print_error(f'Click intercepted for element: {by_selector} {selector}')
                return False
        return wrapper

    @catch_common_errors
    @handle_popup
    def click_button(self, by_selector, selector):
        """Searches for button and clicks it"""
        element = self.wait.until(
            EC.element_to_be_clickable((by_selector, selector))
        )
        element.click()
        return True

    @catch_common_errors
    @handle_popup
    def click_select(self, by_selector, selector, value):
        """Searches for select and selects a value"""
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((by_selector, selector))
            )
            select = Select(element)
            select.select_by_visible_text(str(value))
            return True
        except NoSuchElementException:
            print_error(f'No value {value} in select field: {by_selector} {selector}')
            return False

    @catch_common_errors
    @handle_popup
    def use_input(self, by_selector, selector, value):
        """Searches for text input and inputs a value"""
        element = self.wait.until(
            EC.element_to_be_clickable((by_selector, selector))
        )
        element.send_keys(value)
        element.send_keys(Keys.ENTER)
        return True
