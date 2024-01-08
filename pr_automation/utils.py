import configparser
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

config = configparser.ConfigParser()
config.read("./settings.conf")


def get_otp_value(email_or_phone, requests=None) -> str:
    """
    Get the OTP for given Email or Phone
    :param email_or_phone: Enter Email ID or Phone number to get OTP
    :return: OTP Code or OTP_NOT_FOUND value
    """
    url = f"{config['fv']['OTP_API']}/{config['fv']['OTP_SECRET_KEY']}/{email_or_phone}"
    response = requests.get(url)
    otp_response = response.json()
    if len(otp_response.get('response')) == 6:
        return otp_response.get('response')
    else:
        return "OTP_NOT_FOUND"


def enter_text(self, by_locator, text):
    if text is not None:
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    else:
        return None
def keys_to_typing(val):
    print("Value of val:", val)
    if val is None:
        return []
    # Rest of the code
