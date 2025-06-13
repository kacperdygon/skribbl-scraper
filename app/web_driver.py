"""File with web driver singleton"""
import os
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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

        match browser:
            case "chrome":
                options = webdriver.ChromeOptions()
                if browser_profile_path:
                    user_data_dir = os.path.dirname(browser_profile_path)
                    profile_dir = os.path.basename(browser_profile_path)
                    options.add_argument(f"--user-data-dir={user_data_dir}")
                    options.add_argument(f"--profile-directory={profile_dir}")
                service = webdriver.ChromeService(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service, options=options)
            case "firefox":
                options = webdriver.FirefoxOptions()
                if browser_profile_path:
                    options.add_argument("-profile")
                    options.add_argument(browser_profile_path)
                service = webdriver.FirefoxService(GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=service, options=options)
            case "edge":
                options = webdriver.EdgeOptions()
                print(options.arguments)
                if browser_profile_path:
                    user_data_dir = os.path.dirname(browser_profile_path)
                    profile_dir = os.path.basename(browser_profile_path)
                    options.add_argument(f"--user-data-dir={user_data_dir}")
                    options.add_argument(f"--profile-directory={profile_dir}")
                service = webdriver.EdgeService(EdgeChromiumDriverManager().install())
                self.driver = webdriver.Edge(service=service, options=options)
            case "safari":
                options = webdriver.SafariOptions()
                service = webdriver.SafariService()
                self.driver = webdriver.Safari(service=service, options=options)
            case _:
                raise ValueError("Unsupported browser")

    def get_driver(self) -> WebDriver:
        """Returns driver"""
        return self.driver

    def reload_driver(self, browser, browser_profile_path):
        """Quits from driver if there is any and inits new one"""
        if self.driver:
            self.driver.quit()
        self._init_driver(browser, browser_profile_path)
