import configparser

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

config = configparser.ConfigParser()
config.read("./settings.conf")


def ag_grid_row(x):
    return x.split("\n")


def clear_element(element):
    element.send_keys(Keys.CONTROL + "a" + Keys.DELETE)


class BasePage:
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver: WebDriver = driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def click1(self, element):
        element.click()

    # this function performs click on web element whose locator is passed to it.
    def click_direct(self, by_locator):
        self.driver.find_element(by_locator[0], by_locator[1]).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # def enter_text(self, by_locator, text):
    #     print("Value of text:", text)
    #     if text is not None:
    #         return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    #     else:
    #         return None

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

    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def send_keys(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def file_upload(self, by_locator, file_path):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(file_path)

    # this function performs to get the text of web element whose locator is passed to it.
    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    # this function performs to get the value of input field whose locator is passed to it.
    def get_attribute(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).get_attribute('value')

    # this function perform
    def is_selected(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_selected()

    # this function performs to get the location of multiple web elements whose locator is passed to it.
    def locate_elements(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))

    # this function performs to clear the text of web element whose locator is passed to it.
    def clear(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(
            Keys.CONTROL + "a" + Keys.DELETE)

    def static_dropdown(self, by_locator, text):
        a = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))

        for b in a:
            if b.text == text:
                b.click()

    def dropdown_click(self, by_locator, n):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        for i in range(n):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(
                Keys.ARROW_DOWN)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def drag_and_drop(self, by_source, by_target):
        source = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_source))
        target = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_target))
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def dragdrop(self, by_source, by_target):
        source_column = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_source))
        destination_column = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_target))
        # card = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='card'
        # and text()='Task 1']")))
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_column, destination_column).perform()

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_selected_option(self, locator):
        element = self.driver.find_element(*locator)
        selected_option = element.get_attribute("value")
        return selected_option

    def find_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def find_element(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def enter_text1(self, element, text):
        element = WebDriverWait(element.parent, 10).until(EC.visibility_of(element))
        element.clear()
        element.send_keys(text)
