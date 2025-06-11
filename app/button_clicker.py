"""Button clicker class"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

class ButtonClicker:
    """Handles clicking buttons"""
    def __init__(self, driver: WebDriver, timeout = 10):
        self.wait = WebDriverWait(driver, timeout)
        self.driver = driver

    @staticmethod
    def handle_popup(func):
        """Waits for clickable button with given parameters or button closing popup,
        in case button closing popup is clickable and element with given selectors 
        isn't it closes the popup and passes the element, in case button with given 
        selector is clickable it just passes it"""
        def wrapper(self: 'ButtonClicker', *args, **kwargs):
            by_selector = args[0]
            selector = args[1]

            element = None

            try:
                element = self.wait.until(
                    EC.element_to_be_clickable((by_selector, selector))
                )
            except TimeoutException:
                print(selector, 'not found')
                return False

            self.check_and_close_ads()
            self.driver.switch_to.default_content()

            try:
                element = self.wait.until(
                    EC.element_to_be_clickable((by_selector, selector))
                )
            except TimeoutException:
                return False

            return func(self, *args, element=element, **kwargs)
        return wrapper

    @handle_popup
    def click_button(self, by_selector, selector, element: WebElement = None):
        """Clicks an element"""
        try:
            if element is None:
                element = self.driver.find_element(by_selector, selector)
            element.click()
            return True
        except ElementClickInterceptedException:
            print('button is under sth')
            return False

    @handle_popup
    def click_select(self, by_selector, selector, value, element: WebElement = None):
        """Like click_button but works for select"""
        try:
            if element is None:
                element = self.driver.find_element(by_selector, selector)
            select = Select(element)
            select.select_by_visible_text(str(value))
            return True
        except NoSuchElementException:
            print('Wrong {index} value')
            return False

    def check_and_close_ads(self):
        """Checks if there are any ads on a site and closes them"""

        if not self.look_and_switch_to_frame('aswift_2'):
            return False
        if self.look_for_popup_button():
            return True
        self.look_and_switch_to_frame('ad_iframe')
        if self.look_for_popup_button():
            return True

        return False

    def look_and_switch_to_frame(self, iframe_id):
        """switches to frame with passed id if the frame is enabled"""
        try:
            iframe = self.driver.find_element(By.ID, iframe_id)
            if iframe.is_displayed() and iframe.is_enabled():
                self.driver.switch_to.frame(iframe)
                return True
            else:
                return False
        except NoSuchElementException:
            return False


    def look_for_popup_button(self):
        """Looks for button in current frame and clicks it"""
        try:
            button = self.driver.find_element(By.ID, 'dismiss-button')
            print(button.tag_name)
            button.click()
            return True
        except NoSuchElementException:
            print('not found button')
            return False
        