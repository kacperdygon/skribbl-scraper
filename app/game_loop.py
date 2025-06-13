"""Manages game loop"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from app.handlers.button_clicker import ButtonClicker
from app.handlers.window_manager import WindowManager
from app.word_saver import WordSaver
from app.scrape_speed_tracker import ScrapeSpeedTracker

class GameLoop:
    """Manages game loop"""
    def __init__(self, driver: WebDriver, button_clicker: ButtonClicker,
                 word_saver: WordSaver, config):
        self.config = config
        self.driver = driver
        self.button_clicker = button_clicker
        self.window_manager = WindowManager(driver)
        self.word_saver = word_saver
        self.scrape_speed_tracker = None

    def start(self):
        """Loops through whole game by calling loop_through_round"""
        rount_count = self.config["lobby_settings"]["rounds"]
        # current round
        for i in range(rount_count):
            self.loop_through_round()
            i = i + 1

    def loop_through_round(self):
        """Loops through round by calling loop through turn for every player"""
        player_count = self.config["lobby_settings"]["player_count"]
        i = player_count - 1 # currently drawing player
        while i  > -1:
            current_word = self.load_avaible_words(i)
            self.loop_through_turn(i, player_count, current_word)
            i = i - 1

    def loop_through_turn(self, drawing_player, player_count, current_word):
        """Loops through turn and calls guess_word for every player that
        is not currently drawing"""

        # i - currently guessing player
        for i in range(player_count):
            if i == drawing_player:
                continue
            self.guess_word(current_word, i)

    def load_avaible_words(self, drawing_player):
        """Switches tab and loads avaible words for certain player,
        sends them to WordSaver"""
        self.window_manager.switch_window(drawing_player)
        wait = WebDriverWait(self.driver, self.config["timeout"])
        # check if words were hidden yet so next statement won't load words from previous round
        wait.until(lambda d: all(
            not e.is_displayed() for e in d.find_elements(By.CSS_SELECTOR, '.words.show .word')
            ))
        elements = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.words.show .word'))
            )
        words = []
        for element in elements:
            words.append(element.text)
        self.word_saver.save_words(words)

        if self.scrape_speed_tracker:
            self.scrape_speed_tracker.record(self.config["lobby_settings"]["word_count"])

        self.button_clicker.click_button(By.CSS_SELECTOR, '.words.show .word')

        return words[0]

    def guess_word(self, word, guessing_player):
        """Switches tab and guesses word"""
        self.window_manager.switch_window(guessing_player)
        self.button_clicker.use_input(By.CSS_SELECTOR, '#game-chat input', word)

    def set_scrape_speed_tracker(self, scrape_speed_tracker: ScrapeSpeedTracker):
        """Sets scrape speed tracker for tests"""
        self.scrape_speed_tracker = scrape_speed_tracker
