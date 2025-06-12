"""Button clicker class"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from app.utils.ad_handler import AdHandler

class ButtonClicker:
    """Handles clicking buttons"""
    def __init__(self, driver: WebDriver, config: dict):
        self.wait = WebDriverWait(driver, config["timeout"])
        self.driver = driver
        self.config = config

    @staticmethod
    def handle_popup(func):
        """decorator """
        def wrapper(self, *args, **kwargs):

            if self.config["check_for_popup"]:
                ad_handler = AdHandler(self.driver)
                ad_handler.check_and_close_ads()

            return func(self, *args, **kwargs)
        return wrapper

    @handle_popup
    def click_button(self, by_selector, selector):
        """Clicks an element"""
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((by_selector, selector))
            )
            element.click()
            return True
        except TimeoutException:
            print(f'no such element: {by_selector}, {selector}')
            return False
        except ElementClickInterceptedException:
            print('Click intercepted')
            return False

    @handle_popup
    def click_select(self, by_selector, selector, value):
        """Like click_button but works for select"""
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((by_selector, selector))
            )
            select = Select(element)
            select.select_by_visible_text(str(value))
            return True
        except TimeoutException:
            print(f'no such element: {by_selector}, {selector}')
            return False

    def use_input(self, by_selector, selector, value):
        """Like click_select but works for input"""
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((by_selector, selector))
            )
            element.send_keys(value)
            element.send_keys(Keys.ENTER)
            return True
        except TimeoutException:
            print(f'no such element: {by_selector}, {selector}')
            return False