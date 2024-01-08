import time

from selenium.webdriver import Keys, ActionChains

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators


class Playback(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def playback(self):
        self.click(Locators.PLAYBACK)
        time.sleep(2)
        self.dropdown_click(Locators.PLAYBACK_SITE, 1)
        time.sleep(2)
        self.enter_text(Locators.PLAYBACK_DATE, "23-12-2023 15:30")
        self.dropdown_click(Locators.PLAYBACK_VEHICLE, 1)
        self.click(Locators.PLAYBACK_BUTTON)
