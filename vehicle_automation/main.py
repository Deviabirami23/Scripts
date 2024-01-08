import configparser
import time

import requests
from selenium import webdriver

from vehicle_automation.vehicle_test_cases.authentication.logout import Logout
from vehicle_test_cases.authentication.login import Login

config = configparser.ConfigParser()
config.read("./settings.conf")


def check_internet_connection():
    try:
        # Attempt to make a request to a known URL (e.g., Google's public DNS)
        response = requests.get('https://dns.google.com/resolve')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print('Connected to the internet')
        return True
    except requests.RequestException as e:
        print(f'Internet connection error: {e}')
        return False



def run_test_cases():
    """
    One single method to run all test cases
    :return:
    """
    driver = webdriver.Chrome(executable_path="D:/chromedriver_win32")
    driver.get(config['vehicle']['TEST_URL'])
    if not check_internet_connection():
        return

    vehicle_login = Login(driver)
    vehicle_logout = Logout(driver)
    vehicle_login.do_login(1)
    # Logout
    vehicle_logout.do_logout()
    # Login again to test - it means reuse code wherever you want
    time.sleep(2)
    vehicle_login.do_login(1)
    time.sleep(20)


if __name__ == '__main__':
    run_test_cases()
