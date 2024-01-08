import time

from pr_automation.base import BasePage
from pr_automation.locators import Locators
from pr_automation.pr_test_cases import logging


class Income_tax(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_income_tax(self):
        self.click(Locators.tax_slab)
        time.sleep(2)
        self.click(Locators.income_tax)
        time.sleep(2)

