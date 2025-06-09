from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://skribbl.io/')

wait = WebDriverWait(driver, 10)

accept_cookies_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button"))
)

accept_cookies_button.click()

create_game_button = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "button-create"))
)

create_game_button.click()

get_invite_button = wait.until(
    EC.element_to_be_clickable((By.ID, "button-invite"))
)

get_invite_button.click()

invite_link = pyperclip.paste()

driver.execute_script(f"window.open('{invite_link}', '_blank');")
tabs = driver.window_handles
driver.switch_to.window(tabs[1])

play_game_button = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "button-play"))
)

play_game_button.click()

driver.switch_to.window(tabs[0])

input('Naciśnij coś')
driver.quit()