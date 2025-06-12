"""Module with class handling bot joining"""
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from app.utils.window_manager import WindowManager
from app.utils.button_clicker import ButtonClicker

class BotJoiner():
    """Class handling joining game with other bots"""

    def __init__(self, window_manager: WindowManager, driver: WebDriver,
                 config: dict, join_link: str):
        self.window_manager = window_manager
        self.driver = driver
        self.config = config
        self.join_link = join_link

    def join_all_bots(self):
        """Handles bot joining with loop"""
        i = 1 # starts at 1 because index 0 is already assigned to host
        player_count = self.config['lobby_settings']['player_count']
        while i < player_count:
            time.sleep(1)
            self.join_bot(i)
            i += 1


    def join_bot(self, index):
        """Opens new tab and joins with a new bot"""
        button_clicker = ButtonClicker(self.driver, self.config)

        self.window_manager.open_new_tab(self.join_link)
        self.window_manager.switch_window(index)
        button_clicker.click_button(By.CLASS_NAME, "button-play") # join
