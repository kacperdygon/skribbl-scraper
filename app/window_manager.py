"""Module with class for switching windows"""
from typing import Callable
from selenium.webdriver.remote.webdriver import WebDriver

class WindowManager:
    """Class for handling window switching"""
    def __init__(self, driver: WebDriver, check_and_close_tabs: Callable[[], None]):
        self.driver = driver
        self.check_and_close_tabs = check_and_close_tabs

    def switch_window(self, index):
        """Handles switching window"""
        tabs = self.driver.window_handles
        if 0 <= index < len(tabs):
            self.driver.switch_to.window(tabs[index])
            self.check_and_close_tabs()
        else:
            print(f"No window with index {index}")

    def open_new_tab(self, url: str):
        """Opens new tab with given url"""
        self.driver.execute_script(f"window.open('{url}', '_blank');")
