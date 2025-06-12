"""Module with class for handling lobby configuration"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from app.utils.button_clicker import ButtonClicker

class LobbyConfigurator:
    """Class loading and lobby configuration and setting it"""
    def __init__(self, driver: WebDriver, config):
        self.config = config
        self.driver = driver

    def apply_settings(self):
        """Applies settings in the lobby"""
        self.__use_select('item-settings-slots', 'player_count')
        self.__use_select('item-settings-language', 'language')
        self.__use_select('item-settings-rounds', 'rounds')
        self.__use_select('item-settings-wordcount', 'word_count')

    def __use_select(self, element_id, index):
        if index in self.config["lobby_settings"]:
            button_clicker = ButtonClicker(self.driver, self.config)
            button_clicker.click_select(By.ID, element_id, self.config["lobby_settings"][index])
