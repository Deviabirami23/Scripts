import time
import requests

from selenium.webdriver.common.by import By

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators
from vehicle_automation.logging_file import get_logger


class Configure_student(BasePage):
    a = "https://royal-dev.techgenzi.com/assets/list"
    b = requests.get(a)
    print(b.status_code)

    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)
        # self.click(Locators.MENU)
        # time.sleep(3)
        self.click(Locators.CONFIGURE)
        time.sleep(10)
        self.click(Locators.STUDENT)

    def add_new_student(self):
        self.click(Locators.CHECKBOX)
        time.sleep(2)
        self.click(Locators.ADD)
        try:
            get_logger().info("To add new data, " + self.get_text(Locators.ALERT_MSG))
            self.click(Locators.OK_BUTTON)
            time.sleep(3)
        except:
            get_logger().warning("There is no alert message")
        finally:
            self.click(Locators.CHECKBOX)  # Deselecting the checkbox
            time.sleep(1)

        # ADD NEW STUDENT
        self.click(Locators.ADD)
        time.sleep(2)
        self.dropdown_click(Locators.STUDENT_SITE_NAME, 1)
        time.sleep(5)
        self.enter_text(Locators.STUDENT_NAME, 'Test A')
        time.sleep(2)
        self.enter_text(Locators.STUDENT_IDCARD, 'TEST001')
        self.enter_text(Locators.DOB, '23-03-2019')
        self.enter_text(Locators.CLASS_NAME, 'I')
        self.enter_text(Locators.SECTION, 'B')
        self.scroll_down()
        self.enter_text(Locators.FATHER_NAME, 'John Henry')
        self.enter_text(Locators.MOTHER_NAME, 'Marry')
        self.enter_text(Locators.CONTACT_NUMBER, '9876512345')
        self.enter_text(Locators.ADDRESS, 'Saibaba colony, CBE-38')
        try:
            self.click(Locators.STUDENT_SUBMIT_BUTTON)
            get_logger().info("Student was created successfully!")
            time.sleep(8)
        except:
            self.is_visible(Locators.STUDENT_CANCEL_BUTTON)
            self.click(Locators.STUDENT_CANCEL_BUTTON)
            print("Student creation failed.")
            time.sleep(5)

    def update_existing_student(self):

        self.click(Locators.STUDENT)

        self.click(Locators.CHECKBOX)
        time.sleep(5)
        self.click(Locators.EDIT)
        time.sleep(2)
        self.dropdown_click(Locators.STUDENT_SITE_NAME, 2)
        self.click_clear_and_enter_text(Locators.STUDENT_NAME, 'Test automation edit')
        self.click_clear_and_enter_text(Locators.STUDENT_IDCARD, 'TEST0101')
        self.click_clear_and_enter_text(Locators.DOB, '23-03-2018')
        self.click_clear_and_enter_text(Locators.CLASS_NAME, 'II')
        self.click_clear_and_enter_text(Locators.SECTION, 'C')
        self.click_clear_and_enter_text(Locators.FATHER_NAME, 'John Henry')
        self.click_clear_and_enter_text(Locators.MOTHER_NAME, 'Marry')
        self.click_clear_and_enter_text(Locators.CONTACT_NUMBER, '9876512345')
        self.click_clear_and_enter_text(Locators.ADDRESS, 'Saibaba Kovil, CBE-38')
        time.sleep(2)
        try:
            self.click(Locators.STUDENT_SUBMIT_BUTTON)
            get_logger().info("Student was updated successfully!")
            time.sleep(8)
        except:
            self.click(Locators.STUDENT_CANCEL_BUTTON)
            get_logger().warning("Student update failed.")
            time.sleep(5)
