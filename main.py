"""main"""
import sqlite3
from app.utils.web_driver import WebDriverManager
from app.skribbl_scraper import SkribblScraper
from app.globals import load_config

config = load_config()
selected_browser = config["browser"]
browser_profile_path = config["browser_profile_path"]

connection = sqlite3.connect('words')

driver = WebDriverManager(selected_browser, browser_profile_path).get_driver()

bot = SkribblScraper(driver, connection, config)

bot.create_and_join_lobby()
bot.configure_lobby()
bot.join_lobby_with_bots()
bot.start_game()

connection.close()
driver.quit()
