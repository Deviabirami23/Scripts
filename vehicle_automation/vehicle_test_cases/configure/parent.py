import time
import time
import unittest

import requests

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators
from vehicle_automation.logging_file import GetLogger, get_logger


# logging.basicConfig(level=logging.INFO)


class Configure_parent(BasePage, unittest.TestCase, GetLogger):

    def __init__(self, driver):
        super().__init__(driver)
        # self.click(Locators.MENU)
        time.sleep(4)
        self.click(Locators.CONFIGURE)
        time.sleep(10)
        self.click(Locators.PARENT)
        time.sleep(5)

    def add_new_parent(self):

        self.click(Locators.CHECKBOX)
        time.sleep(2)
        self.click(Locators.ADD)
        try:
            get_logger().info("To add new data, " + self.get_text(Locators.ALERT_MSG))
            self.click(Locators.OK_BUTTON)
            time.sleep(2)
        except:
            get_logger().info("There is no alert message")
        finally:
            self.click(Locators.CHECKBOX)  # Deselecting the checkbox
            time.sleep(1)

        self.click(Locators.ADD)
        time.sleep(2)
        self.click(Locators.SUBMIT)
        time.sleep(1)

        try:
            print(self.get_text(Locators.SITE_ALERT) + ", for site name")
            print(self.get_text(Locators.PARENT_NAME_ALERT) + ", for parent name")
            print(self.get_text(Locators.PARENT_MOBILE_NUMBER_ALERT) + ", for mobile number")

        except:
            print("There is no alert messages for required fields")

        a = self.dropdown_click(Locators.PARENT_SITE_NAME, 2)
        b = self.enter_text(Locators.PARENT_NAME, 'John')
        c = self.enter_text(Locators.MOBILE_NUMBER, '9876519345')
        # self.click(Locators.LOGIN_REQUIRED)
        url = 'https://demoapi.parivahaneye.com/users/'

        response = requests.post(url, json={
            "site": a,
            "name": b,
            "mobile": c
        })

        time.sleep(2)
        try:
            self.click(Locators.PARENT_SUBMIT_BUTTON)
            if response.status_code == 200:
                get_logger().info(f"Parent was created successfully!. Status code: {response.status_code}")
                time.sleep(8)
            else:
                get_logger().warning(f"Failed to create parent. Status code: {response.status_code}")
                print(response.text)  # Print the response content for debugging
                time.sleep(5)
                self.click(Locators.PARENT_CANCEL_BUTTON)

        except:
            print(response.content)
            self.click(Locators.PARENT_CANCEL_BUTTON)
            get_logger().warning(f"Failed to create parent. Status code: {response.status_code}")

        time.sleep(3)

    def edit_existing_parent(self):
        self.click(Locators.EDIT)
        time.sleep(10)
        try:
            get_logger().info("To edit data, " + self.get_text(Locators.ALERT_MSG))
            self.click(Locators.OK_BUTTON)
            time.sleep(2)
        except:
            get_logger().warning("There is no alert message")
        finally:
            self.click(Locators.PARENT)
            time.sleep(2)

        time.sleep(3)
        self.click(Locators.CHECKBOX)

        self.click(Locators.EDIT)
        self.dropdown_click(Locators.PARENT_SITE_NAME, 2)
        self.click_clear_and_enter_text(Locators.PARENT_NAME, 'John Henry')
        try:
            self.click(Locators.PARENT_SUBMIT_BUTTON)
            get_logger().info(f"Parent was updated successfully!. ")
            time.sleep(8)
        except:
            self.click(Locators.PARENT_CANCEL_BUTTON)
            get_logger().warning(f"Parent update failed.")
            time.sleep(5)

