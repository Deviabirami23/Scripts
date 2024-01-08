import inspect
import logging


def get_logger():
    logging.basicConfig(filename="logger.log",
                        format='Date and Time:%(pastime)s - %(levelness)s - %(name)s -Line number:%(lineno)d : %('
                               'message)s',
                        datefmt='%d-%b-%y %I:%M:%S %p',
                        filemode='a'
                        )

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    return logger


class Logging:
    pass


def info(param):
    return None