import time

from pr_automation.base import BasePage
from pr_automation.locators import Locators


class Earning(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        driver.implicitly_wait(5)

    ### add new earning ###
    def add_earning(self):
        self.click(Locators.configuration)
        time.sleep(2)
        self.click(Locators.earning)
        time.sleep(2)
        # Add new earning
        self.click(Locators.add_icon)
        time.sleep(2)
        self.enter_text(Locators.name, 'Basic amount test')
        time.sleep(2)
        self.enter_text(Locators.payslip, 'Basic pay')
        time.sleep(2)
        self.dropdown_click(Locators.calc, 2)
        time.sleep(2)
        self.dropdown_click(Locators.pf, 1)
        self.dropdown_click(Locators.tax_type, 1)
        self.enter_text(Locators.description, 'Automation')
        self.dropdown_click(Locators.pay_type, 1)
        self.dropdown_click(Locators.active, 1)
        self.dropdown_click(Locators.esi, 1)
        self.dropdown_click(Locators.flexible, 1)
        time.sleep(2)
        try:
            self.click(Locators.submit)
            print("Earning was created successfully!")
            time.sleep(8)
        except:
            self.click(Locators.cancel)
            print("Earning creation failed.")
            time.sleep(5)

        ### edit earning ###

        # time.sleep(2)
        # checkboxes = self.find_elements(Locators.checkbox)
        # random_index = random.randint(0, len(checkboxes) - 1)
        # checkbox = checkboxes[random_index]
        # if not checkboxes:
        #     print("No employee salary configuration found for editing.")
        # else:
        #     checkboxes[random_index].click()
        #     time.sleep(2)
        self.click(Locators.checkbox)
        time.sleep(2)
        self.click(Locators.edit_icon)
        time.sleep(2)
        self.clear(Locators.name)
        time.sleep(2)
        self.send_keys(Locators.name, 'Basic Pay test')
        self.clear(Locators.payslip)
        self.send_keys(Locators.payslip, 'Basic Pay one')
        time.sleep(2)
        self.clear(Locators.calc)
        self.dropdown_click(Locators.calc, 1)
        self.clear(Locators.pf)
        self.dropdown_click(Locators.pf, 2)
        self.dropdown_click(Locators.tax_type, 2)
        self.clear(Locators.description)
        self.send_keys(Locators.description, 'Automation update')
        self.dropdown_click(Locators.pay_type, 2)
        self.dropdown_click(Locators.active, 2)
        self.dropdown_click(Locators.esi, 2)
        self.dropdown_click(Locators.flexible, 2)
        time.sleep(2)
        self.click(Locators.submit)
        time.sleep(5)
        print("Selected Earning was updated successfully!")
        time.sleep(2)

        ### delete earning ###
        time.sleep(2)
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
