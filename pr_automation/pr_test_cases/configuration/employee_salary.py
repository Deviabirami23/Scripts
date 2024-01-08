from selenium.common import NoAlertPresentException
from pr_automation.base import BasePage, clear_element
from pr_automation.locators import Locators
import random
import time


class Employee_Salary(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_employee_salary(self):
        self.click(Locators.configuration)
        time.sleep(3)
        self.click(Locators.employee_salary)
        time.sleep(3)
        
# add employee salary config

        self.click(Locators.emp_add)
        time.sleep(2)
        self.dropdown_click(Locators.emp_emp_id, 2)
        time.sleep(5)
        self.dropdown_click(Locators.tds, 1)
        time.sleep(2)
        self.dropdown_click(Locators.regime, 1)
        time.sleep(2)
        self.dropdown_click(Locators.pt, 1)
        time.sleep(2)
        self.dropdown_click(Locators.salary_structure_name, 2)
        time.sleep(2)
        self.dropdown_click(Locators.pay_Wage_type, 1)
        time.sleep(2)
        self.send_keys(Locators.effect_date, "03-06-2023")
        time.sleep(3)
        self.click(Locators.next)
        time.sleep(8)
        month_amt_fields = self.find_elements(Locators.monthly_amount)
        component_type_fields = self.find_elements(Locators.component_type)
        print("No. of component type fields =", len(component_type_fields))
        print("No. of amount fields =", len(month_amt_fields))

        for i in range(len(month_amt_fields)):
            field = month_amt_fields[i]
            component_type = component_type_fields[i].get_attribute("value")
            if component_type == "Earning":
                earn = random.randint(1001, 2000)
                self.enter_text1(field, str(earn))
            elif component_type == "Deduction":
                deduct = random.randint(100, 999)
                if deduct > 0:
                    self.enter_text1(field, str(deduct))
            else:
                print("Invalid component type:", component_type)
            time.sleep(2)

        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Salary structure was created successfully!")
            time.sleep(2)
        except NoAlertPresentException:
            print("Salary structure creation failed.")
            time.sleep(2)

# edit employee salary config

        time.sleep(3)
        checkboxes = self.find_elements(Locators.checkbox)
        if not checkboxes:
            print("No employee salary configuration found for editing.")
        else:
            random_index = random.randint(0, len(checkboxes) - 1)
            checkboxes[random_index].click()
            self.click(Locators.emp_edit)
        time.sleep(2)
        self.dropdown_click(Locators.tds, 2)
        time.sleep(2)
        self.dropdown_click(Locators.pt, 2)
        time.sleep(3)
        self.dropdown_click(Locators.pay_Wage_type, 1)
        time.sleep(7)
        self.send_keys(Locators.effect_date, "09-06-2023")
        time.sleep(5)
        self.click(Locators.next)
        time.sleep(8)

        # month_amt_fields = self.find_elements(Locators.monthly_amount)
        # component_type_fields = self.find_elements(Locators.component_type)

        for i in range(len(month_amt_fields)):
            field = month_amt_fields[i]
            component_type = component_type_fields[i].get_attribute("value")

            self.click1(field)
            time.sleep(2)
            clear_element(field)
            time.sleep(2)

            if component_type == "Earning":
                earn = random.randint(1001, 2000)
                self.enter_text1(field, str(earn))
            elif component_type == "Deduction":
                deduct = random.randint(100, 999)
                if deduct > 0:
                    self.enter_text1(field, str(deduct))
            else:
                print("Invalid component type:", component_type)
            time.sleep(2)

        try:
            self.click(Locators.submit1)
            print("Salary structure was updated successfully!")
            time.sleep(2)
        except NoAlertPresentException:
            print("Salary structure update failed.")
            time.sleep(2)


# delete employee salary config

        time.sleep(5)
        checkboxes = self.find_elements(Locators.checkbox)
        if not checkboxes:
            print("No employee salary configuration found for delete.")
        else:
            random_index = random.randint(0, len(checkboxes) - 1)
            checkboxes[random_index].click()
            self.click(Locators.emp_delete)

            try:
                self.click(Locators.pop_del)
                print("Salary structure was deleted successfully!")
            except NoAlertPresentException:
                print("Salary structure deletion failed.")
