"""main"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from app.clicker import ButtonClicker
from app.helpers import switch_window

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://skribbl.io/')

button_clicker = ButtonClicker(driver, 10)

# #cookies
button_clicker.click_button(By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")

#create
button_clicker.click_button(By.CLASS_NAME, "button-create")

#invite
button_clicker.click_button(By.ID, "button-invite")

invite_link = pyperclip.paste()

driver.execute_script(f"window.open('{invite_link}', '_blank');")

switch_window(driver, 1)

#join
button_clicker.click_button(By.CLASS_NAME, "button-play")

switch_window(driver, 0)

#play game
# button_clicker.click_button(By.ID, "button-start-game")

input('Naciśnij coś')
driver.quit()
