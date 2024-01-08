import time

from pr_automation.base import BasePage
from pr_automation.locators import Locators
from pr_automation.pr_test_cases import logging


class Earned_Leave(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # add new deduction
    def add_earnedLeave(self):

        #add earned leave
        self.click(Locators.earned_leave)
        self.click(Locators.add_icon)
        self.dropdown_click(Locators.emp_id, 4)
        self.send_keys(Locators.noOfDays, 20)
        time.sleep(2)
        self.click(Locators.submit)
        time.sleep(3)
        self.click(Locators.cancel)
        time.sleep(2)

        #edit earned leave
        self.click(Locators.checkbox)
        self.click(Locators.edit_icon)
        self.clear(Locators.emp_id)
        self.dropdown_click(Locators.emp_id, 3)
        self.clear(Locators.noOfDays)
        self.send_keys(Locators.noOfDays,25)
        self.click(Locators.submit)
        self.click(Locators.cancel)
        time.sleep(2)

        #delete earned leave
        self.click(Locators.checkbox)
        time.sleep(2)
        self.click(Locators.delete_icon)
        time.sleep(2)
        self.driver.switch_to.alert.accept()  # for click ok to in alert to delete
        time.sleep(3)
        # self.driver.switch_to.alert.dismiss()                 # for clicking cancel in alert




