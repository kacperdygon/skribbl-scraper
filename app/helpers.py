"""Various helper functions"""

def switch_window(driver, index):
    """Handles switching window"""
    tabs = driver.window_handles
    driver.switch_to.window(tabs[index])