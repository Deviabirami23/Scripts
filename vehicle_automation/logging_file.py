import inspect
import logging


def get_logger():
    logging.basicConfig(filename="logfile.log",
                        format='Date and Time:%(asctime)s - %(levelname)s - %(name)s -Line number:%(lineno)d : %(message)s',
                        datefmt='%d-%b-%y %I:%M:%S %p',
                        filemode='a'
                        )

    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)
    return logger


class GetLogger:

    pass
