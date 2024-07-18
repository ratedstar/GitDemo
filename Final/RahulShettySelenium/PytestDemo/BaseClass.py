import inspect
import logging

class BaseClass:
    def get_logger(self):
        loggerNmae = inspect.stack()[1][3]
        logger = logging.getLogger(loggerNmae)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

