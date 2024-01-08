import random
import time

from pr_automation.base import BasePage, clear_element
from pr_automation.locators import Locators


class Other_Deduction(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_otherDeduction(self):
        self.click(Locators.other_deduction)
        time.sleep(3)
        # Add new deduction
        self.click(Locators.add_icon)
        time.sleep(2)
        self.dropdown_click(Locators.emp_id, 1)
        time.sleep(2)
        self.dropdown_click(Locators.deduction_name, 1)
        self.dropdown_click(Locators.deduction_name, 2)
        self.dropdown_click(Locators.pay_month, 2)
        descriptions = self.find_elements(Locators.description_od)
        amounts = self.find_elements(Locators.amount_od)
        print(len(descriptions))
        print(len(amounts))

        for desc in descriptions:
            text = "Extra amount to be deducted"
            self.enter_text1(desc, text)

        for amt in amounts:
            # rupees = "200"
            rupees = random.randint(100, 500)  # Generate a random value
            self.enter_text1(amt, rupees)

        self.click(Locators.submit)
        time.sleep(8)
        print("The other deduction data created successfully! ")
        time.sleep(2)

        # Edit other deduction
        time.sleep(2)
        self.click(Locators.checkbox)
        time.sleep(2)
        self.click(Locators.edit_icon)
        time.sleep(2)
        self.dropdown_click(Locators.emp_id, 1)
        time.sleep(2)
        self.dropdown_click(Locators.deduction_name, 2)
        time.sleep(2)
        self.clear(Locators.pay_month)
        self.dropdown_click(Locators.pay_month, 1)
        descriptions = self.find_elements(Locators.description_od)  # Refresh the descriptions list
        amounts = self.find_elements(Locators.amount_od)  # Refresh the amounts list
        print("The number of deduction and description fields are : ", len(descriptions))
        print("The number of amount fields are ", len(amounts))

        for desc in descriptions:
            text = "Automation"
            self.click1(desc)
            time.sleep(2)
            clear_element(desc)
            time.sleep(2)
            self.enter_text1(desc, text)
            time.sleep(2)

        for amt in amounts:
            rupees = "100"
            self.click1(amt)
            time.sleep(2)
            clear_element(amt)
            time.sleep(2)
            rupees = random.randint(100, 500)
            self.enter_text1(amt, rupees)
            time.sleep(2)

        self.click(Locators.submit)
        time.sleep(3)
        # self.click(Locators.cancel)
        # time.sleep(3)
        print("Selected other deduction data was updated successfully! ")
        time.sleep(2)

        # Delete other deduction
        time.sleep(2)
        self.click(Locators.checkbox)
        time.sleep(3)
        self.click(Locators.delete_icon)
        time.sleep(2)
        self.driver.switch_to.alert.accept()  # Click OK in the alert to delete
        time.sleep(3)
        print("Selected other deduction data was deleted successfully! ")
        time.sleep(2)
