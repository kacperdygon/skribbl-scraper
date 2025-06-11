"""Module with class for switching windows"""
from selenium.webdriver.remote.webdriver import WebDriver

class WindowManager:
    """Class for handling window switching"""
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def switch_window(self, index):
        """Handles switching window"""
        tabs = self.driver.window_handles
        if 0 <= index < len(tabs):
            self.driver.switch_to.window(tabs[index])
        else:
            print(f"No window with index {index}")

    def open_new_tab(self, url: str):
        """Opens new tab with given url"""
        self.driver.execute_script(f"window.open('{url}', '_blank');")
