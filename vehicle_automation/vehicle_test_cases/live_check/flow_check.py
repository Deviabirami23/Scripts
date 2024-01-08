import configparser
import time

import requests

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators
from vehicle_automation.logging_file import get_logger

config = configparser.ConfigParser()
config.read("./settings.conf")


class flow_check(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_flow(self):
        url = 'https://track.parivahaneye.com'
        response = requests.get(url)

        self.driver.maximize_window()
        time.sleep(3)
        self.enter_text(Locators.USERNAME, 'Vijayakumar.samiyappan@techgenzi.com')
        self.enter_text(Locators.PASSWORD, '9150047713@Pari')
        self.click(Locators.EYE_BUTTON)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)

        self.click(Locators.MENU)

        self.click(Locators.DASHBOARD)
        self.click(Locators.STATUS_TAB)
        cards = [Locators.ALL_VEHICLES, Locators.GPS_INSTALLED, Locators.RUNNING_VEHICLES, Locators.IDLE_VEHICLES,
                 Locators.STOPPED_VEHICLES, Locators.OUT_OF_NETWORK]
        for card in cards:
            self.click(cards)
            time.sleep(4)
            self.click(Locators.CLOSE)
            time.sleep(2)

        self.click(Locators.FILTER_TAB)
        self.click(Locators.FILTER_BUTTON)

        self.click(Locators.HEALTH_DASHBOARD)

        self.click(Locators.REPORTS)
        reports = [Locators.OVERSPEED_TAB, Locators.GEOFENCE_TAB, Locators.NOTIFICATION_TAB, Locators.DAYWISE_TAB,
                   Locators.SUMMARY_TAB, Locators.NON_WORKING_HOURS_TAB, Locators.NOT_TRACKING_TAB,
                   Locators.FILLTOFILL_TAB,
                   Locators.MANAGEMENT_REPORT, Locators.TRIP_REPORT, Locators.FUELFILL_TAB, Locators.GATEPASS_TAB,
                   Locators.REPORT_DASHBOARD]

        for report in reports:
            self.click(reports)
            time.sleep(8)

        self.click(Locators.USER_AND_ROLES)

        self.click(Locators.COMPANY)
        self.click(Locators.COMPANY_CODE_TAB)
        self.click(Locators.COMPANY_CODE_ASSIGN)

        self.click(Locators.CONFIGURE)
        configure_list = [Locators.VEHICLE, Locators.STUDENT, Locators.STUDENT_ASSIGN, Locators.ROUTE,
                          Locators.PARENT, Locators.DRIVER, Locators.CONDUCTOR, Locators.SUPERVISOR,
                          Locators.HELPER, Locators.ASSIGN]
        for config_list in configure_list:
            self.click(configure_list)
            time.sleep(8)
            if self.is_visible(Locators.GO_BACK):
                self.click(Locators.GO_BACK)
