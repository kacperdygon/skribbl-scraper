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
        """Loops through whole game by calling loop_through_round"""
        rount_count = self.config["lobby_settings"]["rounds"]
        # current round
        for i in range(rount_count):
            self.loop_through_round()
            i = i + 1

    def loop_through_round(self):
        """Loops through round by calling loop through turn for every player"""
        print('looping through round')
        player_count = self.config["lobby_settings"]["player_count"]
        i = player_count - 1 # currently drawing player
        while i  > -1:
            current_word = self.load_avaible_words(i)
            self.loop_through_turn(i, player_count, current_word)
            i = i - 1

    def loop_through_turn(self, drawing_player, player_count, current_word):
        """Loops through turn and calls guess_word for every player that
        is not currently drawing"""
        print(f'looping through turn for drawing player {drawing_player}')

        # i - currently guessing player
        for i in range(player_count):
            if i == drawing_player:
                continue
            self.guess_word(current_word, i)

    def load_avaible_words(self, drawing_player):
        """Switches tab and loads avaible words for certain player,
        returns chosen word (first one from the avaible ones),"""
        print(f'loading avaible words for player {drawing_player}')
        self.window_manager.switch_window(drawing_player)
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.words.show .word'))
            )
        words = []
        for element in elements:
            words.append(element.text)
        self.button_clicker.click_button(By.CSS_SELECTOR, '.words.show .word')

        return words[0]

    def guess_word(self, word, guessing_player):
        """Switches tab and guesses word for certain player"""
        print(f'guessing word {word} for player {guessing_player}')
        self.window_manager.switch_window(guessing_player)
        result = self.button_clicker.use_input(By.CSS_SELECTOR, '#game-chat input', word)
        print(f'Guess sent: {result}')
