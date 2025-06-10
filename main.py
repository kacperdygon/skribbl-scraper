"""main"""
from app.web_driver import WebDriverManager
from app.skribbl_scraper import SkribblScraper
from app.globals import load_config

selectedBrowser = load_config()["browser"]
driver = WebDriverManager(selectedBrowser).get_driver()

bot = SkribblScraper(driver)

bot.create_and_join_lobby()
bot.configure_lobby()

input('Naciśnij coś')
driver.quit()
