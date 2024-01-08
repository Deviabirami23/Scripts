import configparser
import time

import requests

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators
from vehicle_automation.logging_file import get_logger

config = configparser.ConfigParser()
config.read("./settings.conf")


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self):
        self.driver.maximize_window()
        time.sleep(3)

        username = 'Vijayakumar.samiyappan@techgenzi.com'
        password = '98765432'

        self.click(Locators.USERNAME)
        self.enter_text(Locators.USERNAME, username)
        time.sleep(2)
        self.enter_text(Locators.PASSWORD, password)
        time.sleep(2)
        self.click(Locators.EYE_BUTTON)
        time.sleep(2)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        time.sleep(3)
        self.driver.save_screenshot("screenshots/screenshot.png")
        self.click(Locators.LOGIN_SUBMIT_BUTTON)

        response = self.login_request(username, password)

        time.sleep(10)

        if response.status_code == 200:
            get_logger().info("Logged in successfully!!")
        elif response.status_code == 400:
            get_logger().warning("400 BAD REQUEST: %s", response.text)
        else:
            get_logger().warning("Login Failed: %s", response.text)

        self.driver.save_screenshot("D:/VehicleAutomation/vehicle_automation/vehicle_test_cases/screenshots/screenshot.png")
        auth_token = response.json()
        print('auth_token', auth_token)


    def login_request(self, username, password):
        base_url = "https://demoapi.parivahaneye.com"
        endpoint = '/users/login'
        url = f'{base_url}{endpoint}'
        data = {"username": username, "password": password}
        response = requests.post(url, json=data)
        # print(response.content)
        print(response)
        # print(response.headers)
        return response


    # def do_login1(self, log_in):
    #     self.driver.maximize_window()
    #     time.sleep(2)
    #     people = [{"username_admin": "11100050", "password_admin": "12345678"},
    #               {"username_user": "Deviabirami.v@techgenzi.com", "password": "12345678"},
    #               {"username_err": "Deviabirami@techgenzi.com", "password_err": "12345678"},
    #               {"username1": "11100051", "password1": "12345678"}]
    #     # Login as an Admin
    #     if 0 == log_in:
    #         self.reduce(people[0]["username_admin"], people[0]["password_admin"])
    #         # Login as a User
    #     elif 1 == log_in:
    #         self.reduce(people[1]["username_user"], people[1]["password"])
    #
    #     elif 2 == log_in:
    #         self.reduce(people[2]["username_err"], people[2]["password_err"])
    #     elif 3 == log_in:
    #         self.reduce(people[3]["username1"], people[3]["password1"])
    #     else:
    #         print("Login Error")
    #
    # def reduce(self, username, password):
    #     self.enter_text(Locators.USERNAME, username)
    #     self.enter_text(Locators.PASSWORD, password)
    #     self.click(Locators.LOGIN_SUBMIT_BUTTON)
    #     time.sleep(2)
    #     print("Logged in successfully!!")
    #     time.sleep(2)
