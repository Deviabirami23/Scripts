import time
from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators


class Configurations(BasePage):
    BASE_URL = "https://royal-dev.techgenzi.com/assets/list"

    def __init__(self, driver):
        super().__init__(driver)

    def _configure_role(self, role, role_locators, role_name, role_mobile):
        self.click(Locators.MENU)
        time.sleep(4)
        self.click(Locators.CONFIGURE)
        time.sleep(12)
        self.click(role_locators['ROLE'])
        time.sleep(10)
        self.click(Locators.ADD)
        time.sleep(2)
        self.dropdown_click(role_locators['SITE_NAME'], 1)
        time.sleep(2)
        self.enter_text(role_locators['NAME'], role_name)
        self.enter_text(role_locators['MOBILE_NO'], role_mobile)
        time.sleep(6)
        try:
            self.click(Locators.SUBMIT)
            print(f"{role} created successfully")
            time.sleep(8)
        except:
            self.click(Locators.CANCEL)
            print(f"{role} not created")
            time.sleep(5)

        time.sleep(3)
        self.click(Locators.CHECKBOX)
        time.sleep(3)
        self.click(Locators.EDIT)
        time.sleep(3)
        self.dropdown_click(role_locators['SITE_NAME'], 2)
        self.click_clear_and_enter_text(role_locators['NAME'], f"{role_name} Updated")
        try:
            self.click(Locators.SUBMIT)
            print(f"{role} updated successfully")
            time.sleep(8)
        except:
            self.click(Locators.CANCEL)
            print(f"{role} update failed")
            time.sleep(5)

    def driver_config(self):
        role_locators = {
            'ROLE': Locators.DRIVER,
            'SITE_NAME': Locators.DRIVER_SITE_NAME,
            'NAME': Locators.DRIVER_NAME,
            'MOBILE_NO': Locators.DRIVER_MOBILE_NO,
        }
        self._configure_role('Driver', role_locators, 'KUMAR', '9876212345')

    def conductor_config(self):
        role_locators = {
            'ROLE': Locators.CONDUCTOR,
            'SITE_NAME': Locators.CONDUCTOR_SITE_NAME,
            'NAME': Locators.CONDUCTOR_NAME,
            'MOBILE_NO': Locators.CONDUCTOR_MOBILE_NO,
        }
        self._configure_role('Conductor', role_locators, 'KUMAR', '9876212345')

    def supervisor_config(self):
        role_locators = {
            'ROLE': Locators.SUPERVISOR,
            'SITE_NAME': Locators.SUPERVISOR_SITE_NAME,
            'NAME': Locators.SUPERVISOR_NAME,
            'MOBILE_NO': Locators.SUPERVISOR_MOBILE_NO,
        }
        self._configure_role('Supervisor', role_locators, 'KUMAR', '9876212345')

    def helper_config(self):
        role_locators = {
            'ROLE': Locators.HELPER,
            'SITE_NAME': Locators.HELPER_SITE_NAME,
            'NAME': Locators.HELPER_NAME,
            'MOBILE_NO': Locators.HELPER_MOBILE_NO,
        }
        self._configure_role('Helper', role_locators, 'KUMAR', '9876212345')
