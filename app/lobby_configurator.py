"""Module with class for handling lobby configuration"""
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from app.globals import load_config

class LobbyConfigurator:
    """Class loading and lobby configuration and setting it"""
    def __init__(self, driver: WebDriver):
        self.config = load_config()["lobby_settings"]
        self.driver = driver

    def apply_settings(self):
        """Applies settings in the lobby"""
        self.__use_select('item-settings-language', 'language')
        self.__use_select('item-settings-rounds', 'rounds')
        self.__use_select('item-settings-wordcount', 'word_count')

    def __use_select(self, element_id, index):
        if index in self.config:
            select_element = self.driver.find_element(By.ID, element_id)
            select = Select(select_element)
            try:
                select.select_by_visible_text(str(self.config[index]))
            except NoSuchElementException:
                print('Wrong {index} value')
