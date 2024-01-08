import configparser
import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

config = configparser.ConfigParser()
config.read("./settings.conf")


class BasePage:
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver: WebDriver = driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # this function performs click on web element whose locator is passed to it.
    def click_direct(self, by_locator):
        self.driver.find_element(by_locator[0], by_locator[1]).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def clear(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(
            Keys.CONTROL + "a" + Keys.DELETE)

    def check_duplicate(self, by_locator):
        elements = self.driver.find_elements(*by_locator)
        if elements:
            return True
        return False

    def dropdown_click(self, by_locator, n):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()
        for i in range(n):
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).send_keys(
                Keys.ARROW_DOWN)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def get_selected_option(self, locator):
        element = self.driver.find_element(*locator)
        selected_option = element.get_attribute("value")
        return selected_option

    def click_clear_and_enter_text(self, by_locator, new_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        # Click on the element (optional, if not focused)
        element.click()
        # Use Ctrl+A to select all text, then press Delete to clear it
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

        # Enter new text
        element.send_keys(new_text)

    def scroll_down(self, scroll=0):
        script = "window.scrollBy(0,{})"
        return self.driver.execute_script(script.format(scroll))

    def ag_grid_row(self, by_locator):
        x = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        return x.split("\n")

    def send_keys(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def file_upload(self, by_locator, file_path):
        element = self.driver.find_element(*by_locator)
        element.send_keys(file_path)
        time.sleep(3)  # You may adjust the sleep duration based on your application's response time
        element.send_keys(Keys.ENTER)

    def switch_to_original_window(self):
        # Switch back to the original window or tab
        original_window_handle = self.driver.window_handles[0]
        self.driver.switch_to.window(original_window_handle)

    def required_field_message(self, by_locator):
        """
            This will show the error message
        :param by_locator:
        :return:
        """
        x = []
        a = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for b in a:
            x.append(b.text)
        return ','.join(repr(str(i)) for i in x)
