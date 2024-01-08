import configparser
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

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
        service_obj = Service(config['pr']['CHROME_DRIVER_LOCATION'])
        self.driver = webdriver.Chrome(service=service_obj,
                                       options=chrome_options)
        self.driver.get(config['pr']['TEST_URL'])
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self):
        # Cleanup driver to solve memory issues
        self.driver.close()
        self.driver.quit()
