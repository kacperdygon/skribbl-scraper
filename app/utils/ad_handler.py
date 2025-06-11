"""Button clicker class"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

class AdHandler:
    """Handles removing ad popups"""
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_and_close_ads(self):
        """Checks if there are any ads on a site and closes them"""
        try:
            if not self.__look_and_switch_to_frame('aswift_2'):
                return False
            if self.__look_for_popup_button():
                return True
            self.__look_and_switch_to_frame('ad_iframe')
            if self.__look_for_popup_button():
                return True

            return False
        finally:
            self.driver.switch_to.default_content()

    def __look_and_switch_to_frame(self, iframe_id):
        """switches to frame with passed id if the frame is enabled"""
        try:
            iframe = self.driver.find_element(By.ID, iframe_id)
            if iframe.is_displayed() and iframe.is_enabled():
                self.driver.switch_to.frame(iframe)
                return True
            return False
        except NoSuchElementException:
            return False


    def __look_for_popup_button(self):
        """Looks for button in current frame and clicks it"""
        try:
            button = self.driver.find_element(By.ID, 'dismiss-button')
            print(button.tag_name)
            button.click()
            return True
        except NoSuchElementException:
            return False
        