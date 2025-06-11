"""main"""
from app.utils.web_driver import WebDriverManager
from app.skribbl_scraper import SkribblScraper
from app.globals import load_config



config = load_config()
selected_browser = config["browser"]
browser_profile_path = config["browser_profile_path"]

driver = WebDriverManager(selected_browser, browser_profile_path).get_driver()

bot = SkribblScraper(driver, config)

bot.create_and_join_lobby()
bot.configure_lobby()
bot.start_game()

input('Click enter to continue...')
driver.quit()
