import time
import requests

from selenium.webdriver.common.by import By

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators
from vehicle_automation.logging_file import get_logger


class Configure_studentRouteAssign(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.click(Locators.MENU)
        # time.sleep(2)
        self.click(Locators.CONFIGURE)
        time.sleep(3)

    def add_studentRouteAssign(self):

        self.click(Locators.STUDENT_ASSIGN)
        time.sleep(10)
        self.click(Locators.ADD)
        time.sleep(10)
        self.dropdown_click(Locators.STUDENT_NAME_ASSIGN, 2)
        self.dropdown_click(Locators.ASSIGN_ROUTE_NAME, 2)
        self.dropdown_click(Locators.ASSIGN_STOP_NAME, 2)
        time.sleep(2)
        self.click(Locators.ADD_ROUTE_BUTTON)
        time.sleep(2)
        self.click(Locators.DELETE_ROUTE_BUTTON)
        time.sleep(4)
        try:
            self.click(Locators.SUBMIT)
            get_logger().info("Route was assigned to the student successfully!")
            time.sleep(8)
        except:
            self.click(Locators.GO_BACK)
            get_logger().warning("Route was not assigned to the student")
            time.sleep(5)

    def edit_studentRouteAssign(self):

        time.sleep(3)
        self.click(Locators.STUDENT_ASSIGN)
        time.sleep(10)
        try:
            get_logger().info("To edit data, " + self.get_text(Locators.ALERT_MSG))
            self.click(Locators.OK_BUTTON)
            time.sleep(2)
        except:
            get_logger().warning("There is no alert message")
        finally:
            self.click(Locators.CHECKBOX)  # Deselecting the checkbox

        time.sleep(3)
        self.click(Locators.EDIT)
        time.sleep(7)
        self.dropdown_click(Locators.STUDENT_NAME_ASSIGN, 3)
        self.dropdown_click(Locators.ASSIGN_ROUTE_NAME, 2)
        self.dropdown_click(Locators.ASSIGN_STOP_NAME, 2)
        self.click(Locators.ADD_ROUTE_BUTTON)
        self.click(Locators.DELETE_ROUTE_BUTTON)
        try:
            self.click(Locators.SUBMIT)
            get_logger().info("Route was updated to the student successfully!")
            time.sleep(8)
        except:
            self.click(Locators.GO_BACK)
            get_logger().warning("Route was not updated to the student")
            time.sleep(5)




    def delete_studentRouteAssign(self):
        self.click(Locators.STUDENT_ASSIGN)
        time.sleep(3)
        self.click(Locators.DELETE)
        time.sleep(2)
        try:
            get_logger().info("To delete data, " + self.get_text(Locators.ALERT_MSG))
            self.click(Locators.OK_BUTTON)
            time.sleep(2)
        except:
            get_logger().warning("There is no alert message")
        finally:
            self.click(Locators.CHECKBOX)  # Deselecting the checkbox
            time.sleep(1)

        self.click(Locators.DELETE)
        time.sleep(3)
        if self.click(Locators.YES_BUTTON):
            get_logger().info("Route assigned to the student deleted successfully!")
            time.sleep(3)
        else:
            get_logger().warning("Route assigned to the student was not deleted !")
            self.click(Locators.NO_BUTTON)
