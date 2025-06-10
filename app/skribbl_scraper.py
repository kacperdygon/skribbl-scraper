"""Good bot"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pyperclip
from app.button_clicker import ButtonClicker
from app.window_manager import WindowManager
from app.lobby_configurator import LobbyConfigurator

class SkribblScraper:
    """Handles everything"""
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = 'https://skribbl.io/'
        self.button_clicker = ButtonClicker(driver, 10)
        self.window_manager = WindowManager(driver, self.button_clicker.check_and_close_ads)

    def create_and_join_lobby(self):
        """Creates and joins bots to lobby"""
        self.driver.get('https://skribbl.io/')

        self.button_clicker.click_button(By.CSS_SELECTOR,
        ".fc-button.fc-cta-consent.fc-primary-button") # cookies
        self.button_clicker.click_button(By.CLASS_NAME, "button-create") # create
        self.button_clicker.click_button(By.ID, "button-invite") # invite

        invite_link = pyperclip.paste()

        self.window_manager.open_new_tab(invite_link)

        self.window_manager.switch_window(1)
        self.button_clicker.click_button(By.CLASS_NAME, "button-play") # join
        self.window_manager.switch_window(0)

    def configure_lobby(self):
        """Handles lobby configuration with LobbyConfigurator"""
        lobby_configurator = LobbyConfigurator(self.driver)
        lobby_configurator.apply_settings()
    