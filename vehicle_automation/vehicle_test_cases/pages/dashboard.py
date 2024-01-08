import time
from lib2to3.pgen2 import driver
from logging import getLogger

import requests
from bs4 import BeautifulSoup
# from response import Response
import requests, openpyxl
from selenium import webdriver

from selenium.webdriver import Keys, ActionChains

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators


class Dashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def download_files(self, category):
        self.click(Locators.DASHBOARD)
        time.sleep(2)
        self.click(category)
        time.sleep(5)

        try:
            self.click(Locators.PDF_DOWNLOAD)
            time.sleep(5)
            getLogger().info(f"PDF file for {category} downloaded successfully")
        except:
            getLogger().info(f"PDF file for {category} download failed")
            time.sleep(5)

        self.switch_to_original_window()
        time.sleep(4)

        try:
            self.click(Locators.EXCEL_DOWNLOAD)
            time.sleep(5)
            getLogger().info(f"EXCEL file for {category} downloaded successfully")
        except:
            getLogger().info(f"EXCEL file for {category} download failed")
            time.sleep(5)

        self.click(Locators.CLOSE_CARD)

    def test_dashboard(self):
        categories = [Locators.ALL_VEHICLES, Locators.GPS_INSTALLED, Locators.RUNNING_VEHICLES, Locators.IDLE_VEHICLES,
                      Locators.STOPPED_VEHICLES, Locators.OUT_OF_NETWORK]

        for category in categories:
            self.download_files(category)

    def check_filters(self):
        actions = ActionChains(self.driver)

        self.click(Locators.FILTER_TAB)
        time.sleep(3)
        self.click(Locators.FILTER_MENU)
        self.click(Locators.FILTER_BUTTON)
        self.click(Locators.SITE)
        time.sleep(4)
        self.click(Locators.SITE_SELECT[0])
        time.sleep(2)
        self.click(Locators.SITE_SELECT[1])
        time.sleep(2)
        self.click(Locators.SITE_SELECT[3])
        time.sleep(3)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(4)
        self.click(Locators.DEVICE_STATUS)
        time.sleep(4)
        self.click(Locators.STATUS_SELECT[0])
        time.sleep(2)
        self.click(Locators.STATUS_SELECT[1])
        time.sleep(2)
        self.click(Locators.STATUS_SELECT[2])
        time.sleep(2)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(4)
        self.click(Locators.ROUTES)
        time.sleep(4)
        self.click(Locators.ROUTES_SELECT[0])
        time.sleep(2)
        self.click(Locators.ROUTES_SELECT[1])
        time.sleep(2)
        time.sleep(2)
        self.click(Locators.ROUTES_SELECT[2])
        time.sleep(3)
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(4)

        try:
            self.click(Locators.FILTERED_VEHICLES[0])
            time.sleep(3)
            self.click(Locators.FILTERED_VEHICLES[1])
            time.sleep(3)
            self.click(Locators.FILTERED_VEHICLES[3])
            time.sleep(5)
            getLogger().info("Vehicles present for your applied filter")
        except:
            getLogger().info("No vehicles present for your filter")

        self.enter_text(Locators.SEARCH_VEHICLE, 'KA18AA1009')
        time.sleep(3)
        try:
            self.click(Locators.FILTERED_VEHICLES[0])
            getLogger().info("Searched vehicle present!!")

        except:
            getLogger().info("Searched vehicle not present")

        try:

            response = requests.get(self.driver.current_url)
            print(response)

            soup = BeautifulSoup(response.text, 'html.parser')
            vehicles = soup.find('div',
                                 class_="Vehicle_Dashboard2")
            time.sleep(20)
            print("vehicles:", vehicles)
            # for vehicle in vehicles:
            #     # print(vehicle)
            #     # vehicle_name = vehicle
            #     break
        except Exception as e:
            print(e)
