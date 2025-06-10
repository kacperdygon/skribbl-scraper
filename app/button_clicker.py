"""Button clicker class"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

class ButtonClicker:
    """Handles clicking buttons"""
    def __init__(self, driver: WebDriver, timeout = 10):
        self.wait = WebDriverWait(driver, timeout)
        self.driver = driver

    def click_button(self, by_selector, selector):
        """Waits till button with given selectors is avaible and then clicks it """
        self.check_and_close_ads()
        try:
            button = self.wait.until(
                EC.element_to_be_clickable((by_selector, selector))
            )
        except TimeoutException:
            self.check_and_close_ads()
            button = self.wait.until(
                EC.element_to_be_clickable((by_selector, selector))
            )


        button.click()

    def check_and_close_ads(self):
        """Checks if there are any ads on a site and closes them"""
        try:
            button = self.driver.find_element(By.ID, "dismiss-button")
            button.click()
        except NoSuchElementException:
            pass
