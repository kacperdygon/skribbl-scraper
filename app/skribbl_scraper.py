"""Good bot"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pyperclip
from app.utils.button_clicker import ButtonClicker
from app.utils.window_manager import WindowManager
from app.lobby_configurator import LobbyConfigurator
from app.game_loop import GameLoop

class SkribblScraper:
    """Handles everything"""
    def __init__(self, driver: WebDriver, config: dict):
        self.driver = driver
        self.config = config
        self.url = 'https://skribbl.io/'
        self.button_clicker = ButtonClicker(driver, config)
        self.window_manager = WindowManager(driver)

    def create_and_join_lobby(self):
        """Creates and joins bots to lobby"""
        self.driver.get('https://skribbl.io/')

        self.button_clicker.click_button(By.CSS_SELECTOR,
        ".fc-button.fc-cta-consent.fc-primary-button") # cookies
        self.button_clicker.click_button(By.CLASS_NAME, "button-create") # create
        self.button_clicker.click_button(By.ID, "button-invite") # invite

        invite_link = pyperclip.paste()

        time.sleep(1) # avoid "joining too quickly" error

        self.window_manager.open_new_tab(invite_link)
        self.window_manager.switch_window(1)
        self.button_clicker.click_button(By.CLASS_NAME, "button-play") # join
        self.window_manager.switch_window(0)


    def configure_lobby(self):
        """Handles lobby configuration with LobbyConfigurator"""
        lobby_configurator = LobbyConfigurator(self.driver, self.config)
        lobby_configurator.apply_settings()

    def start_game(self):
        """Handles game start"""
        self.button_clicker.click_button(By.ID, 'button-start-game') # start game
        game_loop = GameLoop(self.driver, self.button_clicker, self.window_manager, self.config)
        game_loop.start()
        