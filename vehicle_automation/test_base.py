import configparser
import unittest

from selenium import webdriver

config = configparser.ConfigParser()
config.read("./settings.conf")


class TestBase(unittest.TestCase):
    """
    Base test class to initiate web driver in one place and reuse it everywhere.
    """
    def setUp(self) -> None:
        """
        Setup google driver
        :return:
        """
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(config['vehicle']['TEST_URL'])
        self.driver.implicitly_wait(3)
        self.driver.save_screenshot("D:/VehicleAutomation/vehicle_automation/screenshots.png")
        self.driver.maximize_window()

    def tearDown(self):
        # Cleanup driver to solve memory issues
        self.driver.close()
        self.driver.quit()
