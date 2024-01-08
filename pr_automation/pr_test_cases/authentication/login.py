import time
import unittest

from selenium.webdriver.chrome import webdriver

from pr_automation.base import BasePage
from selenium.webdriver.common.by import By
from pr_automation.locators import Locators


class Login(BasePage):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self):
        self.send_keys(Locators.USERNAME_INPUT, "ithod@pgc.com")
        self.send_keys(Locators.PASSWORD_INPUT, "Dev@12345")
        time.sleep(2)
        # self.is_clickable(Locators.LOGIN_SUBMIT_BUTTON)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        time.sleep(20)
        print("Logged in successfully")
        self.click(Locators.PAYROLL_CARD)
        time.sleep(2)

    def assertTrue(self, LOGIN_SUBMIT_BUTTON):
        pass

    def get_logger(self):
        pass
