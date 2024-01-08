import configparser
import time

from selenium import webdriver

from pr_automation.pr_test_cases.authentication.logout import Logout
from pr_test_cases.authentication.login import Login

config = configparser.ConfigParser()
config.read("./settings.conf")


def run_test_cases():
    """
    One single method to run all test cases
    :return:
    """
    driver = webdriver.Chrome(executable_path="./lib/chromedriver")
    driver.get(config['fv']['TEST_URL'])
    fv_login = Login(driver)
    fv_logout = Logout(driver)
    fv_login.do_login()
    # Logout
    fv_logout.do_logout()
    # Login again to test - it means reuse code wherever you want
    time.sleep(2)
    fv_login.do_login()
    time.sleep(20)


if __name__ == '__main__':
    run_test_cases()
