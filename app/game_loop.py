"""Manages game loop"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from app.utils.button_clicker import ButtonClicker
from app.utils.window_manager import WindowManager

class GameLoop:
    """Manages game loop"""
    def __init__(self, driver: WebDriver, button_clicker: ButtonClicker,
                 window_manager: WindowManager, config):
        self.config = config
        self.driver = driver
        self.button_clicker = button_clicker
        self.window_manager = window_manager

    def start(self):
        rount_count = self.config["lobby_settings"]["rounds"]
        i = 0
        while i < rount_count:
            self.loop_through_round()
            i = i + 1

    def loop_through_round(self):
        player_count = self.config["lobby_settings"]["player_count"]
        i = player_count - 1 # currently drawing player
        while i  > -1:
            self.window_manager.switch_window(i)
            current_word = self.load_avaible_words()
            self.loop_through_turn(i, player_count, current_word)
            i = i - 1

    def loop_through_turn(self, current_player, player_count, current_word):

        i = 0 # currently guessing player
        while i < player_count:
            if i == current_player:
                break
            self.window_manager.switch_window(i)
            self.guess_word(current_word)
            i = i + 1

    def load_avaible_words(self):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.words.show .word'))
            )
        print('located')
        words = []
        for element in elements:
            words.append(element.text)
        self.button_clicker.click_button(By.CSS_SELECTOR, '.words.show .word')

        return words[0]

    def guess_word(self, word):
        print('word:', word)
        input()
        element = self.driver.find_element(By.CSS_SELECTOR, '#game-chat input')
        print(element.tag_name)
        print(element.is_displayed(), element.is_enabled())

        input()

        self.button_clicker.use_input(By.CSS_SELECTOR, '#game-chat input', word)
