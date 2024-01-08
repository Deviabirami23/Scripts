import time
from pr_automation.base import BasePage
from selenium.webdriver.common.by import By

from pr_automation.locators import Locators


class Logout(BasePage):
    """
    Logout common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)

    # def do_logout(self):
    #     """
    #     Click the account icon and then click logout link
    #     :return:
    #     """
    #     self.click(Locators.PROFILE)
    #     self.click(Locators.LOGOUT_BUTTON)
    #     # self.hover_to(Locators.ACCOUNT_MENU)
    #     # self.click(Locators.LOGOUT_LINK)

    def do_logout(self):
        self.click(Locators.PROFILE_CLICK)
        time.sleep(2)
        self.click(Locators.LOGOUT_BUTTON)
        time.sleep(3)
        print("Logged out Successfully!!")
