import time

from selenium.webdriver import Keys, ActionChains

from vehicle_automation.base import BasePage
from vehicle_automation.locators import Locators


class Profile_settings(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def my_account(self):
        self.click(Locators.PROFILE)
        self.click(Locators.MY_ACCOUNT)
        self.click(Locators.PROFILE)
        # self.click(Locators.DOWNLOAD_APPS)
        # time.sleep(30)
        # self.click(Locators.PROFILE)
        self.click(Locators.USER_HISTORY)
        time.sleep(3)
        self.click(Locators.PROFILE)
        self.click(Locators.CONFIGURE_COMPANY)
        time.sleep(5)
        # self.click(Locators.CONFIGURE_COMPANY_CODE_CHANGE)
        time.sleep(4)
        try:
            self.enter_text(Locators.CONFIGURE_COMPANY_CODE_CHANGE, 'Test')
            time.sleep(8)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
        except:
            self.click(Locators.CLOSE_BUTTON)
            print("Unable to change company code!")

        finally:
            print("Something went wrong!!!")
        time.sleep(4)



