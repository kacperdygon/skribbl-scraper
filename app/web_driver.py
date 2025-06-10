"""File with web driver singleton"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class WebDriverManager:
    """Singleton with browser driver to support different browsers"""
    _instance = None

    def __new__(cls, browser="chrome"):
        if cls._instance is None:
            cls._instance = super(WebDriverManager, cls).__new__(cls)
            cls._instance._init_driver(browser)
        return cls._instance

    def __init__(self, browser="chrome"):
        if not hasattr(self, 'driver'):
            self.driver = None
            self._init_driver(browser)

    def _init_driver(self, browser):

        if browser == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
        elif browser == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service)
        else:
            raise ValueError("Unsupported browser")

    def get_driver(self):
        """Returns driver"""
        return self.driver
    