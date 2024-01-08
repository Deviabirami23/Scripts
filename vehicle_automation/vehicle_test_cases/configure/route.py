import time
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators


class Configure_route(BasePage):
    a = "https://royal-dev.techgenzi.com/assets/list"
    b = requests.get(a)
    print(b.status_code)

    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.locations = ['CBE']  # Initial location

    def route_config(self):
        self.click(Locators.MENU)
        time.sleep(4)
        self.click(Locators.CONFIGURE)
        time.sleep(10)
        self.click(Locators.ROUTE)
        time.sleep(5)
        self.click(Locators.ADD)
        time.sleep(5)
        self.click(Locators.ROUTE_SITE_NAME)
        time.sleep(4)
        self.enter_text(Locators.ROUTE_NAME, 'Aut Route')
        time.sleep(3)
        # self.dropdown_click(Locators.ROUTE_ACTIVE,1)
        time.sleep(3)

        self.enter_text(Locators.LOCATORS_row1[0], 'School')
        self.enter_text(Locators.LOCATORS_row1[1], 'Coimbatore')
        self.enter_text(Locators.LOCATORS_row1[2], '11.029384')
        self.enter_text(Locators.LOCATORS_row1[3], '76.019283')
        self.send_keys(Locators.LOCATORS_row1[4], '01-15')

        self.click(Locators.ADD_STOP)
        time.sleep(2)

        self.enter_text(Locators.LOCATORS_row2[0], 'Giri Nager')
        self.enter_text(Locators.LOCATORS_row2[1], 'Coimbatore')
        self.enter_text(Locators.LOCATORS_row2[2], '11.429384')
        self.enter_text(Locators.LOCATORS_row2[3], '76.059283')
        self.send_keys(Locators.LOCATORS_row2[4], '02-15')
        self.send_keys(Locators.LOCATORS_row2[5], '02-30')

        time.sleep(2)

        self.enter_text(Locators.LOCATORS_row3[0], 'School')
        self.enter_text(Locators.LOCATORS_row3[1], 'Coimbatore')
        self.enter_text(Locators.LOCATORS_row3[2], '11.029384')
        self.enter_text(Locators.LOCATORS_row3[3], '76.019283')
        self.send_keys(Locators.LOCATORS_row3[4], '03-15')

        self.click(Locators.SUBMIT)

        time.sleep(2)

