import time
from lib2to3.pgen2 import driver

import requests

from selenium.webdriver.common.by import By

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators


class Assign(BasePage):
    a = "https://royal-dev.techgenzi.com/assets/list"
    b = requests.get(a)
    print(b.status_code)

    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def assign_config(self):
        self.click(Locators.MENU)
        time.sleep(4)
        self.click(Locators.CONFIGURE)
        time.sleep(10)
        self.click(Locators.ASSIGN)
        time.sleep(3)
        self.click(Locators.SELECT_1)
        time.sleep(5)
        self.click(Locators.selection_1)
        time.sleep(5)
        print("i")
        self.dropdown_click(Locators.SELECT_1_VALUE, 3)
        print('j')
        self.click(Locators.SELECT_2)
        self.click(Locators.selection_2)
        time.sleep(5)
        self.click(Locators.SELECT_TO_ASSIGN)
        time.sleep(2)
        self.click(Locators.ASSIGN_BUTTON)
        time.sleep(3)
        self.click(Locators.SUBMIT)
        try:
            self.click(Locators.SUBMIT)
            print("Assigned successfully!")
            time.sleep(8)
        except:
            self.click(Locators.CANCEL)
            print("Not Assigned, try new!!")
            time.sleep(5)
