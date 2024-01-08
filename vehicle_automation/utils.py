import configparser

import requests

# import requests

config = configparser.ConfigParser()
config.read("./settings.conf")


def get_otp_value(email_or_phone) -> str:
    """
    Get the OTP for given Email or Phone
    :param email_or_phone: Enter Email ID or Phone number to get OTP
    :return: OTP Code or OTP_NOT_FOUND value
    """
    url = f"{config['leave']['OTP_API']}/{config['leave']['OTP_SECRET_KEY']}/{email_or_phone}"
    response = requests.get(url)
    otp_response = response.json()
    if len(otp_response.get('response')) == 6:
        return otp_response.get('response')
    else:
        return "OTP_NOT_FOUND"
