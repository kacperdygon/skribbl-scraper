"""File with web driver singleton"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class WebDriverManager:
    """Singleton with browser driver to support different browsers"""
    _instance = None

    def __new__(cls, browser, browser_profile_path):
        if cls._instance is None:
            cls._instance = super(WebDriverManager, cls).__new__(cls)
            cls._instance._init_driver(browser, browser_profile_path)
        return cls._instance

    def __init__(self, browser, browser_profile_path):
        if not hasattr(self, 'driver'):
            self.driver = None
            self._init_driver(browser, browser_profile_path)

    def _init_driver(self, browser, browser_profile_path):

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if browser_profile_path:
                options.add_argument(f"user-data-dir={browser_profile_path}")
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            if os.path.exists(browser_profile_path):
                print('sigma')
            if browser_profile_path:
                options.add_argument("-profile")
                options.add_argument(browser_profile_path)
            print(options.arguments)
            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError("Unsupported browser")

    def get_driver(self):
        """Returns driver"""
        return self.driver
    