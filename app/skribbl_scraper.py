"""Good bot"""
import sqlite3
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pyperclip
from app.utils.button_clicker import ButtonClicker
from app.utils.window_manager import WindowManager
from app.lobby_configurator import LobbyConfigurator
from app.game_loop import GameLoop
from app.word_saver import WordSaver
from app.bot_joiner import BotJoiner

class SkribblScraper:
    """Handles everything"""
    def __init__(self, driver: WebDriver, database_connection: sqlite3.Connection, config: dict):
        self.driver = driver
        self.config = config
        self.url = 'https://skribbl.io/'
        self.window_manager = WindowManager(driver)
        self.database_connection = database_connection

    def create_and_join_lobby(self):
        """Creates lobby"""
        self.driver.get('https://skribbl.io/')

        button_clicker = ButtonClicker(self.driver, self.config)

        button_clicker.click_button(By.CSS_SELECTOR,
        ".fc-button.fc-cta-consent.fc-primary-button") # cookies
        button_clicker.click_button(By.CLASS_NAME, "button-create") # create
        button_clicker.click_button(By.ID, "button-invite") # invite

    def join_lobby_with_bots(self):
        """Manages joining lobby with other bots in new tabs"""
        invite_link = pyperclip.paste()

        bot_joiner = BotJoiner(self.window_manager, self.driver, self.config, invite_link)
        bot_joiner.join_all_bots()

    def configure_lobby(self):
        """Handles lobby configuration with LobbyConfigurator"""
        print("configuring lobby")
        lobby_configurator = LobbyConfigurator(self.driver, self.config)
        lobby_configurator.apply_settings()

    def start_game(self):
        """Handles game start"""

        word_saver = WordSaver(self.database_connection, self.config)
        button_clicker = ButtonClicker(self.driver, self.config)

        while True:
            print('starting game...')
            self.window_manager.switch_window(0)
            button_clicker.click_button(By.ID, 'button-start-game') # start game
            game_loop = GameLoop(self.driver, button_clicker, self.window_manager,
                                 word_saver, self.config)
            game_loop.start()
