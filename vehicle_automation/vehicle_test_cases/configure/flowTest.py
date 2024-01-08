import time
import requests

from selenium.webdriver.common.by import By

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators


class WorkFlow(BasePage):
    a = "https://royal-dev.techgenzi.com/assets/list"
    b = requests.get(a)
    print(b.status_code)


    def __init__(self, driver):
        super().__init__(driver)

    def test_workflow(self):
        self.click(Locators.MENU)
        time.sleep(4)
        self.click(Locators.CONFIGURE)
        time.sleep(10)
        self.click(Locators.VEHICLE)
        time.sleep(5)
        self.click(Locators.ADD)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(2)
        self.dropdown_click(Locators.VEH_SITE_NAME,1)
        self.enter_text(Locators.VEH_NAME,'Vehicle number 1')
        try:
            self.click(Locators.SUBMIT)
            print("Vehicle was created successfully!")
            time.sleep(8)
        except:
            self.click(Locators.CANCEL)
            print("Vehicle creation failed.")
            time.sleep(5)

        self.click(Locators.STUDENT)

        self.dropdown_click(Locators.STUDENT_SITE_NAME, 1)
        time.sleep(2)
        self.enter_text(Locators.STUDENT_NAME, 'Test flow')
        self.enter_text(Locators.STUDENT_IDCARD, 'TEST001')
        self.enter_text(Locators.CLASS_NAME, 'I')
        self.enter_text(Locators.SECTION, 'B')
        self.enter_text(Locators.CONTACT_NUMBER, '9876512345')
        try:
            self.click(Locators.SUBMIT)
            print("Student was created successfully!")
            time.sleep(8)
        except:
            self.click(Locators.CANCEL)
            print("Student creation failed.")
            time.sleep(5)

        self.click(Locators.PARENT)
        time.sleep(5)
        self.click(Locators.ADD)
        time.sleep(2)
        self.dropdown_click(Locators.PARENT_SITE_NAME, 1)
        self.enter_text(Locators.PARENT_NAME, 'Test flow')
        self.enter_text(Locators.MOBILE_NUMBER, '9876512345')
        self.click(Locators.LOGIN_REQUIRED)
        time.sleep(2)
        if self.click(Locators.SUBMIT):
            time.sleep(2)
            print("Parent created successfully")
        else:
            print("Parent not created")
            self.click(Locators.CLOSE)


