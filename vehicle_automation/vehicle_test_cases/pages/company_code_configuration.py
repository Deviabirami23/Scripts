import time

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators


class Company_code_config(BasePage):
    BASE_URL = "https://royal-dev.techgenzi.com/assets/list"

    def __init__(self, driver):
        super().__init__(driver)

    def config_comp_code(self):
        self.click(Locators.COMPANY)
        time.sleep(2)
        self.click(Locators.COMPANY_CODE_TAB)
        time.sleep(2)
        self.click(Locators.COMPANY_ADD_BUTTON)
        time.sleep(2)
        self.enter_text(Locators.COMPANY_NAME, 'Test data')
        time.sleep(2)
        self.enter_text(Locators.COMPANY_CODE, 'Aut')
        time.sleep(2)
        self.enter_text(Locators.COMPANY_ADDRESS, 'Saibaba colony')
        time.sleep(2)
        try:
            self.click(Locators.SUBMIT_BUTTON)
            print("Company Code was created successfully!")
            time.sleep(8)
        except:
            self.click(Locators.CANCEL_BUTTON)
            print("Company Code not created")
            time.sleep(5)



        self.click(Locators.CHECKBOX)
        time.sleep(2)
        self.click(Locators.COMPANY_EDIT_BUTTON)
        time.sleep(2)
        self.click_clear_and_enter_text(Locators.COMPANY_NAME, 'Test Edit')
        time.sleep(2)
        self.enter_text(Locators.COMPANY_CODE, 'Aut')
        time.sleep(2)
        self.enter_text(Locators.COMPANY_ADDRESS, 'Saibaba colony, CBE')
        time.sleep(2)
        try:
            self.click(Locators.SUBMIT_BUTTON)
            print("Company Code was updated successfully!")
            time.sleep(8)
        except:
            self.click(Locators.CANCEL_BUTTON)
            print("Company Code not updated")
            time.sleep(5)

        time.sleep(2)
        self.click(Locators.CHECKBOX)
        time.sleep(2)
        self.click(Locators.COMPANY_DELETE_BUTTON)
        time.sleep(2)
        try:
            self.click(Locators.YES_BUTTON)
            print("Company Code was DELETED successfully!")
            time.sleep(8)
        except:
            self.click(Locators.NO_BUTTON)
            print("Company Code not deleted")
            time.sleep(5)
