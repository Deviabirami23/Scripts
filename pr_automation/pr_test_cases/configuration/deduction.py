import time
from lib2to3.pgen2 import driver
from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pr_automation.base import BasePage
from pr_automation.locators import Locators


class Deduction(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.error_handler = None

    # add new deduction
    def add_deduction(self):
        self.click(Locators.configuration)
        self.click(Locators.deduction)
        self.click(Locators.add_icon)
        time.sleep(2)
        self.enter_text(Locators.name, 'Deduction Y')
        self.enter_text(Locators.payslip, 'Deduction A')
        time.sleep(2)
        self.dropdown_click(Locators.deduction_type, 1)
        self.dropdown_click(Locators.active, 1)
        self.enter_text(Locators.description, 'Automation')
        time.sleep(2)
        self.dropdown_click(Locators.pay_type, 2)
        time.sleep(2)
        self.dropdown_click(Locators.calc, 2)
        time.sleep(3)

        selected_option = self.get_selected_option(Locators.pay_type)
        if selected_option == "Variable":
            self.dropdown_click(Locators.other_det, 1)
            time.sleep(2)
            self.click(Locators.submit)
            time.sleep(5)
            print("The Deduction created successfully!")
            time.sleep(2)
        else:
            self.click(Locators.submit)
            time.sleep(5)
            print("The Deduction created successfully!")
            time.sleep(2)

        # edit deduction
        time.sleep(2)
        self.click(Locators.checkbox)
        time.sleep(2)
        self.click(Locators.edit_icon)
        time.sleep(2)
        self.click(Locators.name)
        time.sleep(2)
        self.clear(Locators.name)
        time.sleep(2)
        self.send_keys(Locators.name, 'Test B')
        self.click(Locators.payslip)
        self.clear(Locators.payslip)
        time.sleep(2)
        self.send_keys(Locators.payslip, 'Test Z')
        self.dropdown_click(Locators.deduction_type, 2)
        self.dropdown_click(Locators.active, 2)
        self.dropdown_click(Locators.pay_type, 2)
        self.dropdown_click(Locators.calc, 1)
        selected_option = self.get_selected_option(Locators.pay_type)
        time.sleep(2)
        if selected_option == "Variable":
            self.dropdown_click(Locators.other_det, 1)
            time.sleep(2)
            self.click(Locators.submit)
            time.sleep(5)
            print("Selected deduction was updated successfully!")
            time.sleep(2)

        else:
            self.click(Locators.submit)
            time.sleep(5)
            print("Selected deduction was updated successfully!")
            time.sleep(2)


        # delete deduction

        time.sleep(2)
        self.click(Locators.checkbox)
        time.sleep(2)
        self.click(Locators.delete_icon)
        time.sleep(2)
        self.driver.switch_to.alert.accept()  # for click ok to in alert to delete
        time.sleep(2)
        print("Selected deduction was deleted successfully!")
        time.sleep(2)
        # self.driver.switch_to.alert.dismiss()  # for clicking cancel in alert

    def assertTrue(self, param):
        pass

    def is_element_enabled(self, other_det):
        pass
