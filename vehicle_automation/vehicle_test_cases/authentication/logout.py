import time
from vehicle_automation.base import BasePage
from selenium.webdriver.common.by import By

from vehicle_automation.locators import Locators


class Logout(BasePage):
    """
    Logout common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        self.click(Locators.PROFILE)
        time.sleep(2)
        self.click(Locators.LOGOUT_BUTTON)
        print("Logged out successfully!!")
