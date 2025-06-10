"""Button clicker class"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ButtonClicker:
    """Handles clicking buttons"""
    def __init__(self, driver, timeout=10):
        self.wait = WebDriverWait(driver, timeout)

    def click_button(self, by_selector, selector):
        """Waits till button with given selectors is avaible and then clicks it """
        button = self.wait.until(
            EC.element_to_be_clickable((by_selector, selector))
        )
        button.click()
