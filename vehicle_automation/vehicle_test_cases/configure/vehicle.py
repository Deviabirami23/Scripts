import logging
import time
import requests

from selenium.webdriver.common.by import By

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators
from vehicle_automation.logging_file import get_logger


class Configure_vehicle(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.click(Locators.MENU)
        # time.sleep(3)
        self.click(Locators.CONFIGURE)
        time.sleep(10)
        self.click(Locators.VEHICLE)
        time.sleep(4)

    def add_new_vehicle(self):

        self.click(Locators.CHECKBOX)
        time.sleep(2)
        self.click(Locators.ADD)
        try:
            get_logger().info("To add new data, " + self.get_text(Locators.ALERT_MSG))
            self.click(Locators.OK_BUTTON)
            time.sleep(2)
        except:
            get_logger().warning("There is no alert message")
        finally:
            self.click(Locators.CHECKBOX)  # Deselecting the checkbox
            time.sleep(1)

        # ADDING NEW VEHICLE
        self.click(Locators.ADD)
        time.sleep(3)
        self.scroll_down()
        time.sleep(5)
        self.scroll_down()
        self.click(Locators.VEH_SUBMIT_BUTTON)
        time.sleep(1)

        try:
            print(self.get_text(Locators.VEHICLE_SITE_ALERT) + ", for site name")
            print(self.get_text(Locators.VEH_NUMBER_ALERT) + ", for Vehicle Reg number")

        except:
            print("There is no alert messages")

        self.dropdown_click(Locators.VEH_SITE_NAME, 1)
        self.enter_text(Locators.VEH_NUMBER, 'Test01')
        time.sleep(4)
        self.enter_text(Locators.VEH_NAME, 'Vehicle Test')
        time.sleep(3)
        # self.enter_text(Locators.VEH_ENGINE_NUMBER, '2456')
        # self.enter_text(Locators.VEH_CHASSIS_NUMBER, '2345')
        # self.enter_text(Locators.VEH_RC_NUMBER, '2345')
        # self.enter_text(Locators.VEH_FC_NUMBER, '2345')
        # self.enter_text(Locators.VEH_TAX_RECEIPT_NUMBER, '2345')
        # self.enter_text(Locators.VEH_PERMIT_NUMBER, '6789')
        # self.scroll_down()
        self.enter_text(Locators.VEH_SEAT_CAPACITY, '50')
        self.scroll_down()
        self.enter_text(Locators.VEH_FUEL_CAPACITY, '25')
        self.enter_text(Locators.FUEL_TYPE, 'Diesel')
        self.scroll_down()
        self.enter_text(Locators.SPEEDLIMIT, '30')
        self.scroll_down()
        time.sleep(3)
        self.click(Locators.ATTACHMENTS)
        time.sleep(4)
        self.file_upload(Locators.ATTACHMENTS, "D:/VehicleAutomation/vehicle_automation/Image_test.png")
        time.sleep(2)
        self.enter_text(Locators.RC_EXP_DATE, '23-03-2025')
        self.enter_text(Locators.FC_EXP_DATE, '23-03-2025')
        self.enter_text(Locators.EMISSION_EXP_DATE, '23-03-2025')
        self.enter_text(Locators.INSURANCE_EXP_DATE, '23-03-2025')
        self.enter_text(Locators.TAX_EXP_DATE, '23-03-2025')
        self.enter_text(Locators.PERMIT_EXP_DATE, '23-03-2025')
        time.sleep(3)
        url = 'https://demoapi.parivahaneye.com/school-app/assets/create-asset'
        response = requests.post(url, json={})
        try:
            response.raise_for_status()
            if response.status_code == 200:
                get_logger().info("Vehicle was created successfully!")
                time.sleep(8)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            print(response.text)
            self.click(Locators.VEH_CANCEL_BUTTON)
            get_logger().warning("Vehicle not created!")
            time.sleep(2)
        except requests.exceptions.RequestException as err:
            print(f"Request Error: {err}")
            self.click(Locators.VEH_CANCEL_BUTTON)
            get_logger().warning("Vehicle not created!")
            time.sleep(2)

        # UPDATING EXISTING VEHICLE

    def update_existing_vehicle(self):
        self.click(Locators.CHECKBOX)
        self.click(Locators.EDIT)
        time.sleep(3)
        self.dropdown_click(Locators.VEH_SITE_NAME, 2)
        self.click_clear_and_enter_text(Locators.VEH_NUMBER, 'Aut')
        time.sleep(4)

        self.click_clear_and_enter_text(Locators.VEH_NAME, 'Vehicle Test')
        time.sleep(3)
        self.click_clear_and_enter_text(Locators.VEH_ENGINE_NUMBER, '2456')
        time.sleep(2)
        self.click_clear_and_enter_text(Locators.VEH_CHASSIS_NUMBER, '2345')
        self.click_clear_and_enter_text(Locators.VEH_RC_NUMBER, '2345')
        self.click_clear_and_enter_text(Locators.VEH_FC_NUMBER, '2345')
        self.scroll_down()
        self.click_clear_and_enter_text(Locators.VEH_TAX_RECEIPT_NUMBER, '2345')
        self.scroll_down()
        time.sleep(2)
        self.click_clear_and_enter_text(Locators.VEH_PERMIT_NUMBER, '6789')
        time.sleep(2)
        self.scroll_down()
        self.click_clear_and_enter_text(Locators.VEH_SEAT_CAPACITY, '50')
        self.scroll_down()
        self.click_clear_and_enter_text(Locators.VEH_FUEL_CAPACITY, '25')
        self.click_clear_and_enter_text(Locators.FUEL_TYPE, 'Diesel')
        self.scroll_down()
        self.click_clear_and_enter_text(Locators.SPEEDLIMIT, '30')
        self.scroll_down()
        time.sleep(2)
        self.click_clear_and_enter_text(Locators.RC_EXP_DATE, '23-03-2025')
        self.click_clear_and_enter_text(Locators.FC_EXP_DATE, '23-03-2025')
        self.click_clear_and_enter_text(Locators.EMISSION_EXP_DATE, '23-03-2025')
        self.click_clear_and_enter_text(Locators.INSURANCE_EXP_DATE, '23-03-2025')
        self.click_clear_and_enter_text(Locators.TAX_EXP_DATE, '23-03-2025')
        self.click_clear_and_enter_text(Locators.PERMIT_EXP_DATE, '23-03-2025')
        edit_veh_url = "https://demoapi.parivahaneye.com/school-app/assets/update-asset"
        response = requests.post(edit_veh_url, json={})
        try:
            response.raise_for_status()
            if response.status_code == 200:
                get_logger().info("Vehicle was updated successfully!")
                time.sleep(8)
        except:
            print(response.text)
            self.click(Locators.VEH_CANCEL_BUTTON)
            get_logger().warning("Vehicle not updated!")
            time.sleep(2)
        # except requests.exceptions.RequestException as err:
        #     print(f"Request Error: {err}")
        #     self.click(Locators.VEH_CANCEL_BUTTON)
        #     print("Vehicle not updated!")
        #     time.sleep(2)

        time.sleep(6)

    def download_vehicle_reports(self):
        self.click(Locators.DOWNLOAD)
        time.sleep(2)
        self.click(Locators.PDF)
        get_logger().info("PDF for vehicle list downloaded successfully")
        self.switch_to_original_window()
        time.sleep(5)
        self.click(Locators.DOWNLOAD)
        time.sleep(2)
        self.click(Locators.EXCEL)
        get_logger().info("Excel file for vehicle list downloaded successfully")
        time.sleep(5)
